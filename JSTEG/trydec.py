from PIL import Image, ImageTransform
print("Digite a imagem que deseja decifrar:")
source = input()
#Abre a imagem
image = Image.open(source)
#Gera a matriz de quantizacao da imagem
response = image.quantization
message_len = response[0][0]
message = []
i = 1
#Tenta recuperar a mensagem
while i <= message_len :
    message.append(chr(response[0][i]))
    i += 1
message = (''.join(message))
print(message)
