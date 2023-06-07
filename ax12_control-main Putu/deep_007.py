import camcapture   # Running camcapture.py
from ultralytics import YOLO
import cv2
import torch
import numpy as np


# Load a model
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


# Install the dependencies
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Store the data into a data frame
df = pd.read_csv('tb_manip.csv')

# Take corresponding data into variables
xdata_img = np.array(df['x_img'])
ydata_img = np.array(df['y_img'])
xdata_manip = np.array(df['x_manip'])
ydata_manip = np.array(df['y_manip'])

# Reshape the data for sklearn
xdata_img = xdata_img.reshape((-1, 1))
ydata_img = ydata_img.reshape((-1, 1))
xdata_manip = xdata_manip.reshape((-1, 1))
ydata_manip = ydata_manip.reshape((-1, 1))

### FOR X MODEL ###
# Create a linear regression object
model = LinearRegression()
# Fit the model
model1 = model.fit(xdata_img, xdata_manip)


### FOR Y MODEL ###
# Create a linear regression object
model = LinearRegression()
# Fit the model
model2 = model.fit(ydata_img, ydata_manip)


x_manip_pred = model1.predict(np.array([[x_img]]))
y_manip_pred = model2.predict(np.array([[y_img]]))
x_manipulator = round(x_manip_pred[0, 0])
y_manipulator = round(y_manip_pred[0, 0])
print(x_manipulator, y_manipulator)
