'''
Dictionary - Get Method

Fungsi get() dapat kita gunakan untuk mendapatkan value dari key yang spesifik

'''

dic = {'a':10,'b':20,'c':30,'d':40}
a = dic.get('a') # fungsi get untuk mendapatkan value dari key a
print(a)

#output : 10

# Kita juga dapat memberikan default value dalam sebuah fungsi get().
#syntax
dic.get(key,default_value)


#Sehingga jika kita menggunakan fungsi get() untuk sebuah key yang tidak ada di dalam sebuah dictionary maka fungsi get() akan mengembalikan default value tersebut.

dic = {'a':10,'b':20,'c':30,'d':40}
b = dic.get('z',0) # tidak terdapat key z dalam dictionary dic sehingga dikembalikan value 0
print(b)

#output
0