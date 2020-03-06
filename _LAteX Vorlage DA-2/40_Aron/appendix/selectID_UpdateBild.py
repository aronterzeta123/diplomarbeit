#!/usr/bin/python3

import MySQLdb
import sys
import os
import subprocess
variable3=sys.argv[1]
conn=MySQLdb.connect('localhost','aronterzeta','aronterzeta','test')
mycursor=conn.cursor()
conn.close()
