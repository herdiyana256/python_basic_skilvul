# List - Addition and deletion 
# dalam pemograman sebuah data akan sering kali berubah-ubah bergantung dengan pemrosesan yang dilakukan . 
# Dalam tipe data list pun kita bisa melakukan penambahan, pengurangan dan ekspansi list. 



'''
    Addition

    + Operator 
    - Gunakan operator + untuk menambhkan dua list yang berbeda
    - Dalam kasus berikut, semua item person1 dan person2 akan dimasukkan dalam satu list yaitu person_list
'''
person1 = ['Herdiyan Adam Putra', 20,1,180,0,100.0]
person2 = ['Adam Putra', 25,1,170,0,70.0]

person_list = person1 + person2 
print(person_list)

'''
    ['Herdiyan Adam Putra', 20,1,180,0,100.0, 'Adam Putra', 25,1,170,0,70.0]

    

    append() 
    Selain menggunakan + kita juga bisa menambahkan single item pada list menggunakan fungsi append() dimana fungsi ini adalah metode untuk menambahkan item baru ke akhir sebuah list yang sudah ada. 
    Berikut contoh implementasi fungsi append() pada sebuah list : 
'''

a_list = ['a', 'b', 'c', 'd', 'e'] 
a_list.append('f') # menambahkan karakter f 
print(a_list)

# output :
# ['a','b','c','d','e','f']



'''
        extend()
    - Fungsi extend() untuk menambahkan list atau item dibelakang sebuah list
    - seperti contoh di bawah ini, terdapat list1 dan list2. karena kita mengaplikasikan list1.extend(list2) maka element dari list2 yaitu [1,2,3] akan ditambahkan ke belakang list1 sehinggga element pada list1 akan menjadi pada list1 akan menjadi ['a', 'b', 'c', 1,2,3]
    - Namun kita juga dapat memasukkan element individual seperti d ke dalam list tersebut

'''

list1 = ['a', 'b', 'c']
list2 = [1,2,3]
list1.extend(list2)
print(list1)

list1.extend('d')
print(list1)

#  output : 
'''
    #output
['a','b','c',1,2,3]
['a','b','c',1,2,3,'d']

'''





'''
        DELETION 

del
Dengan menggunakan del statement, kita dapat menghapus item dalam indeks yang di inginkan . 

'''
n_list = [11,22,33,44,55,66]
print(n_list) # print seluruh items


del n_list[3] # delete 44
print(n_list)



# output : 
'''
    [11,22,33,44,55,66]
[11,22,33,55,66]
'''



'''
    pop()
    pop() method berfungsi kurang lebih mirip dengan del namun pop() juga mengembalikan value index yang dihapus. 
    Apabila kita tidak mengisi  index dalam metode pop()  maka element terakhir yang akan di hilangkan dari list .
'''
# Contoh : 
n_list = [10,20,30]
print(n_list) # print seluruh items 


n = n_list.pop()
print('n = ',n)
print('n_list =', n_list)


'''
    [10,20,30]
    n = 30 
    n_list = [10,20]
'''




'''
    remove() 
    remove() memungkinkan kita untuk menghapus nilai tertentu dari list  berdasarkan nilai itu sendiri. 
    Contoh nya kita dapat menghapus 44 dari dari sebuah list [11,22,33,44,55,66] tanpa mengetahui indeksnya . 

example : 
'''

# output : 
'''
    [11,22,33,44,55,66] 
    [11,22,33,55,66]
    

'''






