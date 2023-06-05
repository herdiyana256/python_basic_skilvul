'''
    NESTED LOOP 
    Nested loop - Perulangan ganda mengacu pada struktur

    
    Contoh nested loop menggunakan for dibawah ini berisi pernyataaan for yang berada di dalam pernyataan for lain nya . 
    kode ini merupakan perhitungan perkalian dari 2 x 1 hingga 9 x 9 


'''
for  i in range(2,10): 
        for j in range(1,10): 
                print('{}x{} = {:2d}, '.format(i, j, i*j), end = '')   
                print() # executes inner loop and change line


# Struktur dari nested loop adalah sebagai berikut : 
'''
    Outer Loop -------- for in range(2,10)
                        for j in range (1,10): 
                            print('{}*{}={2d}'.format(i, j, i*j), end='')
                        print()

                '''
i memiliki nilai dari 2 hingga 9 
j bagian dalam memiliki nilai dari 1 hingga 9 
struktur ini diulang, menghasilkan 72 perhitungan dan output secara total
Dalam kasus double for loop atau tripe for loop, menjadi sulit untuk membaca dan memahami kode.
untuk alasan ini, nested loop tidak disarankan menggunakan struktur lebih dari tiga loop 
'''