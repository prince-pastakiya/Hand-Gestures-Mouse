Overview:

This project uses computer vision and machine learning to recognize hand gestures and control the mouse cursor on the screen. It utilizes the MediaPipe library for hand detection and tracking, and PyAutoGUI for mouse control.

How it Works:

The program captures video from the default camera using OpenCV.
It flips the video horizontally to match the user's perspective.
The MediaPipe Hand Detection model is used to detect and track hand landmarks in the video frame.
The program draws the detected hand landmarks on the video frame.
It identifies the tip of the index finger and thumb, and calculates their positions on the screen.
The mouse cursor is moved to the position of the index finger tip.
When the thumb and index finger are close together (within a certain distance), a mouse click event is triggered.

Requirements:

OpenCV (cv2)

MediaPipe (mp)

PyAutoGUI (pyautogui)

Usage:

Run the script using Python (e.g., python hand_gesture_mouse_control.py).

Hold your hand in front of the camera, with your palm facing the camera.

Move your index finger to control the mouse cursor.

Bring your thumb and index finger together to trigger a mouse click.
