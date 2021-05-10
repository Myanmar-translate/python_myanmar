import turtle           

colors = [
  'violet',   # colors[0]
  'blue',     # colors[1]
  'green',    # colors[2]
  'yellow',   # colors[3]
  'gold',     # colors[4]
  'orange',   # colors[5]
  'red'       # colors[6]
  ]

def sq(size, col):  # ���������� ������� ������� size ����� col
  t.color(col)
  for i in range(4):
    t.fd(size)
    t.left(90)

# ���������� n ���������, 
# ������ ������� size, 
# ������ ��������� �� d ������
# ��� ���������� i ���������
def sqn(size, d, n, i):
  if n == 0:          # ���� �� ���� ������ �������� ���������        
    return 
  if size <= 0:        # ���� ��������� ������� ���������, ������ �� ��������
    return

  sqn(size-d, d, n-1, i+1) # �������� ��������� �������
    
  sq(size, colors[i])   # colors[i] - ����� ���� ����� i �� colors
    
t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)

sqn(100, 20, 7, 0)    # 7 ���������, ������ �������� 200, ������ �� 20 ������

turtle.done()    