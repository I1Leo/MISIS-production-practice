import cv2
from ultralytics import YOLO

model_path = './detector/models/best.pt'
model = YOLO(model_path)


def get_corners(box):
    x_center, y_center, width, height = box[:4]
    x1 = x_center - width / 2
    y1 = y_center - height / 2
    x2 = x_center + width / 2
    y2 = y_center + height / 2
    return (x1, y1), (x2, y1), (x1, y2), (x2, y2)


def find_rectangle_corners(image_path):
    img = cv2.imread(image_path)
    results = model.predict(img)
    pred_boxes = results[0].boxes.xywhn.cpu()
    corners = [get_corners(box) for box in pred_boxes]
    flattened_corners = [corner for corner_set in corners for corner in corner_set]
    return flattened_corners
