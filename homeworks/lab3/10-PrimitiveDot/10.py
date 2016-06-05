#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mod

for A,B in (mod.Dot(1,2,3),mod.Dot(3,4,5)), (mod.Dot(1,2),mod.Dot(3)):  
	print A 
	
	try:  
		print "{:.3f}".format(A.distance(B))  
		print A.middle(B)  
	except ValueError:  
		print "ERROR"  