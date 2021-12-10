import io
import cv2
import imutils
import numpy as np
import pytesseract
import time
import logging
import socketserver
import base64
import json
from websocket_server import WebsocketServer
from camera import StartCamera,changeDisplay
from http import server
import cgi
import RPi.GPIO as GPIO
import threading
import database 
import textfilter

from views.homeView import HomeView
from views.whitelistView import WhitelistView
from views.whitelistaddView import WhitelistaddView

RELAY_PIN=23
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)


          

CroppedImage=None
ScreenImage=None
ScreenRealTime=None
ScreenText=""
ScreenTextStatus=False

OpenedText=None
OpenedDelay=0

#start camera
def myfun(image,cropped,text,realtime):

    #cv2.imshow("Frame",realtime)
    #output = StreamingOutput()
    if text is not None and text!='':
        global ScreenText
        global ScreenTextStatus
        
        global OpenedText
        global OpenedDelay
        global RELAY_PIN
        
        #if(True):
        if(time.time()-OpenedDelay>10):
                OpenedDelay=time.time()
                OpenedText=None
        
        ScreenText=textfilter.filter(text)

        result=database.searchCar(ScreenText)
        if(result  and ScreenText!=OpenedText):
            ScreenTextStatus=True
            GPIO.output(RELAY_PIN, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(RELAY_PIN, GPIO.LOW)
            OpenedText=ScreenText
        elif result:
            ScreenTextStatus=True
        else:
            ScreenTextStatus=False

        WSresponse=json.dumps([ScreenText,ScreenTextStatus])
        WebSocketSendMessage(WSresponse)
        #print("Detected Number is:", ScreenText)


    global CroppedImage
    if(cropped is not None):
        CroppedImage=cropped
    global ScreenImage
    if(image is not None):
        ScreenImage=image
    global ScreenRealTime
    if(realtime is not None):
        ScreenRealTime=realtime
    

#def StartMyCamera():
    #StartCamera(myfun)
#end camera


#http server
def StartServer():
    print("Server basladi")
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
    
    def do_POST(self):
        form = cgi.FieldStorage(
        fp=self.rfile,
        headers=self.headers,
        environ={
            'REQUEST_METHOD': 'POST',
            'CONTENT_TYPE': self.headers['Content-Type'],
        })
        response=""
        
        if(self.path=="/addplate"):
            database.addCar(form.getvalue('plate'))
            response="Added plate "+form.getvalue('plate')
        elif(self.path=="/deleteplate"):
            database.deleteCar(form.getvalue('id'))
            response="Deleted plate "
        elif(self.path=="/changedisplay"):
            changeDisplay(form.getvalue("mode"))
            response="Success"

        content = response.encode("utf-8")
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(content))
        self.end_headers()
        self.wfile.write(content)
    def do_GET(self):
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/index.html')
            self.end_headers()
        elif self.path == '/index.html':
            PAGE=HomeView()
            content = PAGE.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
        elif self.path == '/whitelist.html':
            PAGE=WhitelistView()
            content = PAGE.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
        elif self.path == '/whitelistadd.html':
            PAGE=WhitelistaddView()
            content = PAGE.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
        elif self.path.find('/assets/')!=-1:
            ifile = open("/home/pi/camera_device/"+self.path.lstrip('/'),'rb')
            content=ifile.read()
            ifile.close()
            
            conType=''
            if(self.path.find('.css')!=-1):
                conType='text/css'
            if(self.path.find('.js')!=-1):
                conType='text/javascript'
            if(self.path.find('.png')!=-1):
                conType='image/png'
            if(self.path.find('.jpg')!=-1):
                conType='image/jpeg'
            if(self.path.find('.woff')!=-1):
                conType='font/woff'
            if(self.path.find('.ttf')!=-1):
                conType='font/ttf'
            if(self.path.find('.otf')!=-1):
                conType='font/otf'
            if(self.path.find('.html')!=-1):
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
                image_bytes=[0]
                if(CroppedImage is not None):
                    image_bytes = cv2.imencode('.jpg', CroppedImage)[1].tobytes()
                
                    
                self.wfile.write(b'--FRAME\r\n')
                self.send_header('Content-Type', 'image/jpeg')
                self.send_header('Content-Length', len(image_bytes))
                self.end_headers()
                if(len(image_bytes)>10):
                    self.wfile.write(image_bytes)
                    self.wfile.write(b'\r\n')

            
        


class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True
    
#end http server


#websocket
WsServer=None
def NewWebSocketClient(client, server):
    global WsServer
    WsServer=server
    global ScreenText
    #server.send_message(client,"Salam")

thisTime=0
def WebSocketSendMessage(msg):
    global thisTime
    if(len(msg)>6 and (time.time()-thisTime>1 )):
        thisTime=time.time()
        WsServer.send_message_to_all(msg)
def StartWebSocket():
    global WsServer
    WsServer = WebsocketServer(host='', port=8082, loglevel=logging.INFO)
    WsServer.set_fn_new_client(NewWebSocketClient)
    WsServer.run_forever()
#end websocket

p1 = threading.Thread(target=StartServer)
#p2 = threading.Thread(target=StartMyCamera)

p3 = threading.Thread(target=StartWebSocket)
p1.start()
#p2.start()
p3.start()
StartCamera(myfun)