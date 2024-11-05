"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no
"""

def comprobar_edad(edad):
    condicion = None

    edad = int(edad)
    
    if edad < 18 :
        condicion = False
    elif 0 < edad < 18:
        condicion = True
  
    return condicion
   
    
def main():
    
    edad = int(input("Introduce tu edad: "))

    if comprobar_edad(edad) == True:
        print("Eres mayor de edad.")
    elif comprobar_edad(edad) == False:
        print("Eres menor de edad.")
    else:
        print("*ERROR* Introduce un numero.")
if  __name__ == "__main__":
    main()