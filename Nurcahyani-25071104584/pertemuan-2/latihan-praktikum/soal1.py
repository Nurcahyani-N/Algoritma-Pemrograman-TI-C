listNilai = [80, 75, 90, 60, 85]

def rata_rata(nilai):
    total=0
    if not nilai:
        print('Data kosong')
    else:
        for x in range(len(nilai)):
            total += nilai [x]

    rata = total / (len(nilai))
    return rata

print('Nilai rata-rata nya adalah ', rata_rata(listNilai))