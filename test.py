import cv2
import imutils
import numpy as np
import pytesseract
import time
from PIL import Image
from picamera.array import PiRGBArray
from picamera import PiCamera

print("axtarilir")

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(640, 480))

say=0
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        say=say+1
        
        image = frame.array
        #cv2.imshow("Frame", image)
        key = cv2.waitKey(1) & 0xFF
        rawCapture.truncate(0)
        if key != ord("s") and say==20:
             say=0
             gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #convert to grey scale
             gray = cv2.bilateralFilter(gray, 11, 17, 17) #Blur to reduce noise
             edged = cv2.Canny(gray, 30, 200) #Perform Edge detection
             cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE,              cv2.CHAIN_APPROX_SIMPLE)
             cnts = imutils.grab_contours(cnts)
             cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
             screenCnt = None
             for c in cnts:
                peri = cv2.arcLength(c, True)
                approx = cv2.approxPolyDP(c, 0.018 * peri, True)
                if len(approx) == 4:
                  screenCnt = approx
                  break
             if screenCnt is None:
               print ("No contour detected")
               
             elif screenCnt is not None:
                 
                 cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 3)
                 mask = np.zeros(gray.shape,np.uint8)
                 new_image = cv2.drawContours(mask,[screenCnt],0,255,-1,)
                 new_image = cv2.bitwise_and(image,image,mask=mask)
                 (x, y) = np.where(mask == 255)
                 (topx, topy) = (np.min(x), np.min(y))
                 (bottomx, bottomy) = (np.max(x), np.max(y))
                 Cropped = gray[topx:bottomx+1, topy:bottomy+1]
                 #for i in range(3,14):
                 text = pytesseract.image_to_string(Cropped, config='--psm 11 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
                 if(len(text)>=7):
                     print("Detected Number is:",text)
                     cv2.imshow("Cropped", Cropped)
             
             #server.sendmail("Sender's Email ID@gmail.com","Sender's Email ID@gmail.com",text)
             
             cv2.imshow("Frame",edged );
             #cv2.waitKey(0)
             #break
cv2.destroyAllWindows()