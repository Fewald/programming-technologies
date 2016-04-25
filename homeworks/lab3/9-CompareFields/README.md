Реализовать класс Comparator, содержащий только поле value и метод compare, возвращающий результат сравнения value с полем value любого другого объекта (аналогичный работе стандартной функции cmp()). Если такого поля нет, метод возвращает 1.
Input:
   C = mod.Comparator(123)
   class Test: pass
   T = Test()
   T.value = 124
   print C.compare(T)
Output:
 -1
