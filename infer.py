import torch
from torchvision.transforms import transforms
import numpy as np
from torch.autograd import Variable
from torchvision.models import squeezenet1_1
from io import open
import os
from PIL import Image
from train import GestureNet


# Load the saved model.
checkpoint = torch.load("gestures_4.model")
model = GestureNet(num_classes=2)
model.load_state_dict(checkpoint)
model.eval()


def predict_image_class(image_path):
    image = Image.open(image_path)
    image = image.convert('RGB') # Model expects RGB.

    transformation = transforms.Compose([
        transforms.CenterCrop(200), # Image size defined here.
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])

    # Preprocess the image.
    image_tensor = transformation(image).float()

    # Add an extra batch dimension since pytorch treats all images as batches.
    image_tensor = image_tensor.unsqueeze_(0)

    if torch.cuda.is_available():
        image_tensor.cuda()

    # Turn the input into a Variable
    input = Variable(image_tensor)

    # Predict the class of the image.
    output = model(input)
    index = output.data.numpy().argmax()

    return index


if __name__ == "__main__":
    imagefile = "data/test/3004 Brick 1x2/0008.png"
    imagepath = os.path.join(os.getcwd(), imagefile)

    index = predict_image_class(imagepath)
    print("Predicted Class: ", index)
