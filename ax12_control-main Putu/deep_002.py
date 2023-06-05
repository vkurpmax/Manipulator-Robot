from ultralytics import YOLO

# Load a model
#model = YOLO('yolov8n.pt')  # load an official model
model = YOLO('best_002.pt')  # load a custom model

# Predict with the model
results = model(source='img0004.png',
                conf=0.55,
                save=True,
                save_txt=True,
                show=True,
                show_labels=True)  # predict on an image
