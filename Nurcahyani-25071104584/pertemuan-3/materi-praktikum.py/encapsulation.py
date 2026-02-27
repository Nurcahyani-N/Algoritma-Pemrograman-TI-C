class Person:
  def __init__(self, name, age):
    self.name = name # Public property
    self._age = age # Protected property
    self.__age = age # Private property

p1 = Person("Emil", 25)
print(p1.name)
print(p1._age) #protected. bisa diakses krn seharusnya tidak
print(p1._Person__age) #mangling, buat ngintip
