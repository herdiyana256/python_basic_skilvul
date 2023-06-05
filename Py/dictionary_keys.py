'''
  Dictionary - Items, Keys, Values
Kita dapat menampilkan seluruh key yang ada di dalam sebuah dictionary dengan fungsi keys() seperti contoh berikut ini:  


'''
dic = {'a': 10,'b': 20,'c': 30, 'd': 40}
print(dic.keys()) # mengakses seluruh key yang ada dalam dictionary

#output
dict_keys(['a','b','c','d'])


#selain itu kita juga dapat menampilkan seluruh value yang ada di dalam sebuah dictionary dengan fungsi values() sesuai contoh berikut:

dic = {'a': 10,'b': 20,'c': 30, 'd': 40}
print(dic.values()) # mengakses seluruh values yang ada dalam dictionary

#output
dict_values([10,20,30,40])




#Kita juga dapat mengakses seluruh item dalam sebuah dictionary dengan fungsi items(). Jika fungsi items() digunakan menggunakan for loop maka akan mengembalikan sebuah tipe data tuple yang berisi (key,value) dan bisa kita manfaatkan seperti kode di bawah ini:

dic = {'a': 10,'b': 20,'c': 30, 'd': 40}
print(dic.items()) # mengakses seluruh items yang ada dalam dictionary

#output
dict_items([('a', 10), ('b', 20), ('c', 30), ('d', 40)])

# kita juga bisa menggunakan *for loop* untuk mengakses seluruh *item* satu per satu

for str1,num, in dic.items():
    print(str1,':',num)

#output
a : 10
b : 20
c : 30
d : 40
