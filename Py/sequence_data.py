# SEQUENCE DATA TYPES - INTRO 
'''

SEQUENCE DATA TYPES - INTRO
Dalam Python, sequence adalah kumpulan terutut dari tipe data yang serupa atau bisa juga berbeda.
Sequence memungkinkan untuk menyimpan beberapa nilai secara terorganisir dan efisien. 
Ada beberapa jenis tipe data sequence dalam Python yaitu : 

list
tuple
range dan string 



Objek yang disebut dari tipe data sequence disebut objek sequence dan setiap nilai objek sequence tersebut disebut element.



SEQUENCE DATA TYPES - ITERATOR
Tipe data sequence dapat menggunakan operator perkalian, yang membuat element objek berulang kali.
Namun, perkalian objek tidak mungkin dilakukan untuk range dengan operator *. Untuk melakukan iteration, kita dapat  menulisinya sebagai [tipe data urutan] * integer.


Contoh-contoh iteration dalam tipe data sequence 
'''
# LIST 
list1 = [11,22,33,44] * 2 
print(list1)

# output : 
[11,22,44,11,22,33,44]

#TUPLES 
tup1 = (1,2,3)
print(tup1 * 2)
# output : 
(1,2,3,1,2,3)

#STRING 
str2 = 'hello'
print(str2 * 3)


# output : hellohellohello



# RANGE 
'''
    Sama seperti operator + kita juga tidak bisa menggunakan  operator * untuk  tipe data range dengan mengubah tipe data tersebut ke dalam list atau tuple terlebih dahulu . 

'''
range(10) * 3 
    # type error : unsupported operand types(s) for *:  'range' and 'int'




# example : 
ran = list(range(5)) * 3
print(ran)
# Output : 
[0,1,2,3,4,0,1,2,3,4,0,1,2,3,4]




ran = tuple(range(5)) * 3
print(ran)
# Output :
(0,1,2,3,4,0,1,2,3,4,0,1,2,3,4)


#example : contoh operator yang membuat element objek berulang kali adalah operator B, yaitu * (bintang).
a = "Hello"
b = a * 3 
print(b)

# Output : HelloHelloHello



# Other example : 
a = [1,2,3,4]
b = a * 2
print(b)

#[1, 2, 3, 4, 1, 2, 3, 4]






