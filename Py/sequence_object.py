# SEQUENCE OBJECT ITERATION 

'''
    SEQUENCE OBJECT ITERATION
    ADALAH TEKNIK PENGLANGAN(LOOPING) PADA SEBUAH SEQUENCE OBJECT, SEPERTI STRING, LIST, TUPLE ATAU RANGE, DIMANA SETIAP ELEMENT DIDALAM SEQUENCE OBJECT TERSEBUT DIAKSES SECARA BERURUTAN.
    DALAM PYTHON, TEKNIK PENGULANGAN INI DAPAT DILAKUKAN MENGGUNAKAN FOR LOOP. PADA SETIAP ITERATION PERULANGAN, VARIABLE ITERASI AKAN DIISI DENGAN NILAI SETIAP ELEMENT DALAM SEQUENCE OBJECT SECARA BERURUTAN .


    CONTOH PENGGUNAAN SEQUENCE OBJECT ITERATION PADA SEBUAH STRING : 
'''
s = "hello"
    for c in s:
        print(c)



'''
h 
e
l
l
o



Pada contoh di atas, setiap karakter dari string "hello" diakses secara berurutan dalam setiap iterasi perulangan. Variabel c akan berisi nilai karakter pada setiap iterasi.


Contoh penggunaan sequence object iteration pada sebuah list:
'''
my_list = ["apple", "banana", "cherry"]
    for item in my_list:
        print(item)


'''
apple
banana
cherry


Pada contoh di atas, setiap elemen dari list ["apple", "banana", "cherry"] diakses secara berurutan dalam setiap iterasi perulangan. Variabel item akan berisi nilai elemen pada setiap iterasi.



Contoh penggunaan sequence object iteration pada sebuah range:
'''
for i in range(1,5):
        print(i)



# output :
'''
    1
    2
    3
    4

    Pada contoh di atas, setiap angka dalam urutan bilangan bulat dari 1 hingga 4 diakses secara berurutan dalam setiap iterasi perulangan. Variabel i akan berisi nilai angka pada setiap iterasi.

'''



'''
    SEQUENCE OBJECT ITERATION
    SEBELUM NYA KITA SUDAH MELAKUKAN LOOPING DENGAN FUNGSI range() DIMANA KITA MENGHASILKAN ANGKA SESUAI DENGAN RANGE YANG KITA BERIKAN DAN MELAKUKAN ITERASI SESUAI RANGE TERSEBUT. 
    NAMUN APABILA SEBUAH DATA SUDAH DISEDIAKAN, SEBAGAI CONTOH SEBUAH LIST DENGAN ELEMENT TERTENTU, KITA PERLU SEBUAH CARA UNTUK SECARA BERURUTAN MENGUNJUNGI NILAI-NILAI DIDALAM LIST TERSEBUT.


    KODE DIBAWAH INI MELAKUKAN EKSEKUSI YANG SECARA BERURUTAN MENGUNJUNGI NILAI-NILAI DIDALAM LIST [11,22,33,44,55,66] . VARIABLE n SECARA BERURUTAN DITETAPKAN KEPADA 11,22,33,44,55 DAN 66


    Dengan menggunakan sequence object iteration kita dapat mengunjungi dan memproses data secara individual, masing-masing elemen dalam sebuah list
'''
number = [11,22,33,44,55,66]
    for n in numbers:
        print('n = ', n)

'''
n = 11
n = 22
n = 33
n = 44
n = 55
n = 66
'''    



