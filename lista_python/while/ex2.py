T=float(input('Forneça o capital Total para empréstimo: '))
c=float(input('Forneça o capital emprestado: '))
if(c>T):
    print(f'Empréstimo negado, capital total é de {T}')

else:
    while c<=T:
        m=float(input('Forneça a quantidade de meses para quitação:'))
        if c<=10000:
            t=0.1
        else:
            t=0.7
        
        j= c*t*m
        print(f'Taxa de juros aplicada: {t:.1f}%')
        print(f'Juros devido: {j}')
        print(f'Valor total: {j+c}')
        T= T-(j+c)
        if c<=T:
            c=float(input('Forneça o capital emprestado: '))
        else:
             print(f'Empréstimo negado, capital total é de {T}')
    