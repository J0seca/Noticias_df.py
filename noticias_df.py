#-*- coding: UTF-8 -*-

#Noticias DF

import urllib
from urllib import request
from bs4 import BeautifulSoup
import time
source = urllib.request.urlopen("http://df.cl")
soup = BeautifulSoup(source)

for link in soup.find_all("h2"):
    print(25*"-" + "\n" + link.get_text() + "\n")
    enlace = str(link.a).split('"')[1:2]
    print("http://df.cl" + "".join(enlace) + "\n" + "\n")
    time.sleep(5)
