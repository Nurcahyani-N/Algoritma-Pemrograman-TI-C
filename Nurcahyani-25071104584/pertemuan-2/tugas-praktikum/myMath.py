def penjumlahan (a,b):
    return a + b
print (penjumlahan(9,7))


def pengurangan (a,b):
    return a - b
print (pengurangan(2,5))


def perkalian (a,b):
    return a*b
print (perkalian(8,9))


def pembagian (a,b):
    if b == 0:
       print ("Pembagian tidak dapat dilakukan karena pembagi bernilai 0")
    else:
       return a / b
print (pembagian(9,3))


def mod (a,b):
    return a % b
print (mod (8,5))


n = 7
fbnc = []
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range (n) :
  fbnc.append(fibonacci(n-i))
print (fbnc)
