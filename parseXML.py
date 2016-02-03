#!C:/Python27/python.exe -u
import xml.sax

#asi lo corri en linea de comandos: python parseXML.py
class FilmParser(xml.sax.ContentHandler):
   def __init__(self):
      xml.sax.ContentHandler.__init__(self)

   def startElement(self, name, attrs):
      print("start element: '" + name + " ' ")
   
   def endElement(self, name ):
      print ("end element: '" + name + "'")
      
   def characters(self , content):
      print ("characters: '" + content + "'")
      
def main (xmlFile):
    source = open (xmlFile)
    xml.sax.parse(source, FilmParser())

print ("fin")
main("films.xml")
    