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

repeticion(frutas,True,0) 



