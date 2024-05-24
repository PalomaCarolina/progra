import sys
sys.stdout
hombre = []
otro = []
def repeticion(lista,controlador=True,sangria=0, archivo=any):
    for x in lista:
        if isinstance(x,list):
            repeticion (x,controlador,sangria+1,archivo)
        else:
            if sangria:
                for Tab in range (sangria):
                    print("\t", end="",file=archivo)
                print(x,file=archivo) 
try: 
    info = open ("archivo.txt")
    for linea in info: 
        try: 
            (personaje, dialogo)=linea.split(':', 1)
            dialogo = dialogo.strip()
            if personaje == 'Hombre':
                hombre.append(dialogo)
            elif personaje == 'Otro hombre':
                 otro.append(dialogo)
        except ValueError: 
             pass 
    info.close() 
except IOError: 
    print ('Falta el archivo')
"""finally:
    print (hombre)
    print(otro)"""
#ejercicio escritura
try:
    sal = open('salida.txt', "w+")
    sal2 = open('salida2.txt', "a")
    repeticion(hombre,True,1,sal)
    repeticion(otro,True,1,sal2)
except IOError as error:
    print ('error de archivo:' + str(error) )
finally:
    sal.close()
    sal2.close()


                 