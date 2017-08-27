import urllib2
import lxml.html


obec_exp = '//*[@id="telo"]/table[1]//tr/td[2]/table//tr/td[1]/table[1]//tr[1]/td/text()'
kraj_exp = '//*[@id="telo"]/table[1]//tr/td[2]/table//tr/td[3]/table[2]//tr[1]/td[2]/a/text()'
okres_exp = '//*[@id="telo"]/table[1]//tr/td[2]/table//tr/td[3]/table[2]//tr[2]/td[2]/a/text()'
region_exp = '//*[@id="telo"]/table[1]//tr/td[2]/table//tr/td[3]/table[2]//tr[3]/td[2]/text()'
ico_exp = '//*[@id="telo"]/table[1]//tr/td[2]/table//tr/td[3]/table[2]//tr[4]/td[2]/text()'
obyvatelov_exp = '//*[@id="telo"]/table[1]//tr/td[2]/table//tr/td[3]/table[2]//tr[5]/td[2]/text()'
starosta_exp = '//*[@id="telo"]/table[1]//tr/td[2]/table//tr/td[3]/table[2]//tr[8]/td[2]/text()'
mobil_exp = '//*[@id="telo"]/table[1]//tr/td[2]/table//tr/td[3]/table[2]//tr[9]/td[2]/text()'
telefon_exp = '//*[@id="telo"]/table[1]//tr/td[2]/table//tr/td[3]/table[1]//tr[3]/td[4]/table//tr/td/text()'
email_exp = '//*[@id="telo"]/table[1]//tr/td[2]/table//tr/td[3]/table[1]//tr[5]/td[3]/a/text()'
web_exp = '//*[@id="telo"]/table[1]//tr/td[2]/table//tr/td[3]/table[1]//tr[6]/td[3]/a/text()'


url = "https://www.e-obce.sk/obec/trnovo/trnovo.html"

html = urllib2.urlopen(url).read()

root = lxml.html.fromstring(html)

obec = root.xpath(obec_exp)
kraj = root.xpath(kraj_exp)
okres = root.xpath(okres_exp)
region = root.xpath(region_exp)
ico = root.xpath(ico_exp)
obyvatelov = root.xpath(obyvatelov_exp)
starosta = root.xpath(starosta_exp)
mobil = root.xpath(mobil_exp)
telefon = root.xpath(telefon_exp)
email = root.xpath(email_exp)
web = root.xpath(web_exp)

# CSV view
print obec[0] + "," + kraj[0] + "," + okres[0] + "," + region[0] + "," + obyvatelov[0] + "," + starosta[0] + "," + mobil[0] + "," + telefon[0] + "," + email[0] + "," + web[0]


# Summary view
# print obec[0]
# print kraj[0]
# print okres[0]
# print region[0]
# print ico[0]
# print obyvatelov[0]
# print starosta[0]
# print mobil[0]
# print telefon[0]
# print email[0]
# print web[0]
