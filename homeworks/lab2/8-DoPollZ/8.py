#!/usr/bin/env python
# -*- coding: utf-8 -*-
## @author Михаил Драгункин <contact@unsektor.com>

## Вспомогательная функция для проверки типа данных Integer
def is_int(str):
    try: 
        int(str)
        return True
    except ValueError:
        return False

## Begin.
data = str(raw_input(' > Ввести целочисленное выражение в польской инверсной записи\n : ')).strip().split(' ')

## Список математических операторов
operators = ['+','-','*','/']

## Магия
stack = []

for key in data:	
	if (is_int(key) == True):
		stack.append(str(key))
	elif (key in operators):
		if len(stack) < 2:
			print ' ! Something went wrong'
			exit(2)
		temp = eval(str(stack[0]) + str(key) + str(stack[1]))
		stack.pop(0)
		stack[0]=temp
	else:
		print 'ERROR'
		exit(1)

print stack[0]
exit(0)
## End.