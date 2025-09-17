import random
from english_words import get_english_words_set


def AKA ():
	user =input ("enter your A.K.A !!! :" )
	print (" Hooo yyyeeeaaah your A.K.A is : ", user )
AKA()

word =list (get_english_words_set(["gcide"]))
enigme = random.choice (list(word)).lower()
caracter = len(enigme)

def espace():
	print("_"*caracter)
espace()

fautes = 0
limite = 12
reponse =""*caracter

while "_".join(reponse) != enigme and fautes < limite :
	letter= input ("enter a letter : ").lower()
 
	if letter in enigme :	
		for i in range (len(enigme)):
			if enigme[i] == letter :
				reponse[i] == letter
			else :
        			fautes += 1
			print("heu...heu...Non !!")
			print ("il te reste  :", limite - fautes, "vie" )

		if fautes == limite:
			print ("yoou loose ! play again", "le mot était :", enigme)
			break	
		if enigme == reponse:
			print ("GG you a GOOAATTTT !!!!")
			break
