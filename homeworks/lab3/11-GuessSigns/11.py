#!/usr/bin/python
# -*- coding: utf-8 -*-
## @author Михаил Драгункин <contact@unsektor.com>

## @function getBinarySequenceForLength - Возвращает массив строк со значением числа в некоторой системе счисления
## @param {Integer} length
## @param {Integer} base
## @returns {List} 
def getBinarySequenceForLength(length, base):
	## Последовательность строк, счётчик
	sequence = []; i=0
	
	while (i < 2**length):
		sequence.append(str("{0:b}".format(i)))
		## Использование префикса, для соответсвия одной длине строки -> 1 -> 00001
		sequence[i]='0'*(length-len(sequence[i]))+sequence[i]
		i+=1
	return sequence

## @function getAllPossibleCombinationsOfSymbols - Возвращает массив всевозможных перестановок символов
## @param {List} alphabet - do nothing, алфавит символов
## @param {List} length - ограниче длины строки всевозможных перестановок символов
## @returns {List}
def getAllPossibleCombinationsOfSymbols(alphabet, length):
	sequence = getBinarySequenceForLength(length, len(alphabet))
	
	edits = [('0', '-'), ('1', '+')]
	for i,v in enumerate(sequence):
		for search, replace in edits:
			sequence[i] = sequence[i].replace(search, replace)
		sequence[i]=list(sequence[i])
	return sequence

## @function magic - возвращает список всевозможных вариаций операций между числами списка
## @param {List} numbers - массив чисел, между которыми необходимо подобрать всевозможные вариации символов алфавита (операторы сложения и вычитания)
## @returns {List}
def magic(numbers):
	## Если число одно, возвращаем его в строковом представлении
	if len(numbers) == 1:
		return numbers
	
	## Количество символов между числами
	## Например: 10, 20, 30 -> 2
	counter = len(numbers)-1
	
	## Получаем всевозможные перестановки операторов + и -
	variations = getAllPossibleCombinationsOfSymbols(['+', '-'], counter)
	
	possible_variations=[]
	for j in variations:
		temp = numbers[:]; counter=len(j)
		while (counter != 0):
			temp.insert(counter, j[counter-1])
			counter-=1
		possible_variations.append(''.join(temp))
	return possible_variations

## @function compareSequences - распечатывает сравнение равенст двух математических выражений
## @param {List} left - Список строк математических выражений
## @param {List} right - Список строк математических выражений
## @returns {Void} - nothing is nothing
def compareSequences(left, right):
	for key_left, value_left in enumerate(left):
		for key_right, value_right in enumerate(right):
			print ' > ', value_left, '=', value_right, ' -> ',  'YES' if eval(value_left) == eval(value_right) else 'NO'

## Begin. Let's get it party start.
numbers = raw_input(' > Введите числа\n : ').strip().split(' ')

i=0
while(i < len(numbers)-1):
	left  = numbers[:i+1]
	right = numbers[i+1:]
	compareSequences(magic(left), magic(right))
	i+=1
## End.