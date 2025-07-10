print('Escolha qual operação')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')

operacao = (input('Qual operação matemática você deseja (De 1 a 4) :'))

num1 = float(input('Digite o primeiro número:'))
num2 = float(input("Digite o segundo número:"))

if operacao == "1":
    resultado = num1+num2
    print('A soma deu', resultado)

elif operacao == "2":
    resultado = num1-num2
    print('A subtração deu', resultado)

elif operacao == "3":
    resultado = num1 * num2
    print('A mutiplicação deu', resultado)

elif operacao == "4":
    resultado = num1 / num2
    print('A divisão deu', resultado)

else:
    print('Escolha um número válido')