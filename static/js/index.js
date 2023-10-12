const videoElement = document.getElementById('webcam');
const startButton = document.getElementById('startBtn');
const stopButton = document.getElementById('stopBtn');

let mediaStream;
let socket;

// Establish a WebSocket connection with the server
socket = io.connect('https://' + document.domain + ':' + location.port);

async function startWebcam() {
    try {
        mediaStream = await navigator.mediaDevices.getUserMedia({
            'audio': false,
            'video': {
                facingMode: 'environment'
            }
        });
        videoElement.srcObject = mediaStream;

        startCaptureFrames();

        startButton.hidden = true;
        stopButton.hidden = false;
    } catch (error) {
        console.error('Error accessing webcam:', error);
        alert(`Error accessing webcam: ${error}`);
    }
}

function startCaptureFrames() {
    const canvas = document.createElement('canvas');
    const context = canvas.getContext('2d');
    canvas.width = 64
    canvas.height = 64

    function captureFrame() {
        if (mediaStream.active) {
            context.drawImage(videoElement, 0, 0, canvas.width, canvas.height);
            canvas.toBlob((blob) => {
                if (blob && blob.size > 0) 
                    socket.emit("stream", blob);
            }, 'image/jpeg');
            setTimeout(captureFrame, 200)
        }
    }
    captureFrame();
}

async function stopWebcam() {
    if (mediaStream) {
        mediaStream.getTracks().forEach(track => track.stop());
    }
    startButton.hidden = false;
    stopButton.hidden = true;
}

startButton.addEventListener('click', startWebcam);
stopButton.addEventListener('click', stopWebcam);

socket.on("connect", () => {
    console.log("WebSocket connected");
});

socket.on("disconnect", () => {
    console.log("WebSocket disconnected");
});

socket.on("predictions", (res) => {
    for (let i=0; i<6; i++) {
        let progressbar =  document.getElementById(`result${i}`)
        let confidence = res['data'][i] * 100
        progressbar.style.width = `${confidence}%`
        progressbar.innerHTML = `${confidence.toFixed(0)}%`
    }
});