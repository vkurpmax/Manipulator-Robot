import camcapture
from ultralytics import YOLO
import cv2


# Load a model
#model = YOLO('yolov8n.pt')  # load an official model
model = YOLO('best_002.pt')  # load a custom model

# Predict with the model
results = model(source='img0000.png',
                conf=0.55,
                save=True,
                save_txt=True,
                show=True,
                show_labels=True)  # predict on an image

for result in results:
    boxes = result.boxes  # Boxes object for bbox outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    probs = result.probs  # Class probabilities for classification outputs
    
print(boxes.xyxy)