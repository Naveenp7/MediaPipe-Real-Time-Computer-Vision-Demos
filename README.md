# 🧠 MediaPipe Real-Time Computer Vision Demos

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10.0%2B-orange)](https://mediapipe.dev/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.5%2B-blue)](https://opencv.org/)

This repository showcases a collection of **real-time computer vision applications** built with **MediaPipe** and **OpenCV**. Each script demonstrates a specific MediaPipe solution for tasks like face detection, hand tracking, pose estimation, iris tracking, hair segmentation, selfie segmentation, and holistic tracking. These demos are designed for learning, prototyping, and exploring MediaPipe's capabilities using a webcam feed.

## 📦 Contents

| File Name                  | Description |
|----------------------------|-------------|
| `face_detection.py`        | Detects human faces in real-time video and draws bounding boxes around them. |
| `hand_tracking.py`         | Tracks up to two hands, visualizing 21 landmarks per hand with connections. |
| `pose_estimation.py`       | Estimates full-body pose with 33 keypoints, ideal for motion analysis. |
| `iris_tracking.py`         | Tracks detailed face mesh, including iris landmarks for gaze estimation. |
| `hair_segmentation.py`     | Segments the hair region using MediaPipe's SelfieSegmentation as a proxy. |
| `selfie_segmentation.py`   | Separates the person from the background, replacing it with a solid color (e.g., green). |
| `holistic_tracking.py`     | Combines face, hand, and pose tracking in a single pipeline for full-body perception. |

## 🎯 Features

- 🧑‍🦰 **Face Detection**: Identifies faces with bounding boxes for applications like AR filters.
- 🖐️ **Hand Tracking**: Tracks 21 keypoints per hand, enabling gesture-based controls.
- 🕺 **Pose Estimation**: Visualizes full-body skeletal structure with 33 landmarks.
- 👁️ **Iris Tracking**: Detects eye and iris movements for gaze or accessibility applications.
- 🖼️ **Hair Segmentation**: Isolates hair regions, useful for virtual styling tools.
- 🎥 **Selfie Segmentation**: Separates the person from the background for virtual backgrounds.
- 🔁 **Holistic Tracking**: Integrates face, hand, and pose tracking for comprehensive analysis.

## ⚙️ Installation

### Prerequisites
- **Python**: Version 3.7 or higher.
- **Hardware**: A webcam for real-time input (or modify scripts for video/image input).
- **OS**: Compatible with Windows, macOS, or Linux.

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/mediapipe-vision-demos.git
   cd mediapipe-vision-demos


Install dependencies:
pip install -r requirements.txt

Or manually install:
pip install mediapipe opencv-python numpy


(Optional) Create a requirements.txt file:
mediapipe>=0.10.0
opencv-python>=4.5.0
numpy>=1.21.0



🚀 Usage

Ensure your webcam is connected or modify the script to use a video file (e.g., cv2.VideoCapture('video.mp4')).
Run any script from the terminal:python face_detection.py

Replace face_detection.py with the desired script (e.g., hand_tracking.py, pose_estimation.py, etc.).
A window will display the webcam feed with detection results:
Bounding boxes for faces (face_detection.py).
Landmarks and connections for hands (hand_tracking.py), pose (pose_estimation.py), or both (holistic_tracking.py).
Iris landmarks for eyes (iris_tracking.py).
Segmented hair (hair_segmentation.py) or person (selfie_segmentation.py).


Press q to exit the window.


Webcam Issues: If the webcam fails (cv2.VideoCapture(0)), try a different index (e.g., 1) or use a video file.
Module Errors: Ensure MediaPipe is updated (pip install --upgrade mediapipe).
Performance: For slow performance, reduce video resolution or use a lighter MediaPipe model (adjust model_selection in scripts).
Hair Segmentation: Note that hair_segmentation.py uses SelfieSegmentation as a proxy, as MediaPipe lacks a dedicated hair model.

📚 References

MediaPipe Official Documentation
MediaPipe Python Solutions
OpenCV Documentation
MediaPipe GitHub

📝 License
This project is licensed under the MIT License. See the LICENSE file for details.
🙌 Contributions
Contributions are welcome! Feel free to:

Submit pull requests for bug fixes or new features.
Open issues for questions or suggestions.
Star the repository to show support! 🌟

📬 Contact
For questions or feedback, create an issue or reach out via naveensanthosh830@gmail.com.

Happy coding! 🚀

### Enhancements Made
1. **Badges**: Added GitHub badges for Python version, MediaPipe, OpenCV, and MIT License for visual appeal and quick information.
2. **Structure**: Organized sections clearly with emojis for readability and a professional look.
3. **Requirements**: Included a `requirements.txt` suggestion for easy dependency management.
4. **Screenshots Placeholder**: Kept the screenshot section as a placeholder, as you can add images later to the repository.
5. **Troubleshooting**: Added a dedicated section for common issues, based on previous interactions (e.g., webcam or module errors).
6. **Consistency**: Corrected the typo in your original README (`selfi_segmentation.py` → `selfie_segmentation.py`) and ensured all file names match the provided scripts.
7. **Repository Name**: Suggested `mediapipe-vision-demos` as a placeholder; replace it with your actual repository name.
8. **License**: Referenced an MIT License file (you can create one if needed; let me know if you want a sample).

### Additional Files (Optional)
requirements.txt: Already included in the README setup instructions:mediapipe>=0.10.0
opencv-python>=4.5.0
numpy>=1.21.0
Next Steps

If you need help with any of these steps, want to add specific features, or need assistance setting up the repository, let me know!
