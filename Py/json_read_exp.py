'''
    JSON - Read and Exporting 

    Read JSON Data 
    Modul json dalam Python menyediakan berbagai fungsi untuk membaca file atau string tipe json sebagai dictionary dan mengubah nya menjadi string. 

    Untuk membaca string tipe json, kita dapat gunakan fungsi loads() . 
    Berikut ini adalah proses membaca dan memeriksa informasi data pribadi tipe kamis dalam tipe data json. 
    Data tipe json yang terdiri dari string dapat di ubah menjadi tipe dcitonary melalui fungsi loads() dalam modul json.
'''

import json 

data = '{"Name": "Herdiyan Adam", "Age": 26, "Hobby": ["basskball"], \
    "Family": {"father": "Herdiyan Adam", "mother": Mimi Jubaedah}, "Married": true}'


json_data = json.loads(data)

print(type(json_data))
print(json_data['Name'])
print(json_data['Family']) 
print(json_data['Married'])

'''
    <class 'dict'>
    Herdiyan Adam 
    {'father': 'Herdiyan Adam', 'mother': 'Mimi Jubaedah'}
    True
'''



'''
    Sementara itu kebalikannya, kita bisa menggunakan fungsi dumps() untuk merubah dictionary menjadi json-string. Fungsi dumps() untuk menghasilkan sebuah file tipe JSON dari data dictionary.


'''

import json 
Dictionary = {'Halo': 123, 'Semua': 456}

json_string = json.dumps(Dictionary)


print('Result:  ', json_string)
print('Tipe: ', type(json_string))


'''
Result:  {"Halo": 123, "Semua": 456}
Tipe:  <class 'str'>
'''

# Result json_string merupakan sebuah JSON string hasil dari fungsi json.dumps()



'''
    Result json_string merupakan JSON string hasil dari fungsi jsom.dumps()

'''




'''
    Exporting JSON data
    Untuk membuat format data JSON kedalam sebuah file pada Python, kita dapat menggunakan json.dump(). 

    Harap diperhatikan bahwa ada 2 Method yang berbeda yaitu json.dump() dan json.dump()

'''

import json 

data = '{"title": ""The Old Man and The Sea", "ISBN": "12345", "Author": "Herdiyan Adam"}'
json_data = json.loads(data)

# Code to create json_data as book json file 
with open('book.json', 'w') as f: 
        json.dump(json_data, f, indent='\t')

        
