import urllib2
import lxml.html

url = "https://www.e-obce.sk/obec/trnovo/trnovo.html"
html = urllib2.urlopen(url).read()

root = lxml.html.fromstring(html)


obec_exp = '//*[@id="telo"]/table[1]//tr/td[2]/table//tr/td[1]/table[1]//tr[1]/td/text()'
obec = root.xpath(obec_exp)
print obec[0]

kraj_exp = '//*[@id="telo"]/table[1]//tr/td[2]/table//tr/td[3]/table[2]//tr[1]/td[2]/a/text()'
kraj = root.xpath(kraj_exp)
print kraj[0]

okres_exp = '//*[@id="telo"]/table[1]//tr/td[2]/table//tr/td[3]/table[2]//tr[2]/td[2]/a/text()'
okres = root.xpath(okres_exp)
print okres[0]

region_exp = '//*[@id="telo"]/table[1]//tr/td[2]/table//tr/td[3]/table[2]//tr[3]/td[2]/text()'
region = root.xpath(region_exp)
print region[0]

ico_exp = '//*[@id="telo"]/table[1]//tr/td[2]/table//tr/td[3]/table[2]//tr[4]/td[2]/text()'
ico = root.xpath(ico_exp)
print ico[0]

obyvatelov_exp = '//*[@id="telo"]/table[1]//tr/td[2]/table//tr/td[3]/table[2]//tr[5]/td[2]/text()'
obyvatelov = root.xpath(obyvatelov_exp)
print obyvatelov[0]

starosta_exp = '//*[@id="telo"]/table[1]//tr/td[2]/table//tr/td[3]/table[2]//tr[8]/td[2]/text()'
starosta = root.xpath(starosta_exp)
print starosta[0]

mobil_exp = '//*[@id="telo"]/table[1]//tr/td[2]/table//tr/td[3]/table[2]//tr[9]/td[2]/text()'
mobil = root.xpath(mobil_exp)
print mobil[0]

telefon_exp = '//*[@id="telo"]/table[1]//tr/td[2]/table//tr/td[3]/table[1]//tr[3]/td[4]/table//tr/td/text()'
telefon = root.xpath(telefon_exp)
print telefon[0]

email_exp = '//*[@id="telo"]/table[1]//tr/td[2]/table//tr/td[3]/table[1]//tr[5]/td[3]/a/text()'
email = root.xpath(email_exp)
print email[0]

web_exp = '//*[@id="telo"]/table[1]//tr/td[2]/table//tr/td[3]/table[1]//tr[6]/td[3]/a/text()'
web = root.xpath(web_exp)
print web[0]
