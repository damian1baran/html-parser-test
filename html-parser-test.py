import urllib2
from lxml import etree

import lxml.html

url = "https://www.e-obce.sk/obec/trnovo/trnovo.html"
html = urllib2.urlopen(url).read()

namespaces = {"ns": "http://schemas.xmlsoap.org/wsdl/"}

root = lxml.html.fromstring(html.decode('windows-1250'))

print

print "Root tag:"
print(root.tag)

print

print "Count of elements under root tree:"
print(len(root))

print
print

print "List of elements based on XPath Expression:"
list1 = root.xpath('//*[@id="telo"]/table[1]//tr/td[2]/table//tr/td[3]/table[2]//tr[5]/td[2]/text()')
print list1
print len(list1)
