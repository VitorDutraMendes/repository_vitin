
import math
def F(x,y):  
    if 10<=x and x<=20:
        z= (x**2) + (y**3)
        return z
    elif x>20 and x<=40:
        z= math.sin(x) + math.cos(2*y)
        return z
    elif x>40 and x<=60:
        z= (x*y)/(x+y)
        return z
    else:
        z= 0
        return z
def main():
    vx=float(input('valor de x: '))
    while vx <10 or vx>60:
        print(f'Valor invalido: {vx:.3f}')
        vx=float(input('valor de x: '))

    vy=float(input("valor de y: "))
    z=F(vx,vy)   

    print(f'valor de x: {vx:.3f}')
    print(f'valor de y: {vy:.3f}')
    print(f'F({vx,vy}) = {z:.3f}')



if __name__=="__main__":
    main()
    
