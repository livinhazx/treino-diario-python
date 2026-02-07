
while True:
 
 numero1 = input('Digite um número (ou sair): ')

 if numero1 == 'sair':
  break
 numero2 = int(input('Digite outro número (ou sair):  '))

 if numero2 == 'sair':
  break

 numero1 = int(numero1)
 numero2 = int(numero2)

 if numero1 > numero2:
    print('O número {} é maior'.format(numero1))
 else: 
    print('O número {} é maior'.format(numero2))



