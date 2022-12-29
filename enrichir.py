import re
import sys

# Verify the argv inputs
if len(sys.argv) < 2:
	print("You need to enter the corpus-medical.txt file")
else:	
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
    # In case that all characters are equal and the loop doesn't break then we compare the length
		if(len(INP1) <= len(INP2)):
			return False
		else:
			return True   
	subst_corpus = open("subst_corpus.dic",'w',encoding="utf-16")
	subst_corpus.write("\ufeff")
  # Get lines of both files subst and corpus
	subst = open("subst.dic",'r',encoding="utf-16")
	substLines = subst.readlines()
	subst.close()
	corpusFile = open(sys.argv[1],'r',encoding="utf-8")
	corpusLines = corpusFile.readlines()
	corpusFile.close()

	regex = "^([^A-Za-zéèêïç]| ){0,3}([A-Za-zéèêïç]+) (LP )?:? ?(\d+|\.|,)+ (g|mg|ml|mcg|UI|\d+?/j)"
	