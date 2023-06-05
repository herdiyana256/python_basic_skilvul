
'''
    OPERATOR LOGIKA PADA PYTHON ADALAH OPERATO YANG DIGUNAKAN UNTUK MENGKOMBINASIKAN KONDISI-KONDISI LOGIKA. 
    TERDAPAT TIGA JENIS OPERATOR LOGIKA PADA PYTHON YAITU : AND,OR, DAN NOT 

    1. OPERATOR AND : 
    OPERATOR INI AKAN MENGHASILKAN NILAI TRUE JIKA KEDUA KONDISI YANG DIBANDINGKAN BERNILAI TRUE. 
    JIKA SALH SATU ATAU KEDUA KONDISI BERNILAI FALSE, MAKA HASILNYA AKAN FALSE. AND OPERATOR DI LAMBANGKAN DENGAN "and" : 

    
    2. OR OPERATOR : OPERATOR INI AKAN MENGHASILKAN NILAI TRUE JIKA SALAH SATU ATAU KEDUA KONDISI YANG DI BANDINGKAN BERNILAI TRUE, 
    JIKA KEDUA KONDISI BERNILAI FALSE, MAKA HASILNYA AKAN FALSE. OR OPERATOR DILAMBANGKAN DENGAN "OR". 

    3. NOT OPERATOR : 
    OPERATOR INI AKAN MENGHASILKAN NILAI TRUE JIKA KONDISI YANG DIBANDINGKAN BERNILAI FALSE DAN SEBALIKNYA. NOT OPERATOR DILAMBANGKAN DENGAN "NOT".
    


'''


# CONTOH OPERATOR AND 
x = 10
y = 20 
z = 30 

# jika x lebih kecil dari y DAN y lebih kecul dari Z 
if x < y and y < z:
        print("Kondisi terpenuhi")
else:
        print("Kondisi tidak terpenuhi")





#CONTOH OPERATOR OR
x= 10 
y = 20
z = 30 

# Jika x lebih besar dari y ATAU y lebih kecil dari z
if x > y or y < z:
        print("Kondisi terpenuhi")
else: 
        print("Kondisi tidak terpenuhi")





# Contoh penggunaan operator NOT : 
x = 10 
y = 20 

# jika x bukan 20 
if not x == 20: 
        print("Kondisi terpenuhi")
else:
        print("Kondisi tidak terpenuhi")



'''
    SUMMARY : 


    logical operators menentukan ekpresi logika dan mengembalikan True atau False sebagai hasilnya 


    x and y
x    y     x and y 
false false   false 
false  true   false 
true    false   false 
true    true    true


x or y 
x   y     x   or y 
false false    false 
false   true   true 
true    false   true
true    true    true 

not x 
x     not x 
false    true 
true     false 



OPERATOR                            DESCRIPTION 
x and y                     Jika salah satu dari x atau y Salah, itu benar hanya jika semua nya benar . 
x or y                       Jika salah satu dari x atau y benar, itu salah hanya jika semuanya salah 
not x                        Jika x benar salah. Jika x salah, maka benar 



Terdapat 3 logical operator yang sering digunakan pada python  yaitu and, or, dan not. Contoh : 
penggunaan logical operator dalam kode : 
'''
x = True 
y = False 
print(x and y)
print(x or y) 
print (not x)
print (not y)

'''
    Output : 
False
True
False
True



Operator and mengharuskan semua operan bernilai True agar bisa mengembalikan nilai true dan selain dari kondisi tersebut, operator and akan mengembalikan nilai false .

- Berbeda dengan operator or, jika salah satu operan setidaknya bernilai True maka operator or akan mengembalikan nilai true sementara jika semua operan bernilai false maka operator or akan mengembalikan nilai false. 

- Operator not akan menghasilkan negasi dari nilai operan, jika operan bernilai true maka jika menggunakan operator not, nilai nya akan berubah menjadi false. 


'''

