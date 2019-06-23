import numpy as np
import cv2
import utils
import socketio
import eventlet
import base64
from io import BytesIO
from PIL import Image
from keras.models import load_model
from datetime import datetime
import os

INPUT_SHAPE = (160, 320, 3)

MAX_SPEED = 15
MIN_SPEED = 10
speed_limit = MAX_SPEED

# Socket.IO server
sio = socketio.Server()

# event from simulator
@sio.on('telemetry')
def telemetry(sid, data):
    if data:
        # retrive data
        speed = float(data["speed"])
        steering_angle = float(data["steering_angle"])
        throttle = float(data["throttle"])
        image = Image.open(BytesIO(base64.b64decode(data["image"])))

        try:
           
            image = np.asarray(image)
            image = utils.preprocess(image)
            image = np.array([image])      
            
 
            steering_angle = float(model.predict(image, batch_size=1))

            throttle = 1.0 - steering_angle**2 - (speed/speed_limit)**2
            #throttle=0.05
            
            

            send(steering_angle, throttle)
        except Exception as e:
            print(e)
    else:
        sio.emit('manual', data={}, skip_sid=True)


@sio.on('connect')
def connect(sid, environ):
    send(0, 0)


def send(steer, throttle):
    sio.emit("steer", data={'steering_angle': str(steer), 'throttle': str(throttle)}, skip_sid=True)


app = socketio.WSGIApp(sio)

# simulator will connect to localhost:4567
if __name__ == '__main__':
    model = load_model("behavioral-cloning-model.h5")
    eventlet.wsgi.server(eventlet.listen(('', 4567)), app)
    #os.makedirs('demo')
