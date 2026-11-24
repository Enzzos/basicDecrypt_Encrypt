import os
import pyaes

# Abrir o arquivo criptografado
fileName = 'testeCriptografia.txt'

if not os.path.exists(fileName):
    raise FileNotFoundError(f'Arquivo {fileName} não encontrado')

with open(fileName, 'rb') as openFile:
    fileData = openFile.read()

# Chave de descriptografia (deve ter 16, 24 ou 32 bytes)
decryptKey = b'testeransomware1'  # 16 bytes
aes = pyaes.AESModeOfOperationCTR(decryptKey)
decrypt_data = aes.decrypt(fileData)

# Criar novo arquivo descriptografado antes de remover o original
newFileName = 'testeDescriptografado.txt'
with open(newFileName, 'wb') as newFile:
    newFile.write(decrypt_data)

# Remover o arquivo criptografado somente após salvar o descriptografado
os.remove(fileName)