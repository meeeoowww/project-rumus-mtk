print('===RUMUS ABC===')
print('ax² + bx + c = 0')
      
a = float(input('Masukkan a (angka divariabel x²): '))
b =float(input('Masukkan b (angka divariabel x): '))
c =float(input('Masukkan c (angka tanpa ada variabel x): '))

dua_a = 2 * a
pangkatb = b * b
penjumlahan_dalam = pangkatb - 4 * a * c
akar = penjumlahan_dalam ** 0.5
hasil_awal1 = -1 * b + akar
hasil_awal2 = -1 * b - akar
x1 = hasil_awal1 / dua_a
x2 = hasil_awal2 / dua_a

print(f'x1 = {x1}') 
print(f'x2 = {x2}') 

