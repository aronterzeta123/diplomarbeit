#!/usr/bin/env python
import MySQLdb

def insert_values1(curs, vorname, nachname, email, role):
    add_person=("INSERT INTO person (vorname, nachname, email, role)" \
                "VALUES(%s,%s,%s,%s)")
    data_person=(vorname, nachname, email, role)
    curs.execute(add_person, data_person)

def insert_values2(curs, spX, spY, v1X,v1Y,v2X,v2Y,v3X, v3Y,v4X,v4Y,v5X,v5Y, v6X,v6Y,v7X,v7Y,v8X,v8Y,v9X,v9Y,v10X,v10Y,v11X,v11Y,v12X,v12Y,v13X,v13Y,v14X,v14Y,v15X,v15Y, imagePath, idP):
    add_info=("INSERT INTO info (spX, spY, v1X,v1Y,v2X,v2Y,v3X, v3Y,v4X,v4Y,v5X,v5Y, v6X,v6Y,v7X,v7Y,v8X,v8Y,v9X,v9Y,v10X,v10Y,v11X,v11Y,v12X,v12Y,v13X,v13Y,v14X,v14Y,v15X,v15Y, imagePath, idP)" \
                "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s)")

    data_info=(spX, spY, v1X,v1Y,v2X,v2Y,v3X, v3Y,v4X,v4Y,v5X,v5Y, v6X,v6Y,v7X,v7Y,v8X,v8Y,v9X,v9Y,v10X,v10Y,v11X,v11Y,v12X,v12Y,v13X,v13Y,v14X,v14Y,v15X,v15Y, imagePath, idP)
    curs.execute(add_info, data_info)

conn = MySQLdb.connect('','','127.0.0.1','diploma')
curs = conn.cursor()

try:
    insert_values1(curs,'Elaine','Burton','elaine@htl-shkoder.com',0)
    insert_values1(curs,'Berty','Henry','berty@htl-shkoder.com',0)
    insert_values1(curs,'Logan','May','logan@htl-shkoder.com',0)
    insert_values1(curs,'Mack','Howard','mack@htl-shkoder.com',0)
    insert_values1(curs,'Douglas','Marshall','douglas@htl-shkoder.com',0)
    insert_values1(curs,'Amos','Reeves','amos@htl-shkoder.com',0)
    insert_values1(curs,'Pedro','Buchanan','pedro@htl-shkoder.com',0)
    insert_values2(curs, 202,109,122,121,112,121,112,101,103,102,101,102,140,120,103,120,130,120,120,140,120,110,120,210,121,110,130,140,130,137,171,103,'../Pictures/image1.jpg', 2)
    insert_values2(curs, 222,110,104,120,112,121,112,111,103,102,101,102,141,131,101,120,130,111,120,132,120,120,121,211,120,110,130,110,120,120,121,133,'../Pictures/image2.jpg', 3)
    insert_values2(curs, 202,111,122,111,112,121,114,101,103,101,111,102,110,111,104,110,130,110,120,133,122,113,120,214,130,110,120,110,121,120,128,124,'../Pictures/image3.jpg', 4)
    insert_values2(curs, 242,132,121,130,112,121,122,101,133,102,101,122,140,120,111,120,135,123,120,120,121,120,110,215,124,110,130,110,130,131,131,135,'../Pictures/image4.jpg', 5)
    insert_values2(curs, 245,121,132,110,112,121,112,121,103,122,101,102,130,123,151,120,120,111,120,134,120,112,122,220,150,130,130,110,124,120,101,123,'../Pictures/image5.jpg', 6)
    insert_values2(curs, 223,119,112,122,112,121,112,101,103,102,131,102,140,110,112,120,111,140,122,130,123,130,135,230,127,110,130,110,110,130,120,125,'../Pictures/image6.jpg', 7)
    insert_values2(curs, 211,119,122,130,112,121,112,101,103,102,101,102,144,120,101,120,131,113,120,130,110,111,120,211,120,112,130,110,120,130,121,123,'../Pictures/image7.jpg', 8)
    conn.commit()
    print "Values inserted"
except:
    conn.rollback
    print "Failed to insert values"

conn.close()
