while True: 

 numero = input("Digite a senha:  ou SAIR ")
 if numero == 'SAIR':
  break
 
 numero = int(numero)
 senha = 1234

 if numero == senha:
  print('Senha correta! Acesso liberado.')
  break
 else:
  print('Senha errada. Tente novamente.')
  
