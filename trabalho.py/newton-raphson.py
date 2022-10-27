import math

def f(x):
    #COLOQUE A SUA FUNÇÃO dentro do () !
    return((+ 0.0001*x**8 - 0.0069*x**7 + 0.2543*x**6 - 5.8339*x**5 + 85.0726*x**4 - 777.5254*x**3 + 4187.4718*x**2 -11412.8955*x + 10099.2379)-2.1) 
def df(x):
    h = 0.000001
    return((f(x + h) - f(x))/h )

tol = 0.000001  
xmax = 100   
x0 = float (input("x inicial: "))   
x = 0

i = 1
while(math.fabs(f(x0)) > tol ):   #calcula o valor absoluto da função para que ele nao seja maior que a tol
    x = x0 - f(x0)/df(x0)       #formula NEWTON-RAPHSON
    x0 = x                          
    i = i + 1                       
    if(i >= xmax):
        print ("Não foi possivel encontrar a raiz!")
        break
    if (i < xmax):
        print("Raíz: %f"%(x0))
        print("Interações: %i"%(i))
        print("f(%f) = %f\n"%(x0,f(x0)))
        
        






