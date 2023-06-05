import camcapture
from ultralytics import YOLO
import cv2
import torch


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

tensor = boxes.xyxy.clone().detach().requires_grad_(True)
x_img = (tensor[1,0].item() + (tensor[1,2].item() - tensor[1,0].item()) / 2) - tensor[0,0].item()
y_img = tensor[0,3].item() - (tensor[1,1].item() + (tensor[1,3].item() - tensor[1,1].item()) / 2)

print(f"{x_img:.1f}, {y_img:.1f}")
