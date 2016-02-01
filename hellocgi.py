#!C:/Python27/python.exe -u
import sys
#va en C:/Python27/cgi-bin/hellocgi.py 
#correr el web server, ir a C:/Python27/ y correr CGIHTTPServer
#ir al navegador y correr http://localhost:8000/cgi-bin/hellocgi.py  y listo
sys.stdout.write("Content-type: text/html \r\n\r\n")
sys.stdout.write("<!doctype html><html><head><title>Hello CGI</title></head>")
sys.stdout.write("<body><h2>Hello CGI</h2></body></html>")