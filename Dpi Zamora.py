dpi=(input("ingrese dpi"))
if len(dpi)==13:
    print("dpi correcto")
    print("para presidente puedes votar por partido rojo o partido cafe")
    presidente=input("ingrese su voto: ")
    if presidente=="partido rojo":
        print("voto para partido rojo")
    elif presidente=="partido cafe":
        print("voto para partido cafe")
    else:
        print("voto nulo")    
               
    print("para alcalde puedes votar por partido verde, partido amarillo, partido azul o partido morado")
    alcalde=input("ingrese su voto: ")
    if alcalde=="partido verde":
        print("voto para partido verde")
    elif alcalde=="partido amarillo": 
        print("voto para partido amarillo")
    elif alcalde=="partido azul": 
        print("voto para partido azul")
    elif alcalde=="partido morado": 
        print("voto para partido morado")
    else:
        print("voto nulo")    

    print("por alcalde voto",alcalde)
    print("por presidente voto",presidente)
     


    