#!C:/Python27/python.exe -u
import cgi, sys, os
import sqlite3 as db

#se hace lo mismo que en los otros cgis 
conn = db.connect('test.db')
cursor = conn.cursor()
formdata = cgi.FieldStorage()
title = formdata["title"].value
tipo = formdata["type"].value
director = formdata["director"].value
rowdata = (title, tipo, director)
cursor.execute('insert into films values(?, ?, ?)', rowdata)
conn.row_factory = db.Row
cursor.execute("select * from films")
rows = cursor.fetchall()

sys.stdout.write("Content-type: text/html\r\n\r\n")
sys.stdout.write("")
sys.stdout.write("<html><body><h1>Films</h1><p>")
for row in rows:
   sys.stdout.write("%s %s %s" % (row[0], row[1], row[2]))
   sys.stdout.write("<br />")

sys.stdout.write("</p></body></html>")