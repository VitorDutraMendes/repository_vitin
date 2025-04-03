v= int(input('Informe o número que deseja calcular o Fatorial: '))
while v<=0:
    v= int (input('Número inválido, defina outro:'))
n=1
for i in range(v,-1,-1):
    if((i-v) != 0): n = n*(v-i)
    
print(f'O Fatorial de {v} é: {n}')