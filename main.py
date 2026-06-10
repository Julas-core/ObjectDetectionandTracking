from ultralytics import YOLO
import cv2
import time

model = YOLO('yolov8n.pt')

cap = cv2.VideoCapture("video.mp4")
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

for _ in range(5):
    cap.read()
    time.sleep(0.1)


while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.track(frame, persist=True)
    annotated = results[0].plot()

    cv2.imshow('OBject Detection', annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()