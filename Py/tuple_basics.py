# TUPLE - BASICS
'''
    TUPLE - BASICS
    Tuple adalah sebuah immutable list, dimana setelah dibuat, tuple tidak dapat diubah dengan cara apa pun . 
    Tuple didefinisikan mirip dengan sebuah list, perbedaan adalah list menggunakan tanda kurung siku [] namun tuple menggunakan tanda kurung () . 
    Aturan untuk indeks sama dengan sebuah list.
    Setelah tuple dibuat , Kita tidak dapat menambahkan elemet ke dalam tuple atau menghapus element dari tuple. 

    Namun karena tuple tidak dapat diubah tuple juga memiliki beberapa keunggulan seperti : 

    1. Tuple lebih cepat untuk di proses dibanding dengan list 
    2. Karena data tuple tidak bisa diubah, sehingga melindungi dari perubahan data  yang tidak kita inginkan . 

    Cara mendeklarasikan tuple pun cukup sederhana:

'''
colors = ("red", "green", "blue") # Tuple untuk menyimpan nama 
colors


numbers = (1,2,3,4,5) 
numbers
# (1,2,3,4,5)




# DAN KETIKA KITA MENCOBA UNTUK MENGUBAH SALAH SATU ELEMENT DARI SEBUAH TUPLE, MAKA AKAN MUNCUL ERROR : 
t1 = (1,2,3,4,5)
t[1] = 100 
print(a)

