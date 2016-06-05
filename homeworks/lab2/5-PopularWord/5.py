#!/usr/bin/env python
# -*- coding: utf-8 -*-
## @author Михаил Драгункин <contact@unsektor.com>

## Begin.
## Инициализация *буфера* данных
data = '';

## Ввод строки (до ввода пустой строки)
while True:
	input = raw_input(' > Вводите строки текста (пустая строка доя завершения ввода)\n : ')
	if input != "":
		data += input + ' '
	else:
		break

## Разбиение текста на слова
data = data.strip().split(' ')

## Инициализация индекса слов (словаря)
index = {}

## Подсчёт количества повторений для слов
for key in data:
	if key in index:
		index[key]+=1
	else:
		index[key]=1

## Максимольное количество повтора слов
max = 0

## Определение максимального количества вхождений
for key in index:
	if index[key] > max:
		max=index[key]
## Поиск слов с максимальным количеством повтором в тектсте и вывод
for key in index:
	if index[key] == max:
		print key + ' -> ' + str(index[key])

exit(0);
## End.