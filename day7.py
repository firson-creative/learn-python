import math

nama = input("Masukkan Nama Kamu: ")
print("===============================")
konversiAngka = [ord(char) for char in nama]
totalAngka = sum(konversiAngka)

matematis = totalAngka * 1.6180339887 * 100000
ambil_angka = str(matematis).replace('.', '')

#for item in ambil_angka:
 #   print(item)

kode = list(set(ambil_angka))
print()
print("Kode berdasarkan nama kamu:")
print(kode)