#!C:/Python34/python.exe -u
import htmllib, urllib, formatter, sys

#website = urllib.urlopen("http://www.profmcmillan.com")

website = urllib.urlopen("http://www.mediotiempo.com/")
data = website.read()
website.close()
format = formatter.AbstractFormatter(formatter.DumbWriter(sys.stdout))
ptext = htmllib.HTMLParser(format)
ptext.feed(data)
ptext.close()