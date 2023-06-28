# Sistema de IMC

print('Calcule o seu IMC a baixo: \n')

nome = input('Qual é o seu nome: ')
altura =  float(input('Insira a sua altura: '))
peso  = float(input('Insira o seu peso: '))
print()

Imc = peso / (altura * altura)
Imc = round(Imc, 2)

print()

#  Menor que 18,5  Magreza
if Imc < 18.6:
    print(f'{nome} seu imc é {Imc} procure um profissional da saúde.')
#  18,5 a 24,9 Normal 
elif  18.5 <= Imc < 24.9:
    print(f'{nome} seu imc é {Imc} e você com peso normal.')
#  25 a 29,9	Sobrepeso
elif 25 <= Imc < 29.9:
    print(f'{nome} seu imc é {Imc} e você está com sobrepeso.')
#  30 a 34,9	Obesidade grau I
elif  30 <= Imc < 34.9:
    print(f'{nome} seu imc pe {Imc} e você está com Obesidade Grau I')
#  35 a 39,9	Obesidade grau II
elif 35 <= Imc < 39.9:
    print(f'{nome} seu imc é {Imc} e você está com Obesidade grau II')
    print('Procure um profissional na aréa da saúde.')
#  Maior que 40	Obesidade grau III
else:
    print(' você está com Obesidade grau III')
    print('Procure um profissional na aréa da saúde.')
