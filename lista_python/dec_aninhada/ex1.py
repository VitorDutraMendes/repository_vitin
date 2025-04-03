p=float(input('Digite seu peso (em kg): '))
a=float(input('Digite sua altura (em metros): '))
s=(input('Seu sexo é masculino (M) ou feminino (F)? '))
imc= p/(a*a)
if s== 'M' or s== 'm':
    if imc <= 25:
        print('Você não precisa perder peso para ter IMC <= 25 ')
    else :
        print(f'Você deve perder {p-(25*(a*a)):.2f} para ter IMC = 25')
elif s == 'f' or s== 'F':
    if imc <= 24:
        print('Você não precisa perder peso para ter IMC <= 24')
    else:
        print(f'Você deve perder {p-(24*(a*a)):.2f} para ter IMC = 24')
else:
    print('A entrada contém dados não reconhecidos')
        
        

    
    