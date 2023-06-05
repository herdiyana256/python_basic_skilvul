# ELIF STATEMENT 
'''
    ELIF STATEMENT ADALAH PERNYATAAN LOGIKA DALAM PEMOGRAMAN YANG MEMUNGKINAN UNTUK MENGEVALUASI BEBERAPA KONDISI (BERBEDA DARI KONDISI IF ATAU ELSE TUNGGAL), DAN MENJALANKAN KODE YANG SESUAI DENGAN KONDISI YANG BENAR. 
    ELIF ADALAH SINGKATAN DARI "ELSE IF" DAN BIASANYA DIGUNAKAN SETELAH BLOK IF DAN SEBELUM BLOK ELSE, UNTUK MENAMBAHKAN BEBERAPA KONDISI UNTUK DI PERTIMBANGKAN DALAM ALUR PEMOGRAMAN .

    DALAM SINTAKSIS ELIF, BLOK KODE YANG DIKAITKAN DENGAN KONDISI YANG BENAR HANYA AKAN DI EKSEKUSI JIKA SEMUA KONDISI SEBELUM NYA SALAH . 
    JIKA KONDISI ELIF BENAR MAKA BLOK  KODE YANG TERKAIT DENGAN KONDISI TERSEBUT AKAN DI EKSEKUSI DAN EKSEKUSI PROGRAM AKAN KELUAR DARI STRUKTUR IF/ELSE/ELIF. 
    JIKA TIDAK ADA KONDISI ELIF YANG BENAR, MAKA EKSEKUSI PROGRAM AKAN KELUAR DARI STRUKTUR IF/ELIF/ELSE TANPA MENJALANKAN BLOK KODE APAPUN . 


    BERIKUT ADALAH SINTAKSIS EIF STATEMENT

'''
if kondisi_1: 
        blok kode_1
elif kondisi_2:
        blok kode_2
elif kondisi_3: 
            blok kode_3

else: 
    blok kode_default

    '''
        Dalam sintaksis ini, kondisi_1 adalah kondisi pertama yang akan dievaluasi. Jika kondisi_1 salah, maka akan dievaluasi kondisi_2, dan seterusnya. Jika tidak ada kondisi yang benar, maka eksekusi program akan masuk ke blok kode_default.

    '''



    '''
    Elif Statement
Pertimbangkan sebuah program yang menerima bilangan bulat dari pengguna dan mencetak "Ini positif", "Ini 0", dan "Ini negatif".
Jika True dikembalikan dari pernyataan if pertama, baris kode dieksekusi dan keluar dari pernyataan kondisional.
Jika False, keputusan mungkin harus dibuat sesuai dengan ekspresi kondisional kedua.
Program dengan struktur seperti itu dapat dibangun menggunakan if-elif-else.
elif adalah singkatan dari else if
    

Penggunaan elif diperuntukan untuk mempersingkat baris kode dan membuatnya lebih mudah dibaca dibanding harus menulis else dan if secara terpisah, berikut gambaran dari penggunaan elif vs else dan if:



Kedua kondisi menghasilkan hasil yang sama, namun menggunakan elif lebih sederhana dan mengurangi jumlah baris kode.


    
    '''