import sqlite3
from datetime import datetime





def SQLquery(sql):
    
    con = sqlite3.connect('/home/pi/camera_device/database/database.db')
    
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



