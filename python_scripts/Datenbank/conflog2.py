#!/usr/bin/python3
import MySQLdb

def drop_tables(curs):
    curs.execute('DROP TABLE IF EXISTS logImage')

def create_tables(curs):
    curs.execute("""CREATE TABLE logImage(
                                        idLM int auto_increment,
                                        user varchar(50), 
                                        date datetime,
                                        newImage int,
                                        PRIMARY KEY (idLM),
                                        FOREIGN KEY (newImage) REFERENCES info (idF)
                                        )""")

def insert_values1(curs, newImage):
    add_log=("INSERT INTO log (user, date, newImage)" \
                "VALUES(current_user(), now(), %s)")
    data_log=(newImage)
    curs.execute(add_log, data_log)

def insert_values2(curs, imagePath, idP):
    add_image=("INSERT INTO info (imagePath, idP)" \
                "VALUES(%s, %s)")
    data_image=(imagePath, idP)
    curs.execute(add_image, data_image)

def insert_procedure(curs):
    curs.execute("DROP PROCEDURE IF EXISTS logImage")
    curs.execute("""CREATE PROCEDURE logImage()
                    BEGIN
                        DECLARE id int;
                        SELECT max(idF) into id FROM info;
                        INSERT INTO logImage (user, date, newImage) VALUES (current_user(), now(), id);
                    END
                """)

def insert_trigger(curs):
    curs.execute("DROP TRIGGER IF EXISTS addImage")
    curs.execute("""CREATE TRIGGER addImage 
                    AFTER INSERT 
                    ON info 
                    FOR EACH ROW
                    CALL logImage();
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

try:
    insert_procedure(curs)
    conn.commit()
    print ("Procedure created")
except:
    conn.rollback    
    print ("Procedure failed")

try:
    insert_trigger(curs)
    conn.commit()
    print ("Trigger created")
except:
    conn.rollback    
    print ("Trigger failed")

#try:
#insert_values1(curs,'../Pictures/image4.jpg',1)
insert_values2(curs,'../Pictures/image4.jpg',1)
conn.commit()
#    print ("Values inserted")
#except:
#    conn.rollback
#    print ("Failed to insert")
    
conn.close()
