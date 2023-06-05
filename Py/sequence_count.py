# SEQUENCE DATA TYPES - COUNT METHOD
'''
    Method count() mengembalikan jumlah element dalam objek sequence. 
    Metode ini bisa digunakan untuk mencari element yang terdapat di dalam objek sequence dan juga mengetahui berapa banyak element di dalam objek sequence tersebut . 
    Dalam kode di bawah ini, tiga buah angka 11 ditemukan dalam list1, sehingga mengembalikan angka 3. 

'''
list1 = [11,11,11,22,33,44] 
print(list1.count(11)) # mencari total angka 11 dalam list 

# output : 3 

# Method count() dapat juga digunakan untuk tipe data tuple, range, dan string : 


# Tuple : 
tup1 = (11,11,11,22,33,44) 
    print(tup1.count(11)) # mencari total angka 11 dalam tuple. 


# output : 3 





# STRINGS : 
# Kita juga bisa menghitung jumlah sebuah karakter di dalam sebuah string 

str1 = 'Hello World'
print(str1.count('1')) # mencari total huruf 1 dalam string

# output : 3 


# CONTOH PENGGUNAAN DAN APLIKASI METODE count() dalam kode . 
ran == range(0,5,1)
print(len(ran))
    print(ran.count(2))
# output : 5 1


# ran memiliki lima element 0,1,2,3,4. Banyak nya element yang di cetak dengan menggunakan fungsi len adalah 5 . 


# Pada sisi lain, ketika menggunakan metode count() untuk melihat seberapa banyak angka 2 dalam variabel yang dijalankan, itu akan mencetak 1 karena hanya ada 1 angka 2 dari range 0 hingga 5 . 

