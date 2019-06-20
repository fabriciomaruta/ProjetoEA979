from PIL import Image, ImageTransform
print("Digite o nome do arquivo de imagem em que a esteganografia sera feita:")
source = input()
image = Image.open(source)
#generate dict containing arrays
response_ar = image.quantization
print("Digite o que deseja esconder:")
hidden = input()
a =  []
#Cria vetor contendo mensagem a ser escondida
for f in hidden:
    a.append(f)
response_ar[0][1] = 0
i=0
while i < len(response_ar[0]):
    response_ar[0][0] = len(a)
    if i < len(a):
        response_ar[0][i+1] = ord(a[i]) 
    i += 1
image.save("out.jpg", qtables=response_ar)
print("Imagem gerada no arquivo out.jpg")
