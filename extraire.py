import sys
from bs4 import BeautifulSoup
import urllib.request

subst = open("subst.dic",'w',encoding='utf-16-le')
subst.write('\ufeff')
infos1 = open("infos1.txt",'w')
intervalCollector = sys.argv[1] 
currentPage = intervalCollector[0] 
lastPage = intervalCollector[2]
userPort = sys.argv[2]
counter = 0
number = 0

# Using the ord function to browse all the alphabet on the interval from the current page to the last page
while(ord(currentPage) <= ord(lastPage)):
    src = urllib.request.urlopen('http://127.0.0.1:' + str(userPort) + '/vidal/vidal-Sommaires-Substances-' + currentPage + '.htm')
    soup = BeautifulSoup(src, 'lxml')
    # Using soup.find to return a list of ul tag with specific class
    founded = soup.find('ul', class_='substances list_index has_children')
    founded.text.strip()
    for med in founded.text.splitlines():
        if not med.strip():
            continue
        subst.write( med + ",.N+subst\n")
        number = number + 1
    # Writing the number of medicines with the current letter (page) on the infos1 file
    infos1.write("The number of medicines with the letter " + str(currentPage) + " is: " + str(number) + "\n")
    # Adding the number of the medicines to the counter to know the total number at the end
    counter = number + counter
    # Assign 0 to the number for the next iteration
    number = 0
    # Adding one to the ord of the current page then transform it to a character to work with ord on the condition of the while again
    currentPage = chr(ord(currentPage) + 1)
# Writing the total number of medicines on the infos1 file
infos1.write("The total number of medicines is:" + str(counter))
