#!/usr/bin/python
# -*- coding: utf-8 -*-
## @author Михаил Драгункин <contact@unsektor.com>

## @function compute - Расчитвыает минимальную стоимость пути с земли до последней ступени (на которую наступать обязательно), при условии, что идти можно только вверх и перешагивать можно не более, чем через S-1 ступень
## @param {List} db_price - стоимость ступеней
## @param {Integer} step_width - ширина шага
## @returns {Integer}
def compute(_db_price, step_width):
	## Если до последней ступень можно шагнуть одним шагом
	if len(_db_price) <= step_width:
		## Возвращаем стоимость последней ступени
		return _db_price[-1]
	
	## Проходим каждую ступень
	for i, v in enumerate(db_price):
		## Определяем, в каких пределах возможно наступать на ступени
		
		if not(i < step_width):
			## Определяем минимальную стоимость шага
			min_price = min(_db_price[i-step_width:i])
			_db_price[i] += min_price
	return _db_price[-1]

## Begin.

db_price = [int(x) for x in raw_input(' : Введите стоимость ступеней (через запятую)\n : ').split(', ')]

step_width = int(input(' : Введите ширину шага\n : '))

print ' >', compute(db_price, step_width)

exit(0)
## End.