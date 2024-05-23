try:
    archivo=open("alumnos posgrado.txt")
    for linea in archivo:
        try:
            (alumno, matricula, posgrado)=linea.split('-')
            print (linea, end="")
            print(' Alumno: ', end='')
            print(alumno, end='')
            print(' Matricula: ', end='')
            print(matricula, end="")
            print(' Posgrado: ', end='')
            print(posgrado, end="")

        except:
            pass
    archivo.close()
except:
    print("el archivo no se encuentra")

    try:
    archivo=open("alumnos posgrados.txt")
    for linea in archivo:
        try:
            (alumno, matricula, posgrado)=linea.split('-')
            print (linea, end="")
            print(' Alumno: ', end='')
            print(alumno, end='')
            print(' Matricula: ', end='')
            print(matricula, end="")
            print(' Posgrado: ', end='')
            print(posgrado, end="")

        except:
            pass
    archivo.close()
except:
    print("el archivo no se encuentra")
