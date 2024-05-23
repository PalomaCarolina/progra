frutas=["manzana",1, "moras",2, "platano",3, ["golden",11, "fresa",21, "dominico",31,["amarillo",12, "rojo",22, "amarilloynegro",32,],"sangria",41, "chino",51],"naranja",4, "Kiwi",5]


def repeticion(frutas,controlador=True,sangria=0):
    for x in frutas:
        if isinstance(x,list):
            repeticion (x,controlador,sangria+1)
        else:
            if controlador:
                for Tab in range (sangria):
                    print("\t", end="")
                print(x)            


def recursiva(frutas,sangria=0):
    for x in frutas:
        if isinstance(x,list):
            recursiva(x,sangria+1)
        else:
            for Tab in range(sangria):
                print("\t",end="")
            print(x)

def imprimelista(frutas):
    for x in frutas:
        if isinstance(x,list):
            imprimelista(x,)
        else:
            for Tab in range():
                print("\t",end="")
            print(x)

recursiva(frutas,0)
recursiva(frutas,5)
repeticion(frutas,True,0)
repeticion(frutas,false,0)
imprimelista(frutas)


