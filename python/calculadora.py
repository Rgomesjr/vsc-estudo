print('CALCULADORA')

num1 = float(input('Digite um numero para fazer a operação: '))
num2 = float(input('Digite outro numero para fazer a operação: '))

print()

print('Escolha entre essas operações :')
print('+ , - , * , / ')
operacao = input('Digite a opeção desejada :')

print()

if operacao == "+":
    resultado = num1 + num2
    print('Sua conta deu :' , resultado)

elif operacao == "-":
    resultado = num1 - num2
    print('Sua conta deu :' , resultado)

elif operacao == "*":
    resultado = num1 * num2
    print('Sua conta deu :' , resultado)

elif operacao == "/":
    resultado = num1 / num2
    print('Sua conta deu :' , resultado)

else:
    print('Digite da maneira correta.')