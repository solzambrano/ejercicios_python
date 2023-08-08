#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
def parity(num):
    if(num%2==0):
        print('el numero es par')
    else:
        print('el numero ingresado es impar')

def inputNumber():
    try:
        number=int(input('ingrese un numero')) # si ingreso 15.0 al poner int delante del input ignora el decimal
        parity(number)
    except:
        print('debe ingresar un numero')

inputNumber()