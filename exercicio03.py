while True:

    numero = input("Digite um número (ou sair): ")

    if numero == 'sair':
        break

    numero = int(numero)

    if numero < 10:
        print('O número {} é menor que 10.'.format(numero))
    elif 10 <= numero <= 50:
        print('O número {} é maior ou igual que 10 e menor ou igual que 50.'.format(numero))
    else:
        print('O número {} é maior que 50.'.format(numero))