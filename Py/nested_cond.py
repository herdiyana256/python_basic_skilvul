'''
    NESTED CONDITIONAL STATEMENT 
    IF DAN ELSE STATEMENT JUGA DAPAT DISUSUN SEBAGAI NESTED IF-ELSE STATEMENT SEPERTI KODE DI BAWAH INI : 
'''

num = -100 
if num < 0: 
        print(num, 'adalah bilangan negative')

else: 
        print(num, 'adalah bukan bilangan negative')
if num % 2 == 0: 
print (num, 'adalah bilangan genap')

else: 
    print(num, 'adalah bilangan ganjil')

# output : -100 adalah bilangan negative

#Dalam kode di atas, if-else digunakan dua kali. Pernyataan if-else di luar disebut pernyataan outer if-else, dan pernyataan if-else di dalam disebut pernyataan inner if-else.

'''
    Pernyataan if-else ganda dapat terjadi dalam situasi di mana kondisi spesifik memerlukan verifikasi tambahan setelah True atau False dikembalikan untuk kondisi pertama. Sehingga dalam kode diatas, langkah validasi pertama adalah mengecek apakah angka tersebut adalah angka negatif <0 atau positif >0 dan kemudian validasi kedua adalah jika angka tersebut adalah positif, apakah nomor itu ganjil atau genap, sehingga diperlukan if dan else yang kedua.


'''