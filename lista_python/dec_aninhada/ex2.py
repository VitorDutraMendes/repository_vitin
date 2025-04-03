import math
def switch(n,l):
    opcao = {
        3 : f'O polígono é um triângulo com área: {(((l**2)*math.sqrt(3))/4):.2f}' ,
        4 : f'O polígono é um quadrado com área: {(l**2):.2f}',
        5 : f'O polígono é um pentágono com área: {((5*l**2)/(4*math.tan(0.6283))):.2f}',
        6 : f'O polígono é um hexágono com área: {((3*(l**2)* math.sqrt(3))/2):.2f}'
        }
    return opcao.get(n, 'Não é pooligono')

if __name__ == '__main__':
    q = int(input('Digite a quantidade de lados: '))
    if q < 3:
        print('Não é um polígono')
    elif q > 6:
        print('Polígono não identificado')
    else:
        l = float(input('Digite a medida do lado: '))
        print(f'{switch(q,l)}')
        