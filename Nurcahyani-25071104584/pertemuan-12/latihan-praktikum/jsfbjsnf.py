struktur = {
    "Skripsi_Aqil": {
        "Bab_1": {
            "pendahuluan.docx": 45,
            "latar_belakang.docx": 62
        },
        "Bab_2": {
            "landasan_teori.docx": 118,
            "referensi": {
                "paper_A.pdf": 340,
                "paper_B.pdf": 210
            }
        },
        "Bab_3": {
            "metodologi.docx": 89,
            "diagram": {
                "flowchart.png": 512,
                "erd.png": 278,
                "arsitektur": {
                    "sistem.png": 430
                }
            }
        },
        "sidang": {
            "presentasi.pptx": 2048,
            "catatan_revisi.txt": 15
        },
        "README.txt": 8
    }
}

#TUGAS A
def total_ukuran (folder: dict) -> int:
    total = 0
    for item, value in folder.items():
        if type (value) == dict:
            total += total_ukuran(value)
        else:
            total += value 
    return total

#TUGAS B
def hitung_file(folder: dict) -> int:
    jumlah = 0
    for item, value in folder.items():
        if type (value) == dict:
            jumlah += hitung_file(value)  
        else:
            jumlah += 1
    return jumlah

#TUGAS C
def cari_terbesar(folder: dict) -> tuple:
    nama_max = '   '
    ukuran_max = -1
    
    for item, value in folder.items():
        if type (value) == dict:
            nama_sub, ukuran_sub = cari_terbesar(value)
            if ukuran_sub > ukuran_max:
                nama_max = nama_sub
                ukuran_max = ukuran_sub
        else:
            if value > ukuran_max:
                nama_max = item
                ukuran_max = value
                
    return (nama_max, ukuran_max)

#TUGAS D
def tampilkan_tree(folder: dict, nama: str = 'root', level: int = 0):
    indentasi = '  ' * level
    if type (folder) == dict:
        print(f'{indentasi}📁 {nama}')
        for item, value in folder.items():
            tampilkan_tree(value, item, level + 1)
    else:
        print(f'{indentasi}📄 {nama} ({folder} KB)')

print('===TUGAS A===')
print(f'Total ukuran skripsi: {total_ukuran(struktur)} KB')

print('\n===TUGAS B===')
print(f'Jumlah file: {hitung_file(struktur)} file')

print('\n===TUGAS C===')
nama_f, ukur_f = cari_terbesar(struktur)
print(f'File terbesar: {nama_f} ({ukur_f} KB)')

print('\n===TUGAS D===')
tampilkan_tree(struktur, 'Skripsi_Aqil', 0)