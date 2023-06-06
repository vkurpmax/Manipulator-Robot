import camcapture
from ultralytics import YOLO
import cv2
import torch
import numpy as np


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


# Install the dependencies
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
plt.style.use('bmh')

# Store the data into a data frame
df = pd.read_csv('tb_manip.csv')

xdata_img = np.array(df['x_img'])
xdata_manip = np.array(df['x_manip'])

# Reshape the data for sklearn
xdata_img = xdata_img.reshape((-1, 1))
xdata_manip = xdata_manip.reshape((-1, 1))

# Create a linear regression object
model = LinearRegression()

# Fit the model
model.fit(xdata_img, xdata_manip)

# Predict the y-values for the trendline
xdata_manip_pred = model.predict(xdata_img)

def plotfig():
    # Plot the original data points\
    plt.figure(figsize=(16,8))
    plt.scatter(xdata_img, xdata_manip, color='b', label='Data X')

    # Plot the trendline
    plt.plot(xdata_img, xdata_manip_pred, color='r', label='Trendline')

    # Add labels and title
    plt.xlabel('x_img')
    plt.ylabel('x_manip')
    plt.title('Trendline Plot')

    # Add legend
    plt.legend()

    # Show the plot
    plt.show()

#x_arr_img = 
x_manip_pred = model.predict(np.array([[x_img]]))
x_manipulator = round(x_manip_pred[0, 0])
print(x_manipulator)
