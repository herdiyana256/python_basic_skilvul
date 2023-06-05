'''
    Set - Definition and Declaration

Tipe data set adalah tipe data dasar yang disediakan oleh Python tetapi tidak disediakan sebagai tipe dasar dalam bahasa pemrograman lain seperti C atau Java. Ada beberapa poin penting dalam tipe data set :

Dalam set, tidak diperbolehkan ada data yang sama atau duplikat sehingga data di dalam set sifatnya adalah unik.
Tipe data set adalah unordered sehingga item dapat muncul dalam urutan yang berbeda setiap kali kita menggunakannya dan kita tidak bisa mengakses data menggunakan index atau key seperti tipe data list atau dictionary.
Tipe data set juga tidak bisa kita ubah setelah kita membuatnya




Set Declaration
Ada beberapa cara untuk membuat tipe data set, berikut adalah beberapa contohnya:

Making empty               -     set0 = set()
Making basic set           -       set1 = {1,2,3,4}
Making set from tuple      -  n_tuple = (1,2,3,4)
                                    set2 = set(n_tuple)

Making set from list        -   n_list = [1,2,3,4]
                                set3 = set(n_list)
'''



#Berikut contoh penerapannya dalam kode untuk membuat set dari list serta membuat set dari tuple :

days_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat' , 'Sun' ] # list
days_set = set(days_list) # membuat set dari list
print(days_set)

#output
{'Sun', 'Sat', 'Wed', 'Fri', 'Thu', 'Mon', 'Tue'}
fruits_tuple = ('apple','orange','water melon')
fruits_set = set(fruits_tuple) # membuat set dari tuple
print(fruits_set)

#output
{'water melon', 'apple', 'orange'}
