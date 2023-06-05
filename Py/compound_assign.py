"""
    COMPOUND ASSIGNMENT OPERATOR ADALAH OPERATOR YANG DIGUNAKAN UNTUK MEMODIFIKASI NILAI DARI SEBUAH VARIABEL DENGAN NILAI LAIN SECARA SINGKAT DAN MUDAH. 
    COMPOUND ASSIGNMENT OPERATORS DIGUNAKAN UNTUK MEMPERSINGKAT PENULISAN OPERASI MATEMATIKA SEPERTI PENJUMLAHAN, PENGURANAGAN, PERKALIAN, PEMBAGIAN, DAN MODULUS PADA SEBUAH VARIABEL . 




    CONTOH PENGGUNAAN COMPUND ASSIGNMENT OPERATORS :  

"""
 x = 10
x += 5 



# Berikut adalah daftar Compund Assignment Operators yang tersedia di Python 

'''
+= (Penambahan)
-= (Pengurangan)
*= (Perkalian)
/= (Pembagian)
//= (Pembagian bulat)
%= (Modulus)
**= (Perpangkatan)


'''




'''
    COMPOUND ASSIGNMENT OPERATORS : 

    
    - Compound assignment operators terdiri dari binary operator dan simple assignmen operator. 
    - Compound assignment operatos melakukan operasi binary pada kedua operan dan menyimpan hasil operasi tersebut di operan kiri . 
    - ada berbagai compund assignment operators di Python. Bahkan jika kamu tidak terbiasa dengan compound assignment operators, kita masih dapat menggunakan operator artimatika dan operator assignment untuk membuat kode tanpa masalah . 
    

    Contoh - contoh dari Compound Assignment Operators: 

OPERATOR                DESCRIPTION                          EXAMPLE
+=                      KOMBINASI DARI ADDITION OPERATOR     i+=10
                        DAN SIMPLE ASSIGNMENT OPERATOR
-=                      KOMBINASI DARI SUBTRACTION OPERATOR  i-=10        
                        SIMPLE ASSIGNMENET OPERATOR 

*=                      KOMBINASI DARI MULTIPLICATION OPERATOR     i*= 10
                        DAN SIMPLE ASSIGNMENT OPERATOR                      


/=                     KOMBINASI DARI DIVISION OPERATOR DAN         i / =10
                        SIMPLE ASSIGNMENT OPERATOR                                            


^=                     KOMBINASI DARI BITWISE XOR(^) OPERATOR DAN SIMPLE     i^=10
                        ASSIGNMENT OPERATOR 

%=                     KOMBINASI DARI MODULO OPERATOR DAN SIMPLE        i %=10
                        ASSIGNMENT OPERATOR                                  

                        
CONTOH DARI COMPOUND ASSIGNMENT OPERATORS : 
'''

num = 200 
num   +=  100 
print(num)

num -= 100 
print(num)


num *= 20 
print(num)



num /= 2 
print(num)


'''
   300
200
4000
2000.0 

'''




# Example other : 
a = 10
a += 200
a -= 100
a = a * 2

print(a)

'''
    Output dari kode di atas adalah 220.

Pada baris pertama, variabel a diberi nilai awal 10.

Pada baris kedua, a ditambahkan dengan nilai 200 menggunakan operator +=. Sehingga nilai dari a menjadi 210.

Pada baris ketiga, a dikurangi dengan nilai 100 menggunakan operator -=. Sehingga nilai dari a menjadi 110.

Pada baris keempat, nilai a dikalikan dengan 2. Sehingga nilai dari a menjadi 220.

Setelah operasi di atas dilakukan, nilai akhir dari a adalah 220. Kemudian nilai variabel a dicetak menggunakan fungsi print().


'''