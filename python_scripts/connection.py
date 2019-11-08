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
    print("Name bitte eingeben: ")
    variable1=input()
    print("ID eingeben bitte:")
    variable2=int(input())
    insert_value(curs,variable2,variable1)
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
