# Object Tracking for Autonomous Mobile Robot (Raspberry Pi 4)

An autonomous mobile robot that can detect and track objects using image processing and deep learning methods on a Raspberry Pi 4. The robot can follow objects in real-time and adjust its movement accordingly.

# # Features

- Track objects using color detection (HSV color space).

- Detect circular objects using Hough Circle Transform.

- Use MobileNet SSD deep learning for multiple object classes.

- Real-time robot movement control based on detected objects.


# # Methods
# # # 1. Color-Based Tracking

- Convert RGB → HSV.

- Mask the target color (e.g., green ping-pong ball).

- Detect contours and control movement based on contour area.

# # # 2. Circle Detection (Hough Transform)

- Convert image to grayscale & blur.

- Detect circles with OpenCV Hough Circle function.

- Track object and control robot based on circle area.

# # # 3. Deep Learning (MobileNet SSD)

- Pre-trained on MS COCO dataset (91 classes)

- Detect multiple objects and select a target for tracking

- Track object using contour-based movement control

# # Hardware

- Raspberry Pi 4.

- Camera module for real-time video.

- Motors with PWM control (Arduino recommended for optimization).

# # Challenges

- Lighting conditions affect image processing detection.

- Deep learning is slower on Raspberry Pi 4.

- Motor control mismatch may cause continuous rotation in one direction.

# # Results

- Color and circle tracking are fast but sensitive to the environment.

- Deep learning allows flexible object tracking, but is slower.

- Robot can follow multiple object types in real-time.
  
# # Future Improvements

- Improve motor control with Arduino for precise PWM

- Optimize deep learning model for faster real-time tracking

- Add support for more object classes and dynamic selection

# # # License

This project is open-source. Feel free to use and modify.
