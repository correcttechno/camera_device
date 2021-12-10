import requests
from database import readApiSettings





def checkNetwork(plate,scaned_image,croped_image):
    apiSettings=readApiSettings()

    url = apiSettings[0]
    myobj = {
        'plate': plate
    }
   
    
    x = requests.post(url, data = myobj,files={'file':scaned_image})

    print(x.text)
    return True