import urllib2
import lxml.html

url = "https://www.e-obce.sk/obec/trnovo/trnovo.html"
html = urllib2.urlopen(url).read()

root = lxml.html.fromstring(html)

xpathexpression = '//*[@id="telo"]/table[1]//tr/td[2]/table//tr/td[3]/table[2]//tr[5]/td[2]/text()'
print "XPATH Expression: " + xpathexpression
list1 = root.xpath(xpathexpression)
print "Value of HTML element identified based on XPATH: " + str(list1[0])
#print "Number of elements found: " + str(len(list1))
