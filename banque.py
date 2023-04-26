#coding:utf-8


#client=[]

class Clients():
	"""docstring for Clients"""
	def __init__(self, nom,prenom,email,numero,profession,solde):
		#super().__init__(solde)
		self.nom=nom
		self.prenom=prenom
		self.email=email
		self.numero=numero
		self.profession=profession
		self.solde=solde
						

class Banque():
	"""docstring for Banque"""
	
	def __init__(self):
		
		self.client=[]	

#inscription

	def inscription(self,a):
		self.client.append(a)
		print('{} {} inscrit avec succès!!'.format(self.client[-1].nom,self.client[-1].prenom) )
			

#depot

	def depot(self,tel,montant):
		for i in range(len(self.client)):
			if tel== self.client[i].numero:
				self.client[i].solde=self.client[i].solde + montant
				print("depot effectué avec succès")
				break

		
	def retrait(self,tel,montant):
		for i in range(len(self.client)):
			#vérification
			if tel==self.client[i].numero:
				self.client[i].solde=self.client[i].solde -montant
				print("Retrait effectué avec succès")
				break
#virement

	def virement(self,numero_debiteur,numero_crediteur,montant):
		for i in range(len(self.client)):
			if numero_debiteur==self.client[i].numero:

				#ok le premmier client a un compt, vérifiions pour le receveur

				for j in range(len(self.client)):
					if numero_crediteur==self.client[j].numero:
						#montant=int(input("Entrer le montant --: "))

						self.retrait(numero_debiteur,montant)
						self.depot(numero_crediteur,montant)

						print("Bien !!!")

	def supression(self, nom,tel):
		for i in range(len(self.client)):
			if tel==self.client[i].numero:
				self.client.pop(i)
				print("client supprimé avec succès")



	def info_client(self,tel):
		for i in range(len(self.client)):
			if tel==self.client[i].numero:
				print('Nom: {}'.format(self.client[i].nom))
				print('Prenom: {}'.format(self.client[i].prenom))
				print('email: {}'.format(self.client[i].email))
				print('numero: {}'.format(self.client[i].numero))
				print('profession: {}'.format(self.client[i].profession))
				print('solde: {} XOF'.format(self.client[i].solde))
	

	def solde_banque(self):
		solde=0
		for i in range(len(self.client)):
			solde= solde + self.client[i].solde

		print("---------------- Banque---------------")
		print('ref:00012545524af41552s45')
		print("Solde : {} XOF".format(solde))
			


		