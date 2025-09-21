import random
from english_words import get_english_words_set
import time

def AKA ():
	user =input ("enter your A.K.A !!! :" )
	print (" Hooo yyyeeeaaah your A.K.A is : ", user )
	return user
user = AKA ()

word =list (get_english_words_set(["gcide"]))
enigme = list( random.choice (list(word)).lower())
caracter = len(enigme)
etat =["_"]*caracter
lettres =[]
fautes = 0
limite = 12
start =time.time()
tableau_de_score = []

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

def chrono () :
	temps_écoulé = time.time()-start
	minutes = int(temps_écoulé // 60)
	secondes = int(temps_écoulé % 60)
	centiemes = int((temps_écoulé * 100) % 100)
	temps_str = f"{minutes:02d}:{secondes:02d}:{centiemes:02d}"
	print ( "\nTemps écoulé : ", minutes, "m :", secondes,"s :", centiemes, "c" )
	return temps_str

def affichage () :
	global user, enigme,tableau_de_score
	temps_str = chrono ()
	tableau_de_score.append({
	"joueur": user,
	"mot": "".join(enigme),
	"temps": temps_str
	})

	print("\n=== TABLEAU DE SCORES ===")
	for i, score in enumerate(tableau_de_score, 1):
		print(f"{i}. AKA: {score['joueur']} -- Mot: {score['mot']} -- Temps: {score['temps']}")


while etat !=  enigme:
	print("\nLe mot est : ", *etat )
	lettre = input("Entrer une lettre ou un mot : ")
	if  lettre not in lettres :
		lettres.append( lettre )
	word_or_let(lettre)


	if fautes >= limite:
		print (*etat)
		print ("you loose ! play again", "le mot était :", *enigme)
		affichage ()
		break
	if etat == enigme:
		print (*etat)
		print ("GG you a GOOAATTTT !!!!")
		affichage ()
		break

	print (" il te reste : ", limite-fautes, "vies" )
	print ("les lettres déja jouées sont : ", *lettres )

