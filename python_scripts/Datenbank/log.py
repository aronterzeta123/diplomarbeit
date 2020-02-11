#!/usr/bin/python3
import MySQLdb

def drop_tables(curs):
    curs.execute('DROP TABLE IF EXISTS log')

def create_tables(curs):
    curs.execute("""CREATE TABLE log(
                                        idL int auto_increment,
                                        user varchar(50), 
                                        date datetime,
                                        info varchar(50),
                                        id int,
                                        PRIMARY KEY (idL)
                                        )""")

def insert_values1(curs, vorname, nachname, email, rolle):
    add=("INSERT INTO person (vorname, nachname, email, rolle)" \
                "VALUES(%s,%s,%s,%s)")
    data=(vorname, nachname, email, rolle)
    curs.execute(add, data)

def insert_values2(curs):
    add=("UPDATE person SET vorname = 'Rando' WHERE idP = 1 ")
    curs.execute(add)

def insert_values3(curs):
    add=("""  INSERT INTO info (imagePath, idP)
                    VALUES('../Pictures/asdf.jpg',1)""")
    curs.execute(add)

def insert_values4(curs):
    add=(""" UPDATE info
                    SET idP = 1
                    WHERE idF = 1
                    """)
    curs.execute(add)

def newUser(curs):
    curs.execute("DROP TRIGGER IF EXISTS newUser")
    curs.execute("""CREATE TRIGGER newUser
                    AFTER INSERT 
                    ON person 
                    FOR EACH ROW
                    BEGIN
                        DECLARE lastid int;
                        SELECT MAX(idP) into lastid from person;
                        INSERT INTO log (user, date, info, id) VALUES (current_user(), now(), "User Registered", lastid);
                    END
                """)

def updateUser(curs):
    curs.execute("DROP TRIGGER IF EXISTS updateUser")
    curs.execute("""CREATE TRIGGER updateUser
                    AFTER UPDATE
                    ON person
                    FOR EACH ROW
                    BEGIN
                        DECLARE lastid int;
                        SELECT MAX(idP) into lastid from person;
                        INSERT INTO log (user, date, info, id) VALUES (current_user(), now(), "User Updated", lastid);
                    END
                """)

def newImage(curs):
    curs.execute("DROP TRIGGER IF EXISTS newImage")
    curs.execute("""CREATE TRIGGER newImage
                    AFTER INSERT 
                    ON info
                    FOR EACH ROW
                    BEGIN
                        DECLARE lastid int;
                        SELECT MAX(idF) into lastid from info;
                        INSERT INTO log (user, date, info, id) VALUES (current_user(), now(), "New Image", lastid);
                    END
                """)

def updateImage(curs):
    curs.execute("DROP TRIGGER IF EXISTS updateImage")
    curs.execute("""CREATE TRIGGER updateImage
                    AFTER UPDATE
                    ON info
                    FOR EACH ROW
                    INSERT INTO log (user, date, info) VALUES (current_user(), now(), "Info Updated");
                """)

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
    conn.commit()
    print ("Created tables")
except:
    conn.rollback
    print ("Failed to create tables")

#try:
newUser(curs)
updateUser(curs)
newImage(curs)
updateImage(curs)
conn.commit()
    #print ("Trigger created")
#except:
    #conn.rollback    
    #print ("Trigger failed")

#try:
insert_values1(curs,'Elaine','Burton','elaine@htl-shkoder.com',0)
insert_values2(curs)
insert_values3(curs)
insert_values4(curs)
conn.commit()
#    print ("Values inserted")
#except:
#    conn.rollback
#    print ("Failed to insert")
    
conn.close()
