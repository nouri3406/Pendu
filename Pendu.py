import random
from english_words import get_english_words_set

def AKA ():
	user =input ("enter your A.K.A !!! :" )
	print (" Hooo yyyeeeaaah your A.K.A is : ", user )
AKA()

word =list (get_english_words_set(["gcide"]))
enigme = list( random.choice (list(word)).lower())
caracter = len(enigme)
etat =["_"]*caracter 		
lettres =[]
fautes = 0
limite = 12

def word_or_let (lettre) :
	if len(lettre) > 1 :
		word(lettre)
	else :
		let(lettre)

def word (lettre) :
	global etat, fautes, enigme, caracter, lettres
	if list(lettre) == enigme :
		etat = enigme
	else :
		fautes +=5

def let (lettre) :
	global etat, fautes, enigme, caracter,lettres 
	if lettre in enigme :
		for i, y in enumerate (enigme) :
			if lettre == y :
				etat [i]  = lettre
	else :
		fautes += 1

while etat !=  enigme:
	print("\nLe mot est : ", *etat )
	lettre = input("Entrer une lettre ou un mot : ")
	if  lettre not in lettres :
		lettres.append( lettre )
	word_or_let(lettre)

	if fautes >= limite:
		print ("you loose ! play again", "le mot était :", *enigme)
		break
	if etat == enigme:
		print (*etat)
		print ("GG you a GOOAATTTT !!!!")
		break
	print (" il te reste : ", limite-fautes, "vies" )
	print ("les lettres déja jouées sont : ", *lettres )
