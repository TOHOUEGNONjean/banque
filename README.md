# Utilisation de la POO pour simuler une banque
##  Fonctionnalités
### Inscription
### Dépôt 
### Retrait
### Virement
### Supprimer un compte
### Information client
### Consulter solde banque

#banque.py

Ce code est en Python et définit deux classes : Clients et Banque.

La classe Clients a pour but de créer des clients avec les attributs suivants : nom, prénom, email, numéro de téléphone, profession et solde. Elle contient un constructeur init() qui initialise ces attributs pour chaque instance de la classe.

La classe Banque contient une liste de clients et des méthodes pour gérer les opérations bancaires. Elle a également un constructeur init() qui initialise la liste des clients.

Les méthodes de la classe Banque sont les suivantes :

  inscription() : cette méthode prend un objet client en entrée et ajoute ce client à la liste des clients de la banque.
  depot() : cette méthode prend un numéro de téléphone et un montant en entrée, trouve le client correspondant dans la liste des clients et ajoute le montant à son solde.
  retrait() : cette méthode prend un numéro de téléphone et un montant en entrée, trouve le client correspondant dans la liste des clients et soustrait le montant de son solde.
  virement() : cette méthode prend les numéros de téléphone des deux clients impliqués dans le virement et le montant à transférer en entrée. Elle utilise les méthodes retrait() et depot() pour effectuer le virement.
  supression() : cette méthode prend un nom et un numéro de téléphone en entrée, trouve le client correspondant dans la liste des clients et le supprime de la liste.
  info_client() : cette méthode prend un numéro de téléphone en entrée, trouve le client correspondant dans la liste des clients et affiche ses informations.
  solde_banque() : cette méthode calcule le solde total de la banque en additionnant le solde de chaque client et l'affiche.
  
#client.py

Le programme affiche un menu permettant à l'utilisateur de choisir entre différentes options : inscription, dépôt, retrait, virement, suppression de compte, information client, solde banque, et quitter.

En fonction de l'option choisie par l'utilisateur, le programme exécute une méthode spécifique du module "banque". Par exemple, si l'utilisateur choisit l'option "dépôt", le programme demande à l'utilisateur de saisir le numéro du compte sur lequel il souhaite effectuer le dépôt et le montant à déposer, puis il appelle la méthode "depot" du module "banque" en lui transmettant ces informations.

Le code utilise des classes pour représenter les clients et les comptes bancaires. Le module "banque" contient des méthodes pour gérer les clients et les comptes, telles que l'ajout d'un nouveau client, le dépôt d'argent sur un compte, le retrait d'argent d'un compte, le virement entre deux comptes, la suppression d'un compte, l'obtention d'informations sur un client, et la récupération du solde total de la banque.

Le code utilise une boucle while pour afficher le menu à l'utilisateur tant qu'il ne choisit pas l'option "quitter".

#Execution

Assurez-vous d'avoir Python installé sur votre ordinateur. Si ce n'est pas le cas, téléchargez et installez Python à partir du site officiel :              https://www.python.org/downloads/

Ouvrez une invite de commandes (ou un terminal) et accédez au répertoire où se trouve votre fichier client.py.

Exécutez le programme en tapant python client.py dans l'invite de commandes (ou le terminal).

Le programme affichera un menu d'options à l'utilisateur, qui peut choisir entre plusieurs fonctionnalités telles que l'inscription d'un client, le dépôt, le retrait, le virement, la suppression d'un compte, l'affichage des informations d'un client ou le solde de la banque.

Suivez les instructions fournies par le programme pour utiliser chaque fonctionnalité.

Lorsque vous avez terminé d'utiliser le programme, choisissez l'option "Quitter" pour sortir du programme.
