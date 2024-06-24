import sqlite3
from datetime import datetime
import hashlib
import random




def SQLquery(sql):
    
    con = sqlite3.connect('/home/msb/camera_software/database/database.db')
    
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    return cur


# car functions
def addCar(plate):
    now = datetime.now()
    Nowdate = now.strftime("%d/%m/%Y %H:%M:%S")
    sql="insert into cars('plate','addDate') values('"+str(plate).upper()+"','"+Nowdate+"')"
    SQLquery(sql)

def deleteCar(id):
    sql="delete from cars where id="+str(id)
    SQLquery(sql)

def updateCar(plate,id):
    sql="update cars set plate='"+plate+"' where id="+str(id)
    SQLquery(sql)

def selectCars():
    sql="select * from cars order by id desc"
    return SQLquery(sql)

def selectCar(id):
    sql="select * from cars where id="+str(id)
    return SQLquery(sql).fetchone()

def searchCar(plate):
    sql="select * from cars where plate='"+plate+"'"
    res=SQLquery(sql).fetchone()
    if(res is not None):
        return res
    else:
        return False
#end car functions



#api functions

def editApi(request_url,plate,date,scaned_image,cropped_image):
    if(request_url is None):
        request_url=''
    sql="update settings set value='"+request_url+"' where key='api_request_url'"
    SQLquery(sql)

    sql="update settings set value='"+plate+"' where key='api_plate'"
    SQLquery(sql)

    sql="update settings set value='"+date+"' where key='api_date'"
    SQLquery(sql)

    sql="update settings set value='"+scaned_image+"' where key='api_scaned_image'"
    SQLquery(sql)

    sql="update settings set value='"+cropped_image+"' where key='api_cropped_image'"
    SQLquery(sql)

def readApi():
    sql="select * from settings where key like 'api_%'"
    return SQLquery(sql)

def readApiSettings():
    request_url=''
    plate=''
    date=''
    scaned_image=''
    cropped_image=''

    for row in readApi():
        if(row[1]=='api_request_url'):
            request_url=row[2]
        elif(row[1]=='api_plate' and row[2]=='1'):
            plate=row[2]
        elif(row[1]=='api_date' and row[2]=='1'):
            date=row[2]
        elif(row[1]=='api_scaned_image' and row[2]=='1'):
            scaned_image=row[2]
        elif(row[1]=='api_cropped_image' and row[2]=='1'):
            cropped_image=row[2]
    return {
        'request_url':request_url,'plate':plate,'date':date,'scaned_image':scaned_image,'cropped_image':cropped_image
    }


def setLogin(username,password):
    sql="select * from settings where key='login_username'"
    seluser=SQLquery(sql).fetchone()[2]
    sql="select * from settings where key='login_password'"
    selpass=SQLquery(sql).fetchone()[2]

    if(seluser==username and selpass==password):
        uid=round(random.random()*100000)
        sql="update settings set value='"+str(uid)+"' where key='login_token'"
        SQLquery(sql)
        return str(uid)
    else:
        return False


def getToken(url):
    sql="select value from settings where key='login_token'"
    result=SQLquery(sql)
    return url+"?token="+result.fetchone()[0]

def setRootPassword(password,token):
    sql="select value from settings where key='login_token'"
    result=SQLquery(sql)
    mytoken=result.fetchone()[0]
    if(token==mytoken):
        sql="update settings set value='"+password+"' where key='login_password'"
        SQLquery(sql)
        return True
    else:
        return False

def setNewToken():
    uid=round(random.random()*100000)
    sql="update settings set value='"+str(uid)+"' where key='login_token'"
    SQLquery(sql)