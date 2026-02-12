#if-elif-else
temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")

#shorthand if, hanya ditulis satu baris
a = 5
b = 2
if a > b: print("a is greater than b")
#shorthand if else
a = 2
b = 330
print("A") if a > b else print("B")
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)
#multiple condition
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#logical operator
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#nested if
score = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")

#pass statement
age = 16

if age < 18: #stlh titik dua harus ada sasuatu disini
  pass #untuk menghandle error, tetapi tidak ngeprint apapun
else:
  print("Access granted")