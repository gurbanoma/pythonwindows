#!C:/Python27/python.exe -u
import cgi, os, sys

#va en C:/Python27/cgi-bin/querys.py 
#correr el web server, ir a C:/Python27/ y correr CGIHTTPServer
#ir al navegador y correr http://localhost:8000/cgi-bin/querys.py  y listo
sys.stdout.write("Content-type: text.html\r\n\r\n")
sys.stdout.write("")
sys.stdout.write("<html><body>")
sys.stdout.write("<h2>Query String</h2>")

form = cgi.FieldStorage()
for field in form.keys():
   sys.stdout.write("%s -> %s<br />" % (field, form[field].value))
sys.stdout.write("</body></html>")