import sys, os
temp = os.path.abspath(os.pardir) + '\\temp\\'

import pickle
import hashlib

class Keeper:

	def __init__(self, fname):
		self.fname = fname
		self.files = {'cfilepath': temp + 'temp1234.rybdb',
						'pwfile': temp + 'temp1234_pw.rybdb',
						'markerfile': 'sal_marker.rybdb',
						'dbpw': self.hashpw("Quel'danas2007"),
						'resetpw': True}
		
		if os.path.exists(self.fname):
			self.load()
		else:
			self.save()

	def hashpw(self, pw):
		md5_hasher = hashlib.md5()
		md5_hasher.update(str.encode(pw))
		return md5_hasher.digest()

	def load(self):
		self.files = pickle.load(open(self.fname, "rb"))

	def save(self):
		pickle.dump(self.files, open(self.fname, "wb"))