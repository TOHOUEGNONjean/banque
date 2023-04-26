#coding:utf-8

from banque import *


continu=True
banq=Banque()
while continu:
	
	print('------------------- Bienvenu -------------')

	print("Que voulez vous ?")

	print('------------ 1- Inscription ')
	print('------------ 2- Dépôt ')
	print('------------ 3- Retrait ')
	print('------------ 4- Virement')
	print('------------ 5- Supprimer un compte ')
	print('------------ 6- information client ')
	print('------------ 7- solde Banque ')
	print('------------ 8- Quitter ')

	choix=int(input("entrer un nombre entier --: "))

	
	if choix==1:
		n=int(input('nombre de client '))

		for i in range(n):
			print('client {}'.format(i+1))
			nom=input('Nom : ')
			prenom=input('prenom : ')
			email=input('email : ')
			numero=int(input('numero : '))
			profession = input("Profession ")
			solde= int(input('solde '))
			
			cli=Clients(nom,prenom,email,numero,profession,solde)

			banq.inscription(cli)

	elif choix==2:
		numero=int(input('entrer le numéro : '))
		montant=int(input('entrer le montant : '))
		banq.depot(numero,montant)

	elif choix==3:
		numero=int(input('entrer le numéro : '))
		montant=int(input('entrer le montant : '))
		banq.retrait(numero,montant)

#virement
	elif choix==4:

		numero_debiteur=int(input("entrer le numéro du débiteur "))
		numero_receveur= int(input("entrer le numéro du reveveur "))
		montant=int(input("le montant "))

		banq.virement(numero_debiteur,numero_receveur,montant)

	elif choix==5:
		nom=input("entrer votre nom ")
		numero= int(input("entrer votre numéro "))
		banq.supression(nom,numero)
	

	elif choix == 6:
		numero= int(input("entrer votre numéro "))
		banq.info_client(numero)
	elif choix==7:
		
		banq.solde_banque()
	elif choix==8:
		continu=False

