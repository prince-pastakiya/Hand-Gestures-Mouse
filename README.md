Overview:

This project uses computer vision and machine learning to recognize hand gestures and control the mouse cursor on the screen. It utilizes the MediaPipe library for hand detection and tracking, and PyAutoGUI for mouse control.

Python Libraries:

1. OpenCV (cv2)
2. MediaPipe (mp)
3. PyAutoGUI (pyautogui)

How it Works:

1. The program captures video from the default camera using OpenCV.
2. It flips the video horizontally to match the user's perspective.
3. The MediaPipe Hand Detection model detects and tracks hand landmarks in the video frame.
4. The program draws the detected hand landmarks on the video frame.
5. It identifies the tip of the index finger and thumb and calculates their positions on the screen.
6. The mouse cursor is moved to the position of the index fingertip.
7. A mouse click event is triggered When the thumb and index finger are close together.

Usage:

1. Run the script using Python (main.py).
2. Hold your hand in front of the camera, with your palm facing the camera.
3. Move your index finger to control the mouse cursor.
4. Bring your thumb and index finger together to trigger a mouse click.
