#!/usr/bin/python3.5
import MySQLdb
import sys
conn=MySQLdb.connect('localhost','aronterzeta','aronterzeta','test')
mycursor=conn.cursor()
var1=input("Bitte email eingeben")
b=""
d=sys.argv[1]
print(b)
bool=False
myresult=""
try:
    mycursor.execute("select * from person p join info i on p.idP = i.idP where p.email='%s'"%(var1))
    global myresult
    myresult=mycursor.fetchall()
    for x in myresult:
        if x[3]==var1:
            bool=True
        else:
            bool=False
except:
    print ("Select Statement nicht gut")
if bool:
    os.system('./Log_Erkennung_PersonExistiert.py')
    b="existiert"
    for res in myresult:
        exec(open('68fLandmarks2.py').read())
        for x in range(17):
            for y in range(17):
                i=3
                if(arrayvlera[[x][y]]==res[i]):
                    print("Kot")
                    i+=1
                y+=1
            x+=1
        #array1 = getPoints(fotojaprejkameras)
        #array2 = getPoints(fotojadatenbankepersonit)
        #match = 'true'
        #for x in range(68):
        #   x = arra1[x][0] - arra2[x][0]
        #   y = arra1[x][1] - arra2[x][1]
        #   d = rranja((x*x)+(y*y))
        #   if d>toleranc:
        #       match='false'
        #   break
else:
    os.system('./Log_Erkennung_PersonExistiertNicht.py')
    b="nicht existiert"

        
