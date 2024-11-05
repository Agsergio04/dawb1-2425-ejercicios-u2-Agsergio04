def determinar_tipo(valor):
    tipo = None

    if 0 < valor < 0.4:
        tipo = "Inaceptable"
    if 0.4 < valor < 0.6:
        tipo = "Aceptable"
    if valor > 0.6:
        tipo = "Meritorio"

    return tipo 


def pedir_numero():
    return input("Introduce el valor: ")


def calcular_sueldo(valor):
    return 2400 * valor


def comprobar_valor(valor):
    return float(valor)


def main():
    bandera = True

    while bandera:
        
        numero = pedir_numero()

        if numero.lower() == "fin":
            break
           
        tipo = determinar_tipo(float(numero))
        sueldo = calcular_sueldo(float(numero))

        print(f"Tu tipo es {tipo} y tu sueldo es {sueldo} euros")

        if float(numero) < 0:
            raise ZeroDivisionError("**ERROR**\nIntroduce un numero positivo")
        if numero.lower() == "salir":
            bandera = False
        
        print("**ERROR**\nIntroduce un numero valido.")
        
        
        
if __name__ == "__main__":
    main()