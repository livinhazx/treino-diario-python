
def ler_numero():
  valor = input("Digite um número: (ou sair) ")

  if valor.lower == 'sair':
   return None
  
  return int(valor)
 
while True:
 
 numero1 = ler_numero()

 if numero1 is None:
  break 
 
 numero2 = ler_numero()

 if numero2 is None:
  break 
 
 operacao = int(input("1 Soma | 2 Sub | 3 Mult | 4 Div: "))



 soma = numero1 + numero2
 sub = numero1 - numero2
 mult = numero1 * numero2
 div = numero1 / numero2


 if operacao == 1:
  print('O resultado da soma é {}.'.format(soma))
 elif operacao == 2:
  print('O resultado da subtração é {}.'.format(sub))
 elif operacao == 3:
  print('O resultado da multiplicação é {}.'.format(mult))
 elif operacao == 4:
  if  numero2 == 0:
   print('Não existe divisão por 0. ')
  else:
   print('O resultado da divisão é {}.'.format(div)) 
 else:
  print('Operação inválida.')
  

