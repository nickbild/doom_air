import torch
from torchvision.transforms import transforms
import numpy as np
from torch.autograd import Variable
from torchvision.models import squeezenet1_1
from io import open
import os
from PIL import Image
from train import GestureNet
import cv2
from time import sleep
import cv2


img_width = 300
img_height = 300


# Load the saved model.
checkpoint = torch.load("gestures_4.model")
model = GestureNet(num_classes=2)
model.load_state_dict(checkpoint)
model.eval()


def predict_image_class(image):
    transformation = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])

    # Preprocess the image.
    image_tensor = transformation(image).float()

    # Add an extra batch dimension since pytorch treats all images as batches.
    image_tensor = image_tensor.unsqueeze_(0)

    if torch.cuda.is_available():
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
            if score > 1.0:
                print("Predicted Class: ", index)

        cap.release()
    else:
        print('Unable to open camera.')

