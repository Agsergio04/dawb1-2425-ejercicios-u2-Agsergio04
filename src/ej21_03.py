def division_numero(primer_numero,segundo_numero):
    resultado  = 0
    
    numerador,denominador = primer_numero,segundo_numero
    
    resultado = numerador / denominador
    
    return resultado

def main():
    bandera = True
    while bandera:
        
        primer_numero = int(input("Introduce un numero: "))
        segundo_numero = int(input("Introduce otro numero: "))
            
        
        
        if segundo_numero == 0:
            print("**ERROR**\nNo puedes dividir por 0.")
            
        if segundo_numero != 0:
            resultado = division_numero(primer_numero,segundo_numero)
            bandera = False
        
    print(f"El resultado de dividir {primer_numero:.2f} entre {segundo_numero:.2f} es {resultado:.2f}")

if __name__ == "__main__":
    main()