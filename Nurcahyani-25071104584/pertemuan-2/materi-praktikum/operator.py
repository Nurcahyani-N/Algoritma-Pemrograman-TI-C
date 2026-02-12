#aritmatika 
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

#assignment
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

#comparison
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#logical
x = 5

print(x > 0 and x < 10)
print(x < 5 or x > 10)
print(not(x > 3 and x < 10))

#identity
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y) #mencari dan membandingkan alamat
print(x == y) #membandingkan isi
print(x is not y)

#membership
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)
print("pineapple" not in fruits)

text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)

#bitwise, menggunakan nomor binary untuk perbandingannya
print(6 & 3)
print(6 | 3)
print(6 ^ 3)

#presedences, urutan eksekusi sebuah statement. menggunakan intuisi matematika
print((6 + 3) - (6 + 3))