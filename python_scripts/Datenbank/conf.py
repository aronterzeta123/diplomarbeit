#!/usr/bin/python3
import MySQLdb

def drop_tables(curs):
    curs.execute('DROP TABLE IF EXISTS info')
    curs.execute('DROP TABLE IF EXISTS person')

def create_tables(curs):
    curs.execute("""CREATE TABLE person(
                                        vorname varchar(50) not null,
                                        nachname varchar(50) not null,
                                        email varchar(50) not null primary key,
                                        role int not null,
                                        imagePath varchar(50)
                                        );""")

def insert_values1(curs, vorname, nachname, email, rolle):
    add_person=("INSERT INTO person (vorname, nachname, email, role)" \
                "VALUES(%s,%s,%s,%s)")
    data_person=(vorname, nachname, email, rolle)
    curs.execute(add_person, data_person)

conn = MySQLdb.connect('localhost','aronterzeta','aronterzeta','test')
curs = conn.cursor()

try:
    drop_tables(curs)
    conn.commit()
    print ("Tables dropped")
except:
    conn.rollback()
    print ("Table drop failed")

try:
    create_tables(curs)
    conn.commit()
except:
    conn.rollback()
    print ("Failed to create tables")
conn.close()
