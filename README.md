![Doom AIr](https://raw.githubusercontent.com/nickbild/doom_air/master/img/logo.jpg)

# Doom Air

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

The CNN was ultimately trained on 3,300 images (300 per gesture).  I tried as many as 32,000 training images, but found that I got a bit sloppy in the course of capturing so many images and some of the gestures were a bit off what I actually wanted detected, so the network would get a bit confused at times.  Machine learning requires a lot of data, yes, but the quality of that data also matters.

I found it necessary to capture each gesture from a variety of slightly varying angles and lighting conditions or the resultant network was not tolerant of the unavoidable variances that will be present in real data.  Here are a few of the images captured for the 'shoot' gesture, for example:

![](https://raw.githubusercontent.com/nickbild/doom_air/master/img/train_data_example.gif)

To capture so many images, I created an [automated pipeline](https://github.com/nickbild/doom_air/blob/master/util/all_gestures.sh) that would prompt me for each gesture, then capture images at a specified interval.

Designing the model and finding optimal parameters involved a lot of intuition, trial and error, and time on AWS GPU instances.  Trial and error seems to pretty well be the state of the art in machine learning at this time.  I'm being slightly flippant in saying this, but only slightly.  There are some efforts, such as [AutoML](https://en.wikipedia.org/wiki/Automated_machine_learning) that are working to improve the present situation.

It was also necessary to consider that, while the Jetson Nano has some decent AI horsepower, it is limited.  So, I needed to keep my models reasonable or they'd run too slow for real time image classification.

I settled on a model with 8 convolutional layers and 2 fully connected layers.  It evaluated the test data set with approximately 98% accuracy, and performed very well under real conditions.  The depth of the convolutional layers helped pick out higher order features, like arms, legs, head, etc.  Too shallow of a network would only pick out basic features like lines, and it would struggle to recognize gestures.

### AWS

I trained on `g3s.xlarge` instances at Amazon AWS, with Nvidia Tesla M60 GPUs.  The `Deep Learning AMI (Ubuntu) Version 23.1` image has lots of machine learning packages preinstalled, so it's super easy to use.  Just launch an EC2 instance from the web dashboard, then clone my github repo:

```
git clone https://github.com/nickbild/doom_air.git
```

Then start up a Python3 environment with PyTorch and dependencies and switch to my codebase:

```
source activate pytorch_p36
cd doom_air
```

Now, run my training script:

```
python3 train.py
```

That's it!  Now, watch the output to see when the test accuracy gets to a good level (percentage in the 90s).

This will generate `*.model` output files from each epoch that you can download, e.g. with `scp` to use with the `infer_rt.py` script.

To train for your own gestures, just place your own images in the `data` folder under `train` and `test`.  You can make your own folders there if you want to add new gestures.

## Evaluation

To make the evaluation rock-solid, I used a few tricks.  First, I tested the model out in real time and found what scores were associated with correct gestures.  Scores indicate the degree of certainty the model assigns to an image belonging to the predicted class.  Only predictions with scores greater than or equal to this threshold would make a REST request.

Second, I found that during the transition from one gesture to the next, an inadvertent gesture may be very briefly made.  To correct for this, I require 2 of the same gestures in a row before triggering an action.  Since I kept my model small (and therefore, fast) this was possible with no performance degradation.

## Media

See it in action:
[YouTube](https://www.youtube.com/watch?v=b2sixeEpBuU)

The Jetson Nano with CSI camera:
![](https://raw.githubusercontent.com/nickbild/doom_air/master/img/jetson_nano_sm.jpg)

The setup (Jetson straight ahead, projection on the wall, lamp for illuminating gestures well):
![](https://raw.githubusercontent.com/nickbild/doom_air/master/img/scene_sm.jpg)

The projector:
![](https://raw.githubusercontent.com/nickbild/doom_air/master/img/projector_sm.jpg)

## About the Author

[Nick A. Bild, MS](https://nickbild79.firebaseapp.com/#!/)
