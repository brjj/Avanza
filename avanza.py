import csv;
from datetime import datetime;
from urllib.request import urlopen;
from bs4 import BeautifulSoup;

#----------------------------------------------------------
quote_page = "" #Skriv URL här
#t.ex:
#https://www.avanza.se/fonder/om-fonden.html/788395/avanza-auto-1


csv_path = "" #mapp att spara .csv filen i
#t.ex:
#D:\program\python\index.csv


#----------------------------------------------------------

def convertString(string):
    x,y = string.split(",");
    string = x + "." + y;
    return float(string);

try:
    page = urlopen(quote_page);
except:
    print("Kunde inte öppna URL");
    exit()
soup = BeautifulSoup(page, "html.parser");
name = soup.find("h1", attrs={"class" : "large marginBottom10px"});
name = name.text.strip();
price = soup.find(attrs={"class" : "SText bold"});
price = price.text.strip();

print(name + ": NAV "+ price);

price = str(convertString(price)) + "kr";
try:
    with open(csv_path, "a") as csv_file:
        writer = csv.writer(csv_file, delimiter=";");
        writer.writerow([name, price, datetime.now().strftime("20%y/%m/%d - %H:%M")]);
except:
    print("Kunde inte spara filen!")
    exit()
