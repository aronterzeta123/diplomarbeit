#!/usr/bin/python3
import MySQLdb
import time
import logging
db_server='localhost'
db_user='aronterzeta'
db_password='aronterzeta'
db_dbname='test'
db_tbl_log='log'
log_file_path='/home/pi/diplomarbeit/python_scripts/fehlerlog.txt'
log_error_level='DEBUG'
log_to_db=True

class LogDBHandler(logging.Handler):
    def __init__(self,sql_conn,sql_cursor,db_tbl_log):
        logging.Handler.__init__(self)
        self.sql_cursor=sql_cursor
        self.sql_conn=sql_conn
        self.db_tbl_log=db_tbl_log
    def emit(self,record):
        tm=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(record.created))
        self.log_msg=record.msg
        self.log_msg=self.log_msg.strip()
        self.log_msg=self.log_msg.replace('\'', '\'\'')
        sql='insert into '+self.db_tbl_log + ' (log_level, ' + \
            'log_levelname,log,created_at,created_by) ' + \
            'values (' + \
            '' + str(record.levelno) + ', ' + \
            '\'' + str(record.levelname) + '\', ' + \
            '\'' + str(self.log_msg) + '\', ' + \
            ' \'' + tm + '\', ' + \
            '\'' + str(record.name) + '\')'
        try:
            self.sql_cursor.execute(sql)
            self.sql_conn.commit()
        except MySQLdb.Error as e:
            print (sql)
            print("Critical DB Error")
if(log_to_db):
    log_conn=MySQLdb.connect(db_server,db_user,db_password,db_dbname,30)
    log_cursor=log_conn.cursor()
    logdb=LogDBHandler(log_conn,log_cursor,db_tbl_log)

logging.basicConfig(filename=log_file_path)
if(log_to_db):
    logging.getLogger('').addHandler(logdb)
log=logging.getLogger('Gesichtserkennung')
log.setLevel(log_error_level)
test_var='Taster wurde nicht gedrueckt'
log.error('This event occurred: %s' % test_var)

