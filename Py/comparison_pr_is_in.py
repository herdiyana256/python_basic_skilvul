# COMPARISON OPERATOR IS & IN 

# COMPARISON OPERATOR LS

# Operator is memeriksa apakah kedua objek itu sama. Perbedaan nya dengan operator == adalah operator == memeriksa nilai dari kedua objek 

a = 1 
b = 1.0 
print(a == b)
print (a is b)


# output : True  False 


'''
    OPERATOR is MEMERIKSA APAKAH KEDUA OBJEK ITU SAMA. PERBEDAAN NYA DENGAN OPERATOR == ADALAH OPERATOR == MEMERIKSA NILAI DARI KEDUA OBJEK 

'''
a = 1 
b = 1.0 
print(a == b)
print(a is b)


# output :  True False


'''
Baris ketiga menggunakan operator == untuk memeriksa apakah kedua nilai tersebut sama. Karena kedua nilai sama, sehingga hasilnya adalah True.
Baris keempat memeriksa apakah kedua objek itu sama. Karena a adalah bilangan integer sedangkan b adalah bilangan float, kedua objek tidak sama. Dengan kata lain, mereka disimpan dalam memori yang berbeda dan oleh karena itu, hasilnya adalah False.


'''





'''
    Comparison Operator In 
    Operator in memeriksa untuk melihat apakah kedua string cocok sebagai. Operator in sering digunakan untuk 
    menentukan apakah ada karakter yang cocok didalam string, apabila terdapat kecocokan maka akan mengembalikan nilai True dan jika tidak akan mengembalikan nilai False.

'''
print('aaa' in 'aaa-bbb-ccc')
print('bbb' in 'aaa-bbb-ccc')
print('ddd' in 'aaa-bbb-ccc')

# output  : True True False 




# Dalam kode diatas, karena string 'aaa' dan 'bbb' termasuk dalam string 'aaa-bbb-ccc', hasilnya adalah True, sementara 'ddd' tidak termasuk dalam string 'aaa-bbb-ccc' sehingga hasil nya adalah False.