'''

List - Declaration 
Apa itu tipe data list ?

List digunakan untuk menyimpan data dari tipe data yang berbeda secara berurutan .
Setiap element memiliki address mereka masing-masing, yang disebut sebagai indeks.
Nilai indeks dimulai dari 0 dan berlanjut hingga element terakhir yang disebut positive index. 
Ada juga negative indexing yang dimulai dari -1 dan memungkinkan anda mengakses element dari yang terakhir hingga yang pertama . 



'''
score list =  [87,84,95,67,88,94,63]
score_list 

'''
    [87,84,67,88,94, 63]
'''


score_list = [87,84,95,67,88,94,63]
print(score_list[0], score_list[3])
# 87 67 


'''
    score_list 0 1 2 3 4 5 6 -> Indeks untuk merujuk pada nilai item 
    item atau element           87 84 95 67 88 94 63
                Merujuk ke item pertama sebagai score_list[0]

            

List Declaration 
Dalam Mendeklarasikan list, kita hanya perlu menggunakan keyword list atau menggunakan []. 
List tidak membatasi tipe data yang bisa terkandung dialam list, sehingga kita bisa memasukan data integer, string dan lain lain ke dalam sebuah list. 
Untuk memisahkan antara element dengan element lain nya kita dapat menggunakan, berikut contoh deklarasi sebuah list: 

'''
fruit = ['banana', 'apple', 'orange', 'kiwi'] # List with string 
print(fruits)
mixed_list = [100,200, 'apple', 400]
print(mixed_list)

'''
    ['banana', 'apple', 'orange', 'kiwi'] 
    [100,200, 'apple', 400]

List dalam python dapat memiliki tipe data yang berbeda termasuk bilangan bulat, bilangan real, string dll.

'''




'''
    Selain memasukan data secara manual, kita juga bisa membuat sebuah list dengan bantuan function, contoh nya adalah function range()

'''
list4 = list(range(1.10))
list4
# [1,2,3,4,5,6,7,8,9]

# gunakan fungsi range untuk membuat urutan angka 
