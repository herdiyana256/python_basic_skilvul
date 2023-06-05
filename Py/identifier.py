"""
DEKLARASI VARIABEL 


INDENTIFIER 
IDENTIFIER ADALAH NAMA YANG DIBERIKAN UNTUK SEBUAH ENTITAS SEPERTI CLASS, FUNCTION, VARIABEL DAN SEJENISNYA . 
INI MEMBANTU KITA UNTUK MEMBEDAKAN SATU ENTITAS DENGAN ENTITAS LAIN NYA . 


KITA AKAN BELAJAR BERKERJA DENGAN BERBAGAI DATA, TETAPI UNTUK MELAKUKAN NYA, KITA MEMERLUKAN NAMA YANG BERBEDA UNTUK MEMBEDAKAN DATA DI DALAM KODE . 
SAMA SEPERTI SEORANG MEMBEDAKAN ORANG DENGAN MENGGUNAKAN NAMA, SEPERTI "ADAM" DAN "PUTRA", IDENTIFIER MEMAINKAN PERAN VARIAVEL PEMBEDA. 


ATURAN ATURAN DALAM PEMBUARAN VARIABEL : 
- IDENTIFIER DAPAT BERUPA KOMBINASI HURUF ATAU ANGKA GARIS BAWAH (_) , TETAPI TIDAK DAPAT TERDIRI DARI SIMBOL KHUSUS APAPUN. 
- IDENTIFIER TIDAK DAPAT DI MULAI DENGAN ANGKA 
- IDENTIFIER TIDAK BOLEH BERISI SPASI ATAU TAB 
- IDENTIFIER PEKA TERHADAP HURUF BESAR DAN KECIL . OLEH KARENA ITU, VARIABEL index DAN INDEX ADALAH VARIABEL YANG BERBEDA. 
- IDENTIFIER TIDAK DAPAT MENGGUNAKAN SALAH SATU DARI * PYTHON RESERVED WORLD * . 


CONTOH : 
PENGGUNAAN IDENTIFIER DALAM PEMBUATAN VARIABEL : 
"""
 

 lebar = 10 # indentifier untuk membedakan lebar persegi panjang dari data lain 
tinggi = 5 # indentifier untuk membedakan tinggi persefi panjang dari data lin 
luas_kotak = lebar * tinggi 


print('luas area kotak = ' , luas_kotak)


# output : luas area kotak = 50 

# dengan menggunakan identifier lebar dan tinggi, kita  dapat memebedakan lebar dan tinggi persegi panjang dari data lain . 



# meskipun kamu dapat dengan bebas memberi nama identifier, kami tidak dapat menggunakan kata kunci bawaan Python sebagai identifier. selain itu, kata kunci tidak dapat digunajan sebagai nama variabel. Berikut keyword bawaan python yang tidak dapat digunakan sebagai identifier . 


"""
    kata kunci bawaan pythin yang tidak dapat digunakan sebagai pengidentifikasi 



    false  class      return     is             finally     None 
    if      for       lambda     continue       True        def
    from    while     nonlocal   and            del         global 
    not     with      as         elif           try          or 
    yield   assert     else      import         pass        break 
    except  in          raise 

Jika  kita menggunakan salah satu dari kata kunci tersebut maka akan muncul error :
"""

global = 500
# File "ipython-input-6-6cbed63281ae>", line 1 Global = 500 