votc1=0
votc2=0
votinv=0
votoval=0
votoinval=0
perc1=0
perc2=0
percinv=0
votostotal=0
percval=0

cand1=input('Forneça o nome do candidato 1: ')
nc1=int(input('Forneça o número do candidato 1: '))
cand2=input('Forneça o nome do candidato 2: ')
nc2=int(input('Forneça o número do candidato 2: '))
elt=int(input(' Forneça a quantidade de eleitores: '))
while elt<3:
    print('quantidade de eleitores inferior a 3')
    elt=int(input(' Forneça a quantidade de eleitores: '))

print('## Votacao iniciada')
for i in range(elt):
    voto=int(input('Forneça o número do candidato que deseja votar: '))
    if voto== nc1:
        votoval+=1
        votc1+=1

    elif voto==nc2:
        votoval+=1
        votc2+=1

    else:
        votoinval+=1

    votostotal+=1



perc1=(votc1/votoval)*100
perc2=(votc2/votoval)*100
percval=(votoval/votostotal)*100
percinv=(votoinval/votostotal)*100
  

print(f'votos para cand1={perc1:.2f}% ({votc1}votos)')
print(f'votos para cand2={perc2:.2f}% ({votc2}votos)')
print(f'votos validos:{percval:.2f}% ({votoval}votos)')
print(f'votos invalidos:{percinv:.2f}% ({votoinval}votos)')
    
    

    