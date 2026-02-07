def ler_numero():
    valor = input("Digite um número (ou sair): ")

    if valor.lower() == 'sair':
        return None

    if not valor.isnumeric():
        print('Digite apenas números!')
        return ler_numero()

    return int(valor)


while True:

    numero1 = ler_numero()
    if numero1 is None:
        break

    numero2 = ler_numero()
    if numero2 is None:
        break

    operacao = input("1 Soma | 2 Sub | 3 Mult | 4 Div: ")

    if operacao == '1':
        print(numero1 + numero2)

    elif operacao == '2':
        print(numero1 - numero2)

    elif operacao == '3':
        print(numero1 * numero2)

    elif operacao == '4':
        if numero2 == 0:
            print("Não existe divisão por 0")
        else:
            print(numero1 / numero2)

    else:
        print("Operação inválida")
