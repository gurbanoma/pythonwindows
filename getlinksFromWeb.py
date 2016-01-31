#!C:/Python34/python.exe -u
import urllib, htmllib, formatter

#website = urllib.urlopen("http://www.profmcmillan.com")
#https://espanol.yahoo.com/
website = urllib.urlopen("https://espanol.yahoo.com/")
data = website.read()
website.close()
format = formatter.AbstractFormatter(formatter.NullWriter())
ptext = htmllib.HTMLParser(format)
ptext.feed(data)
for link in ptext.anchorlist:
   print(link)