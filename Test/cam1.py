import cv2
from picamera2 import Picamera2
piCam=Picamera2()
piCam.preview_configuration.main.size=(1280,720)    # Biggest (1920, 1080) may not be 30 fps
piCam.preview_configuration.main.format="RGB888"
piCam.preview_configuration.align()
piCam.configure("preview")
piCam.start()
while True:
    frame=piCam.capture_array()
    cv2.imshow("piCam",frame)
    if cv2.waitKey(1)==ord('q'):
        break
cv2.destroyAllWindows()