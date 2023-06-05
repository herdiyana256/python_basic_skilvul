# 0 Install Python Extension 
# 1 open project 
# 2 Create new project 
# 3  Open Integrated Terminal 
# 4  Running Python Program ( example : python3 hello.py) -> version python lalu masukan nama file yang mau dijalankan kode program nya 


print ("Hello Everyone!") 

print  (1 + 2)





#Python Syntax - Print Function 
#Menampilkan Hasil dalam Program menggunakan Fungsi - print()
#fungsi print() dalam bahasa pemograman Python adalah sebuah command untuk menampilkan hasil didalam ()
#untuk menampilkan sebuah karakter atau kalimat menggunakan fungsi print() maka karakter atau kalimat tersebut harus dilingkupi dengan tanda kutip ("")
 

print("Hello World!")

#output : Hello World



#untuk mencetak nilai numerik, masukkan angka tanpa tanda kutip 
print(26)
print(7.5)

#output : 26 & 7.5



# Anda juga dapat menggabungkan string dan angka dengan operator koma 
print("Hello," 26) 
# output : Hello 26 


# Menggunakan operator * dan + 
print('Hello' * 3) # akan menduplicate string Hello sebanyak 3 kali 
print(10 * 16) # akan menambahkan kedua bilangan tersebut 


print("Hello" + "World") # akan menggabungkan kedua string tersebut 
print (10 + 16) # akan menambahkan kedua bilangan tersebut 

# Output : HelloHelloHello  160  Hello World  26 


# peringatan ! Operator + tidak bisa digunakan untuk 2 tipe data yang digabungkan seperti string dan integer 
print("Hello" + 3) # akan muncul error 




#========================================================================

# PYTHON SYNTAX - COMMENT 
# KOMENTAR DALAM PROGRAM MERUPAKAN BAGIAN YANG CUKUP PENTING UNTUK MEMBERI TAHU MAKSUD DAN TUJUAN DARI PROGRAM TERSEBUT .
# KOMENTAR MERUPAKAN BAGIAN DARI PROGRAM YANG TIDAK AKAN DI EKSEKUSI OLEH SISTEM . DALAM BAHASA PEMOGRAMAN PYTHON, TERDAPAT 2 TIPE KOMENTAR : 
# 1. SINGLE LINE COMMEND DAN 
# 2. MULTIPLE LINE COMMENT 

# UNTUK MEMBERI KOMENTAR KITA MENGGUNAKAN SINTAKS # UNTUK SINGLE-LINE COMMENT ATAU """ UNTUK MULTI LINE COMMENT . 

""" PROGRAM INI BERTUJUAN UNTUK 
MENAMPILKAN ANGKA 5 
DENGAN MENGGUNAKAN FUNGSI PRINT """


print(5) # menampilkan angka 5 




# BAB 2 


# Errors in Python 
# Contoh tipe tipe Error 
# Dalam Pemograman Python terdapat beberapa tipe tipe error yang dapat muncul dalam pembuatan program , contoh nya adalah 
# Syntax Error
# Runtime Error 


"""
    Syntax Error : 
1. Bahasa Pemogram digunakan di bawah aturan dan konvensi yang ketat. 
Menulis kode yang menyimpang dari aturan tata bahasa menghasilkan syntax error.
2.Untuk mencegah kesalahan sintaks atau syntax  error kita harus memplajari dan mempraktikkan tata bahasa dan kode Python sesuai dengan aturan yang di tetapkan . 
3.Untuk mencetak string 'Halo', tanda kutip harus digunakan di kedua sisi string. Namun, pada kode di baah ini terjadi kesalahan sintaks karena string tidak di kutip pada kedua sisi. 
"""
print('Hello) 
      



# Runtime Error 
"""
    1. Berbeda dengan kesalahan sintaks, kode yang benar secara tata bahasa masih dapat menyebabkan kesalahan selama eksekusi. 
    Jenis kesalahan ini disebut kesalahan runtime atau Runtime Error. 
    2. Untuk Mencegah kesalahan Runtime, kamu harus mempertimbangkan kemungkinan penggunaa memasukkan data yang salah . 
 4. Dalam kode di bawah ini, pengguna memasukkan string dua dan bukan bilangan bulat 2 , sehingga kesalahan runtime terjadi.
"""

num = int(input('Input an Integer: '))
# Input an integer : two 

# Value error  <iPython-input-3-2c1961

# Value error Invalid Literal for int() with base 10: 'two'.

