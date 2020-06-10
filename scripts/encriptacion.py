import os, datetime
from cryptography.fernet import Fernet

root_dir = '/app/decrypteds'

for directory, subdirectories, files in os.walk(root_dir):
    for nameFile in files:
        if nameFile != '.gitignore':
            os.remove(os.path.join(directory, nameFile))

root_dir = '/app/encrypteds'

for directory, subdirectories, files in os.walk(root_dir):
    for nameFile in files:
        if nameFile != '.gitignore':
            os.remove(os.path.join(directory, nameFile))

root_dir = '/app/keys'

date_time = os.path.join(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))

for directory, subdirectories, files in os.walk(root_dir):
    for nameFile in files:
        if nameFile != '.gitignore':
            os.remove(os.path.join(directory, nameFile))


root_dir = '/app/data'
date_time = os.path.join(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))

for directory, subdirectories, files in os.walk(root_dir):
    for nameFile in files:
        if directory == '/app/data' and nameFile != '.gitignore':
            # Generate key
            key = Fernet.generate_key()
            print(key)

            # Save file key
            file = open(os.path.join('keys/',nameFile + ' ' + date_time + '.key'),'wb')
            file.write(key) # The key is type bytes
            file.close()

            # Open the file to encrypt
            with open(os.path.join(directory, nameFile), 'rb') as f:
                data = f.read()

            # Open the file to encrypt
            with open(os.path.join('keys/',nameFile + ' ' + date_time + '.key'), 'rb') as f:
                key = f.read()

            # Data encrypted 
            fernet = Fernet(key)
            encrypted = fernet.encrypt(data)

            # Write the encrypted file 
            with open(os.path.join('encrypteds/',nameFile + ' ' + date_time + '.encrypted'), 'wb') as f:
                f.write(encrypted)

            with open(os.path.join('keys/',nameFile + ' ' + date_time + '.key'),'rb') as f:
                key = f.read() # The key is type bytes
            
            # Write the encrypted file 
            with open(os.path.join('encrypteds/',nameFile + ' ' + date_time + '.encrypted'), 'rb') as f:
                data = f.read()

            # Data decrypted
            fernet = Fernet(key)
            decrypted = fernet.decrypt(data)

            # Write the decrypted file 
            with open(os.path.join('decrypteds/',nameFile + ' ' + date_time + '.decrypted'), 'wb') as f:
                f.write(decrypted)
