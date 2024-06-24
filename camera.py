import io
import cv2
import time
import imutils
import numpy as np
import pytesseract
import threading
import re
from openalpr import Alpr
#from picamera.array import PiRGBArray
#from picamera import PiCamera



#camera = PiCamera()
#camera.resolution = (1296, 976)
#camera.framerate = 30
#rawCapture = PiRGBArray(camera, size=(1296, 972))

#camera = cv2.VideoCapture("rtsp://admin:ruslan1424%@192.168.16.64:554/Streaming/Channels/101")
camera = cv2.VideoCapture(0)
#camera.set(1, 1296)
#camera.set(2, 972)

#camera.set(cv2.CAP_PROP_FPS, 30)

CroppedImage=None
ScreenImage=None
ScreenRealTime=None
ScreenText=""


def ScanResults():
    global ScreenRealTime
    global ScreenImage
    global ScreenText
    global CroppedImage
    
    if True:
        frame=ScreenRealTime
        # OpenALPR nesnesini başlat
        alpr = Alpr("sg", "/etc/openalpr/openalpr.conf", "/usr/share/openalpr/runtime_data")

        # Alpr başlatılamazsa hata mesajı ver
        if not alpr.is_loaded():
            print("OpenALPR yüklenemedi. Lütfen yüklemeyi kontrol edin.")
            return frame

        # Plakaları tanı
        results = alpr.recognize_ndarray(frame)

        # Tanımlanan plakaları çerçevele
        for plate in results['results']:
            for candidate in plate['candidates'][:1]:
                # Plakayı ve güven puanını al
                plate_str = candidate['plate']
                confidence = candidate['confidence']

                #if plate_str in plates:
                """  GPIO.output(output_pin, GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(output_pin, GPIO.LOW) """
                ScreenText=plate_str

                # Plakayı ve güven puanını çerçevele
                if confidence > 0:
                    coordinates = plate['coordinates']

                    x1, y1 = coordinates[0]['x'], coordinates[0]['y']
                    x2, y2 = coordinates[2]['x'], coordinates[2]['y']

                    CroppedImage=ScreenRealTime[y1:y2, x1:x2]

                    cv2.rectangle(frame, (x1, y1),
                                (x2, y2), (255, 0, 0), 2)
                    #cv2.putText(frame, plate_str, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX,
                    #            2, (0, 255, 0), 2)
                    

        alpr.unload()
        ScreenImage=frame
                     
                    
                    
                
           


def StartCamera(callback):
    global ScreenImage
    global ScreenRealTime
    global ScreenText
    global CroppedImage

    #p3 = threading.Thread(target=ScanResults,daemon=False)
    #p3.start()
    #for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    while True:
        key = cv2.waitKey(1) & 0xFF
        ret, fr = camera.read()
        ScreenRealTime=fr
        threading.Thread(target=ScanResults,daemon=False).start()
        callback(ScreenImage,CroppedImage,ScreenText,fr)  