# Dictionary - Function and Operators 

'''
    len() function dan in Operator
    Untuk Mengetahui jumkah item dalam sebuah dictionary, kita bisa menggunakan fungsi len() seperti berikut : 

    
'''

a = {'abc': 100, 'def': 200 }
print(len(a))

# output : 2 



'''
    in Operator bisa digunakan untuk memvalidasi apakah key ada  di dalam sebuah dictionary. 
    Operator in akan mengembalikan nilai True apabila key tersebut ditemukan dalam dictionary dan operator not in melakukan kebalikan dari operator in. 

'''

person = {'Name': 'Herdiyan Adam', 'Age': 26, 'Weight': 59}

len(person) # Mengembalikna jumlah item dalam dictionary


'name' in person # 'Nama' ditemukan sebagai salah satu kunci 

'Job' in person # Job tidak ditemukan sebagai salah satu kunci 

'Herdiyan Adam' in person # 'Herdiyan Adam' ditemukan di nilai tetapi tidak di kunci (hati-hati)

'Herdiyan Adam' not in person # Mengembalikan True karena 'Herdiyan Adam' tidak ditemukan di kunci





# Example : 
Person = {'Nama': 'Herdiyan Adam','Umur': 26}
print(len(Person))
# 2 