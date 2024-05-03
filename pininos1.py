obrasCine=["peli1",1111,"peli2",1112,"peli3",1113,["subpeli1",1121,"subpeli2",1122,"subpeli3",1123,["subsubpeli1",1221,"subsubpeli2",1222,"subsubpeli3",1223],"subpeli4",1124,"subpeli5",1125],"peli5",1115,"peli6",1116]

for x in obrasCine:
    if isinstance(x,list):
        for y in x:
            if isinstance(y,list):
                for z in y:
                    print (z)
            else:
                print (y)
    else:
        print (x)
        obrasCine=["peli1",1111,"peli2",1112,"peli3",1113,["subpeli1",1121,"subpeli2",1122,"subpeli3",1123,["subsubpeli1",1221,"subsubpeli2",1222,"subsubpeli3",1223],"subpeli4",1124,"subpeli5",1125],"peli5",1115,"peli6",1116]

def repeticion(obrasCine):
    for x in obrasCine:
        if isinstance(x,list):
            for y in x:
                if isinstance(y,list):
                    for z in y:
                        print (z)
                else:
                    print (y)
        else:
            print (x)
                
repeticion(obrasCine)