import pickle
import os

class Keeper:

	def __init__(self, fname):
		self.fname = fname
		self.files = {'cfilepath': 'temp1234.db'}
		
		try:
			self.load()
		except:
			self.save()



	def load(self):
		self.files = pickle.load(open(self.fname, "rb"))

	def save(self):
		pickle.dump(self.files, open(self.fname, "wb"))

#Keeper('keeper.db')