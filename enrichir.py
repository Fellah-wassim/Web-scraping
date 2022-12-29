import re
import sys

# Verify the argv inputs
if len(sys.argv) < 2:
	print("You need to enter the corpus-medical.txt file")
else:	
	subst_corpus = open("subst_corpus.dic",'w',encoding="utf-16")
	subst_corpus.write("\ufeff")
  # Get lines of both files subst and corpus
	subst = open("subst.dic",'r',encoding="utf-16")
	substLines = subst.readlines()
	subst.close()
	corpusFile = open(sys.argv[1],'r',encoding="utf-8")
	corpusLines = corpusFile.readlines()
	corpusFile.close()
	reg = "^([^A-Za-zéèêïç]| ){0,3}([A-Za-zéèêïç]+) (LP )?:? ?(\d+|\.|,)+ (g|mg|ml|mcg|UI|\d+?/j)"
  # Define order function
	def order(INP1,INP2):
		alphabetFR=["a","b","c","ç","d","e","é","è","ê","f","g","h","i","ï","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
		counter = 0
    # Compare between the character of input1 and input2, return true if the input2 comes first and false on the contrary
		while counter < len(INP1) and counter < len(INP2):
			if alphabetFR.index(INP1[counter]) > alphabetFR.index(INP2[counter]):
				return True
			if alphabetFR.index(INP1[counter]) < alphabetFR.index(INP2[counter]):
				return False
			else:
        # Move to the next character if the current characters are equal
				counter = counter + 1
    # In case that all characters are equal and the loop doesn't break then we compare the length (the shortest first)
		if(len(INP1) <= len(INP2)):
			return False
		else:
			return True   

	lineNumber = 1 
  # CorpusListWithoutDoubles is a list of enrichment medical entities without duplicates
	CorpusListWithoutDoubles=[]
  # enrichListWithoutDoubles is a list of enrichment medical entities without duplicates
	enrichListWithoutDoubles=[]
	for L in corpusLines:
    # Make sure to encode the line on utf-16 with BOM
		L = L.encode("utf-16-le").decode("utf-16-le")
    # Searching for the medicine on the line and ignoring the case-insensitive 
		search = re.findall(reg, L, re.IGNORECASE)
		if len(search) > 0: 
      # To index the medicine we use two square bracket because we have a list inside a list
			line = search[0][1].lower()+",.N+subst\n"
			# Add the line to the subst_corpus.dic file
			subst_corpus.write(line)
			# Check if the line doesn't exist on the subst.dic lines
			if(not(line in substLines)):  
        # If the line doesn't exit on the subst.dic lines we need to add it to the lines, keeping the order
				# First we need to search the position where to insert the line
				position = 0
        # While position is lower then subsLines and the subsLines[position] is still come before the line then search for the position
				while position < len(substLines) and order(line,substLines[position]):
					position = position + 1
        # If the position is inside the substLines then insert the line on that position
				if position < len(substLines):
					substLines.insert(position,line)
					if(not(line in enrichListWithoutDoubles)):
						enrichListWithoutDoubles.append(line)
			if(not(line in CorpusListWithoutDoubles)):
				CorpusListWithoutDoubles.append(line)
			print(str(lineNumber)+" "+ search[0][1].lower())
			lineNumber = lineNumber + 1
	subst_corpus.close()
	
	subst=open("subst.dic",'w',encoding="utf-16-le")
	subst.write("\ufeff")
  # We write directly on the subst.dic file because we ordered the list of substLines before with the order function
	for L in substLines:
		subst.write(L)
	subst.close()
	
  # Create the infos2.txt file
	infos2 = open("infos2.txt",'w',encoding="utf-16")
	total = 0
  # For every single letter we search for the medicine that starts with this letter and write it to the info2 file and count the total number
	for letter in ["a","b","c","ç","d","e","é","è","ê","f","g","h","i","ï","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] :
		counter = 0
		for listElement in CorpusListWithoutDoubles:
			if(listElement[0] == letter):
				infos2.write(listElement)
				counter = counter + 1
		infos2.write("Total with letter "+ letter + " is: " + str(counter)+ "\n")
		infos2.write("\n++++++++++++++++++++++++++++++++++++++++\n\n")
		total = total + counter
	infos2.write("The total number of medicines from the corpus is: " + str(total) + "\n")		
	infos2.close()

	# Create the infos3.txt file
	infos3 = open("infos3.txt",'w',encoding="utf-16")
	total = 0
  # We do the same as the functionality of infos2.txt 
	for letter in ["a","b","c","ç","d","e","é","è","ê","f","g","h","i","ï","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] :
		counter = 0
		for listElement in enrichListWithoutDoubles:
			if(listElement[0] == letter):
				infos3.write(listElement)
				counter = counter + 1
		infos3.write("Total with letter " + letter + " is: " + str(counter) + "\n")
		infos3.write("\n++++++++++++++++++++++++++++++++++++++++\n\n")
		total = total + counter
	infos3.write("The total number of medicines stored for enrichment is: " + str(total) + "\n")		
	infos3.close()
		

