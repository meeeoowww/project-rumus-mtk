def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y == 0:
        return "Tidak bisa dibagi dengan nol!"
    return x / y

while True:
    ("Pilih operasi:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")

    pilih = input("Masukkan pilihan (1/2/3/4): ")
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    if pilih == '1':
        print("Hasil:", tambah(angka1, angka2))
    elif pilih == '2':
        print("Hasil:", kurang(angka1, angka2))
    elif pilih == '3':
        print("Hasil:", kali(angka1, angka2))
    elif pilih == '4':
        print("Hasil:", bagi(angka1, angka2))
    else:
        print("Pilihan tidak valid.")
    if pilih == "5":
        print('Kembali')
    