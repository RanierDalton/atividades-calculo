# Exercício 1
'''
peso = float(input('Qual a sua massa em KG? '))
altura = float(input('Qual a sua altura em Metros? '))

imc = peso / (altura**2)

print(f'O seu IMC é de {imc:.1f}')
'''

# Exercício 2 
'''
peso = float(input('Qual a sua massa em KG? '))
altura = float(input('Qual a sua altura em Metros? '))

imc = peso / (altura**2)

print(f'O seu IMC é de {imc:.1f}')

if imc < 18.5:
    print('Diagnóstico: Abaixo do peso normal')
elif imc >= 18.5 and imc < 25:
    print('Diagnóstico: Peso normal')
elif imc >= 25 and imc < 30:
    print('Diagnóstico: Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Diagnóstico: Obeso')
elif imc >=40:
    print('Diagnóstico: Obesidade Mórbia')
'''

# Exercício 3
peso = float(input('Qual a sua massa em KG? '))
altura = float(input('Qual a sua altura em Metros? '))

imc = peso / (altura**2)

# Exercício 4 - Os valores ficam com duas casas decimais
print(f'O seu IMC é de {imc:.2f}')

if imc < 18.5:
    print('Diagnóstico: Abaixo do peso normal')
elif 18.5 <= imc < 25:
    print('Diagnóstico: Peso normal')
elif 25 <= imc < 30:
    print('Diagnóstico: Sobrepeso')
elif 30 <= imc < 40:
    print('Diagnóstico: Obeso')
elif imc >= 40:
    print('Diagnóstico: Obesidade Mórbia')