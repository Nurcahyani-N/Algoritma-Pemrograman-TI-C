total=int(input(f'Masukkan total hari keterlambatan: '))

while total > 0:
    if total < 0:
        print('Error, input ulang data')
    if total == 0:
        print('Tidak ada denda')
    else:
        print('Total denda Anda: Rp.')