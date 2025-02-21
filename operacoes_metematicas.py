import math

# Aluno: Ranier - RA.: 04242043
# Exemplos 
print('\n\nEXEMPLOS\n')
a = 6
b = 3
soma = a+b
subtracao =a-b
multiplicacao = a*b
divisao =a/b
print ("Vamos mostrar todos os resultados")
print ("a=", a)
print ("b=", b)
print ("a+b=",soma)
print ("a-b=",subtracao)
print ("a*b=",multiplicacao)
print ("a/b=",divisao)

print ('\n')
a1=6.5
b1=2.5
soma = a1+b1
subtracao =a1-b1
multiplicacao = a1*b1
divisao =a1/b1
print ("Vamos mostrar todos os resultados")
print ("a1=", a1)
print ("b1=", b1)
print ("a1+b1=",soma)
print ("a1-b1=",subtracao)
print ("a*b=",multiplicacao)
print ("a/b=",divisao)

# Exercício 1
print('\nEXERCÍCIOS PROPOSTOS\n')
a = 2
potencia_ao_quadrado = math.pow(a,2)
potencia_ao_cubo = math.pow(a,3)
potencia_a_quarta = math.pow(a,4)
print(f'1 - a² = {potencia_ao_quadrado} | a³ = {potencia_ao_cubo} | a**4 = {potencia_a_quarta}')

# Exercício 2
x = 512
raiz_quadrada_de_x = math.pow(x, 1/2)
raiz_cúbica_de_x = math.pow(x, 1/3)
raiz_quarta_de_x = math.pow(x, 1/4)
print(f'2 - √x = {potencia_ao_quadrado} | ³√x = {potencia_ao_cubo} | 4√x = {potencia_a_quarta}')

# Exercício 3
w = 3345.61
piso = math.floor(w)
teto = math.ceil(w)
_round = round(w)
print(f'3 - piso = {piso} | teto = {teto} | arredondamento = {_round}')

'''
    Exercício 4 

    O round é uma função embutida do python para arredondar os números de acordo com as casas decimais e os valores delas
'''
arredondar_casa = round(w,1) # arredonda para ficar 1 casa decimal
round(w,0) # arredonda, porém ainda sobre uma casa decimal com 0

# Exercício 5
x1=1.456
x2=3.678
x3=7.5
print(f'5 - x1 = {round(x1)} | x2 = {round(x2)} | x3 = {round(x3)}')

# Exercício 6
print(f'6 - int(floor(1.456)) = {int(math.floor(1.456))}')

# Atividades de POTÊNCIA 
print('\nEXERCÍCIOS DE POTÊNCIA - 7\n')
# Exercicio 1
expressao_um = 2 ** 3
print('Exercício 1: ', expressao_um)

# Exercicio 2
expressao_dois = -2 ** 3
print('Exercício 2: ', expressao_dois)

# Exercicio 3
expressao_tres = 1 ** 0
print('Exercício 3: ', expressao_tres,)

# Exercicio 4
expressao_quatro = -1 ** 0
print('Exercício 4: ', expressao_quatro)

# Exercicio 5
expressao_cinco = 2 ** 0
print('Exercício 5: ', expressao_cinco)

# Exercicio 6
expressao_seis = (2/5) ** 3
print('Exercício 6: ', expressao_seis)

# Exercicio 7
expressao_sete = 3 ** -2
print('Exercício 7: ', expressao_sete)

# Exercicio 8
expressao_oito = (1/2) ** -3
print('Exercício 8: ', expressao_oito)

# Exercicio 9
expressao_nove = (-1 ** 3) ** 4
print('Exercício 9: ', expressao_nove)

# Exercicio 10
expressao_dez = (1/2) ** 3
print('Exercício 10: ', expressao_dez)

# Exercicio 11
expressao_onze = (1/4) ** 4
print('Exercício 11: ', expressao_onze)

# Exercicio 12
expressao_doze = 0 ** 4
print('Exercício 12: ', expressao_doze)

# Exercicio 13
expressao_treze = 1 + (0.41 ** 2)
print('Exercício 13: ', expressao_treze)

# Exercicio 14
expressao_quatorze = 1/4 + (5 ** 2) - (2 ** -4)
print('Exercício 14: ', expressao_quatorze)

# Exercicio 15
expressao_quinze = (2 ** -3) + (-4 ** -5)
print('Exercício 15: ', expressao_quinze)

# Exercicio 16
expressao_dezesseis = (((4/5 - 1/2) + 1)**-2) + (1 / ((1 + (3 ** 2)) - ((4 - 5) ** -2)))
print('Exercício 16: ', expressao_dezesseis)