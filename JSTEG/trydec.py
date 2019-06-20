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
secondMatrix = 0
receiverCounter = 1
while i <= message_len + 1:
	if i == 64 and secondMatrix == 0 : 
		secondMatrix = 1
		receiverCounter = 0
	message.append(chr(response[secondMatrix][receiverCounter]))
	i += 1
	receiverCounter += 1
message = (''.join(message))
print(message)
