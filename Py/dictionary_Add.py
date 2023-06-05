# Dicitoary - Adding, Modifying, Delete, Vslues 


# Adding Items 
# Berikut contoh kode untuk menambahkan item baru dalam sebuah Dictionary . Kita hanya perlu menambahkan dengan cara : 

nama_dictionary[nama_kunci] = nilai 


# Agar lebih jelas, berikut kode untuk menambahkan item dengan dengan key job dan value  Data Scientist

person = {'Name': 'Herdiyan Adam', 'Age': 27, 'Weight' : 59 }
person['Job'] = 'Data Scientist' # key  baru : Masukan nilai dari key tersebut 
print(person)

# Output :{'Name': Herdiyan Adam, 'Age': 26, 'Weight': 59, 'Job': 'Data Scientist'} 



'''
    Modifying items 
    Dalam Mengubah nilai dari sebuah key dalam dictionary yaitu caranya kurang lebih sama dengan menambahkan item ke dalam dictionary, Perbedaan nya hanya terletak pada nama dari key. 
    Untuk mengubah nilai, Nama key yang digunakan adalah nama key yang memang sudah ada didalam dictionary tersebut . 
    Namun Jika ingin menambahkan item baru, harus menggunakan nama key yang baru . 
    Kode di bawah contoh untuk mengubah nilai dari key age yaitu 26 -> 27: 

'''

# example : 
person ={'Name' : 'Herdiyan Adam', 'age': 26, 'Weight': 59} 
person['age'] = 27 # Ubah Value dari key yang sudah ada 'Age'
print(person)

#output : 
{'Name': 'Herdiyan Adam', 'Age': 27, 'Weight': 59}





# Deleting Items 
# Terakhir, untuk menghapus sebuah item dari dictionary kita bisa menggunakan del keywords. Berikut contoh untuk menghapus key Age dari person :
person = {'Name': 'Herdiyan Adam', 'Age': 27, 'Weight': 59}
del person['Age'] # DELETE VALUE DARI KEY YANG SUDAH ADA 'Age'
print(person) 
# Output : 

{'Name': 'Herdiyan Adam', 'Weight': 59}


# untuk menghapus dictionary kita harus berhari-hati karena jika kita menghapus item dengan key belum ada, maka akan muncul KeyError

person = {'Name': 'Herdiyan Adam', 'Age': 27, 'Weight': 59}
del person['Hometown']

'''
        KeyError : 
        <ipython-input-24-2edca7f1d7c> in <module>
        --------> del person ['Hometown']
        KeyError 'Howntown'
'''


# Example : 
person = {}
person['Umur'] = 15 
print(person)
# {'Umur': 15}


