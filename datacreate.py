import numpy as np
import cv2
import sqlite3
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0)

def update(id, name):
        conn=sqlite3.connect("FaceBase.db")
        cmd="SELECT * FROM People WHERE ID=" + str(id)
        cursor = conn.execute(cmd)
        isExistId = 0
        for row in cursor:
                isExistId = 1
        if isExistId==1:
                sample=row[5]
                cmd = "UPDATE People SET Name=" + str(name) +", Age="+age+", Gender="+str(gender)+", Criminal_Records="+str(cr)+", Sample="+str(row[5]+1)+" WHERE Id="+str(id)
        else:
                cmd = "INSERT INTO People(ID,Name,Age,,Gender,Criminal_Records,Sample) VALUES(" + str(id) +"," + str(name)+","+age+","+str(gender)+","+str(cr)+", 1)"
                sample=0
        conn.execute(cmd)
        conn.commit()
        conn.close()
        return sample
        
id=raw_input('enter user id ')
name=raw_input('enter username ')
age=raw_input('enter age ')
gender=raw_input('enter gender ')
cr=raw_input('enter criminal record if any ')
sample = update(id, name)
sampleNum=sample*60

while(True):
        ret, img = cam.read()
        gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces=faceDetect.detectMultiScale(gray, 1.3, 5)
        for(x, y, h, w) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0),2)
                cv2.imwrite("dataset/User."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
                cv2.imshow("Face", img)
                cv2.waitKey(100)
                sampleNum+=1
        if(sampleNum>=(sample*60 + 60)):
                break
cam.release()
cv2.destroyAllWindows()
