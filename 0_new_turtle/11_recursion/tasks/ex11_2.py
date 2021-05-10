# -*- coding: utf-8 -*-
import turtle           
import time

hues = [
  'violet',   # hues[0]
  'blue',     # hues[1]
  'green',    # hues[2]
  'yellow',   # hues[3]
  'gold',     # hues[4]
  'orange',   # hues[5]
  'red'       # hues[6]
  ]

def sq(size, col):          # ���������� ������� ������� size ����� col
  t.color(col)
  for i in range(4):
    t.fd(size)
    t.left(90)

# ���������� n ���������, 
# ������ ������� size, 
# ������ ��������� �� d ������
# ��� ���������� i ���������
def sqn(size, d, n, i):
  if n == 0:                # ���� �� ���� ������ �������� ���������        
    return 
  if size <= 0:             # ���� ��������� ������� ���������, ������ �� ��������
    return

  sqn(size-d, d, n-1, i+1)  # �������� ��������� �������
  sq(size, hues[i])         # �������� 1 ������� 
    
t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)

sqn(200, 20, 7, 0)    # 7 ���������, ������ �������� 200, ������ �� 20 ������

turtle.done()    