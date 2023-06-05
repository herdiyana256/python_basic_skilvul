'''
List - Slicing 
Dalam dunia pemograman , kadang kita tidak memerlukan keseluruhan data dari sebuah list . 
Dalam bahasa pemograman Python kita dapat melakukan slicing terhadap list yang kita punya . 
Slicing sendiri berarti mengiris bagian tertentu dari sebuah list . 
Untuk melakukan slicing kita dapat gunakan sintaks list_name[start:end]  untuk menyatakan section yang kita mau pisahkan . 






index      0    1  2    3    4    5   6    7 
Original list a_list    10  20  30   40   50   60  70   80 
 List after slicing    20   30   40    50 
                        Result of the a_list [1:5] slicing: until 50, which is the 5-1 index

                        

Perhatikan contoh penggunaan slicing pada python : 

'''



a_list = [10,20,30,40,50,60,70,80]
a_list[1:5]

# [20,30,40,50]



a_list[0:5]
# [10,20,30,40,50,60,70,80]

# Terdapat beeberapa kombinasi slicing yang dapat kita pakai sesuai kebutuhan dan keinginan kita, kombinasi yang sering dipakai adalah sebagai berikut : 



'''
        Syntax                    Function
    a_list[start:end]          Slicing item dari awal hingga (akhir-1) (tidak termasuk item dari indeks akhir)
    a_list[start:]             Slicing dari awal hingga akhir list. Slicing bagian akhir dari list 
    a_list[:end]               Slicing dari awal hingga akhir-1 indeks
    a_list[:]                  Slicing keseluruhan list 
    a_list[start:end:step]     Slicing dengan melewatkan satu step dari awal hingga akhir -1
    a_list[-2:]                Slicing dua item dari akhir 
    a_list[:-2]                Slicing seluruh item dari awal kecuali dua item terakhir 
    a_list[::-1]               Import semua item tetapi dalam urutan terbalik
    a_list[1::-1]              Slicing dua item pertama dalam urutan terbalik 

'''
