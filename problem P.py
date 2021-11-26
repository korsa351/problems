import requests
import simplecrypt
from simplecrypt import encrypt, decrypt

passwords_file = requests.get('https://stepik.org/media/attachments/lesson/24466/passwords.txt')
encrypted_file = requests.get('https://stepik.org/media/attachments/lesson/24466/encrypted.bin')

passwords = passwords_file.content.decode('utf8').split()
encrypted_information = encrypted_file.content

for password in passwords:
    try:
        print(decrypt(password, encrypted_information))
        print(password)
    except simplecrypt.DecryptionException:
        continue
