def definir_genero(entrada):
    genero = None
    
    if entrada.lower() == "hombre":
        genero = "hombre"
    elif entrada.lower() == "mujer":
        genero = "mujer"
    
    return genero
def elegir_aula(entrada,genero):
    aula = "B"
    letra_nombre = entrada[0]
    
    if letra_nombre.upper() < "M" and genero == "mujer":  
        aula = "A"
    elif letra_nombre.upper() > "N" and genero == "hombre":
        aula = "A"
        
    return aula
def main():
    try:
        nombre = input("Introduce tu nombre: ")
        sexo = input("Introduce tu genero (hombre/mujer): ")
        
        genero = definir_genero(sexo)
        
        if genero == None:
            raise ValueError("**ERROR**\nPor favor Introduce un genero Valido.")
        
        aula = elegir_aula(nombre,genero) 
        
    except ValueError:
        print("Introduce un genero valido")
    else:
        print(f"{nombre} eres del aula {aula}")
if __name__ == main():
    main()