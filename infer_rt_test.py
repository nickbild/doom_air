import torch
from torchvision.transforms import transforms
import numpy as np
from torch.autograd import Variable
from torchvision.models import squeezenet1_1
from io import open
import os
from PIL import Image
from train_test import GestureNet
import cv2
from time import sleep
import cv2
import requests


img_width = 300
img_height = 300
doom_host = "192.168.1.113:5000"
trained_model = "gestures_61_1630-1650_arch14.model"
num_classes = 11


# Load the saved model.
checkpoint = torch.load(trained_model)
model = GestureNet(num_classes=num_classes)
model.load_state_dict(checkpoint)
model.eval()

transformation = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])


def predict_image_class(image):
    # Preprocess the image.
    image_tensor = transformation(image).float()

    # Add an extra batch dimension since pytorch treats all images as batches.
    image_tensor = image_tensor.unsqueeze_(0)
    image_tensor.cuda()

    # Turn the input into a Variable.
    input = Variable(image_tensor)

    # Predict the class of the image.
    output = model(input)
    index = output.data.numpy().argmax()
    score = output[0, index].item()

    return index, score


def gstreamer_pipeline (capture_width=3280, capture_height=2464, display_width=img_width, display_height=img_height, framerate=21, flip_method=0) :
    return ('nvarguscamerasrc ! '
    'video/x-raw(memory:NVMM), '
    'width=(int)%d, height=(int)%d, '
    'format=(string)NV12, framerate=(fraction)%d/1 ! '
    'nvvidconv flip-method=%d ! '
    'video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! '
    'videoconvert ! '
    'video/x-raw, format=(string)BGR ! appsink'  % (capture_width,capture_height,framerate,flip_method,display_width,display_height))


if __name__ == "__main__":
    cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)

    if cap.isOpened():
        while True:
            ret_val, img = cap.read()
            index, score = predict_image_class(img)

            #print("Predicted Class: ", index)
            #print("Score: ", score)

            if index == 0 and score > 29:
                print("Backwards")
                #requests.get("http://{}/backward".format(doom_host))
            elif index == 1 and score > 35:
                print("Crouch")
                #requests.get("http://{}/crouch".format(doom_host))
            elif index == 2 and score > 35:
                print("Forwards")
                #requests.get("http://{}/forward".format(doom_host))
            elif index == 3 and score > 10:
                print("God mode")
                #requests.get("http://{}/god_mode".format(doom_host))
            elif index == 4 and score > 44:
                print("Jump")
                #requests.get("http://{}/jump".format(doom_host))
            elif index == 5 and score > 35:
                print("Left")
                #requests.get("http://{}/left".format(doom_host))
            elif index == 6 and score > 33:
                print("Next Weapon")
                #requests.get("http://{}/next_weapon".format(doom_host))
            elif index == 7:
                print("Nothing")
                pass
            elif index == 8 and score > 35:
                print("Right")
                #requests.get("http://{}/right".format(doom_host))
            elif index == 9 and score > 30:
                print("Shoot")
                #requests.get("http://{}/fire".format(doom_host))
            elif index == 10 and score > 23:
                print("Use")
                #requests.get("http://{}/space".format(doom_host))

        cap.release()
    else:
        print('Unable to open camera.')
