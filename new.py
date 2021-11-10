import io
import cv2
import imutils
import numpy as np
import pytesseract
import time
import logging
import socketserver
import base64

from threading import Condition
from http import server

from PIL import Image
import multiprocessing as mp

#from picamera.array import PiRGBArray
#from picamera import PiCamera

print("axtarilir")

#camera = PiCamera()
#camera.resolution = (640, 480)
#camera.framerate = 90
#rawCapture = PiRGBArray(camera, size=(640, 480))

camera = cv2.VideoCapture(0)
camera.set(3, 640)
camera.set(4, 480)
ret,image

PAGE = """\
<html>
<head>
<title>MSB Camera</title>
</head>
<body>
<center><h1>MSB Camera</h1></center>
<center><img src="stream.mjpg" width="640" height="480"></center>
</body>
</html>
"""


def StartCamera(callback):
    #for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    while True:
        ret, rawCapture = camera.read()
        image = rawCapture
        
        #image = frame.array
        key = cv2.waitKey(1) & 0xFF
        #rawCapture.truncate(0)
        if True:

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

                cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 3)
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
                for i in range(3, 14):
                    text = pytesseract.image_to_string(
                        Cropped,
                        config=
                        '--psm 11 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
                    )
                    if (len(text) >= 7):
                        print("Detected Number is:", text)
                callback(image)            
        return image
            

###
def myfun(dat):
    
    cv2.imshow("Cropped", dat)
    image=dat
    #Uncomment the next line to change your Pi's Camera rotation (in degrees)
    #camera.rotation = 90
    address = ('', 8000)
    server = StreamingServer(address, StreamingHandler)
    server.serve_forever()
    


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
                ret,img = camera.read()
                image_bytes = cv2.imencode('.jpg', img)[1].tobytes()
                #cv2.imshow("Frame",output)
                #output = StreamingOutput()
                self.wfile.write(b'--FRAME\r\n')
                self.send_header('Content-Type', 'image/jpeg')
                self.send_header('Content-Length', len(image_bytes))
                self.end_headers()
                self.wfile.write(image_bytes)
                self.wfile.write(b'\r\n')
                #cv2.imshow("Frame",frame)
            except Exception as e:
                logging.warning('Removed streaming client %s: %s',
                                self.client_address, str(e))
        else:
            self.send_error(404)
            self.end_headers()


class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True




while camera:
    StartCamera(myfun)
    
    


