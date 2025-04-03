import math
ladri=int(input('Forneça o tipo de ladrilho (1 ou 2): '))
area=float(input(' Forneça a área da sala: '))
if ladri==1: 
    print(f' Quantidade de ladrilhos:{ math.ceil(area/80)}')
else:
    print(f' Quantidade de ladrilhos:{ math.ceil(area/60)}')

