#!/usr/bin/env python
# -*- coding: utf-8 -*-
## @author Михаил Драгункин <contact@unsektor.com>

## Begin.
## m - Число, n - Количество строк
m, n = list(map(int, raw_input(' > Ввести через запятую M и N\n : ').strip().split(',')))

## Определение длины строки максимального числа (результата умножения)
max_result_number_length = len(str(m*n))

## Определение длины строки максимального числа (первого множителя - N)
max_number_length = len(str(n))

i=1
while i <= n:
	print ('_' * (max_result_number_length-len(str(m*i))) if len(str(m*i)) < max_result_number_length else '') + str(m*i) + '_=' + '_' * max(1, (1+max_number_length-len(str(i)) if len(str(i)) < max_number_length else 1)) + str(i) + '_*_' + str(m)
	i += 1

exit(0)
## End.