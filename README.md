# Utilisation de la POO pour simuler une banque
##  Fonctionnalités
### Inscription
### Dépôt 
### Retrait
### Virement
### Supprimer un compte
### Information client
### Consulter solde banque

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
  
  
