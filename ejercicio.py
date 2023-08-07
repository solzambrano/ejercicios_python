# Escribir un programa que pregunte la edad y muestr por pantalla si es mayor de edad o no
# def inputData () :
#     answer=input('ingrese su edad')
#     if(answer > '18'):
#         print('es mayor de edad')
#     else:
#         print('no es mayor de edad')

# inputData()

#las entradas siempre son ingresadas como string, para poder comparar string con entero necesito que sean del mismo tipo
def inputData () :
    try:
        answer=int(input('ingrese su edad')) 
        print(answer)
        if(answer > 18):
            print('es mayor de edad')
        else:
            print('no es mayor de edad')
    except:
        print('debe ingresar un valor numerico')

inputData()


