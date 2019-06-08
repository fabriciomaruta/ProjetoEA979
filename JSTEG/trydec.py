from PIL import Image, ImageTransform

image = Image.open("out.jpg")
response = image.quantization
print(response)
message_len = response[0][0]
message = []
i = 1
while i < message_len :
    message.append(chr(response[0][i]))
    i += 1
print(message)
