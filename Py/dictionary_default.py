
'''
    Dictionary - Default Dict
Fungsi defaultdict() berguna untuk memberikan initial value apabila sebuah key tidak ada didalam sebuah dictionary . 
Mari kita lihat contoh error di bawah ini : 


Terjadi kesalahan saat anda mencoba mengakses key yang tidak ada didalam dictionary(dic)
'''

x = {'a': 0, 'b': 0, 'c':0, 'd': 0}
x['z']

'''
Dari contoh di atas kita bisa melihat bahwa jika kita mencoba mengakses key z dari sebuah dictionary x yang tidak memiliki key tersebut, maka akan muncul KeyError.

Sehingga untuk mencegah hal ini terjadi kita butuh fungsi defaultdict(). Fungsi defaultdict() ini akan membantu kita agar mencegah KeyError dan akan mengembalikan default value. defaultdict() merupakan bagian dari collections module sehingga kita harus melakukan import dengan menggunakan:from collections import defaultdict
'''

#Untuk menggunakan defaultdict() mari kita perhatikan contoh di bawah ini:
from collections import defaultdict # import default dict method dari collections module

keys = ('a','b','c','d')
y = dict.fromkeys(keys,100)
y = defaultdict(int) # set default value sebagai integer

print(y['z']) # mengakses key z dari dictionary y

#output : 0 


#Pada contoh di atas kita mencoba mengakses key z yang tidak ada di dalam dictionary y, namun karena kita sudah memanggil fungsi defaultdict() dan kita sudah set default value sebagi int dan default value dari int adalah 0, maka program akan mengembalikan nilai 0 dan KeyError tidak terjadi.

