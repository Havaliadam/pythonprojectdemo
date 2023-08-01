import requests
from bs4 import BeautifulSoup
import pandas as pd 
url="https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/Temel-Degerler-Ve-Oranlar.aspx?endeks=03#page-1"
r=requests.get(url)
print(r)