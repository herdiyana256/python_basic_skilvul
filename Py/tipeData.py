# TIPE DATA BASIC



"""     
    KLASIFIKASI TIPE DATA : 
- DALAM PYTHON , OPERATOR BERLAKU BERBEDA TERGANTUNG PADA TIPE DATA 
- HASIL OPERASI PERKALIAN * BILANGAN 100 DAN 2 ADALAH 200 . 
- NAMUN, HASIL OPERASI PERKALIAN STRING '100' DAN '2' ADALAH '100100'. DENGAN KATA LAIN, HASIL OPERASI PERKALIAN DARI STRING 'Halo' DAN NUMERIK 2 ADALAH 'HALOHALO', TETAPI OPERASI PERKALIAN PADA HURUF TERSEBUT BERBEDA DENGAN OPERASI PERKALIAN PADA NILAI NUMERIK. 
"""
100 * 2 # Temukan perkalian nilai numerik 100 dan 2 
'Hello' * 2 # Temukan perkalian string 'Halo' dan 2 
# HelloHello 


'100' * 2 # Temukan Perkalian string '100' dan 2 






"""
    BASIC DATA TYPES : 
BERIKUT RANGKUMAN STRUKTUR DATA DALAM BAHASA PYTHON YANG PENTING DAN AKAN TERUS DIPAKAI SELAMA KELAS INI . 
STRUKTUR DATA YANG AKAN DIGUNAKAN ADALAH : 
1. NUMBER 
2. BOOLEAN 
3. STRING 
4. LIST 
5. TUPLE
6. DICTIONARY 




A. NUMBER 
int 
ex :10,200 

B. BOOLEAN 
ex: 
True, False 

C. STRING 
ex : 'hello'
'100'


D. LIST 
ex : 
[10,20,30]


E. TUPLE 
ex : (10,20,30)

F. DICTIONARY 
ex : {'name' : 'Adam',
    'age' : 26,
    'height' : 56.5
}


G. FLOAT 
ex ": 3.14 


H. COMPLEX 
ex: 4 + 3j 



CARA MEMBEDAKAN DAN MENGETAHUI TIPE DATA : 

1. ISTILAH YANG MENGACU PADA NILAI NUMERIK, FUNGSI DAN KELAS YANG MERUPAKAN DARI PROGRAM PYTHON ADALAH OBJEK . 
2. PERAN OPERATOE BERBEDA TERGANTUNG PADA APAKAH TIPE DATA OBJEK ADALAH INTEGER ATAU STRING 
3. FUNGSI TYPE() MENGEMBALIKAN TIPE OBJEK, MARI KITA PERIKSA TIPE DATA MENGGUNAKAN KODE DI BAWAH INI : 

"""

type(100) # Mmeberi thau tipe data dari 100  -> int 

type(100.0) # float 

type (10 + 3j) # type data bilangan kompleks berupa bilangan real + imajiner seperti  10 + 3j 

# complex 





# CARA MENGUBAH TIPE DATA 
# STRING '10' DAPAT DIUBAH MENJADI TIPE DATA INTEGER MENGGUNAKAN FUNGSI INT ('10'). OLEH KARENA ITU , int ('10') / 2 DIJALANKAN TANPA ERROR 
# UNTUK MENGUBAH NILAI NUMERIK 1O PADA PYTHON KE STRING '10', GUNAKAN FUNGSI str(10).
int ('10') / 2 # Ubah String '10' MENJADI BILANGAN BULAT DAN BAGI DENGAN 2 
# 5.0 

'I Like number' + str(10) # ubah angka 10 menjadi string dan gunakan + operator 
# 'I Like number 10'


a = None 
type(a)

# NoneType 






# TIPE DATA STRING 
# String characteristics 

"""
    Dalam Python, string sangat cocok untuk menampilkan informasi dalam perangkat lunak . 
    contoh : 
    Nama pengguna ID , dan kata sandi dapat di nyatakan sebagai string.


    - String dalam Python adalah bentuk di manasetiap huruf terhubung . 
    - Operasi penjumlahan dan perkalian di mungkinkan untuk string dalama Python 
    - Huruf dan spasi dalam sebuah string juga disebut dengan character 

    
    String Operator 
    Mari kita lihat operasi + dan * yang di perbolehkan dalam string . 
    Operasi + dari string menghubungkan dua string menjadi satu string . Operasi*  dari string harus berupa bilangan bulat . 
    Artinya, akan menduplikasi string tersebut atau berulang sejumlah bilangan bulat n . 



"""
'I' + ' Love' + ' Python!' # String dapat ditambahkan ke string . 
'Python ' * 10 # Menghasilkan string 'Python' diulang sebanyak 10 kali 
'*' * 50  # Menghasilkan string '*' diulang sebanyak 50 kali 
str(100) * 10 # String '100' diulang sebanyak 10 kali . 




# STRING INDEXING
# Positive index 
"hello"[0]  # 'h'

"hello"[2] # 'l'

# Pengindeksan string : Pengindeksan string dapat digunakan untuk mendapatkan hanya beberapa character dari string yang panjang. Gunakan tanda kurung besar [] dan nomor / urutan index. 

# Contoh diatas jika kita ingin mendapatkan character pertama dalam string tersebut, tidak menggunakan angka indeks 1 melainkan dimulai dari angka indeks 0 . 





# NEGATIVE INDEX 
#  JIKA INGIN MENDAPATKAN CHARACTER DIHITUNG DARI AKHIR DARI SEBUAH STRING, MAKA KITA DAPAT MENGGUNAKAN TANDA - DAN DI MULAI DARI INDEKS 1 UNTUK MENDAPATKAN CHARACTER TERAKHIR DARI STRING . 

"hello"[-1] # 'o'




# STRING BUILT-IN FUNCTION 
"""
    DALAM TIPE DATA STRING DALAM PYTHON, KITA JUGA DAPAT MENGGUNAKAN BUILT-IN FUNCTION YANG DISEDIAKAN OLEH PYTHON .
    BERIKUT ADALAH CONTOH - CONTOH NYA : 
    
    1. SPLIT () -> Digunakan untuk memisahkan string sesuai dengan separator yang kita inginkan dan mengemebalikan hasil nya sebagai sebuah list. 


"""
teks = "halo, nama saya, Herdiyan"
x = teks.split(", ")
print(x)


# Output : ['hallo', 'nama saya', 'Herdiyan']

#isLower () -> Digunakan untuk mengecek apakah semua element dalam string adalah huruf kecul, akan mengembalikan True jika iya, dan False jika tidak 
a = "HaLo"
b = "hallo"


print(a.islower())
print(b.islower())


# Output  : False & True

# count () -> digunakan untuk menghitung berapa kali sebuah value mucul dalam sebuah string
teks = "Hallo semuanya, disini saya bersama dengan Adam semuanya"
x = teks.count("semuanya")
print(x)


# Output :  2 






# OPERATOR BASIC 

# Dalam Pemograman , operasi menggunakan informasi numerik dam kemudian menggunakan data tersebut seiring terjadi . Misalnya, informasi seperti tinggi dan berat badan seseorang di nyatakan sebagai nilai numerik seperti 177cm dan 58kg. 

# mari kita pelajari istilah untuk operasi artimatika . Nilai data atau variabel yang akan di pakai pada operasi disebut Operand . 
# SUbjek operasi disebut Operator . Ambil contoh operasi 100 + 200 


# 100 + 20 
# operand - operator - operand 




# Beberapa Operator basic yang dapat di pakai dalam bahasa pemograman Python : 

"""
    operator    arti                aksi 
    +           addition           Tambahkan operand kiri dan operand kanan. 
    -           subtraction        Kurangi Operand kanan dari operand kiri 
    *           Multiplication      kalikan operand kanan dari  kiri
    /           Division            Membagi operand kiri ke operand kanan. Pembagian dalam Bahasa Python pada dasarnya mengembalikan nilai bilangan real . 
    //          floor(division(quotient))        Tidak seperti, hasil pembagian digunakan untuk membuang titik desimal atau  kurang dan hanya memperoleh bagian bilangan bulat . 
    %           Remainder                Operator % dibaca sebagai operator modulo dan tidak ada hubungan nya dengan persentase yang berarti rasio. berguna untuk menemukan sisa pembagian . 
    **          Power                  Kalikan operan kiri dengan operan kanan. Dalam kasus **0,5, operasi akar kuadrat dilakukan . 



"""



# Penggunaan Operator 
# Bahasa Pemograman Python bisa digunakan untuk operasi artimatika sederhana seperti penambahan angka, pengurangan, perkalian hingga menemukan sisa bagi dari suatu operasi pembagian. Berikut contoh penggunaan operator sederhana : 
100 + 20 # temukan penambahan nilai numerik 100 dan 20 


100 * 20 # Temukan perkalian nilai numerik 100 dan 20 


100 - 20 # temukan pengurangan nulai numerik 100 dan 20 


100 / 20 # bagi nilai numerik 100 dengan 20 



100 // 20   # Bagilah nilai numerik 100 dengan 20 dan temukan hasil bagi 



100 % 20 # bagilah nilai numerik 100 dengan 20 dan temukan sisa bagi 

"""
Dalam Python, perbedaan tipe data sangat penting. Karakter dan angka memiliki bentuk yang sama, tetapi sifatnya bisa sangat berbeda 

Contoh angka 10 bisa dihitung . Namun, huruf "10"  tidak mungkin bisa dihitung 


Tergantung pada tipe data, operator yang tersedia berbeda. Dalam kasus berikut, kesalahan tata bahasa terjadi karena string "10" dibagi dengan numerik 2 . 

"""
10 / 2  # 5.0 

'10' / 2 # String 10 dibagi dengan angka 2 

























