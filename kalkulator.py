def kalkulator():
    print('=== Kalkulator Sederhana ===')
    print('Operasi yang tersedia')
    print('1. Penjumlahan (+)')
    print('2. Pengurangan (-)')
    print('3. perkalian(*)')
    print('4. pembagian(/)')

    try:
        angka1 = float(input('Masukkan angka pertama: '))
        angka2 = float(input('Masukkan angka kedua: '))
        operasi = input('pilih operasi (+, -, *, /): ')

        if operasi == '+':
            hasil = angka1 + angka2
        elif operasi == '-':
            hasil = angka1 - angka2
        elif operasi == "*":
            hasil = angka1 * angka2
        elif operasi == '/':
            if angka2 != 0:
                hasil = angka1 / angka2
            else:
                print('Error : Pembagian dengan nol tidak bisa dioperasikan')
        else:
            print('Operasi tidak valid.')
            return
        
        print(f'Hasil: {hasil}')
    
    except ValueError:
        print('Input tidak valid. Harap masukkan angka.')
    
kalkulator()