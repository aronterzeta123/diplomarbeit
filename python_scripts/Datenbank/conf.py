#!/usr/bin/python3
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
                                        rolle int,
                                        PRIMARY KEY (idP)
                                        )""")
    curs.execute("""CREATE TABLE info(
                                        idF int auto_increment,
                                        imagePath varchar(50),
                                        idP int,
                                        PRIMARY KEY (idF),
                                        FOREIGN KEY (idP) REFERENCES person (idP)
                                        )""")

def insert_values1(curs, vorname, nachname, email, rolle):
    add_person=("INSERT INTO person (vorname, nachname, email, rolle)" \
                "VALUES(%s,%s,%s,%s)")
    data_person=(vorname, nachname, email, rolle)
    curs.execute(add_person, data_person)

def insert_values2(curs, imagePath, idP, v1X, v1Y):
    add_person=("INSERT INTO info (imagePath, idP, v1X, v1Y)" \
                "VALUES(%s,%s,%s,%s)")
    data_person=(imagePath, idP, v1X, v1Y)
    curs.execute(add_person, data_person)

conn = MySQLdb.connect('','','127.0.0.1','diploma')
curs = conn.cursor()

try:
    drop_tables(curs)
    conn.commit()
    print ("Tables dropped")
except:
    conn.rollback
    print ("Table drop failed")

try:
    create_tables(curs)
    for x in range(1,65):
        valueX = "'v"+str(x)+"X'"
        valueY = "'v"+str(x)+"Y'"    
    
        curs.execute("SET @s1=CONCAT('ALTER table info add column `',%s,'` DECIMAL(10,10)');" % (valueX))
        curs.execute("Prepare stmt1 from @s1;")
        curs.execute("execute stmt1;")
        curs.execute("deallocate prepare stmt1;")
    
        curs.execute("SET @s2=CONCAT('ALTER table info add column `',%s,'` DECIMAL(10,10)');" % (valueY))
        curs.execute("Prepare stmt2 from @s2;")
        curs.execute("execute stmt2;")
        curs.execute("deallocate prepare stmt2;")
        conn.commit()
    print ("Tables Created")
except:
    conn.rollback
    print ("Failed to create tables")

try:
    insert_values1(curs,'jordi','zmiani','jorzmi14@htl-shkoder.com',1)
    insert_values1(curs,'jordi','zmiani','jorzmi14@htl-shkoder.com',1)
    insert_values1(curs,'jordi','zmiani','jorzmi14@htl-shkoder.com',1)
    insert_values1(curs,'jordi','zmiani','jorzmi14@htl-shkoder.com',1)
    insert_values1(curs,'jordi','zmiani','jorzmi14@htl-shkoder.com',1)
    insert_values1(curs,'jordi','zmiani','jorzmi14@htl-shkoder.com',1)
    insert_values2(curs,'../Pictures/sc1.png', 1, 0.101, 0.101)
    insert_values2(curs,'../Pictures/sc1.png', 1, 0.101, 0.101)
    insert_values2(curs,'../Pictures/sc1.png', 2, 0.101, 0.101)
    insert_values2(curs,'../Pictures/sc1.png', 3, 0.101, 0.101)
    insert_values2(curs,'../Pictures/sc1.png', 4, 0.101, 0.101)
    insert_values2(curs,'../Pictures/sc1.png', 5, 0.101, 0.101)
    insert_values2(curs,'../Pictures/sc1.png', 1, 0.101, 0.101)
    conn.commit()
    print ("Values inserted")
except:
    conn.rollback
    print ("Failed to insert values")

conn.close()
