# Esteganografia em Imagens JPEG

## Motivação
Para a técnica utilizada, o foco foi explorar a compressão de imagens JPEG utilizando a biblioteca **PIL** do python.
Após entender o método de compressão utilizado, teve-se a ideia de atacar a matriz de quantização, que é utilizada junto com a matriz de coeficientes **DCT** para calcular o valor dos pixels da imagem jpeg.
###### Matriz de quantização
A matriz de quantização é uma matriz 8x8 utilizada na compressão JPEG responsável pelo raio de compressão, quanto maior o valor dos coeficientes da matriz, melhor a compressão. 

Como a matriz de quantização é simples de ser recuperada numa imagem, e seus valores permanecem (A não ser que aconteça uma outra compressão do arquivo), acabou que sua característica chamou atenção, pois ela não altera características do conteúdo da imagem, apenas dando a impressão de uma imagem de maior qualidade ou menor qualidade.

## O código
São disponiblizados dois códigos em python, um para esconder a mensagem, e outro para recuperar a mensagem escondida. 
Pelo método utilizado, não é necessário usar a imagem original, o próprio algoritmo recupera a mensagem a partir da matriz de quantização.

Para rodar o programa, é necessário instalar a biblioteca **PIL**, que pode ser instalada pelo pip da seguinte forma:
```sh
sudo pip install pil
```
### Escondendo a mensagem
Após instalar a biblioteca, basta nomear sua imagem jpg para `source.jpg` e rodar o programa, chamando o python3 com o comando :
```sh
python3 trycon.py
```
Siga as instruções pedidas na tela e logo sua mensagem estará escondida.

### Recuperando a mensagem

Para recuperar a mensagem, seu arquivo com a mensagem escondida deve ser nomeado de `out.jpg` (Caso use o próprio programa pra esconder, a imagem gerada já terá esse nome)
Basta chamar o programa, ele imprimirá a mensagem na tela
```sh
python3 trydec.py
```

## Limitações
A grande limitação dessa técnica, por usar a matriz de quantização fornecida pela biblioteca PIL, é que a mensagem a ser escondida, por hora necessita ser menor que 128 caracteres.

### Ideias para contornar o problema:
- Uma das ideias desenvolvidas, é explorar os Bytes que compõem a matriz, embutindo mais de um valor por conjunto de bits.