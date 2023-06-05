''''
    INPUT FUNCTION 
    Input function input () merupakan sebuah fungsi bawaan dari python untuk mendapatkan input data dari user. 
    Contoh penerapan input () yang digabungkan dengan konsep variabel : 

'''

name = input("Enter Name: ")
print("Hello", name.)
print("Welcome to the World of Python Programming!")

'''
    Enter Name : Adam 
Hello, Adam 
Welcome to the Wolrd of Python Programming. 

dari fungsi tersebut user dapat memasukan nama 'Adam' dan input tersebut dapat di olah menjadi sebuah kalimat 'Hello, Adam'



'''



# INPUT TO INTEGERS 
x = int(input("Masukkan integer pertama:" ))
y = int(input("Masukkan integer kedua:" ))
s = x + y
print("Total dari",x,"dan",y,"adalah",s)

#output
Masukkan integer pertama:1
Masukkan integer kedua:2
Total dari 1 dan 2 adalah 3x = int(input("Masukkan integer Pertama: "))
y = int(input("Masykkan integer kedua: "))

s = x + y 
print("Total dari ",x" dan
      )

'''
Fungsi input() dapat digunakan untuk memasukkan bilangan bulat. Namun, fungsi input() selalu mengembalikan input dalam bentuk string. Contoh output yang dihasilkan adalah string "300".
Untuk mengubah string "300" menjadi bilangan bulat 300, nilai kembalian dari fungsi input() harus dikonversikan menggunakan fungsi bawaan Python lainnya yaitu int(). Fungsi int() bertujuan untuk mengubah string menjadi integer

'''




'''
    INPUT ERROR : 
    !!! JIKA ANDA MEMASUKKAN KARAKTER ATAU STRING SEPERTI "hundred" ALIH-ALIH STRING "300" SEBAGAI BERIKUT, FUNGSI 
    INT() TIDAK DAPAT MENGUBAH  "hundred" MENJADI BILANGAN BULAT DAN AKAN MENGASIL KAN VALUE ERROR.


'''