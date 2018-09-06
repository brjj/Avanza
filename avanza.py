
import csv;
from datetime import datetime;
from urllib.request import urlopen;
from bs4 import BeautifulSoup;
import os
os.chmod("D:\program\python", 0o777);

def convertString(string):
    x,y = string.split(",");
    string = x + "." + y;
    return float(string);


quote_page = "https://www.avanza.se/fonder/om-fonden.html/788395/avanza-auto-1"
page = urlopen(quote_page);
soup = BeautifulSoup(page, "html.parser");
name = soup.find("h1", attrs={"class" : "large marginBottom10px"});
name = name.text.strip();
price = soup.find(attrs={"class" : "SText bold"});
price = price.text.strip();

print(name + ": NAV "+ price);

price = str(convertString(price)) + "kr";
with open("D:\program\python\index.csv", "a") as csv_file:
    writer = csv.writer(csv_file, delimiter=";");
    writer.writerow([name, price, datetime.now().strftime("20%y/%m/%d - %H:%M")]);
