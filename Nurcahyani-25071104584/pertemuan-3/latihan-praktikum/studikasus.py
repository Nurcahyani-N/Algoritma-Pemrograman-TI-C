while True:
    try:
        # Input dari user berupa angka
        jumlah = int(input("Masukkan jumlah nilai yang ada: "))
        # Validasi nilai
        if jumlah <= 0:
            # Kalau tidak valid, sengaja munculkan error
            raise ValueError("Jumlah harus lebih dari 0")
        # Kalau valid, keluar dari loop
        break
    except ValueError as e:
        # Menangani error yang terjadi kalau bukan angka yang diinput atau negatif
        print("Input tidak valid:", e)

# Variable seluruh nilai
total = 0
# Perulangan sebanyak jumlah nilai yang diinput user
for i in range(jumlah):
    while True:
        try:
            # Menggunakan float agar bisa menerima angka desimal
            nilai = float(input(f"Masukkan nilai ke-{i+1}: "))
            # Validasi nilai 
            if nilai < 0:
                # Kalau tidak valid, sengaja munculkan error
                raise ValueError("Nilai tidak boleh negatif")
            # Kalau valid, tambahkan ke total
            total += nilai
            # Keluar dari loop
            break
        except ValueError as e:
            # Menangani error yang terjadi kalau bukan angka yang diinput atau negatif
            print("Input tidak valid:", e)

# Menghitung rata-rata dengan membagi total nilai dengan jumlah data
rata = total / jumlah
# Menampilkan hasil rata-rata
print("Rata-rata nilai:", rata)