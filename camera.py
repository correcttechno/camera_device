import io
import cv2
import time
import imutils
import numpy as np
import pytesseract
import threading
import re
from picamera.array import PiRGBArray
from picamera import PiCamera



camera = PiCamera()
camera.resolution = (1296, 976)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(1296, 972))

#camera = cv2.VideoCapture(0)
#camera.set(1, 1296)
#camera.set(2, 972)

#camera.set(cv2.CAP_PROP_FPS, 30)

ScreenCnt = None
ScanImage=None
CroppedImage=None
Text=None
RealTimeImage=None
edged=None

scanData="normal"

def changeDisplay(dat):
    global scanData
    scanData=dat

def ScanResults():
    global ScanImage
    global RealTimeImage
    global CroppedImage
    global Text
    global ScreenCnt
    global edged
    thisTime=0
    while True:
        
            
        if(RealTimeImage is not None and time.time()-thisTime>2):
            thisTime=time.time()
            ScanImage=RealTimeImage
            gray = cv2.cvtColor(ScanImage,cv2.COLOR_BGR2GRAY)  #convert to grey scale
            gray = cv2.bilateralFilter(gray, 11, 17, 17)#Blur to reduce noise
            #gray=cv2.morphologyEx(gray,cv2.MORPH_RECT,(3,3))
            #gray=cv2.threshold(gray,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)[1]
            edged = cv2.Canny(gray, 30, 500)  #Perform Edge detection
            cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE,
                                            cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
            cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]
           
            
            Text=None
            for c in cnts:
                ScreenCnt = None
                peri = cv2.arcLength(c, True)
                approx = cv2.approxPolyDP(c, 0.018 * peri, True)
                applen=len(approx)
                if applen==4:
                    ScreenCnt = approx
                    mask = np.zeros(gray.shape, np.uint8)
                    new_image = cv2.drawContours(
                    mask,
                    [ScreenCnt],
                    0,
                    255,
                    -1,
                    )
                    new_image = cv2.bitwise_and(ScanImage, ScanImage, mask=mask)
                    (x, y) = np.where(mask == 255)
                    (topx, topy) = (np.min(x), np.min(y))
                    (bottomx, bottomy) = (np.max(x), np.max(y))
                    Cropped = gray[topx:bottomx + 1, topy:bottomy + 1]
                    #cv2.imshow("Frame",Cropped)
                    if True:
                        #reader = easyocr.Reader(['en'], gpu = True) 
                        #print(reader.readtext(Cropped))
                        Text = pytesseract.image_to_string(
                            Cropped,
                            config=
                            '--psm 11 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
                            )
                       
                        Text=re.sub('[^A-Za-z0-9]+', '', Text)
                        if Text!="" and Text is not None and len(Text)>6:
                            #cv2.drawContours(ScanImage, [ScreenCnt], -1, (0, 255, 0), 3)
                            CroppedImage=Cropped
                            
                        else:
                            Text=None
                     
                    
                    
                
           


def StartCamera(callback):
    
    global ScanImage
    global RealTimeImage
    global CroppedImage
    global Text
    global ScreenCnt
    global scanData
    
    p3 = threading.Thread(target=ScanResults,daemon=False)
    p3.start()
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    #while True:
        key = cv2.waitKey(1) & 0xFF
        #ret, rawCapture = camera.read()
        #RealTimeImage=rawCapture
        
        #ScanImage = frame.array
        RealTimeImage=frame.array
        
        
        rawCapture.truncate(0)
        
        #if time.time()-thisTime>2 :
            #say+=1
            #thisTime=time.time()
            #ScanResults()
            #
            
             
        
        if(scanData=="normal"):
            callback(ScanImage,CroppedImage,Text,RealTimeImage)  
        else:
            callback(edged,CroppedImage,Text,RealTimeImage)