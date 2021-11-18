import io
import cv2
import time
import imutils
import numpy as np
import pytesseract
import threading
import re
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
ScanImage=None
CroppedImage=None
Text=None
RealTimeImage=None
edged=None

def ScanResults():
    global ScanImage
    global RealTimeImage
    global CroppedImage
    global Text
    global ScreenCnt
    global edged
    while True:
        if(RealTimeImage is not None ):
           
            ScanImage=RealTimeImage
            gray = cv2.cvtColor(ScanImage,cv2.COLOR_BGR2GRAY)  #convert to grey scale
            gray = cv2.bilateralFilter(gray, 11, 17, 17)  #Blur to reduce noise
            edged = cv2.Canny(gray, 30, 200)  #Perform Edge detection
            cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE,
                                            cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
            cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]
           
            ScreenCnt = None
            Text=None
            for c in cnts:
                peri = cv2.arcLength(c, True)
                approx = cv2.approxPolyDP(c, 0.018 * peri, True)
                if len(approx) ==4:
                    ScreenCnt = approx
                    
                elif ScreenCnt is not None:
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
                        if Text!="" and Text is not None:
                            cv2.drawContours(ScanImage, [ScreenCnt], -1, (0, 255, 0), 3)
                            CroppedImage=Cropped
                       
                    
                    
                
           


def StartCamera(callback):
    
    global ScanImage
    global RealTimeImage
    global CroppedImage
    global Text
    global ScreenCnt
    #for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    p3 = threading.Thread(target=ScanResults,daemon=False)
    p3.start()
    while True:
        key = cv2.waitKey(1) & 0xFF
        ret, rawCapture = camera.read()
        RealTimeImage=rawCapture
        
        #ScanImage = frame.array
        #RealTimeImage=frame.array
        
        
        #rawCapture.truncate(0)
        
        #if time.time()-thisTime>2 :
            #say+=1
            #thisTime=time.time()
            #ScanResults()
            #
            
             
        
        callback(ScanImage,CroppedImage,Text,RealTimeImage)  