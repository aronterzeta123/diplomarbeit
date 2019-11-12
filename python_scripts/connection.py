#!/usr/bin/python3.5
import MySQLdb

#def drop_tables(curs):
    #curs.execute("""Drop table if exists test1""")
#def create_tables(curs):
    #curs.execute("""create table test1(id int, name TEXT)""")
def insert_value(curs,id1,name1):
    add_test=("insert into test1(id,name) values(%s,'%s');")
    data_test=(id1,name1)
    curs.execute(add_test%data_test)
    return "inserted values"
#def read_value(curs):
    #curs.execute("select * from test1")
    #return curs.fetchall()
def insert_values1(curs,vorname,nachname,email,role):
    add_person("Insert into person(vorname,nachname,email,role)"\
            "Values(%s,%s,%s,%s)")
    data_person(vorname,nachname,email,role)
    curs.execute(add_person%data_person)
def insert_values2(curs, spX, spY, v1X,v1Y,v2X,v2Y,v3X, v3Y,v4X,v4Y,v5X,v5Y, v6X,v6Y,v7X,v7Y,v8X,v8Y,v9X,v9Y,v10X,v10Y,v11X,v11Y,v12X,v12Y,v13X,v13Y,v14X,v14Y,v15X,v15Y, imagePath, idP):
    add_info=("INSERT INTO info (spX, spY, v1X,v1Y,v2X,v2Y,v3X, v3Y,v4X,v4Y,v5X,v5Y, v6X,v6Y,v7X,v7Y,v8X,v8Y,v9X,v9Y,v10X,v10Y,v11X,v11Y,v12X,v12Y,v13X,v13Y,v14X,v14Y,v15X,v15Y, imagePath, idP)" \
                "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s)")

    data_info=(spX, spY, v1X,v1Y,v2X,v2Y,v3X, v3Y,v4X,v4Y,v5X,v5Y, v6X,v6Y,v7X,v7Y,v8X,v8Y,v9X,v9Y,v10X,v10Y,v11X,v11Y,v12X,v12Y,v13X,v13Y,v14X,v14Y,v15X,v15Y, imagePath, idP)
    curs.execute(add_info, data_info)
print ("Setting up database")
a=""
conn=MySQLdb.connect('localhost','aron','aronterzeta','test')
curs=conn.cursor()
#try:
    #drop_tables(curs)
    #conn.commit()
    #print ("Dropped tables")
#except:
    #conn.rollback()
    #print ("failed to drop")
#try:
    #create_tables(curs)
    #conn.commit()
    #print ("Created tables")
#except:
    #conn.rollback()
    #print ("failed to create")
print (a)
try:
    print("Vorname bitte eingeben: ")
    variable1=input()
    print("Nachname eingeben bitte:")
    variable2=int(input())
    print("email eingeben bitte:")
    variable3=input()
    print("Role eingeben bitte:")
    variable4=int(input())
    insert_values1(curs,variable1,variable2,variable3,variable4)
    #thrras funktionin e eglit edhe manejna i ndaj tdhanat me split edhe i thrras si parametra te funktioni inser_values2
    conn.commit()
    a="inserted values"
    #print ("inserted values")
except:
    conn.rollback()
    a="failed to insert"
#try:
 #   for row in read_values(curs):
  #      print ('Rei')
  #  print ("Read values")
#except:
   # conn.rollback()
   # print ("failed to read values")
