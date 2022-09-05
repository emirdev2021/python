#condicional if ejemplo 1

print("########### MAYOR O MENOR DE EDAD #########")

edad= input ("ingrese su edad: ")

if int(edad) > 17 : 
    print ("es mayor")
else: 
    print ("es menor de edad")

#ejemplo 2

print("\n########### ADIVINA COLOR #########")

color= input("adivina mi color favorito: ")
if color == "rojo": 
    print ("correcto")
else:
     print ("falso")


"""
#mas operadores algunos ya conocidos

== igual
!= diferente
< menor
> mayor
<= menor o igual que
>=mayor o igual 


#OPERADORES LOGICOS
and Y
or O
! Negacion
not NO

"""
#ejemplo 3

print("\n########### COMPROBANDO EL ANO #########")
year = 2022
year = int(input ("en que anio estamos?"))
if year >= 2022:
    print("estamos de 2022 en adelante") 
else :
    print("minimo estamos en 2021")   



print("\n########### USUARIO,EDAD,CONTINENTE #########")

nombre= "Emir Salem"
provincia="Buenos Aires"
continente= "Europa"
edad= 18
mayoria_edad= 18

if edad >= mayoria_edad:
    print (f"{nombre} es Mayor de edad")

    if continente != "America":
        print("el usuario no es americano")
    else:
        print(f"es americano y de {provincia}")
else:
    print (f"{nombre} NO es mayor de edad")


print("\n########### DIA DE LA SEMANA #########")

dia = int(input("Introduce el numero del dia de la semana"))

if dia == 1:
    print("es lunes")
elif dia == 2:
    print("es martes")
elif dia == 3:
    print("es miercoles")
elif dia == 4:
    print("es jueves")
elif dia == 5:
    print("es viernes")
else:
    print("es fin de semana bitch")

print("\n########### EDAD DE TRABAJAR (OPERADOR AND) #########")

edad_minima = 18
edad_maxima = 65
edad_oficial= int(input(" por favor ingrese su edad:"))

if edad_oficial >= edad_minima and edad_oficial < edad_maxima :
    print("Esta en edad de trabajar")
else:
    print("No esta en edad de trabajar si es menor denuncie trabajo infantil, si es mayor puede jubilarse si lo desea")


print("\n########### IDIOMA PAISES (OPERADOR OR) #########")

pais= input ("Indique de que pais es: ")

if pais == "Argentina" or pais== "Mexico" or pais == "Colombia":
    print(f"{pais} es HISPANO HABLANTE")
else:
    print(f"{pais} no es HISPANO HABLANTE ")

print("\n########### IDIOMA PAISES (OPERADOR NOT) #########")

pais= input ("Indique de que pais es: ")

if not (pais == "Argentina" or pais== "Mexico" or pais == "Colombia"):
    print(f"{pais} NO ES HISPANO HABLANTE")
else:
    print(f"{pais} es HISPANO HABLANTE ")


print("\n########### IDIOMA PAISES (OPERADOR NEGACION !=) #########")

country= input ("Indique de que pais es: ")

if country != "Argentina" and country!= "Mexico" and country != "Colombia":
    print(f"{country} NO ES HISPANO HABLANTE")
else:
    print(f"{country} es HISPANO HABLANTE =) ")




