# lambda функции

lesson = 496942

## Синтаксис

**Лямбда-функции** - это функции без имени (анонимные функции). Их объявляют так:

```python
lambda параметры: выражение
```

* **lambda** - ключевое слово. У обычной функции **def**, у анонимной `lambda`
* имени у функции нет
* **параметры** не обязательная часть. Обычно позиционые переменные через запятую. Можно использовать полный синтаксис, который допустим в def.
    * пишем без `()`
* **выражение**:
    * нельзя условные операторы или циклы (можно условные выражения);
    * нельзя **return** или **yield**

Результатом лямбда-выражения является анонимная функция. При ее вызове вычисляется значение *выражение* при указанных значениях параметров. 

Если выражение *выражение* - кортеж, то он должен быть заключен в круглые скобки ()

Пример: лямбда-функция, которая добавляет 's' если аргумент не 1 (окончание множественного числа).

Будем делать множественное число в английском языке. 1 file, 5 files; 1 counter, 9 counters и так далее

```python
s = lambda x: '' if x == 1 else 's'         # Анонимная функция присваивается переменной s.
postfix = s(count)                          # вызов функции 
print(f'{count} file{postfix} processed')   # использование этой функции
```

## Отличия от обычной функции

**Точно не нужно return?**

Не нужно. Эти две функции area (площадь треугольника по основанию w и высоте h) вызываются одинаково:

Обычная функция:
```python
def area1(w, h):
    return w * h / 2
```

Лямбда-функция (заметьте, return нет):
```python
area2 = lambda w, h: w * h / 2
```

Вызываем одинаково:
```python
area1(6, 5)
area2(6, 5)
```

## PEP-8 и лямбда-функции

Если код нужно использовать повторно (вызывать по имени), и функция пишется в одну строку, то лучше написать обычную функцию через def, а не использовать анонимную функцию (лямбду).

Плохо:
```python
area = lambda b, h: 0.5 * w * h 
```

Хорошо:
```python
def area(b, h): return 0.5 * w * h
```

## Где использовать lambda?

Часто используют в сортировке по ключу

Есть список строк. Нужно отсортировать строки по последней букве.
```python
strs = ['xc', 'zb', 'yd' ,'wa']
```
Решение через обычную функцию:
```python
# возвращает последний символ строки
def last_letter(s):
    return s[-1]

# сортирует список строк только по последним буквам
b = sorted(strs, key=last_letter)  ## ['wa', 'zb', 'xc', 'yd']
```
Решение через lambda-функцию:

```python
# сортирует список строк только по последним буквам
b = sorted(strs, key=lambda s: s[-1])  ## ['wa', 'zb', 'xc', 'yd']
```

## Сложный критерий

Дан список студентов. У каждого студента рост в сантиметрах и вес в килограммах.

Отсортируем по весу (по возрастанию), а при равном весе - по росту (по возрастанию).

Для этого в функции, которая возвращает proxy values вернём 1 tuple, в котором все критерии сортировки (вес, рост).

Дано:
```python
a = [(166, 55.2), (157, 55.2), (170, 55.2), (175, 90), (166, 73), (180, 73)]
```
Решение через обычную функцию:
```python
def wh1(t):
    h = t[0]
    w = t[1]
    return (w, h)  # обязательно возвратить tuple, главное вес, потом рост

b = sorted(a, key=wh1)
```

Решение через lambda-функцию:
```python
b = sorted(a, key=lambda t: (t[1], t[0]) )  # обязательно что возвращаем в ( )
```
В обоих случаях получим b:
```python
[(157, 55.2), (166, 55.2), (170, 55.2), (166, 73), (180, 73), (175, 90)]
```

**Возвращаем сложный критерий в ( )**

## Задачи

Специальных задач на lambda-функции не будет.

Попробуйте решать задачи в следующей линейке через lambda-функции.

