# Окружность

lesson = 526321

## Рисуем окружность

Команды черепахи:

* **t.stamp()** - отпечаток черепахи
* **t.dot(10)** - нарисовать точку радиусом 10
* **t.circle(50)** - нарисовать окружность радиусом 50

Внимание! Окружность рисуется из точки на окружности.

![пример](https://stepik.org/media/attachments/lesson/526321/circle.PNG)

```python
import turtle

t = turtle.Turtle()
t.shape('turtle')
t.width(3)

t.color('blue')
t.stamp()			# синий отпечаток

t.fd(50)

t.color('red')
t.dot(10)			# красная точка

t.fd(50)

t.color('green')
t.circle(50)		# зеленая окружность

turtle.done()
```

## TASKTEXT Окружность из центра

Напишите функцию **circle(x, y, r, col)**

Она ставит отпечаток черепахи в точке *(x, y)* и рисует окружность радиуса *r* с центром координат в точке *(x, y)* цветом *col*.

```python
circle(0, 0, 100, 'blue')
circle(0, 100, 50, 'gold')
circle(75, 0, 25, 'red')
```
должен нарисовать:
![окружности](https://stepik.org/media/attachments/lesson/526321/circle11.PNG)

## Новые слова

* красная **горизонтальная** линия 
* зеленая **вертикальная** линия
* синяя **окружность**

![рисунок](https://stepik.org/media/attachments/lesson/526321/vhline0.png)

## TASKTEXT вертикальная и горизонтальная линия

* Скопируйте функцию **circle(x, y, r, col)**.
* Напишите функцию **hline(y0, col)**. Она рисует горизонтальную линию $y=y0$ цветом **col**. Длина линии какая хотите.
* Напишите функцию **vline(x0, col)**. Она рисует вертикальную линию $x=x0$ цветом **col**. Длина линии какая хотите.

```python
circle(0, 0, 100, 'blue')
hline(100, 'violet')
vline(50, 'lightgreen')
```
должен нарисовать

![рисунок](https://stepik.org/media/attachments/lesson/526321/vhline.png)

## слева, посередине, справа

* Квадрат **слева** от круга.
* Треугольник **справа** от круга.
* Круг **между** квадратом и треугольником. Круг **посередине**

![слева и справа](https://stepik.org/media/attachments/lesson/526321/left_right.png)

## над, под, между

* Квадрат **сверху**. Квадрат **над** кругом. 
* Треугольник **снизу**. Треугольник **под** кругом.
* Круг **посередине**. Круг **между** квадратом и треугольником.

![над и под](https://stepik.org/media/attachments/lesson/526321/up_down.png)

## Пересекает

* Прямая **пересекает** квадрат. 
* Прямая **имеет общие точки** с квадратом.

![пересекает](https://stepik.org/media/attachments/lesson/526321/cross1.png)

* Прямая $a$ **пересекается** с прямой $b$.
* $K$ - **точка пересечения** прямых $a$ и $b$.

![точка пересечения](https://stepik.org/media/attachments/lesson/526321/cross2.png)
