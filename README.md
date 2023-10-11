# AI Garbage Classifier
This AI Garbage Classifier is a powerful tool developed to identify and classify six types of materials commonly found in waste: Cardboard, glass, metal, paper, plastic, and trash. It has been trained on a diverse dataset, which can be found [here](https://www.kaggle.com/datasets/mostafaabla/garbage-classification).

## How does it work?

The AI Garbage Classifier operates in a real-time and interactive manner, allowing users to harness its capabilities through a webcam and a server-based system. Here's a breakdown of how it functions:

  1. **Webcam Integration**: Users can start their webcam to capture live video frames.

  2. **Frame Transmission**: Every 200 milliseconds, the current video frame is sent to the server.

  3. **Frame Processing**: Upon receiving the video frames, the server takes the following steps:

  - **Resize to 64x64 Pixels**: Each frame is resized to a consistent 64x64-pixel resolution. This standardization ensures that all frames are processed uniformly.

  - **Normalization**: The resized frame is then normalized. Normalization typically involves scaling the pixel values so that they fall within a specific range (often between 0 and 1) to make them suitable for processing by the AI model. This step ensures that the model receives data in a format it can understand.

  4. **Material Prediction**: After normalization, the processed frame is passed to the AI model. The model has been trained to recognize and classify materials into the six predefined categories: Cardboard, glass, metal, paper, plastic, and trash. The model analyzes the frame and predicts which material it is made of based on the visual features it detects.

  5. **Real-Time Display**: The prediction result is then sent back to the user and displayed on the web interface. This real-time feedback allows users to observe the classification results in real time, providing immediate insights into the material composition of the objects captured by the webcam.

## Uses of this AI
  The are numerous uses of this AI and it has the potential to make a significant positive impact on waste management and recycling processes. Some of its key applications and benefits include:

- ### 1. Automated Waste Sorting
    One of the most immediate and practical uses of this AI is in automated waste sorting systems. Recycling facilities and waste management centers can integrate this AI into their processing lines, allowing for the efficient separation of recyclable materials (Cardboard, glass, metal, paper, and plastic) from non-recyclable waste. This automation reduces the need for manual labor, making the sorting process faster, more accurate, and cost-effective.

- ### 2. Environmental Impact
    By enabling precise waste sorting, this AI contributes to minimizing the environmental impact of waste disposal. Separating recyclable materials from trash not only reduces the amount of waste sent to landfills but also promotes recycling and the reutilization of valuable resources. This has direct and positive consequences for the environment, such as reduced pollution and conservation of natural resources.

- ### 3. Scalability
  The AI Garbage Classifier is highly scalable and adaptable to different settings. It can be integrated into existing recycling and waste management infrastructures with ease. Whether you are running a small recycling facility or managing waste for an entire city, this AI can be implemented at various levels to enhance recycling efforts and sustainability.

## Setup
Python 3.10 works best
### 1. Install required packages
   Begin by running the following command to install the necessary Python packages: `pip install -r requirements.txt`
### 2. Start the Server
  After successfully installing the required packages, start the server by running the following command: `py server.py`. This will initiate the server, and you can access the AI through a web interface on your local machine by visiting [localhost](http://127.0.0.1:5000).
