# Vigenere Chiper

def encrypt(message, key):
    encrypted_message = ''  
    for i in range(len(message)):
        char = message[i]  # Mengakses karakter pada pesan yang akan dienkripsi
        key_char = key[i % len(key)] # Mengakses karakter pada kunci yang sesuai dengan karakter pesan
        
        if char.isalpha():  
            char_num = ord(char.upper()) - 65  # Menghitung nilai numerik dari karakter pesan
            key_num = ord(key_char.upper()) - 65  # Menghitung nilai numerik dari karakter kunci

            encrypted_num = (char_num + key_num) % 26 # Menghitung nilai numerik dari karakter yang dienkripsi
            encrypted_char = chr(encrypted_num + 65)  # Mengonversi nilai numerik kembali menjadi karakter

            if char.isupper():  
                encrypted_message += encrypted_char  
            else:
                encrypted_message += encrypted_char.lower()  
        else:
            encrypted_message += char  # Menambahkan karakter yang bukan huruf ke pesan terenkripsi

    return encrypted_message  


def decrypt(ciphertext, key):
    decrypted_message = ''  
    for i in range(len(ciphertext)):
        char = ciphertext[i]  # Mengakses karakter pada pesan terenkripsi
        key_char = key[i % len(key)] # Mengakses karakter pada kunci yang sesuai dengan karakter pesan

        if char.isalpha():  
            char_num = ord(char.upper()) - 65  # Menghitung nilai numerik dari karakter pesan terenkripsi
            key_num = ord(key_char.upper()) - 65  # Menghitung nilai numerik dari karakter kunci

            decrypted_num = (char_num - key_num) % 26  # Menghitung nilai numerik dari karakter yang didekripsi
            decrypted_char = chr(decrypted_num + 65)  # Mengonversi nilai numerik kembali menjadi karakter

            if char.isupper():  
                decrypted_message += decrypted_char  
            else:
                decrypted_message += decrypted_char.lower()  
        else:
            decrypted_message += char  # Menambahkan karakter yang bukan huruf ke pesan terdekripsi

    return decrypted_message  


def main():
    message = input('Masukkan pesan: ')  
    # Menggunakan key 217, karena 3 Digit terakhir NIM saya adalah 217
    key = '217'  
    ciphertext = encrypt(message, key)
    print("Kunci : ", key)
    print('Hasil Enkripsi Teks : ', ciphertext)
    print('Hasil Dekripsi Teks : ', decrypt(ciphertext, key))

# Memnggil fungsi utama
main()

