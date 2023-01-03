import sys
import re
import sqlite3

# We need to check if the user gives the concord.html file
if len(sys.argv) < 2:
  print("You need to enter the concord.html file")
else:
	concordHtml = open(sys.argv[1], "r", encoding="utf8")
	search = re.findall("<a href=\"(\d| )+?\">(.+)?</a>", concordHtml.read())
	dataBase = sqlite3.connect("extraction.db")
  # We need to make the connection for executing SQL queries
	obj = dataBase.cursor()
  # Creating the table of extraction with the id and posologie
	obj.execute("CREATE TABLE IF NOT EXISTS EXTRACTION (ID INT PRIMARY KEY, POSOLOGIE TEXT)")
  # Insert the searched data to the table 
	counter = 1    
	for element in search:
		obj.execute("INSERT INTO EXTRACTION(ID,POSOLOGIE) VALUES (" + str(counter) + ",'" + element[1] + "')")
		counter = counter + 1
  # We need to save the changes invoked by a transaction to the database before closing the DB
	dataBase.commit()
	dataBase.close()
	concordHtml.close()