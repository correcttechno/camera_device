import io
import cv2
import time
import imutils
import numpy as np
import pytesseract
from PIL import Image
import multiprocessing as mp
import threading
#from picamera.array import PiRGBArray
#from picamera import PiCamera



#camera = PiCamera()
#camera.resolution = (640, 480)
#camera.framerate = 60
#rawCapture = PiRGBArray(camera, size=(640, 480))

camera = cv2.VideoCapture(0)
camera.set(1, 640)
camera.set(2, 480)

camera.set(cv2.CAP_PROP_FPS, 10)

ScreenCnt = None
Image=False
Cropped=False
Text=False
RealTimeImage=False

def ScanResults():
    global Image
    global Cropped
    global Text
    global ScreenCnt
    
    gray = cv2.cvtColor(Image,cv2.COLOR_BGR2GRAY)  #convert to grey scale
    gray = cv2.bilateralFilter(gray, 11, 17, 17)  #Blur to reduce noise
    edged = cv2.Canny(gray, 30, 200)  #Perform Edge detection
    cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE,
                                    cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]
    
    
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * peri, True)
        if len(approx) == 4:
            ScreenCnt = approx
            break
        if ScreenCnt is None:
            print("No contour detected")
        elif ScreenCnt is not None:
            mask = np.zeros(gray.shape, np.uint8)
            new_image = cv2.drawContours(
               mask,
               [ScreenCnt],
               0,
               255,
               -1,
            )
            new_image = cv2.bitwise_and(Image, Image, mask=mask)
            (x, y) = np.where(mask == 255)
            (topx, topy) = (np.min(x), np.min(y))
            (bottomx, bottomy) = (np.max(x), np.max(y))
            Cropped = gray[topx:bottomx + 1, topy:bottomy + 1]
            #cv2.imshow("Frame",Cropped)
            if True:
                Text = pytesseract.image_to_string(
                    Cropped,
                    config=
                    '--psm 11 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
                    )
                if (len(Text) > 6):
                    cv2.drawContours(Image, [ScreenCnt], -1, (0, 255, 0), 3)
                     
                    print("Detected Number is:", Text)
           


def StartCamera(callback):
    thisTime=0
    say=0
    global Image
    global RealTimeImage
    global Cropped
    global Text
    global ScreenCnt
    #for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    while True:
        ret, rawCapture = camera.read()
        Image = rawCapture
        RealTimeImage=rawCapture
        
        #Image = frame.array
        #RealTimeImage=frame.array
        
        key = cv2.waitKey(1) & 0xFF
        #rawCapture.truncate(0)
        
        if time.time()-thisTime>3 :
            say+=1
            thisTime=time.time()
            
            p3 = threading.Thread(target=ScanResults)
            p3.start()
             
        
        callback(Image,Cropped,Text,RealTimeImage)  