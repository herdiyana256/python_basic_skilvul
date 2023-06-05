'''
    PERULANGAN (LOOP) PADA PYTHON MENGGUNAKAN KEYWORD 'FOR'. 
    BERIKUT ADALAH SINTAKS DARI FOR LOOP PADA PYTHON : 
'''

for variable in sequence: 
    # block of code


    '''
    Penjelasan : 
    Variable - adalah variable yang akan digunakan untuk menyimpan setiap element dari 'sequence' pada setiap iterasi perulangan . 
    Sequence adalah objek iterable yang akan di iterasi. Objek iterable dapat berupa list, tuple, string, atau objek yang mendukung iterasi. 

    Setiap element pada 'sequence' akan di simpan pada 'variable' dan  blok kode pada perulangan akan di eksekusi pada setiap iterasi . 


    Contoh penggunaan for loop pada Python :  
    
    '''
    fruits =  ["apple", "banana", "cherry"]
        for fruit in fruits: 
        print(fruit)
    



    '''
        BASIC LOOP - FOR LOOP SYNTAX 
        SEBAGAI CONTOH LOOP STATEMENT YANG PERTAMA KITA AKAN BELAJAR MENGENAI FOR LOOP DIMANA FOR LOOP MEMILIKI SINTAKS SEBAGAI BERIKUT : 

        Variable                    rangefunction
        for   n         in          range(5): 
                for block that will be executed repeatedly


    
    Terdapat 2 komponen penting dalam penggunaan for yaitu:

Variable
Range function
Variabel yang digunakan untuk pernyataan loop umumnya berupa abjad seperti i, j, k, l, dan variabel ini disebut variabel kontrol loop.

Range function merupakan bagian penting dalam for loop syntax yang berguna untuk mengontrol fungsi dan kerja dari loop statement.

Dalam range, kita dapat menghasilkan bilangan bulat berurutan antara nilai awal yang diberikan dan nilai berhenti, seperti dalam rentang (0, 5), atau kita dapat menambahkan nilai tambahan di akhir, seperti dalam rentang (0, 5, 2).
Dalam rentang (0, 5, 1), 1 terakhir adalah nilai langkah default yang ditambahkan di setiap kenaikan.

    

Nilai yang menghentikan looping. Nilai ini dikecualikan dari generasi. 
Nilai yang memulai generasi                ukuran nilai yang berubah dalam satu kenaikan 
                            range(start=0,stop, step=1)

  Dengan memanggil fungsi range(0, stop, 1)menghasilkan bilangan bulat dari 0 hingga (stop-1) dengan kelipat 1.

  Semua angka didalam fungsi range hanya bisa menggunakan integer sehingga jika kita menggunakan float sebagai contoh, akan muncul error                          

    '''
    for i in range(0,9): 
            print(i, 'Welcome to everyone!!')

            