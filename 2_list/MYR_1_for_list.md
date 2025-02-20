# Циклы с list

lesson =

## for перебирает список

Можно напечатать список, перебирая один **элемент** (число) за другим. 

```python
a = [7, 13, -4]     # создали список
for x in a:
    print(x, end=' ')
print()             # печатаем "новую строку"    
```
* `for x in a:` - в переменную `x` по очереди записываем из `a` **числа** 7, 13 и -4.
* `print(x, end=' ')` - печатаем `x`, потом печатаем пробел (а не новую строку!)
* `print()` - печатаем только *курсор на новую строку*

Получим:
```cpp
7 13 -4 
```

## TASKINLINE Напечатать числа > 10

Даны числа. Напечатайте только **числа**, которые больше 10 (`> 10`).

TEST
13 9 -11 87 124 5
----
13 87 124
====
-13 9 -11 -87 -124 -5
----
====
10 11 9
----
11
====

## Напечатать список 2 раза

В списке числа хранятся. Их можно перебрать в цикле много раз. Они не исчезнут.

```python
a = [7, 13, -4]     # создали список

for x in a:         # печатаем 7 13 -4
    print(x, end=' ')
print()

for x in a:         # печатаем 7 13 -4 еще раз
    print(x, end=' ')
print()
```
получим
```cpp
7 13 -4
7 13 -4
```

## TASKINLINE Напечатать сначала четные числа, потом нечетные

Даны числа. 

Напечатайте сначала **четные** числа через пробел.
Потом напечатайте **нечетные** числа через пробел.

В примере четные числа `-12 124`, нечетные числа `13 9 87 5`.

TEST
13 9 -12 87 124 5
----
-12 124 13 9 87 5
====
-13 9 -11 -87 -124 -5
----
-124 -13 9 -11 -87 -5
====
10 11 9
----
10 11 9
====

## Сумма чисел

Нужно найти сумму чисел в списке.

Напишем функцию `summa`, которой передают список и она вычисляет сумму его чисел.

```python
def summa(z):       # внутри функции мы называем список z
    res = 0         # сначала результат 0
    for x in z:     # для каждого числа x из списка z
        res += x    # res увеличим на х
        print(f'x={x} res={res}')
        
    # после цикла вернем результат
    return res
   
a = [10, -3, 6, 8]  # создадим список, список называем a
s = summa(a)        # результат функции сохраним в переменной s
print(s)            # напечатаем ответ
```


## TASKINLINE сумма чисел

**Прочитайте** числа. Напечатайте только их сумму.

TEST
10 -3 6 8
----
21
====
3 4
----
7
====
10
----
10
====
1 2 3 4 5 6 7 8 9
----
45
====

## TASKINLINE сумма четных чисел

**Прочитайте** числа. Напечатайте сумму **четных** чисел.

10 + -6 + 8 = 12

TEST
10 -3 -6 8
----
12
====
3 4
----
4
====
10
----
10
====
1 2 3 4 5 6 7 8 9
----
20
====
-1 -2 -3 -4 -5 -6 -7 -8 -9
----
-20
====

