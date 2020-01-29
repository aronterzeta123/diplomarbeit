#!/usr/bin/python3
import MySQLdb

def insert_procedure(curs):
    curs.execute("DROP PROCEDURE IF EXISTS addCol")
    curs.execute("""CREATE PROCEDURE addCol(IN name VARCHAR(50))
                    BEGIN
                        ALTER TABLE info
                        ADD name VARCHAR(50) NOT NULL;p
                """)

def call_procedure(curs, value, vl):
    add = ("CALL newCol(%s);")
    print (value)
    data= (value)
    #curs.execute(add, data)

try:
    conn = MySQLdb.connect('','','127.0.0.1','diploma')
    curs = conn.cursor()
    print ("Database Working")
except:
    conn = MySQLdb.connect('','','127.0.0.1','backup')
    curs = conn.cursor()
    print ("Backup Database Working")

try:
    for x in range(16,64):
        valueX = "'v"+str(x)+"X'"
        valueY = "'v"+str(x)+"Y'"    
    
        curs.execute("SET @s1=CONCAT('ALTER table info add column `',%s,'` VARCHAR(50)');" % ("'bo'"))
        curs.execute("SET @s1=CONCAT('ALTER table info add column `',%s,'` VARCHAR(50)');" % (valueX))
        curs.execute("Prepare stmt1 from @s1;")
        curs.execute("execute stmt1;")
        curs.execute("deallocate prepare stmt1;")
    
        curs.execute("SET @s2=CONCAT('ALTER table info add column `',%s,'` VARCHAR(50)');" % (valueY))
        curs.execute("Prepare stmt2 from @s2;")
        curs.execute("execute stmt2;")
        curs.execute("deallocate prepare stmt2;")
        conn.commit()
    print ("Procedure created")
except:
    conn.rollback    
    print ("Procedure failed")
    
conn.close()
