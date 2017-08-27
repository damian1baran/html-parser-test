import urllib2
import lxml.html
import re

ans=True
while ans:
    print ("""
    1. 0-500
    2. 500-1000
    3. 1000-1500
    4. 1500-2000
    5. 2000-2500
    6. 2500-3000
    7.Exit/Quit
    """)
    ans=raw_input("Vyber obce...")
    if ans=="1":
      print("\n Vytvaram zoznam obci 0-500")
      page = 'https://www.e-obce.sk/zoznam_vsetkych_obci.html?strana=0'
      ans=None
    elif ans=="2":
      print("\n Vytvaram zoznam obci 500-1000")
      page = 'https://www.e-obce.sk/zoznam_vsetkych_obci.html?strana=500'
      ans=None
    elif ans=="3":
      print("\n Vytvaram zoznam obci 1000-1500")
      page = 'https://www.e-obce.sk/zoznam_vsetkych_obci.html?strana=1000'
      ans=None
    elif ans=="4":
      print("\n Vytvaram zoznam obci 1500-2000")
      page = 'https://www.e-obce.sk/zoznam_vsetkych_obci.html?strana=1500'
      ans=None
    elif ans=="5":
      print("\n Vytvaram zoznam obci 2000-2500")
      page = 'https://www.e-obce.sk/zoznam_vsetkych_obci.html?strana=2000'
      ans=None
    elif ans=="6":
      print("\n Vytvaram zoznam obci 2500-3000")
      page = 'https://www.e-obce.sk/zoznam_vsetkych_obci.html?strana=2500'
      ans=None
    elif ans == "7":
      print("\n Goodbye")
      ans=None
    else:
      print("\n Not Valid Choice Try again")

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

html = urllib2.urlopen(page).read()

# Najdi stranky vsetkych obci
list1 = re.findall('https://+www.e-obce.sk+/obec/+[A-z\-]{1,50}/+.{1,50}.html', html)

for i in list1:

    html = urllib2.urlopen(i).read()

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

    if not obec:
        obec = " " * 5
    if not kraj:
        kraj = " " * 5
    if not okres:
        okres = " " * 5
    if not region:
        region = " " * 5
    if not obyvatelov:
        obyvatelov = " " * 5
    if not starosta:
        starosta = " " * 5
    if not mobil:
        mobil = " " * 5
    if not telefon:
        telefon = " " * 5
    if not email:
        email = " " * 5
    if not web:
        web = " " * 5

    # CSV view
    print obec[0] + "," + kraj[0] + "," + okres[0] + "," + region[0] + "," + obyvatelov[0] + "," + starosta[0] + "," + mobil[0] + "," + telefon[0] + "," + email[0] + "," + web[0]
