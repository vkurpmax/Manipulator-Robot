import cv2
from picamera2 import Picamera2

cam = Picamera2()
cam.preview_configuration.main.size=(1280,720)	# biggest (1920, 1080) may be can not 30 fps
cam.preview_configuration.main.format="RGB888"
cam.preview_configuration.align()
cam.configure("preview")
cam.start()

cv2.namedWindow("Python Webcam Screenshot App")

img_counter = 0

while True:
    frame=cam.capture_array()
    cv2.imshow("piCam",frame)
    k = cv2.waitKey(1)
    if k%256 == 27:
        print("Escape hit, closeing the app")
        break
    
    elif k%256 == 32:
        img_name = "img0000.png".format(img_counter)
        cv2.imwrite(img_name,frame)
        print("screenshot taken")
        print("Start Deep Learning Process. Please Wait!")
        img_counter += 1
        
cv2.destroyAllWindows()
