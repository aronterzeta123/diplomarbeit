#!/usr/bin/env python
import MySQLdb

def drop_tables(curs):
    curs.execute('DROP TABLE IF EXISTS info')
    curs.execute('DROP TABLE IF EXISTS person')

def create_tables(curs):
    curs.execute("""CREATE TABLE person(
                                        idP int auto_increment,
                                        vorname varchar(50),
                                        nachname varchar(50),
                                        email varchar(50),
                                        role int,
                                        PRIMARY KEY (idP)
                                        )""")
    curs.execute("""CREATE TABLE info(
                                        idF int auto_increment,
                                        spX decimal,
                                        spY decimal,
                                        v1X decimal,
                                        v1Y decimal,
                                        v2X decimal,
                                        v2Y decimal,
                                        v3X decimal,
                                        v3Y decimal,
                                        v4X decimal,
                                        v4Y decimal,
                                        v5X decimal,
                                        v5Y decimal,
                                        v6X decimal,
                                        v6Y decimal,
                                        v7X decimal,
                                        v7Y decimal,
                                        v8X decimal,
                                        v8Y decimal,
                                        v9X decimal,
                                        v9Y decimal,
                                        v10X decimal, 
                                        v10Y decimal,
                                        v11X decimal,
                                        v11Y decimal,
                                        v12X decimal,
                                        v12Y decimal,
                                        v13X decimal,
                                        v13Y decimal,
                                        v14X decimal,
                                        v14Y decimal,
                                        v15X decimal,
                                        v15Y decimal,
                                        imagePath varchar(50),
                                        idP int,
                                        PRIMARY KEY (idF),
                                        FOREIGN KEY (idP) REFERENCES person (idP)
                                        )""")

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
    drop_tables(curs)
    conn.commit()
    print "Tables dropped"
except:
    conn.rollback
    print "Table drop failed"

try:
    create_tables(curs)
    conn.commit()
    print "Created tables"
except:
    conn.rollback
    print "Failed to create tables"

try:
    insert_values1(curs,'jordi','zmiani','jorzmi14@htl-shkoder.com',1)
    insert_values2(curs, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,'../Pictures/sc1.png', 1)
    conn.commit()
    print "Values inserted"
except:
    print "Failed to insert values"

conn.close()
