# BASIC LOOP - FOR LOOP 

'''

    Basic loop(while loop)
    Basic loop atau while loop adalah jenis perulangan yang akan mengekesekusi satu blok kode selama suatu kondisi bernilai TRUE. 
    Jika kondisi bernilai FALSE, maka program akan keluar dari loop dan melanjutkan eksekusi program selanjutnya . 
    Berikut adalah contoh penggunaan basic loop dalam Python : 

'''
# example : 

i = 1   
    while i <= 5: 
        print(i)  
    i += 1 

# Program diatas akan menampilkan angka 1 sampai 5 di layar 


'''
2. FOR LOOP 
FOR LOOP ADALAH JENIS PERULANGAN YANG MEMUNGKINKAN KITA UNTUK MENGULANG SUATU BLOK KODE SEJUMLAH KALI BERDASARKAN ELEMENT-ELEMENT PADA SUATU OBJEK ITERABLE, SEPERTI LIST, TUPLE, ATAU STRING.
BERIKUT ADALAH CONTOH PENGGUNAAN FOR LOOP DALAM PYTHON :     

'''
fruit = ["apple", "watermelon","banana"]
    for fruit in fruits: 
        print(fruit)
#Program di atas akan menampilkan nama-nama buah yang terdapat dalam list fruits, yaitu "apple", "banana", dan "cherry".


'''

    KENAPA PERLU LOOP STATEMENT ?
    - ITERASI KODE SESUAI DENGAN KONDISI NYA MEMBANTU MEMECAHKAN MASALAH YANG KOMPLEKS
    - MISALNYA, SEBUAH PROGRAM MENJADI JAUH LEBIH RINGKAS DENGAN MENGGUNAKAN STRUKTUR PERULANGAN DARI PADA COPY DAN PASTE PERNYATAAN TERTENTU UNTUK MENGULANGI TUGAS YANG SAMA. 
    - SELAIN ITU, LOOP STATEMENT DAPAT MENGURANGI WAKTU YANG DI BUTUHKAN UNTUK PEMOGRAMAN

'''


# CONTOH PENERAPAN LOOPING DALAM SEBUAH PROGRAM, PERHATIKAN KODE BERIKUT INI : 
print('Welcome to everyone!!')
print('Welcome to everyone!!')
print('Welcome to everyone!!')
print('Welcome to everyone!!')
print('Welcome to everyone!!')

'''
Output : 
Welcome to everyone!!
Welcome to everyone!!
Welcome to everyone!!
Welcome to everyone!!
Welcome to everyone!!

Contoh program di atas bertugas untuk menampilkan string 'Welcome to everyone!! sebanyak 5 kali tanpa menggunakan loop statement. Namun bayangkan jika kita ingin menampilkan string tersebut sebanyak 1000, 10.000 atau 1.000.000 kali? Maka kode akan sangat panjang hingga menjadi kurang efisien.


DENGAN LOOP STATEMENT KODE AKAN MENJADI LEBIH EFISIEN SEPERTI BERIKUT INI : 
'''
for i in range(5): 
    print('Welcome to everyone!!')

''' 
    Output : 
    Welcome to everyone!!
    Welcome to everyone!!
    Welcome to everyone!!
    Welcome to everyone!!
    Welcome to everyone!!


    Dengan kode berikut kita hanya membutuhkan 2 baris untuk menampilkan output 'Welcome to everyone!!' sebanyak 5 x dan jika kita ingin mengulang nya sebanyak 1000 kali, 
    kita hanya perlu mengganti angka 5 dalam kode tersebyt menjadi 1000 sehingga kode ini menjadi sangat efisien menggunakan loop statement.

'''




