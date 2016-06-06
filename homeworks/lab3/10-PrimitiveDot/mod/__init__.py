#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

class Dot:
	def __init__(self, *coords):
		self.coords = coords
	
	def __str__(self):
		return str(self.coords)
	
	def distance(self, dot):
		## Проверка соответствия пространств
		if len(dot.coords) != len(self.coords):
			raise ValueError()
		
		## Для одного измерения
		if len(dot.coords) == 1:
			return abs(self.coords[0] - dot.coords[0])
		## Для двух измерений
		elif len(dot.coords) == 2:
			return math.sqrt( 
				  (dot.coords[0] - self.coords[0]) ** 2 
				+ (dot.coords[1] - self.coords[1]) ** 2
			)
		## Для трёх измерений
		elif len(dot.coords) == 3:
			return math.sqrt( 
				  (dot.coords[0] - self.coords[0]) ** 2 
				+ (dot.coords[1] - self.coords[1]) ** 2
				+ (dot.coords[2] - self.coords[2]) ** 2
			)
		else:
			raise ValueError('we can\'t handle the time!')
		
	def middle(self, dot):
		if len(dot.coords) == 1:
			return dot.coords[0]
		elif len(dot.coords) == 2:
			return (
				  ## (x1+x2)/2
				  (self.coords[0] + dot.coords[0]) / 2
				  ## (y1+y2)/2
				, (self.coords[1] + dot.coords[1]) / 2
			)
		elif len(dot.coords) == 3:
			return (
				  ## (x1+x2)/2
				  (self.coords[0] + dot.coords[0]) / 2
				  ## (y1+y2)/2
				, (self.coords[1] + dot.coords[1]) / 2
				  ## (z1+z2)/2
				, (self.coords[2] + dot.coords[2]) / 2
			)