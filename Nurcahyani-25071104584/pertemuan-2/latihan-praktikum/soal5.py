import math
x1 = int(input('Input titik x1: '))
y1 = int(input('Input titik y1: '))
x2 = int(input('Input titik x2: '))
y2 = int(input('Input titik y2: '))

def jarak(x1, y1, x2,y2):
   sumbuX = x2-x1
   sumbuY = y2-y1
   kuadrat = (sumbuX ** 2) + (sumbuY ** 2)
   sqrt = math.sqrt(kuadrat)
   return sqrt

hasil = jarak(x1, y1, x2,y2)
print (f'Jarak = {hasil}')