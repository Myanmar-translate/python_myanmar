# Аргументы функций

lesson = 505564

## Уже знаем

* Метод черепахи
    * уже существует
    * `t.метод()` - вызываем метод черепахи `t`
* Новая функция
    * нужно объявить 1 раз `def имя():`
    * можно вызывать много раз `имя()`
    
Функции нужны:

* из большой сложной задачи сделать много маленьких простых задач.
* 1 раз объявить и много раз вызвать, а не повторять одинаковый код.

"Метод черепахи" иногда называют "функция черепахи". Так тоже можно говорить.

[Описание функций и методов turtle](https://docs.python.org/3/library/turtle.html)

## Аргументы функций в математике

Математики используют функции. У функций есть аргументы. У функции sin 1 аргумент.

* $\sin(x)$ 
    * **функция** синус (function)
    * $x$ - **аргумент** функции $\sin$ (argument)
* $\sin(\pi)$ 
    * $\pi$ - **значение** аргумента функции $\sin$ (value)

У функции $log$ два аргумента.

* $\log_{b}(a)$ "логарифм $a$ по основанию $b$"

Аргумент функции иногда называют "параметр функции" (parameter).

В python у функций тоже есть аргументы.   
     
## Аргументы функций черепахи

Вызываем функции черепахи и передаем в функцию цвет, угол, размер линии.

Это **аргументы** (или **параметры**) функции.

```python
t.color('blue')   # передали цвет 'blue' функции черепахи color 
t.lt(45)          # передали угол 45 функции черепахи lt
t.width(3)        # передали размер 3 функции черепахи width
```

## Вся программа

Нужно рисовать цветной треугольник. Каждый треугольник рисуем своим цветом. Красный, зеленый, синий. 

Мы написали программу:

![3 треугольника](https://stepik.org/media/attachments/lesson/479594/01_tri3.png)

```python
import turtle

# Это новая команда - функция
# Назовем ее triangle()
# def пишем с начала строки без пробелов
def triangle():
    # здесь пишем команды - рисовать треугольник
    # команды надо начать с <TAB> (отступа)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
# Здесь закончилась новая команда triangle

# Это место для выполнения команд. Новых и старых.
t = turtle.Turtle()
t.shape('turtle')
t.width(3)

t.color('red')
# выполняется новая команда triangle
triangle()      
t.lt(45)

t.color('green')
# еще раз выполняется новая команда triangle
triangle()      
t.lt(45)

t.color('blue')
# вызывать (выполнять) новые команды можно сколько хочешь
triangle()      

turtle.done()
```

## Еще лучше

Что делает?

* цвет красный
* нарисовать треугольник
* налево 45 градусов
* цвет зеленый
* нарисовать треугольник
* налево 45 градусов
* цвет синий
* нарисовать треугольник
* налево 45 градусов

```python
t.color('red')
triangle()      
t.lt(45)

t.color('green')
triangle()      
t.lt(45)

t.color('blue')
triangle()      
```
Хочу делать:

* нарисовать *красный* треугольник
* налево 45 градусов
* нарисовать *зеленый* треугольник
* налево 45 градусов
* нарисовать *синий* треугольник

```python
triangle('red')      
t.lt(45)
triangle('green')      
t.lt(45)
triangle('blue')      
```

Как сделать?

## SKIP VIDEO

[youtube](https://youtu.be/iaEbDnY5lqQ)

## Аргументы функции

[Видео](https://youtu.be/iaEbDnY5lqQ)


Для новых функций тоже можно указать параметры (аргументы).

Передадим цвет и будем рисовать треугольник.

Аргумент *col* называется "**переменная** col" (**variable**).

```python
# col запомнит название цвета для треугольника
def triangle(col):
    # указываем col в другой команде
    t.color(col)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
```

Выполнять команду triangle нужно с цветом:

```python
# Указываем цвет для треугольника 'red'
triangle('red')      
t.lt(45)

# Указываем цвет для треугольника 'green'
triangle('green')      
t.lt(45)

# Указываем цвет для треугольника 'blue'
triangle('blue')      
```

![3 треугольника](https://stepik.org/media/attachments/lesson/479594/01_tri3.png)

Вся программа:
```python
import turtle

# col запомнит название цвета для треугольника
def triangle(col):
    # указываем col в другой команде
    t.color(col)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)

# Здесь закончилась новая команда triangle

# Это место для выполнения команд. Новых и старых.
t = turtle.Turtle()
t.shape('turtle')
t.width(3)

# Указываем цвет для треугольника 'red'
triangle('red')      
t.lt(45)

# Указываем цвет для треугольника 'green'
triangle('green')      
t.lt(45)

# Указываем цвет для треугольника 'blue'
triangle('blue')      

turtle.done()
```

## TASKTEXT Задача: квадраты и треугольники

* Возьмите пример.
* Напишите в нем функцию **sq(col)**. Она рисует квадрат цвета col.
* Нарисуйте 2 квадрата - зеленый и желтый. Нарисуйте 2 треугольника - красный и синий. Используйте функции `triangle(col)` и `sq(col)`.

![пример](https://stepik.org/media/attachments/lesson/479595/func_t8.png)

Пример: 3 треугольника.
```python
import turtle

# col запомнит название цвета для треугольника
def triangle(col):
    # указываем col в другой команде
    t.color(col)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)

# Здесь закончилась новая команда triangle

# Это место для выполнения команд. Новых и старых.
t = turtle.Turtle()
t.shape('turtle')
t.width(3)

# Указываем цвет для треугольника 'red'
triangle('red')      
t.lt(45)

# Указываем цвет для треугольника 'green'
triangle('green')      
t.lt(45)

# Указываем цвет для треугольника 'blue'
triangle('blue')      

turtle.done()
```
