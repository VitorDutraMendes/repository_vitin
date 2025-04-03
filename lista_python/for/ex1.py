juiz=input('Informe o nome do juiz: ')
p=int(input('Informe a quantidade de partidas: '))
Ifim=0
Ffim=0
Cfim=0 
Tfim =0
for i in range(1,p+1):
    print(f'patida {i}')
    I=int(input('Informe impedimentos.......: '))
    F=int(input('Informe faltas.............: '))
    C=int(input('Informe cartões............: '))
    T=float(input('Informe tempo de acréscimo.: '))
    Ifim+=I
    Ffim+=F
    Cfim+=C
    Tfim+=T

print()
print(f' Estatísticas do {juiz}: ')
print(f' Impedimentos.......: {(Ifim/p):.2f}')
print(f' Faltas.............: {(Ffim/p):.2f}')
print(f' Cartões............: {(Cfim/p):.2f}')
print(f' Tempo de acréscimo.: {(Tfim/p):.2f}')


