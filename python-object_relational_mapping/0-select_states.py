#!/usr/bin/python3
#states from the database
#usage: select.py<mysql un>
#<mysql psw>
#<db>
import sys
import MySQLdb

if __name__ == "__main__";
    db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute('select * from states')
    [print(state) for state in c.fetchall()]