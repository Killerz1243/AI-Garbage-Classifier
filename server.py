from model import load_model
import cv2 
import numpy as np 

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

model = load_model()
model.load_weights('Model-885-1.64-0.704.h5')

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/background")
def background():
    return render_template("background.html")

@socketio.on("connect")
def handle_connect():
    print("WebSocket connected")

@socketio.on("disconnect")
def handle_disconnect():
    print("WebSocket disconnected")

@socketio.on("stream")
def handle_stream(data):
    # Convert the binary data to a numpy array
    data = np.frombuffer(data, dtype=np.uint8)

    # Decode the video frame
    img = cv2.imdecode(data, cv2.IMREAD_COLOR)
    
    img = cv2.resize(img, (64, 64))
    img = cv2.normalize(img, None, 0, 1.0, cv2.NORM_MINMAX, dtype=cv2.CV_32F)

    img = np.expand_dims(img, axis=0)

    res = model.predict(img, verbose=0)

    emit('predictions', {'data': res[0].tolist()})

if __name__ == "__main__":
    socketio.run(app, debug=True)
