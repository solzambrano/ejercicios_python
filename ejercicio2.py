#Escribir un programa que pida al usuario dos números y devuelva su división. Si el usuario no introduce números debe devolver un aviso de error y si el divisor es cero también.

def division (dividendo,divisor):
    if(divisor!=0):
       # print(dividendo/divisor) division real pone un punto despues del entero
        print(dividendo//divisor)  #division entera
    else:
        print('el divisor debe ser distnto de 0')

def inputUser():
    try:
        dividendo=int(input('ingrese el dividendo'))
        divisor=int(input('ingrese el divisor'))
        division(dividendo,divisor)
    except: print('debe ingresar numeros')

inputUser()

