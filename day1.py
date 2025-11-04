#Latihan menuliskan variabel, menggunakan input, dan fungsi if

a = int(input('Nilai A = ')) # deklarasi variabel dan penggunaan statement input
b = int(input('Nilai B = ')) 

if (a > b):
    print("A lebih besar daripada B.")
    a = b
    b = 2 * a

elif (a < b):
    print("A lebih kecil daripada B.")
    b = a
    a = 2 * b

else:
    print("A sama dengan B.")

print("Nilai A: ", a)    
print("Nilai B: ", b)
print('Hello')   