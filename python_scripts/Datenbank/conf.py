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

conn = MySQLdb.connect('localhost','aronterzeta','aronterzeta','test')
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
    conn.commit()
    print "Values inserted"
except:
    print "Failed to insert values"

conn.close()
