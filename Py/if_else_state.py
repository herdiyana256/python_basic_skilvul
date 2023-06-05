'''
    IF ELSE STATEMENT 


    IF ELSE STATEMENT BERARTI : JIKA KONDISINYA BENAR MAKA JALANKAN PERNYATAAN INI DAN JIKA KONDISI NYA TIDAK BENAR MAKA JALANKAN PERNYATAAN YANG LAIN . 

    SEBAGAI CONTOH UNTUK IF-ELSE STATEMENT, PERHATIKAN KODE BERIKUT INI : 

'''
hour = 10 
if hour < 12: 
        print('It is Morning')
else: 
    print('Its is Afternoon')
    # its is morning


'''
    Kondisi kode di atas juga disebut sebagai hubungan yang eksklusif, dimana pagi 'it is morning dan siang it is afternoon tidak bisa terjadi pada waktu yang bersamaan. Pernyataan if-else dapat digunakan untuk hubungan eksklusif tersebut.

Kondisi di atas juga bisa dibuat menggunakan 2 (dua) if statement, namun hal tersebut bukan implementasi yang terbaik karena menjadi kurang optimal.
'''
hour = 10   
    if hour < 12: 
        print('It is Morning')
        if hour >= 12: 
             print('It is Afternoon')

             # It is Morning 


             
     