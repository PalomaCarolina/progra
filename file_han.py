try:
    archivo=open("archivo.txt")
    for linea in archivo:
        try:
            (personaje, dialogo)=linea.split(':')
            print (linea, end="")
            print(personaje, end='')
            print(' dijo: ', end='')
            print(dialogo, end="")
        except:
            pass
    archivo.close()
except:
    print("el archivo no se encuentra")
