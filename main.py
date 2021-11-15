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
from camera import StartCamera

from http import server
import multiprocessing as Process
import threading




PAGE=MyHtml()
          

CroppedImage=False
ScreenImage=False
ScreenRealTime=False

###
def myfun(image,cropped,text,realtime):

    #cv2.imshow("Frame",image)
    #output = StreamingOutput()
    global CroppedImage
    CroppedImage=cropped
    global ScreenImage
    ScreenImage=image
    global ScreenRealTime
    ScreenRealTime=realtime
    
def StartMyCamera():
    StartCamera(myfun)
        
def StartServer():
    print("Server basladi")
    address = ('', 8000)
    server = StreamingServer(address, StreamingHandler)
    server.serve_forever()
             

    
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
        elif self.path.find('/assets/')!=-1:
            ifile = open(self.path.lstrip('/'),'rb')
            content=ifile.read()
            ifile.close()
            
            if(self.path.find('.css')):
                conType='text/css'
            if(self.path.find('.js')):
                conType='text/javascript'
            if(self.path.find('.png')):
                conType='image/png'
            if(self.path.find('.jpg')):
                conType='image/jpeg'
            if(self.path.find('.woff')):
                conType='font/woff'
            if(self.path.find('.ttf')):
                conType='font/ttf'
            if(self.path.find('.otf')):
                conType='font/otf'
            if(self.path.find('.html')):
                conType='text/html'
            
            self.send_response(200)
            self.send_header('Content-Type', conType)
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
                    
                    global ScreenImage
                    image_bytes = cv2.imencode('.jpg', ScreenImage)[1].tobytes()
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
        elif self.path == '/realtime.mjpg':
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
                    
                    global ScreenRealTime
                    image_bytes = cv2.imencode('.jpg', ScreenRealTime)[1].tobytes()
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
    




#x = threading.Thread(target=thread_function, args=(1,))

p1 = threading.Thread(target=StartServer)
p2 = threading.Thread(target=StartMyCamera)

p1.start()
p2.start()
    