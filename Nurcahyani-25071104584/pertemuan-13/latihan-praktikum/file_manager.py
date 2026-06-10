import os

def tampilan_menu():
    print("===============================")
    print("PYTHON FILE MANAGE v1.0")
    print("===============================")

    print("[1] Read file")
    print("[2] Write file")
    print("[3] Delete file")
    print("[0] Exit")

    pilihan = int(input("Pilih Menu: "))
    return pilihan

def pilih_file():
    print("File tersedia:")
    print("[1] catatan.txt")
    print("[2] tugas.txt")
    print("[3] jadwal.txt")

    pilihan = int(input("Pilih File: "))
    return pilihan

def read_file(file):
    if os.path.exists(file):
        print(f"--- Isi {file} ---")
        with open(file, "r") as f:
            print(f.read())
    else:
        print("File belum ada.")

def write_file(file):
    with open(file, "a") as f:
        teks = input(f"Isi untuk {file}: ")
        f.write(teks + "\n")

def delete_file(file):
    if os.path.exists(file):
        os.remove(file)
        print(f"{file} berhasil dihapus.")
    else:
        print("File tidak ada.")

def main():
    while True:
        pilih_menu = tampilan_menu()

        match pilih_menu:
            case 1:
                pilih = pilih_file()

                match pilih:
                    case 1:
                        read_file("catatan.txt")
                    case 2:
                        read_file("tugas.txt")
                    case 3:
                        read_file("jadwal.txt")

            case 2:
                pilih = pilih_file()

                match pilih:
                    case 1:
                        write_file("catatan.txt")
                    case 2:
                        write_file("tugas.txt")
                    case 3:
                        write_file("jadwal.txt")

            case 3:
                pilih = pilih_file()

                match pilih:
                    case 1:
                        delete_file("catatan.txt")
                    case 2:
                        delete_file("tugas.txt")
                    case 3:
                        delete_file("jadwal.txt")

            case 0:
                print("Program selesai.")
                break

        print("------------------------------")

main()