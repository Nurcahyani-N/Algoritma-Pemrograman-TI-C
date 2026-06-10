DAFTAR_PILIHAN = ["gunting", "batu", "kertas", "batu", 
                  "gunting", "kertas", "gunting", "batu"] 

# === BAGIAN A ===
def tentukan_pemenang(pilihan_pemain, pilihan_komputer):
    if pilihan_pemain == pilihan_komputer:
        return "Seri"
    elif (pilihan_pemain == "gunting" and pilihan_komputer == "kertas") or \
         (pilihan_pemain == "batu" and pilihan_komputer == "gunting") or \
         (pilihan_pemain == "kertas" and pilihan_komputer == "batu"):
        return "Pemain"
    else:
        return "Komputer"

def main_satu_giliran(nomor_giliran):
    pilihan_komputer = DAFTAR_PILIHAN[nomor_giliran % len(DAFTAR_PILIHAN)]
    while True:
        pilihan_pemain = input("Masukkan pilihan pemain (gunting/batu/kertas): ").strip().lower()
        if pilihan_pemain in ["gunting", "batu", "kertas"]:
            break
        print("Pilihan pemain tidak valid. Mohon masukkan antara gunting, batu, atau kertas!")

    print("Pilihan Komputer: {pilihan_komputer}")
    hasil = tentukan_pemenang(pilihan_pemain, pilihan_komputer)
    print ("==========================================")
    if hasil == "Pemain":
        print("Hasil dari Ronde Ini: Pemain telah menang!")
    elif hasil == "Komputer":
        print("Hasil dari Ronde Ini: Komputer telah menang!")
    else:
        print("Hasil Main Ronde Ini: Pemain dan Komputer seri!")
    return hasil
    
def main_satu_ronde(nama, nomor_ronde):
    print("\n--- Ronde ke-{nomor_ronde} dimulai! ---")
    menang_pemain = 0
    menang_komputer = 0
    giliran = 0
    while menang_pemain < 3 and menang_komputer < 3:
        hasil_giliran = main_satu_giliran(giliran)
        if hasil_giliran == "Pemain":
            menang_pemain += 1
        elif hasil_giliran == "Komputer":
            menang_komputer += 1
        giliran += 1
        print("Skor Permainan Sementara -> {nama}: {menang_pemain} | Komputer: {menang_komputer}")

    if menang_pemain == 3:
        print("Ronde ke-{nomor_ronde} dimenangkan oleh {nama}!")
        skor = menang_pemain * 10
    else:
        print(f"Ronde ke-{nomor_ronde} dimenangkan oleh Komputer!")
        skor = menang_komputer * 10

    return [nama, skor]

# === BAGIAN B ===
def tampilkan_riwayat(riwayat):
    if len(riwayat) == 0:
        print("Belum ada riwayat permainan.")
        return
    
    print("\n=== RIWAYAT PERMAINAN ===")
    print("No | Pemain | Komputer | Hasil")
    print("-------------------------------")
    
    for i in range(len(riwayat)):
        data = riwayat[i]
        print(f"{i+1}  | {data[0]}     | {data[1]}     | {data[2]}")

# === BAGIAN C ===
def bubble_sort_riwayat(riwayat):
    hasil = riwayat[:]
    
    n = len(hasil)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if hasil[j][1] < hasil[j+1][1]:
                hasil[j], hasil[j+1] = hasil[j+1], hasil[j]
            if not swapped:
                break
    return hasil

def tampilkan_leaderboard(riwayat):
    print("\n=== LEADERBOARD ===")
    for i in range(len(riwayat)):
        print(f"{i+1}. {riwayat[i][0]} - {riwayat[i][1]} poin")

# === Main ===
if __name__ == "_main_":
    nama_pemain = input("Masukkan nama Anda: ").strip()
    if nama_pemain == "":
        nama_pemain = "Pemain"

    riwayat = []
    nomor_ronde = 1

    while True:
        hasil_ronde = main_satu_ronde(nama_pemain, nomor_ronde)
        riwayat.append(hasil_ronde)

        lanjut = input("\nMain lagi? (ya/tidak): ").strip().lower()
        if lanjut != "ya":
            break
        nomor_ronde += 1

    tampilkan_riwayat(riwayat)
    tampilkan_leaderboard(riwayat)

__name__ == "_main_"