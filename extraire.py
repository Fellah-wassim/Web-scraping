import sys
from bs4 import BeautifulSoup
import urllib.request

srt1 = open("subst.dic",'w',encoding='utf-16-le')
srt1.write('\ufeff')
srt2 = open("infos1.txt",'w')
data = sys.argv[1] 
page = data[0] 
fin_page = data[2]
port = sys.argv[2]
i = 0
nbr = 0
while(ord(page) <= ord(fin_page)):
    src = urllib.request.urlopen('http://127.0.0.1:'+ str(port) + '/vidal/vidal-Sommaires-Substances-'+page+'.htm')
    soup = BeautifulSoup(src, 'lxml')
    match = soup.find('ul', class_='substances list_index has_children')
    match.text.strip()
    for ligne in match.text.splitlines():
        if not ligne.strip():
            continue
        srt1.write(ligne+",.N+subst\n")
        nbr = nbr+1
    srt2.write("le nombre des mediacaments avec la lettre " + str(page)+" est: "+ str(nbr)+"\n")
    i = nbr+i
    nbr = 0
    page = chr(ord(page)+1)
srt2.write("le nombre total des medicaments est :"+str(i))
