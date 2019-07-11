#!/bin/sh

echo "\n\n==== FORWARD ====\n\n"
python3 capture_gesture.py forward train > /dev/null
python3 capture_gesture.py forward test > /dev/null

echo "\n\n==== BACKWARD ====\n\n"
python3 capture_gesture.py backward train > /dev/null
python3 capture_gesture.py backward test > /dev/null

echo "\n\n==== LEFT ====\n\n"
python3 capture_gesture.py left train > /dev/null
python3 capture_gesture.py left test > /dev/null

echo "\n\n==== RIGHT ====\n\n"
python3 capture_gesture.py right train > /dev/null
python3 capture_gesture.py right test > /dev/null

echo "\n\n==== USE ====\n\n"
python3 capture_gesture.py use train > /dev/null
python3 capture_gesture.py use test > /dev/null

echo "\n\n==== SHOOT ====\n\n"
python3 capture_gesture.py shoot train > /dev/null
python3 capture_gesture.py shoot test > /dev/null

echo "\n\n==== NEXT ====\n\n"
python3 capture_gesture.py next train > /dev/null
python3 capture_gesture.py next test > /dev/null

echo "\n\n==== GOD MODE ====\n\n"
python3 capture_gesture.py god train > /dev/null
python3 capture_gesture.py god test > /dev/null

echo "\n\n==== NOTHING ====\n\n"
python3 capture_gesture.py nothing train > /dev/null
python3 capture_gesture.py nothing test > /dev/null

echo "\n\n==== JUMP ====\n\n"
python3 capture_gesture.py jump train > /dev/null
python3 capture_gesture.py jump test > /dev/null

echo "\n\n==== CROUCH ====\n\n"
python3 capture_gesture.py crouch train > /dev/null
python3 capture_gesture.py crouch test > /dev/null

