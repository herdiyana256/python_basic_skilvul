'''
    Dictionary - Basics 


    Bahasa Python terdapat tipe data dictionary yang digunakan untuk menyimpan kumpulan pasangan kunci-nilai (key-value pairs) .
    Dictionary dapat digunakan sebagai tabel hash atau kamus, dimana setiap element disimpan dengan menggunakan kunci sebagai reference.

    
    1. Membuat Dictionary : ) Contoh ":

'''
# Example : Membuat Dictionary
my_dict = {'nama': 'Herdiyan', 'usia': 27, 'kota': 'Jakarta' }




# Example : Mengakses Nilai dalam Dictionary :  Untuk mengakses nilai dalam dictionary, kita dapat menggunakan kunci sebagai indeks. Contoh : 
print(my_dict['nama']) # Output : Herdiyan 


# Mengubah Nilai dalam Dictionary :  Kita dapat mengubah nilai dalam dictionary dengan menggunakan kunci sebagai indeks. Contoh : 
my_dict['usia'] = 30 
print(my_dict['usia']) # Output : 30 



# Menambahkan Pasangan Kunci-Nilai Baru : kita dapat menambahkan pasangan kunci-nilai baru ke dalam dictionary dengan menggunakan sintaksis berikut : 
my_dict['pekerjaan'] = 'Engineer'





# Menghapus Pasangan Kunci-Nilai: Untuk Menghapus Pasangan Kunci - Nilai 
# penjelasan : Untuk menghapus pasangan kunci-nilai dalam dictionary, kita dapat menggunakan dara kunci `del` . Contoh : 
del my_dict['kota']



# Menggunakan Metode Dictionary : 
# Dictionary dalam Python juga memiliki metode bawaan yang dapat digunakan untuk berbagai operasi sseperti  mendapatkan daftar semua kunci, mendapatkan daftar semua nilai mendapatkan jumlah pasangan kunci-nilai,  dan lain nya.  Beberapa metode yang umum digunakan adalah `keys()` `values()`, `items()` dan `get()`. 

# itu adalah beberapa dasar-dasar yang perlu diketahui tentang dictionary dalam bahasa  pemograman Python . 




'''
    Pada Lesson ini, kita akan membahas mengenai dictionary, yang merupakan struktur data dalam bahasa Python.  
    Dictionary adalah tipe data yang memiliki data yang memiliki pasangan nilai kunci atau sering disebut key value pair. ini adalah struktur data yang banyak digunakan karena mengacu pada nilai dengan menggunakan kunci. 

    
    Dictionary sangat mirip dengan tipe data list, tetapi karakteristik unik nya adalah memiliki pasangan kunci. 
    Namun, karena dictionary mencari nilai dengan menggunakan kunci, kunci harus unik dan tidak dapat di duplikasi. 

    item dictionary di hubungkan dengan titik dua sebagai [kunci] : [nilai]. Nilai dapat dicari dengan menggunakan [kunci], tetapi [nilai] tidak dapat digunakan untuk mencari [kunci]. 

'''


# Berikut ini adalah sintak yang mendefinisikan dicitionary. pasangan nilai kunci di gabungkan dengan titik dua. dalam contoh ini akan membuat sebuah dictionary yang berisi info nama,numur, dan berat dari seseorang . 
person = {'Name': 'Herdiyan Adam', 'Age': 27, 'Weight' : 82} # Dictionary dengan nama, umur dan berat 

