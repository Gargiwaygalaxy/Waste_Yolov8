
import requests
import cv2
import cvzone
import math
from ultralytics import YOLO

# Set up the YOLO model and video capture
model = YOLO("best.pt")
cap = cv2.VideoCapture(0)

cap.set(3, 640)
cap.set(4, 480)

classNames = ['dry', 'wet']
url = "http://ip-address/push-data"

def detect_and_send():
    global answer
    success, img = cap.read()
    if not success:
        print("Failed to capture image")
        return

    # Perform detection
    results = model(img, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            w, h = x2 - x1, y2 - y1
            cvzone.cornerRect(img, (x1, y1, w, h))

            conf = math.ceil((box.conf[0] * 100)) / 100
            cls = int(box.cls[0])
            answer = classNames[cls]
            cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)))

            # Prepare data to send
            data = {"data": answer}
            try:
                response = requests.post(url, json=data)
                if response.status_code == 200:
                    print("Data sent successfully!")
                    print(response.json())
                else:
                    print(f"Failed to send data. Status code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")

    # Display the image with detections
    cv2.imshow("image", img)
    cv2.waitKey(1)


while True:
    detect_and_send()

