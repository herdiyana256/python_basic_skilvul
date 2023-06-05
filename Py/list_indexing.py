 '''
 
    List - Indexing 
    List Imdexing dan Menghitung Panjang Sebuah List 

    - Dalam sebuah list, dari item pertama adalah 0, dan item terakhir adalah -1 . 
    -  Gunakan fungsi len() untuk menghitung jumlah item dalam list, yang dengan kata lain panjang dari sebuah list 
 
 
 '''


 # example :
 n_list = [11,22,33,44,55,66] 
print(n_list)
print(len(n_list))



# output :
# [11,22,33,44,55,66] 
# 6


# Contoh kode untuk mengakses sebuah list : 
n_list = [11,22,33,44,55,66]
print(n_list[0])  # indeks item pertama dari list adalah 0 
print(n__list[1]) # index item kedua dari list adalah 1 


# output :  11 22



'''
    Berikut rangkuman lengkapnya untuk indeks masing-masing elemen dalam list:


    index : [0] [1] [2] [3] [4] [5]
    n_list : 11 22 33 44 55 66 


    n_list[0] = 11
    n_list[1] = 22 
    n_list[2] = 33
    n_list[3] = 44
    n_list[4] = 55
    n_list[5] = 66 

    
    Dalam melakukan indexing juga kita harus berhati-hati agar tidak melebihi dari maksimum indeks dari suatu list:
'''
n_list = [11,22,33,44,55,66] # Indeks dengan 6 element
n_list[5]   # Nilai element terakhir dari daftar


n_list[6] # Nilai element ke-7 dari indeks tidak ada 

'''
-Jangan masukkan nilai indeks yang lebih besar dari nilai maksimum nilai indeks.
-Maksimum indeks adalah len(n_list)-1.
-Saat menyimpang dari rentang indeks yang dapat diakses, kesalahan berikut terjadi: IndexError: list index out of range.

'''


'''
        Negative Indexing 
        Selain melakukan positive indexing seperti yang sudah kita bahas sebelum nya, kita juga bisa melakukan negative indexing yang  berorientasi dari element terakhir dalam list . 
        
        Referensi element dimungkinkan dengan menggunakan indeks negative  dalam daftar Python. 
        untuk indeks negative, proses pengindeksan dengan mengurangi -1 dari element terakhir sehingga menjadi -1,-2, -3 

        
    n_list[-2] = 55            n_list  = 11 22 33  44  55  66
    n_list[-3] = 44            Negative index           [-6]   [-5]  [-4] [-3] [-2] [-1]
    n_list[-4] = 33
    n_list[-5] = 23
    n_list[-6] = 11 


'''