'''

    MUTABLE vs IMMUTABLE DATA TYPES 
    dalam bahasa pemograman Python, terdapat perbedaan mendesar terhadap tipe-tipe data yang terdapat dalam python . 
    Perbedaan tersebut terletak di apakah value dari objek tersebut bisa di ubah atau tidak.

    Jika setelah data di buat, value tidak dapat diubah, maka tipe data tersebut termasuk dalam immutable data types.

    Sebaliknya jika setelah objek tersebut di buat dan data masih bisa diubah , maka tipe data tersebut ytermasuk dalam mutable data types.



    
        Immutable dan Mutable mengacu pada sifat-sifat objek. 
        objek yang tidak dapat diubah disebut "immutable", yang berarti setelah dibuat, nilai mereka tidak dapat di ubah. 
        sedangkan objek yang dapat di ubah disebut "mutable", yang berarti bahwa nilai mereka dapat diubah setelah dibuat.


        Contoh objek yang immutable di Python meliputi angka,string,dan tuple. 
        Ketika anda membuat objek ini, anda tidak dapat mengubah nilai nya . sebagai contoh, ketika anda membuat sebuah string, Anda tidak dapat mengubah karakter didalam nya tanpa membuat string baru. 
        Contoh kode python berikut ini menunjukan contoh sifat immutable dari objek string : 



'''
my_string = "Hello, World!"
my_String[0] = "h" #TypeError : 'str' object does not support item assignment  
'''
    Disisi lain, contoh objek yang mutable di Python meliputi daftar (list), set, dan dictionary . 
    Setelah Anda membuat objek ini, Anda dapat mengubah nilai-nilai nya. Sebagai contoh , ketika anda membuat sebuah daftar, Anda dapat menambah atau menghapus item didalamnya . 
    Contoh kode Python berikut ini menunjukkan contoh sifat mutable dari object daftar : 

'''
my_list = [1,2,3]
my_list[0] = 4 # nilai didalam daftar dapat diubah.
my_list.append(4) # item baru dapat ditambahkan ke daftar




'''
    Dalam Kasus Objek yang mutable, perubahan yang di lakukan pada objek akan berdampak  pada semua variabel yang merujuk pada objek tersebut. 
    sebagai contoh, jika anda mengubah nilai di dalam daftar, perubahan tersebut akan berdampak pada semua variabel yang merujuk pada daftar tersebut. 
    Contoh kode Python  berikut ini menunjukan contoh ini : 


'''

list1 = [1,2,3]
list2 = list1
list2[0] = 4 
print(list1) # Output : [4,2,3]
print(list2) # Output : [4,2,3]

# Dalam contoh di atas, perubahan yang dilakukan pada list2 juga mempengaruhi nilai list1, karena keduanya merujuk pada objek yang sama.




''' SUMMARY

    mutable vs immutable data types 

    Dalam bahasa Pemograman Python, terdapat perbedaan mendasar terhadap tipe-tipe data yang terdapat dalam Python . 
    Perbedaan tersebut terletak di apakah value dari objek tersebut bisa di ubah atau tidak . 

    - Jika setelah data di buat, value tidak dapat  di ubah, maka tipe data tersebut termasuk dalam immutable data types . 
    - Sebaliknya jika setelah objek tersebut di buat dan data masih bisa di ubah , maka tipe data tersebut termasuk dalam mutable data types.


                       Python data types

    Immutable                             Mutable

    int, float   str tuple               list set dict



Mutable 
list merupakan tipe data mutable sehingga kita dapat merubah variable yang merupakan sebuah list, hal ini dapat dilakukan salah satunya menggunakan fungsi append(): 
contoh :
'''

a = ['apple', 'banana', 'orange']
print(id(a))

a.append('grapes')
print(id(a))
    print(a)


'''
output:
140372445629448
140372445629448
['apple','banana','orange','grapes']

 dari kode diatas, variable a merupakan sebuah list yang kemudian kita tambahkan data baru berupa string grapes. ke dalam list tersebut.  
id dari variabel tersebut tidak berubah yang menandakan ini masih sebuah objek yang sama




Immutable 
string merupakan tipe data immutable dan value tipe data string tidak dapat kita ubah selain dengan membuat objek baru.

berikut contoh pertama dari tipe data string yang bersifat immutable :
'''


message = "Welcome to Skilvul"
message[0]  = 'p'print(message)


'''
    message[0]  = 'p'
    TypeError: 'str' object does not support item assignment

    
Pada  contoh pertamakita melikhat data pada variabel message tidak dapat diubah. 
Perhatikan kembali contoh kedua berikut ini : 
'''
# string
e = 'Halo, semua !'
print (id(e))
    e = 'Halo, Apa Kabar?'
    print(id(e))
    print(e)


'''
    [Out:]
140595675113648
140595675113776
'Halo, Apa kabar?'
'''


