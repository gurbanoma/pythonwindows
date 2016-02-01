#!C:/Python27/python.exe -u
import cgi, os, sys
import sqlite3 as db

#hay que levantar el CGIHTTPServer
#hay que crear las base de datos en el mismo lugar donde esta levanto el server 
conn = db.connect('test.db')
cursor = conn.cursor()
conn.row_factory = db.Row
cursor.execute("select * from films")
rows = cursor.fetchall()

sys.stdout.write("Content-type: text.html\r\n\r\n")
sys.stdout.write("")
sys.stdout.write("<html><body><p>")
for row in rows:
   sys.stdout.write("%s %s %s" % (row[0],row[1],row[2]))
   sys.stdout.write("<br />")
sys.stdout.write("</p></body></html>")