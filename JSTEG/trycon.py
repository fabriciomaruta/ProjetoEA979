from PIL import Image, ImageTransform

image = Image.open('sample.jpg')
#generate dict containing arrays
response_ar = image.quantization
print("Digite o que deseja esconder:")
hidden = input()
a =  []
for f in hidden:
    a.append(f)
response_ar[0][1] = 0
i=0
print(response_ar)
while i < len(response_ar[0]):
    response_ar[0][0] = len(a)
    if i < len(a):
        response_ar[0][i+1] = ord(a[i])
    
    #response_ar[1][i] = 200
    i += 1

print(response_ar)
image.save("out.jpg", qtables=response_ar)

