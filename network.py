import cv2
import requests
import json
import time
import os
from datetime import date
from database import readApiSettings





def checkNetwork(plate,scaned_image,croped_image):
    try:
        apiSettings=readApiSettings()
        url = apiSettings['request_url']

        if(url is not None and url!=''):
           
            
            image_name=str(time.time())+"_img"
            scaned_image_location="images/scaned/"+image_name+".jpg"
            croped_image_location="images/cropped/"+image_name+".jpg"

            if(scaned_image is not None):
                cv2.imwrite(scaned_image_location,scaned_image)
            if(croped_image is not None):
                cv2.imwrite(croped_image_location,croped_image)

            myfiles={}
            myobj = {
                'status':True
            }
            
            if(apiSettings['scaned_image']=='1'):
                myfiles['scaned']=open(scaned_image_location, 'rb')
            if(apiSettings['cropped_image']=='1'):
                myfiles['cropped']=open(croped_image_location, 'rb')
            if(apiSettings['plate']=='1'):
                myobj['plate']=plate
            if(apiSettings['date']=='1'):
                today = date.today()
                myobj['date']=today.strftime("%d/%m/%Y %H:%M:%S")

            x = requests.post(url, data = myobj,files=myfiles)

            response=json.loads(x.text)
            if(response['status']=='success'):
                return True
            else:
                os.remove(scaned_image_location)
                os.remove(croped_image_location)
                return False
    
    except:
        return False
    