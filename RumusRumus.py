def Menu():
    print('===RUMUS-RUMUS MATEMATIKA===')
    print('Pilih rumus yang ingin digunakan:')
    print('0. Keluar')
    print('1. Kalkulator')
    print('2. Rumus ABC')
    print('3. Luas Persegi')
    print('4. Luas Persegi Panjang')
    print('5. Luas Segitiga')
    print('6. Luas Trapesium')
    print('7. Luas Layang-Layang')
    print('8. Luas Lingkaran')
    print('9. Volume Limas(persegi/segitiga)')

def Rumus_persegi_panjang():
    print('===RUMUS LUAS PERSEGI PANJANG===')
    p = float(input('Masukkan panjang sisi(cm): '))
    l = float(input('Masukkan lebar sisi(cm): '))
    hasil = p * l
    print(f'Luas persegi panjang adalah {hasil} cm²')
def Rumus_persegi():
    print('===RUMUS LUAS PERSEGI===')
    s = float(input('Masukkan panjang sisi(cm): '))
    hasil = s * s
    print(f'Luas persegi adalah {hasil} cm²')
def Rumus_abc():
    print('===RUMUS ABC===')
    print('ax² + bx + c = 0')
    a = float(input('Masukkan a (angka divariabel x²): ')) 
    b =float(input('Masukkan b (angka divariabel x): '))
    c =float(input('Masukkan c (angka tanpa ada variabel x): '))
    dua_a = 2 * a
    pangkatb = b * b
    penjumlahan_dalam = pangkatb - 4 * a * c
    akar = penjumlahan_dalam ** 0.5
    hasil_awal1 = -b + akar
    hasil_awal2 = -b - akar
    x1 = hasil_awal1 / dua_a
    x2 = hasil_awal2 / dua_a
    print(f'x1 = {x1}') 
    print(f'x2 = {x2}') 
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
def kalkulator():
    print("Pilih operasi:")
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
def Rumus_segitiga():
    print('===RUMUS LUAS SEGITIGA===')
    a = float(input('Masukkan panjang alas(cm): '))
    t = float(input('Masukkan tinggi segitiga(cm): '))
    hasil = a * t * 0.5
    print(f'Luas segitiga adalah {hasil} cm²')
def Rumus_trapesium():
    print('===RUMUS LUAS SEGITIGA===')
    a = float(input('Masukkan panjang alas a(cm): '))
    b = float(input('Masukkan panjang alas b(cm): '))
    t = float(input('Masukkan tinggi trapesium(cm): '))
    ab = a + b
    hasil = 0.5 * ab * t
    print(f'Luas trapesium adalah {hasil} cm²')
def Rumus_layang():
    print('===RUMUS LUAS LAYANG-LAYANG===')
    a = float(input('Masukkan panjang d1(cm): '))
    b = float(input('Masukkan panjang d2(cm): '))
    ab = a + b
    hasil = 0.5 * ab
    print(f'Luas layang-layang adalah {hasil} cm²')
def Rumus_lingkaran():
    print('===RUMUS LUAS LINGKARAN===')
    a = float(input('Masukkan jari-jari(cm): '))
    hasil = 3.14 * a * a
    print(f'Luas layang-layang adalah {hasil} cm²')
def Rumus_limas():
    print('===RUMUS LUAS LIMAS===')
    print('1. Limas persegi')
    print('2. Limas segitiga')
    pilihL = input('Pilih (1/2): ')
    if pilihL == '1':
        s = float(input('Masukkan panjang sisi alas(cm): '))
        t = float(input('Masukkan tinggi limas(cm): '))
        hasil = s * s * t / 3
        print(f'Besar volume limas persegi adalah {hasil} cm³')
    if pilihL == "2":
        print('===RUMUS LUAS SEGITIGA===')
        a = float(input('Masukkan panjang sisi alas(cm): '))
        t = float(input('Masukkan tinggi segitiga(cm): '))
        tt = float(input('Masukkan tinggi limas(cm): '))
        hasil = a * t * 0.5
        hasil2 = hasil * tt / 3
        print(f'Besar volume limas segitiga adalah {hasil2} cm³')


while True:
    Menu()
    rumus = input('Masukkan nomor untuk memilih rumus : ')
    if rumus == '0':
        print('Terima kasih telah menggunakan program ini!')
        break
    if rumus == '1':
        kalkulator()
    if rumus == '2':
        Rumus_abc()
    if rumus == '3':
        Rumus_persegi()
    if rumus == '4':
        Rumus_persegi_panjang()
    if rumus == '5':
        Rumus_segitiga()
    if rumus == '6':
        Rumus_trapesium()
    if rumus == '7':
        Rumus_layang()
    if rumus == '8':
        Rumus_lingkaran()
    if rumus == "9":
        Rumus_limas()




