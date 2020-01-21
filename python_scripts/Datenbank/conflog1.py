#!/usr/bin/python3
import MySQLdb

def drop_tables(curs):
    curs.execute('DROP TABLE IF EXISTS logUser')

def create_tables(curs):
    curs.execute("""CREATE TABLE logUser(
                                        idL int auto_increment,
                                        user varchar(50), 
                                        date datetime,
                                        newUser int,
                                        PRIMARY KEY (idL),
                                        FOREIGN KEY (newUser) REFERENCES person (idP)
                                        )""")

def insert_values1(curs, newUser):
    add_log=("INSERT INTO log (user, date, newUser)" \
                "VALUES(current_user(), now(), %s)")
    data_log=(newUser)
    curs.execute(add_log, data_log)

def insert_values2(curs, vorname, nachname, email, role):
    add_person=("INSERT INTO person (vorname, nachname, email, role)" \
                "VALUES(%s,%s,%s,%s)")
    data_person=(vorname, nachname, email, role)
    curs.execute(add_person, data_person)

def insert_procedure(curs):
    curs.execute("DROP PROCEDURE IF EXISTS logUser")
    curs.execute("""CREATE PROCEDURE logUser()
                    BEGIN
                        DECLARE id int;
                        SELECT max(idP) into id FROM person;
                        INSERT INTO logUser (user, date, newUser) VALUES (current_user(), now(), id);
                    END
                """)

def insert_trigger(curs):
    curs.execute("DROP TRIGGER IF EXISTS addUser")
    curs.execute("""CREATE TRIGGER addUser 
                    AFTER INSERT 
                    ON person 
                    FOR EACH ROW
                    CALL logUser();
                """)

try:
    conn = MySQLdb.connect('','','127.0.0.1','diploma')
    curs = conn.cursor()
    print ("Database Working")
except:
    conn = MySQLdb.connect('','','127.0.0.1','backup')
    curs = conn.cursor()
    print ("Backup Database Working")
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

try:
    #insert_values1(curs,str(1))
    insert_values2(curs,'Elaine','Burton','elaine@htl-shkoder.com',0)
    conn.commit()
    print ("Values inserted")
except:
    conn.rollback
    print ("Failed to insert")
    
conn.close()
