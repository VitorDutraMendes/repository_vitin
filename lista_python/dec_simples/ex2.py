import math
n = input('Entre com o nome: ')
i = float(input('Entre com a idade: '))
s = input('Entre com o sexo (m ou f): ')
if (s == 'm') :
    if(i < 18) :
        print(f'Faltam {(18-i):.1f} anos para {n} a maioridade')
    else:
      print(f'{n} tem maioridade civil')  
else :
    if(i < 21) :
        print(f'Faltam {(21-i):.1f} anos para {n} a maioridade')
    else:
      print(f'{n} tem maioridade civil') 

