#!/usr/bin/env python
# -*- coding: utf-8 -*-
## @author Михаил Драгункин <contact@unsektor.com>
## Для отладки работы программы - раскоментировать -> #print

## База данных деталей
db_details = []

## База данных инструкций (агрегатов)
db_aggregate = {}

## @function test_aggregate - Функция, проверяющая - возможно ли собрать агрегат
## @param {List} aggregate - Массив деталей (инструкция сборки)
## @return {Boolean} - True, если сборка агрегата возможна, False - если нет.
## @todo - так как используется рекусрсия, желательно использовать кэш - чтобы не просчитывать просчитанные детали по несколько раз
def test_aggregate(details):
	# print 'test: ', details
	if not(isinstance(details, list)) or not(len(details) > 0):
		return False
	
	## PS: Можно сократить до одной строки, но зачем ? (ориентируемся на расширяемость функционала)
	for v in details:
		#print 'component: ', v
		## Проверяем элемент сборки - является ли деталью, состоящей в базе данных
		if v in db_details:
			#print ' * "', v, '" есть в БД деталей - порядок'
			continue
		## Проверяем элемени сборки - является ли агрегатом, состоящей в базе данных и возможно ли его собрать
		elif v in db_aggregate and test_aggregate(db_aggregate[v]):
			#print ' * "', v, '" есть в БД агрегатов и его можно собрать - порядок'
			continue
		## Элемент сборки либо не является деталью, либо не явлется агрегатом, или агрегат - который нельзя собрать.
		else:
			return False
	return True

## Begin.
## Ввод строки (до ввода пустой строки)
while True:
	input = raw_input(' > Введите строки текста (пустая строка доя завершения ввода)\n : ').strip().split(' ')
	
	if input != ['']:
		if len(input) == 1:
			print ' > Добавление "', input[0], '" в список деталей' 
			db_details.append(input[0]);
		else:
			print ' > Добавление "', input[0], '" в список агегатов с деталями: ',  input[1:]
			db_aggregate[input[0]] = input[1:]
	else:
		break

## Если был введен хотя бы один агрегат
if len(db_aggregate) > 0:
	print ' * База данных деталей: ', db_details
	print ' * База данных агрегатов: ', db_aggregate
	print ' * Проверяем, можно ли собрать агрегат "', db_aggregate.keys()[0], '": ', db_aggregate.values()[0]
	
	print 'YES' if test_aggregate(db_aggregate.values()[0]) else 'NO'
	exit(0)
else:
	print ' ! Error: no aggregate found.'
	print 'NO'
	exit(1)
## End.