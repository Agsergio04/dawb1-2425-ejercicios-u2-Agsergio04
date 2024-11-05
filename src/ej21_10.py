def decision():
    return input("Quieres una pizza vegetariana o no(S/N): ")


def pedir_ingredientes():
    primero = input("Elige un primer ingrediente: ")
    segundo = input("Elige un segun ingrediente: ")

    return primero,segundo

def comprobar_ingrediente(decision):
    comprobacion = False
    if (decision == "pimiento") or \
        (decision == "tofu") or \
        (decision == "peperoni") or \
        (decision == "jamon") or \
        (decision == "salmon"):
            comprobacion = True

    return comprobacion


def main():
    bandera = True
    while bandera:
         
        entrada = decision()

        if entrada.lower() == 's':
            entrada = "pizza vegetariana"
            print("Ingredientes vegetarianos: Pimiento y Tofu")

            ingrediente_primero,ingrediente_segundo = pedir_ingredientes()

            if comprobar_ingrediente(ingrediente_primero) and comprobar_ingrediente(ingrediente_segundo):
                print(f"Tu {entrada} lleva Mozzarella,Tomate,{ingrediente_primero},{ingrediente_segundo} ")
                entrada = input("¿Desea pedir otra?(Si no escriba  'salir'): ").lower()

            else:
                print("**ERROR**\nVuelva a Introducir la pizza de nuevo")

        elif entrada.lower() == 'n':
            entrada = "pizza no vegetariana"
            print("Ingredientes no vegetarianos: Peperoni, Jamon y Salmon")

            ingrediente_primero,ingrediente_segundo = pedir_ingredientes()

            if comprobar_ingrediente(ingrediente_primero) and comprobar_ingrediente(ingrediente_segundo):
                print(f"Tu {entrada} lleva Mozzarella,Tomate,{ingrediente_primero},{ingrediente_segundo} ")
                entrada = input("¿Desea pedir otra?(Si no escriba  'salir'): ").lower()

            else:
                print("**ERROR**\nVuelva a Introducir la pizza de nuevo")
        else:
            print("Por favor introduzca s o n (si quiere salir ponga salir)")
                
        if entrada.lower() ==  "salir":
            bandera = False
             
if __name__ == "__main__":
    main()