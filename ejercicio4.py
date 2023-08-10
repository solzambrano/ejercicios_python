#Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor. Considerar el caso en que ambos números son iguales.
#los valores booleanos van con la primer letra en mayuscula
def compare_number(num_1,num_2):
    if(num_1>num_2):
        print('el primer numero es mayor')
    elif(num_1<num_2):
        print('el segundo numero es mayor')
    else :print('los dos numeros son iguales')


def input_Numbers():
    keep='S'
    try:
        while keep =='S':
            number_1= int(input('ingrese un numero: '))
            number_2= int(input('ingrese otro numero: '))
            compare_number(number_1,number_2)
            answer=input('quiere ingresar mas numeros (s/n)?').upper()
            # answer=answer.upper()
            print(answer)
            if answer!='S':
                keep='N'
            # if answer in ('N', 'S'): otra manera de comparar
            #     keep = False if answer == 'N' else True
            # else:
            #     print('Opcion incorrecta. finalizando programa...')
            #     keep=False
    except:
        print('debe ingresar numeros')

input_Numbers()
        