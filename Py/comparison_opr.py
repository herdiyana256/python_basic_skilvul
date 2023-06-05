# COMPARISON OPERATORS -> MENGAMBIL HASIL OPERASI PERBANDINGAN DATA NUMERIK, SEPERTI "LEBIH BESAR DARI" ATAU "KURANG DARI", DAN MENGEMBALIKAN SEBAGAI TRUE ATAU FALSE (BOOLEAN)



# COMPARISON OPERATORS MEMERIKSA HUBUNGAN UKURAN DUA OPERAN YANG SEBANDIN, SEPERTI ANGKA DAN STRING, DALAM ISTILAH SEPERTI LEBIH BESAR DARI ATAU KURANG DARI . 

# HASIL DARI OPERASI INI DIKEMBALIKAN SEBAGAI BENAR ATAU SALAH . TIPE DATA YANG MEMILIKI NULAI TRUE ATAU FALSE DISEBUT BOOLEAN . 

# contoh : 


print('Result of 10 > 50: ', 10 > 5)
print('Result of 5 < 1: ', 5 < 1)
print('Result of 5 == 5', 5 == 5)
print('Result of 5 != 5', 5 != 5)
print('Result of 'a' > 'b:'')print("Result of 'a' > 'b': ", 'a' > 'b')


'''
Result of 10 > 5: True
Result of 5 < 1: False
Result of 5 == 5: True
Result of 5 != 5: False
Result of 'a' > 'b': False
'''



'''
    Contoh-contoh dari comparison operator:

    OPERATOR               DESCRIPTION              A = 100 B = 200

    ==                    Jika dua operand memiliki nilai yang sama, return True                 a == b is False
    !=                    Jika dua operand memiliki nilai yang berbeda, return True              a!=b is True 
    >                     Jika operand kiri lebih besar dari operand kanan, return True          a > b is False
    <                     Jika operand kiri  kurang dari operand kanan, return  True             a < b is True 
    >=                    Jika operand kiri lebih besar dari atau sama dengan operand kanan, return True              a >= b is False 
    <=                    Jika operand kiri kurang dari atau sama dengan operand kanan, return True                 a <= b  is True 


'''



# Penerapan comparison operators 
# diganungkan dengan arithmetic operation 
n = int(input('Masukan sebuah integer: '))
print ('Apakah integer tersebut genap ?', n % 2 == 0)



# output :  Masukan sebuah integer : 60  || Apakah Integer tersebut genap ? True 


'''
    DALAM PROGRAM INI USER DAPAT MEMASUKAN SEBUAH INTEGER DAN DENGAN COMPARISON OPERATOR DAN ARTIHMETIC OPERATION KITA DAPAT MENENTUKAN APAKAH INPUT INTEGER YANG DI MASUKAN ADALAH ANGKA GENAP DENGAN EKPRESI n % 2  == 0 . JIKA GENAP AKAN MENGEMBALIKAN NILAI True DAN JIKA GANJIL AKAN MENGEMBALIKAN NILAI FALSE . 


'''



# STRING COMPARISON 
print ('aaa' == 'aaa')
print('aaa' == 'bbb')
print('aaa' != 'aaa')
print('aaa' != 'bbb')


# outpu : 
'''
    True 
    False 
    False 
    True


'''