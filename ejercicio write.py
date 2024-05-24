try:
    salida = open("archivo.txt", "w")
    salida2 = open("archivo.txt", "w")
    print(hombre,salida)
    print(otro,salida2)
except IOError:
    print ('error de archivo:' + str(error) )
finally:
    salida.close()
    salida.close()