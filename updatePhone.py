#!/usr/bin/env python

class AddBookEntry(object):
	'address book entry calss'
	def __init__(self,nm,ph):
		self.name = nm
		self.phone = ph
		print 'created instance for:',self.name
	def updatePhone(self,newph):
		self.phone = newph
		print 'updated phone for:',self.name

zxx = AddBookEntry('john doe','010-2324343')

print zxx.name,zxx.phone


