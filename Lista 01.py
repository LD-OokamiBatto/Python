# Python
Exerc. aulas que tive c/ Professor Fernando Masanori
##Faça um programa que peça dois números inteiros e imprima a soma desses dois números
a = int(input('Dígite um número: '))
b = int(input('Mais um número: '))
print(a + b)

##Escreva um programa que leia um valor em metros e o exiba convertido em milímetros
m = int(input('Dígite a metragem: '))
print('Milimetros: ',m * 1000)

##Escreva um programa que leia a quantidade de dias,
##horas, minutos e segundos do usuário. Calcule o total em segundos.
d = int(input('Dias:'))
h = int(input('Horas:'))
m = int(input('Minutos:'))
s = int(input('Segundos:'))
Total = d*24*60*60 + h*60*60 + m*60 + s
print('Total:', Total, 'em segundos')

##Faça um programa que calcule o aumento de um salário.
##Ele deve solicitar o valor do salário e a porcentagem do aumento.
##Exiba o valor do aumento e do novo salário
s = float(input('Dígite o salário: R$'))
p = float(input('porcentagem de aumento:'))
a = s * p / 100
novo = s + a
print('Novo salário: R$', novo)

##Solicite o preço de uma mercadoria e o percentual de desconto.
##Exiba o valor do desconto e o preço a pagar.
p = float(input('Valor do produto: R$'))
d = float(input('Porcentagem do desconto:'))
desconto = p * d / 100
preço = p - desconto
print('Preço: R$', preço)
print('Desconto de: R$', desconto)

##Calcule o tempo de uma viagem de carro.
##Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
d = float(input('Distância da viagem:'))
vm = float(input('Velocidade média em Km/h:'))
tempo = d / vm
print('Tempo médio de:', tempo,  'horas')

##Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32
c = float(input('Temperatura em C°:'))
resultado = (c * 9 / 5) + 32
print(resultado, 'F°')

##Faça agora o contrário, de Fahrenheit para Celsius.
f = float(input('Temperatura em F°:'))
resultado = (f-32) * (5 / 9) 
print(resultado, 'c°')

##Escreva um programa que pergunte a quantidade de km percorridos por um carro 
##alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado.
##Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.
p = float(input('Km/h percorridos:'))
d = float(input('Quantos dias alugados:'))
total = (p * 0.15) + (d * 60)
print('Total a pagar: R$', total)

##Escreva um programa para calcular a redução do tempo de vida de um fumante.
##Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
##Considere que um fumante perde 10 minutos de vida a cada cigarro,
##calcule quantos dias de vida um fumante perderá.
##Exiba o total de dias.
print('Questão 10')
qntDeCigarros = int(input('Quantos cigarros por dia:'))
anosFumando = int(input('Há quantos anos fumou ou fuma:'))
totalDeCigarros = (anosFumando * 365) * qntDeCigarros
diasPerdidos = (totalDeCigarros * 10)/24
print('Foram perdidos', diasPerdidos, 'dias de vida')

##Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão.
a = str(2**1000000)
print('2 elevado a um milhao possui', len(a), 'dígitos')
