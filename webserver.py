#!C:/Python34/python.exe -u
#este es un web server como el apache pero es muy ligero y funciona
#hay que poner el index.html y test.html en el mismo path que este archvo y 
#correr en el navegador http://localhost:8000/  y para correr el test.hmtl
#http://localhost:8000/test.html
import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

Handler = SimpleHTTPRequestHandler
Server = BaseHTTPServer.HTTPServer
Protocol = "HTTP/1.0"

if sys.argv[1:]:
   port = int(sys.argv[1])
else:
   port = 8000

server_address = ('127.0.0.1', port)

Handler.protocol_version = Protocol
httpd = Server(server_address, Handler)

print("Serving HTTP")
httpd.serve_forever()