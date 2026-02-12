x = int(input('Masukkan bilangan pokok: '))
y = int(input('Masukkan bilangan pangkat: '))

def pangkat_rekursif(x, y):
  hasil = x
  
  for i in range (y-1):
   hasil = hasil*x
  return hasil

hasil = (pangkat_rekursif(x, y))
print (f'Hasil dari {x} pangkat {y} adalah {hasil}')