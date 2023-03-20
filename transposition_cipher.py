# Transposition Cipher

def encrypt(message, key):
    # Membuat dictionary untuk menyimpan urutan indeks karakter dalam key
    key_dict = {key[i]: i for i in range(len(key))}

    # Menghitung jumlah baris matriks
    rows = len(message) // len(key)
    if len(message) % len(key) > 0:
        rows += 1

    # Menginisialisasi matriks dengan karakter kosong
    matrix = [['' for _ in range(len(key))] for _ in range(rows)]

    # Mengisi matriks dengan karakter pesan
    row = 0
    col = 0
    for c in message:
        matrix[row][col] = c
        col += 1
        if col == len(key):
            col = 0
            row += 1

    # Membaca matriks secara berurutan untuk menghasilkan ciphertext
    cipher = ''
    for k in sorted(key_dict.keys()):
        col = key_dict[k]
        for row in range(rows):
            cipher += matrix[row][col]

    return cipher


def decrypt(cipher, key):
    # Membuat dictionary untuk menyimpan urutan indeks karakter dalam key
    key_dict = {key[i]: i for i in range(len(key))}

    # Menghitung jumlah baris matriks
    rows = len(cipher) // len(key)
    if len(cipher) % len(key) > 0:
        rows += 1

    # Menginisialisasi matriks dengan karakter kosong
    matrix = [['' for _ in range(len(key))] for _ in range(rows)]

    # Mengisi matriks dengan karakter ciphertext
    col = 0
    row = 0
    for k in sorted(key_dict.keys()):
        j = key_dict[k]
        i = 0
        while i < rows and col < len(cipher):
            matrix[i][j] = cipher[col]
            i += 1
            col += 1
        row += 1

    # Membaca matriks secara berurutan untuk menghasilkan plaintext
    plaintext = ''
    for row in matrix:
        plaintext += ''.join(row)

    return plaintext


def main():
    message = input('Masukkan teks: ')
    key = input('Masukkan key: ')  
    cipher = encrypt(message, key)  
    print('Hasil Enkripsi Teks : ', cipher)
    print('Hasil Dekripsi Teks : ', decrypt(cipher, key)) 


main() # Memanggil fungsi utama

