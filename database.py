import sqlite3
from datetime import datetime





def SQLquery(sql):
    
    con = sqlite3.connect('database/database.db')
    
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
    return [
        request_url,plate,date,scaned_image,cropped_image
    ]