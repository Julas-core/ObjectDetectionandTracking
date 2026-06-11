# Object Detection and Tracking with YOLOv8

This project provides a simple implementation of real-time object detection and tracking using the YOLOv8 model on a video file.

## Prerequisites

- Python 3.8+
- OpenCV (`cv2`)
- `ultralytics` (for YOLOv8)

## Installation

1. Clone the repository.
2. Install the required dependencies:

```bash
pip install ultralytics opencv-python
```

## Usage

1. Ensure `yolov8n.pt` (the pre-trained model) and `video.mp4` (the target video) are in the project root directory.
2. Run the main script:

```bash
python main.py
```

- The script will open a window displaying the processed video with bounding boxes and object tracking IDs.
- Press `q` to exit the video display.

## File Structure

- `main.py`: The main script for detection and tracking.
- `video.mp4`: Input video file for processing.
- `yolov8n.pt`: Pre-trained YOLOv8 model weights.
- `test.py`: An auxiliary script for unrelated credit card validation.
- `requirements.txt`: Project dependency list.
