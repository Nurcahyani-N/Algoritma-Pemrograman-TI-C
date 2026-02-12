n = int(input('Masukkan angka yang diinginkan: '))

def total_digit(n):
   if n <= 0:
      return 0
   else:
      digit = (n % 10) + total_digit(n // 10)
      return digit
   
hasil = total_digit(n)
print(f'Jumlah digit dari {n} adalah {hasil}')