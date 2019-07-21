![Doom AIr](https://raw.githubusercontent.com/nickbild/doom_air/master/img/logo.jpg)

# Doom AIr

Play Doom on a giant screen using your body as the controller.

Note: Doom was developed by id Software. I have created a new interface for that game, but not the game itself.

## How It Works

![Project Diagram](https://raw.githubusercontent.com/nickbild/doom_air/master/img/doom_air.jpg)

Doom runs on a laptop, which is connected to a projector.  The laptop also runs a [REST API](https://github.com/nickbild/doom_air/blob/master/api.py) that simulates physical key presses on the keyboard when each endpoint receives a remote request.

A Jetson Nano has a CSI camera pointed at the subject.  It is running a convolutional neural network (CNN) model in real time as images are captured by the camera.  When a gesture (of the set of gestures the model has been trained on) is detected, an API request is sent to the laptop.  This simulates a keypress, and controls the action in Doom.

## Gestures

The CNN has been trained to detect the following gestures.

| Action | Example |
| ----   | ----- |
| Forward | ![](https://raw.githubusercontent.com/nickbild/doom_air/master/data/train/forward/gesture_forward_train_20_1.jpg) |
| Backward | ![](https://raw.githubusercontent.com/nickbild/doom_air/master/data/train/backward/gesture_backward_train_20_1.jpg) |
| Left | ![](https://raw.githubusercontent.com/nickbild/doom_air/master/data/train/left/gesture_left_train_24_2.jpg) |
| Right | ![](https://raw.githubusercontent.com/nickbild/doom_air/master/data/train/right/gesture_right_train_22_2.jpg) |
| Shoot | ![](https://raw.githubusercontent.com/nickbild/doom_air/master/data/train/shoot/gesture_shoot_train_21_3.jpg) |
| Use | ![](https://raw.githubusercontent.com/nickbild/doom_air/master/data/train/use/gesture_use_train_20_5.jpg) |
| Jump | ![](https://raw.githubusercontent.com/nickbild/doom_air/master/data/train/jump/gesture_jump_train_20_1.jpg) |
| Crouch | ![](https://raw.githubusercontent.com/nickbild/doom_air/master/data/train/crouch/gesture_crouch_train_21_3.jpg) |
| Next Weapon | ![](https://raw.githubusercontent.com/nickbild/doom_air/master/data/train/next_weapon/gesture_next_train_20_5.jpg) |
| God Mode | ![](https://raw.githubusercontent.com/nickbild/doom_air/master/data/train/god_mode/gesture_god_train_20_1.jpg) |
| Nothing | ![](https://raw.githubusercontent.com/nickbild/doom_air/master/data/train/nothing/gesture_nothing_train_20_2.jpg) |

## Training

The CNN was ultimately trained on 3,300 images (300 per gesture).  I tried as many as 32,000 training images, but found that I got a bit sloppy in the course of capturing so many images and some of the gestures were a bit off what I actually wanted detected, so the network would get a bit confused a times.  Machine learning requires a lot of data, yes, but the quality of that data also matters.

I found it necessary to capture each gesture from a variety of slightly varying angles and lighting conditions or the resultant network was not tolerant of the unavoidable variances that will be present in real data.  Here are a few of the images captured for the 'shoot' gesture, for example:

![](https://raw.githubusercontent.com/nickbild/doom_air/master/img/train_data_example.gif)

## Media

See it in action:
[YouTube](https://www.youtube.com/watch?v=b2sixeEpBuU)
