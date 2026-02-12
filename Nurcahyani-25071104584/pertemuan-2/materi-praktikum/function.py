#void funct
def my_function():
  print("Hello")
my_function() #kalau ga ada ini, ga akan kepanggil

def my_function(name): #parameter
  print("Hello", name)

my_function("Nur") #argumen
#bisa kek gini juga
def my_function(name= "Nur"):
  print("Hello", name)

my_function() 

#return value
def get_greeting():
  return "Hello from a function"
message = get_greeting()
print(message)
#bisa kek gini juga
def get_greeting():
  return "Hello from a function"
print(get_greeting())

def myfunc():
  x = 300
  print(x)
myfunc()

#lambda, anonnymous funct yang hanya bisa dipakai sekali
x = lambda a : a + 10
print(x(5))

#recursion, memanggil dirinya sendiri dan punya 2 karakteristik
def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1) #akan terjadi loop pada fac

print(factorial(5))