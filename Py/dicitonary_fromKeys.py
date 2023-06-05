'''
    Dictionary - From Keys Method 
    Ada berbagai cara untuk membuat dictionary dan salah satunya adalah menggunakan **fromkeys()**


'''
#syntax
dict.fromkeys(key_list)

#dimana kita bisa mengkonversikan sebuah list atau tuple menjadi sebuah key list dengan value awal adalah None. Untuk lebih jelasnya mari kita perhatikan kode di bawah ini:

keys = ['a','b','c','d']
x = dict.fromkeys(keys)
print(x)

#output
{'a':None , 'b': None, 'c': None, 'd': None}



'''
    Kode di atas menunjukkan cara membuat sebuah dictionary x dengan key berdasarkan data dari sebuah list keys. Key yang ada di dalam dictionary x berasal dari keys dengan value awal yaitu None.

Selain membuat dictionary dari tipe data list, kita juga dapat membuat dictionary dari tipe data tuple dengan cara dan hasil yang sama seperti kode di bawah ini:

'''
keys = ('a','b','c','d')
x = dict.fromkeys(keys)
print(x)

#output
{'a':None , 'b': None, 'c': None, 'd': None}