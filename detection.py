import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

print("Press 'q' to quit")
print("Object Detection and Tracking Running...")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to get frame")
        break

    results = model.track(
        frame,
        persist=True,
        tracker="bytetrack.yaml"
    )

    annotated_frame = results[0].plot()

    cv2.imshow("Object Detection and Tracking", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


print("Detection and Tracking stopped!")


