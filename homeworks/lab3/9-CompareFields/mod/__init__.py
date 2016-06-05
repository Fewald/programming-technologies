#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Comparator:
	def __init__(self, value):
		self.value = value
	
	def compare(self, object):
		if not hasattr(object, 'value'):
			return 1
		
		if object.value > self.value:
			return -1
		elif  object.value < self.value:
			return 1
		else:
			return 0