![Doom AIr](https://raw.githubusercontent.com/nickbild/doom_air/master/img/logo.jpg)

# Doom AIr

Play Doom on a giant screen using your body as the controller.

Note: Doom was developed by id Software. I have created a new interface for that game, but not the game itself.

## How It Works

![Project Diagram](https://raw.githubusercontent.com/nickbild/doom_air/master/img/doom_air.jpg)

Doom runs on a laptop, which is connected to a projector.  The laptop also runs a [REST API](https://github.com/nickbild/doom_air/blob/master/api.py) that simulates physical key presses on the keyboard when each endpoint receives a remote request.

A Jetson Nano has a CSI camera pointed at the subject.  It is running a convolutional neural network (CNN) model in real time as images are captured by the camera.  When a gesture (of the set of gestures the model has been trained on) is detected, an API request is sent to the laptop.  This simulates a keypress, and controls the action in Doom.

# Gestures

The CNN has been trained to detect the following gestures.

---------
| Action | Example |
---------
| Forward |  |
--------
| Backward |  |
--------
| Left |  |
--------
| Right |  |
--------
| Shoot |  |
--------
| Use |  |
--------
| Jump |  |
--------
| Crouch |  |
--------
| Next Weapon |  |
--------
| God Mode |  |
--------
| Nothing |  |
--------

## Media

See it in action:
[YouTube](https://www.youtube.com/watch?v=b2sixeEpBuU)
