#!/usr/bin/python3
import MySQLdb

def insert_procedure(curs):
    curs.execute("DROP PROCEDURE IF EXISTS addCol")
    curs.execute("""CREATE PROCEDURE addCol(IN name VARCHAR(50))
                    BEGIN
                        ALTER TABLE person
                        ADD name VARCHAR(50) NOT NULL;
                """)

def call_procedure(curs, value, vl):
    add = ("CALL newCol(%s);")
    print (value)
    data= (value)
    #curs.execute(add, data)

try:
    conn = MySQLdb.connect('localhost','aronterzeta','aronterzeta','test')
    curs = conn.cursor()
    print ("Database Working")
except:
    conn = MySQLdb.connect('localhost','aronterzeta','aronterzeta','test')
    curs = conn.cursor()
    print ("Backup Database Working")

try:
    for x in range(1,69):
        valueX = "'v"+str(x)+"X'"
        valueY = "'v"+str(x)+"Y'"    
    
        curs.execute("SET @s1=CONCAT('ALTER table person add column `',%s,'` double');" % (valueX))
        curs.execute("SET @s1=CONCAT('ALTER table person add column `',%s,'` double');" % ("'bo'"))
        curs.execute("SET @s1=CONCAT('ALTER table person add column `',%s,'` double');" % (valueX))
        curs.execute("Prepare stmt1 from @s1;")
        curs.execute("execute stmt1;")
        curs.execute("deallocate prepare stmt1;")
    
        curs.execute("SET @s2=CONCAT('ALTER table person add column `',%s,'` double');" % (valueY))
        curs.execute("Prepare stmt2 from @s2;")
        curs.execute("execute stmt2;")
        curs.execute("deallocate prepare stmt2;")
        conn.commit()
    print ("Procedure created")
except:
    conn.rollback    
    print ("Procedure failed")
    
conn.close()
