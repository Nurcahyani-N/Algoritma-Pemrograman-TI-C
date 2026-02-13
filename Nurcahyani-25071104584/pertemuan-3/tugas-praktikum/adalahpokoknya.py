class Vehicle:
    def __init__(self, jenis, merek, trilis):
        self.jenis = jenis
        self.merek = merek
        self.trilis = trilis

    def sound (self):
        return ("Suara")

class Motor(Vehicle):
    def __init__(self, trilis, merek):
      self.__trilis = trilis
      
    def get_trilis(self):
      return self.__trilis
    
    def set_trilis(self, trilis):
      self.__trilis = trilis
    
    def sound(self):
      return ("Ngeng")

class Mobil(Vehicle):
    def __init__(self, trilis, merek):
      self.__trilis = trilis
      
    def get_trilis(self):
      return self.__trilis
    
    def set_trilis(self, trilis):
      self.__trilis = trilis
    
    def sound(self):
      return ("Brom")

a = Vehicle('Kapal','Blabla', 1965)
b = Motor (2007,'Vario')
c = Mobil (2007, 'Brio')

print(a.sound())
print(b.get_trilis())