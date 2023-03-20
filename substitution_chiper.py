# Substitution Cipher

import string
data = string.ascii_letters # Daftar yang berisi semua karakter
	
"""
Buat dict untuk menyimpan substitusi
untuk alfabet yang diberikan dalam teks biasa
berdasarkan kunci
"""	
dict1 = {}
key = 4

for i in range(len(data)):
	dict1[data[i]] = data[(i+key)%len(data)]

plain_text= input("Masukkan Teks : ")
cipher_text=[]
# loop to generate ciphertext
for char in plain_text:
	if char in data:
		temp = dict1[char]
		cipher_text.append(temp)
	else:
		temp = char
		cipher_text.append(temp)
		
cipher_text= "".join(cipher_text)
print("Hasil Enkripsi Text : ",cipher_text)

	
"""
Buat kamus untuk menyimpan substitusi
untuk alfabet yang diberikan dalam sandi
teks berdasarkan kunci
"""	
dict2 = {}	
for i in range(len(data)):
	dict2[data[i]] = data[(i-key)%(len(data))]	
# Mendekripsi Plain Text
decrypt_text = []

for char in cipher_text:
	if char in data:
		temp = dict2[char]
		decrypt_text.append(temp)
	else:
		temp = char
		decrypt_text.append(temp)
		
decrypt_text = "".join(decrypt_text)
print("Hasil Dekripsi Text :", decrypt_text)
