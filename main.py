import cv2
import mediapipe as mp
import pyautogui

# Initialize the camera capture
cap = cv2.VideoCapture(0)

# Create a hand detector and drawing utilities
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

# Get the screen dimensions
screen_width, screen_height = pyautogui.size()

# Initialize the index finger y-coordinate
index_y = 0

while True:
    # Read a frame from the camera
    _, frame = cap.read()
    
    # Flip the frame horizontally (since camera is mirrored)
    frame = cv2.flip(frame, 1)
    
    # Get the frame dimensions
    frame_height, frame_width, _ = frame.shape

    # Convert the frame to RGB (required by MediaPipe)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame using the hand detector
    output = hand_detector.process(rgb_frame)
    
    # Get the detected hand landmarks
    hands = output.multi_hand_landmarks

    if hands:
        # Loop through each detected hand
        for hand in hands:
            # Draw the hand landmarks on the frame
            drawing_utils.draw_landmarks(frame, hand)
            
            # Get the individual landmarks
            landmarks = hand.landmark

            # Loop through each landmark
            for id, landmark in enumerate(landmarks):
                # Convert the landmark coordinates to pixel values
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)

                # If this is the index finger tip (id 8)
                if id == 8:
                    # Draw a circle on the frame to highlight the index finger
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    
                    # Calculate the screen coordinates of the index finger
                    index_x = screen_width / frame_width * x
                    index_y = screen_height / frame_height * y
                    
                    # Move the mouse cursor to the index finger position
                    pyautogui.moveTo(index_x, index_y)

                # If this is the thumb tip (id 4)
                if id == 4:
                    # Draw a circle on the frame to highlight the thumb
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    
                    # Calculate the screen coordinates of the thumb
                    thumb_x = screen_width / frame_width * x
                    thumb_y = screen_height / frame_height * y
                    
                    # Calculate the distance between the index finger and thumb
                    print('Outside: ', abs(index_y - thumb_y))

                    # If the distance is less than 70 pixels, simulate a click
                    if abs(index_y - thumb_y) < 70:
                        pyautogui.click()
                        pyautogui.sleep(1)

    # Display the output frame
    cv2.imshow('Hand Gestures', frame)
    
    # Wait for a key press (required to update the window)
    cv2.waitKey(1)