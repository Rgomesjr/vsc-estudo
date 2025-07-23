amigos = ['Bianca', 'Robson', 'Heloisa', 'Adriana', 'Rodrigo']
numeros = [1, 2, 3, 4, 5]
original = amigos.copy()

print(amigos)
print(numeros)

print()

print('Podemos juntar as listas de amigos e números, podemos inserir dados ou remover, escolha:')
print('extender, inserir, remover')
mudanca = input('Digite sua mudança: ')
print()

if mudanca == "extender":
    amigos.extend(numeros)
    print("Lista estendida:", amigos)

elif mudanca == "inserir":
    print('amigos ou numeros')
    inserido = input('Digite onde deseja inserir: ')
    if inserido == "amigos":
        novo_amigo = input('Digite o nome do amigo a ser inserido: ')
        amigos.append(novo_amigo)
        print("Nova lista de amigos:", amigos)
    elif inserido == "numeros":
        novo_num = input('Digite o número a ser inserido: ')
        numeros.append(int(novo_num))  # converte para int
        print("Nova lista de números:", numeros)
    else:
        print('Digite corretamente: amigos ou numeros')

elif mudanca == "remover":
    print('amigos ou numeros')
    remover_de = input('Digite de qual lista deseja remover: ')
    if remover_de == "amigos":
        nome_remover = input('Digite o nome a ser removido: ')
        if nome_remover in amigos:
            amigos.remove(nome_remover)
            print("Nova lista de amigos:", amigos)
        else:
            print("Nome não encontrado na lista de amigos.")
    elif remover_de == "numeros":
        numero_remover = input('Digite o número a ser removido: ')
        if int(numero_remover) in numeros:
            numeros.remove(int(numero_remover))
            print("Nova lista de números:", numeros)
        else:
            print("Número não encontrado na lista.")
    else:
        print("Digite corretamente: amigos ou numeros")

else:
    print("Opção inválida.")