#!C:/Python27/python.exe -u
import cgi, os, sys
import sqlite3 as db

conn = db.connect('test.db')
conn.row_factory = db.Row
cursor = conn.cursor()
filmdata = cgi.FieldStorage()
title = filmdata["title"].value
tipo = filmdata["type"].value
director = filmdata["director"].value
cursor.execute("update films set type = ? where name = ?", (tipo,title))
conn.row_factory = db.Row
cursor.execute("select * from films")
rows = cursor.fetchall()

sys.stdout.write("Content-type: text/html\r\n\r\n")
sys.stdout.write("")
sys.stdout.write("<html><body><h1>Films</h1><p>")
sys.stdout.write("despues de update <br />")
for row in rows:
   sys.stdout.write("%s %s %s" % (row[0], row[1], row[2]))
   sys.stdout.write("<br />")
sys.stdout.write("</p></body></html>")