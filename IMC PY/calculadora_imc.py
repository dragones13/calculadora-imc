nome = str(input('digite seu nome: '))
peso = float(input('informe seu peso: '))
altura = float(input('digite sua altura: '))
imc = peso / (altura ** 2)

print(f'o seu IMC e de {imc}')

if imc < 18.5:
    print(f'{nome}voce esta abaixo do peso')
elif 18.5 <= imc < 24.9 :
    print(f'parabens {nome} voce esta no peso ideal')
elif 25 <= imc < 29.9:
    print(f'{nome}voce esta com sobrepeso')
elif 30 <= imc < 34.9:
    print (f'{nome} voce esta com obesidadde grau 1')
elif 35 <= imc < 39.9:
    print(f'{nome} voce esta com obesidade grau 2')
else:
    print(f'{nome} voce esta com obesidade morbida grau 3, tome cuidado com sua saude!') 
    

#esse e um projeto de calculadora imc desenvolvido para a aula pratica, 
# esse trabalho tem com o objetivo calcular o imc corporal com base em peso 
# e altura, com essas informacoes e possivel saber se a pessoa esta ou nao 
# com o peso ideal, caso ela esteja no peso ideal a calculadora parabeneliza 
# a pessoa, caso esteja em obesidade grau 3, a calculadora pede para a pessoa cuidar de sua saude.

#as informacoes referente aos dados imc foram pegas da internet.

#a ferramenta google cloud e muito parecida com e VSCODE na qual eu ja sabia utilizar
#nao tive dificuldade na utilizacao.