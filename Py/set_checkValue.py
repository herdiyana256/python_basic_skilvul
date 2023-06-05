'''
    Set - Check Value in Sets
    Untuk Mengakses Value yang ada didalam set, kita bisa menggunakan for loop untuk melakukan * iterasi 
    * untuk mendapatkan item yang ada didalam set 

'''
numbers = {2,1,3}
for x in numbers:
  print(x)

#output
2
1
3

#kita juga bisa melakukan validasi untuk mengecek apakah sebuah item ada di dalam sebuah set dengan menggunakan operator in yang kita juga bisa pakai dalam tipe data list.


numbers = {2,1,3}
if 1 in numbers:
  print("1 terdapat dalam set")

#output
1 terdapat dalam set

#Selain itu kita juga bisa menambahkan serta menghapus value yang ada di dalam set menggunakan fungsi add() serta remove(): Kita bisa menambahkan item baru menggunakan fungsi add():

numbers = {1,2,3}
numbers.add(4)
print(numbers)

#output
{1, 2, 3, 4}



#Dan kita bisa menghapus item dalam set menggunakan fungsi remove():

numbers = {1,2,3,4}
numbers.remove(4)
print(numbers)

#output
{1, 2, 3}