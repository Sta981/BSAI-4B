import cv2
import math
from object_detection import ObjectDetection

od = ObjectDetection()
cap = cv2.VideoCapture("DayTraffic.mp4")

count = 0
center_points_prev = []
tracking_objects = {}
track_id = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    count += 1

    (class_ids, scores, boxes) = od.detect(frame)
    center_points_cur = []

    for box in boxes:
        (x, y, w, h) = box

        if w > 400 or h > 400:
            continue

        cx = int((x + x + w) / 2)
        cy = int((y + y + h) / 2)
        center_points_cur.append((cx, cy))
        
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    new_tracking_objects = {}
    for pt in center_points_cur:
        for obj_id, prev_pt in tracking_objects.items():

            dist = math.hypot(pt[0] - prev_pt[0], pt[1] - prev_pt[1])

            if dist < 35:
                new_tracking_objects[obj_id] = pt
                break
        else:
            new_tracking_objects[track_id] = pt
            track_id += 1
    tracking_objects = new_tracking_objects.copy()

    for obj_id, pt in tracking_objects.items():
        cv2.circle(frame, pt, 5, (0, 0, 255), -1)
        cv2.putText(frame, f"Car ID: {obj_id}", (pt[0], pt[1] - 15), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    cv2.putText(frame, f"Frame: {count}", (20, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow("Real-Time Tracking - Lab 6", frame)
    
    key = cv2.waitKey(1)
    if key == 27: 
        break

cap.release()
cv2.destroyAllWindows()