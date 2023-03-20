# Shift Cipher

def encrypt(pesan, shift):
    hasil = ''  
    for char in pesan:
        # Memeriksa apakah karakter huruf besar lalu melakukan enkripsi
        if char.isupper():
            hasil += chr((ord(char) - 65 + shift) % 26 + 65)
        # Memeriksa apakah karakter huruf kecil lalu melakukan enkripsi
        elif char.islower():
            hasil += chr((ord(char) - 97 + shift) % 26 + 97) 
        else:  # jika karakter bukan huruf, tambahkan karakter asli ke variabel hasil
            hasil += char 
    return hasil

def decrypt(pesan, shift):
    hasil = ''
    for char in pesan:
        # Memeriksa apakah karakter huruf besar lalu melakukan dekripsi
        if char.isupper():  
            hasil += chr((ord(char) - 65 - shift) % 26 + 65)
        # Memeriksa apakah karakter huruf kecil lalu melakukan dekripsi
        elif char.islower():  
            hasil += chr((ord(char) - 97 - shift) % 26 + 97)
        else:  # jika karakter bukan huruf, tambahkan karakter asli ke variabel hasil
            hasil += char  
    return hasil

def main():
    pesan = input('Masukkan pesan: ')
    # Menggunakan shift 17, karena 2 Digit terakhir NIM saya adalah 17
    shift = 17
    ciphertext = encrypt(pesan, shift)
    print("Shift : " + str(shift))
    print('Hasil Enkripsi Teks : ', ciphertext)
    print('Hasil Dekripsi Teks : ', decrypt(ciphertext, shift))

main() # Memanggil fungsi utama


