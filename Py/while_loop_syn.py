'''
While loop syntax 

condition adalah sebuah ekpresi Boolean yang akan di evaluasi saat looping. 
Jika kondisi benar(True), statement didalam blok kode akan di eksekusi . 
Setelah blok kode selesai di eksekusi, kondisi akan di evaluasi lagi dan jika kondisi nya masih benar, blok kode akan di eksekusi lagi.
Proses ini akan terus berlanjut sampai kondisi menjadi salah (False)


Perlu di perhatikan bahwa jika kondisi awal sudah (False) , maka blok kode pada while loop tidak akan pernah dieksekusi . 




While Loop Syntax
sebelum nya pada contoh di topik pertama lesson ini, kita menampilkan 'Welcome to everyone!!' pada program sebanyak 5 kali menggunakan for loop statement.
Sekarang mari kita cari tahu bagaimana jika menggunakan perulangan while.


while statement    ||        
            is the condition of while statement True?
                   ||
                  True
                  ||
                  execute an command or command block

        Example: 
        i = 0 
        while i < 5:
        print('Welcome')
        i = i + 1

        
Step dalam while loop di atas : 
1. Inisianlisasi i ke 0 . 
2. Pernyataan while mencetak 'Welcome' dan meningkatkan nilai i sebagai 1 jika i < 5 bernilai True.
3.Karena nilai i awal adalah 0, iterasi ini juga akan dilakukan sebanyak lima kali . 

'''
i = 0 # initial value 
while i < 5: # kode didalam block akan di eksekusi selama kondisi True
        print('Welcome to everyone!!')


# Contoh tabel berikut adalah merupakan pseudocode pada kolom sebelah kiri dan menerapkan nya menggunakan sintaks Python while loop pada kolom sebelah kanan :

'''
    Form                        Example 

    set intial value            i = 0  : Set Initial Value
    while conditional stateent:    while i < 5 : conditional expression 
    code block be excuted          print ('Welcome to everyone!!')
                                    i += 1


Kalau dilihat while loop syntax sangat mirip dengan if statement.
Selama conditional expression bernilai benar atau True, while loop akan mengulangi dan mengeksekusi kode.

'''