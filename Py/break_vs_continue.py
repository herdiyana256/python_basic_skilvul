# BREAK VS  CONTINUE KEYWORDS
'''

break dan continue adalah contoh dari Loops and control statements, kedua keyword ini dapat mengontrol dan menentukan proses dari sebuah loop 

break berfungsi untuk mengakhiri sebuah looping
contine berfungsi untuk melewati bagian eksekusi yang ada dalam sebuah loop di iterasi tersebut dan lanjut mengekseskusi iterasi selanjutnya 


untuk lebih jelasnya perhatikan penjelasan kedua keyword tersebut : 


BREAK 
while dan loop statement melakukan proses dalam block jika kondisinya benar atau bernilai True. 
Jika break di letakan di tengah proses, maka proses yang sedang berjalan dipaksa segera berakhir dan keluar dari kode blok loop tersebut. 


                Condition ---- false
                ||   True 
                Statement 
                break 
                Statement
                || 

            Flowchart  of break 


    contoh dari break dimana kode di bawah bertujuan untuk mencari huruf vokal dari sebuah string 'Programming' : 

'''
st = 'Programming'# fungsi akan di eksekusi selma huruf adalah konsonan 
for ch in st : 
        if ch in ['a', 'e', 'i', 'o', 'u']
        break # stop loop jika menemukan huruf vokal 
        print (ch)
print('The end')


# output 
'''
    P
    r
    The end

    


    Continue 
    Berbeda dengan break, continue berfungsi untuk melewati bagian eksekusi yang ada dalam sebuah loop di iterasi  selanjutnya 

    Pengakhiran loop hanya berlaku jika kondisinya salah atau False. 



              Condition              false 
                True 
                Statement 
                continue
                Statement




contoh penggunaan continue dalam loop
'''
st = 'Programming' 
# fungsi akan di eksekusi selama huruf adalah konsonan 
for ch in st: 
            if ch in  ['a', 'e', 'i', 'o', 'u']
                continue # skip eksekusi kode di bawah ini jika huruf fokal 
            print(ch)
            print('The end')

'''
    #output
P
r
g
r
m
m
n
g
The end

'''
