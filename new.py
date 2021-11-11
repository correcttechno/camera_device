import io
import cv2
import imutils
import numpy as np
import pytesseract
import time
import logging
import socketserver
import base64
from interface import MyHtml

from threading import Condition
from http import server

from PIL import Image
import multiprocessing as mp

from picamera.array import PiRGBArray
from picamera import PiCamera



camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 60
camera.rotation=45
rawCapture = PiRGBArray(camera, size=(640, 480))

#camera = cv2.VideoCapture(0)
#camera.set(1, 640)
#camera.set(2, 480)

#camera.set(cv2.CAP_PROP_FPS, 10)



PAGE=MyHtml()
CroppedImage=False

def StartCamera(callback,self):
    thisTime=0;
    say=0;
    
    Cropped=False
    screenCnt = None
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    #while True:
        #ret, rawCapture = camera.read()
        #image = rawCapture
        
        image = frame.array
        
        key = cv2.waitKey(1) & 0xFF
        rawCapture.truncate(0)
        if screenCnt is not None :
            cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 3)
        if time.time()-thisTime>1 :
            say+=1
            thisTime=time.time()
            gray = cv2.cvtColor(image,
                                cv2.COLOR_BGR2GRAY)  #convert to grey scale
            gray = cv2.bilateralFilter(gray, 11, 17, 17)  #Blur to reduce noise
            edged = cv2.Canny(gray, 30, 200)  #Perform Edge detection
            cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE,
                                    cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
            cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]
            screenCnt = None
            for c in cnts:
                peri = cv2.arcLength(c, True)
                approx = cv2.approxPolyDP(c, 0.018 * peri, True)
                if len(approx) == 4:
                    screenCnt = approx
                    break
            if screenCnt is None:
                print("No contour detectedd")
            elif screenCnt is not None:

                
                mask = np.zeros(gray.shape, np.uint8)
                new_image = cv2.drawContours(
                    mask,
                    [screenCnt],
                    0,
                    255,
                    -1,
                )
                new_image = cv2.bitwise_and(image, image, mask=mask)
                (x, y) = np.where(mask == 255)
                (topx, topy) = (np.min(x), np.min(y))
                (bottomx, bottomy) = (np.max(x), np.max(y))
                Cropped = gray[topx:bottomx + 1, topy:bottomy + 1]
                if True:
                    text = pytesseract.image_to_string(
                        Cropped,
                        config=
                        '--psm 11 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
                    )
                    if (len(text) > 6):
                        cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 3)
                        callback(image,Cropped,self) 
                        print(say,"Detected Number is:", text)
        
        callback(image,Cropped,self)            
    
            

###
def myfun(image,cropped,self):
    image_bytes = cv2.imencode('.jpg', image)[1].tobytes()
    #cv2.imshow("Frame",cropped)
    #output = StreamingOutput()
    global CroppedImage
    CroppedImage=cropped
    
    if self!=False:
        self.wfile.write(b'--FRAME\r\n')
        self.send_header('Content-Type', 'image/jpeg')
        self.send_header('Content-Length', len(image_bytes))
        self.end_headers()
        self.wfile.write(image_bytes)
        self.wfile.write(b'\r\n')
        
        
        
             

    
    #Uncomment the next line to change your Pi's Camera rotation (in degrees)
    #camera.rotation = 90

    


class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)


class StreamingHandler(server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/index.html')
            self.end_headers()
        elif self.path == '/index.html':
            content = PAGE.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
        elif self.path == '/stream.mjpg':
            self.send_response(200)
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Content-Type',
                             'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()
            try:
                #ret,img = camera.read()
                while True:
                    StartCamera(myfun,self)
                
                #cv2.imshow("Frame",frame)
            except Exception as e:
                logging.warning('Removed streaming client %s: %s',
                                self.client_address, str(e))
        elif self.path == '/cropped.mjpg':
            
            self.send_response(200)
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Content-Type',
                                 'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()
            while True:
                global CroppedImage
                image_bytes = cv2.imencode('.jpg', CroppedImage)[1].tobytes()
                self.wfile.write(b'--FRAME\r\n')
                self.send_header('Content-Type', 'image/jpeg')
                self.send_header('Content-Length', len(image_bytes))
                self.end_headers()
                self.wfile.write(image_bytes)
                self.wfile.write(b'\r\n')

            
        


class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True



address = ('', 8000)
server = StreamingServer(address, StreamingHandler)
server.serve_forever()
    