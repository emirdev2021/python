######### TIPOS DE DATOS

#NONETYPE
nada=None
#STR
cadenaString="hola aca aprendiendo python"
#INT
nroEntero= 10
#FLOAT
nroFlotante=10.2
#BOOL
booleanos= False
#LIST
arrays=[1,2,3,4,5, "array tipico"]
#TUPLE (lista que no cambia)
tuplaNocambia=("array","tupla")

#DICT SIMILAR A OBJETOS EN JS CON PAR VALOR CLAVE
diccionarios={
    "nombre":"Emir",
    "apellido":"Salem",
    "edad" : 30
}
#RANGE 
rango= range(9)
#BYTE
dato_byte=b"probando"

#MOSTRAR TIPO DE DATO Funcion Type
print(type(nada))
print(nada)
print(type(cadenaString))
print(cadenaString)
print(type(nroEntero))
print(nroEntero)
print(type(nroFlotante))
print(nroFlotante)
print(type(booleanos))
print(booleanos)
print(type(arrays))
print(arrays)
print(type(tuplaNocambia))
print(tuplaNocambia)
print(type(diccionarios))
print(diccionarios)
print(type(rango))
print(rango)
print(type(dato_byte))
print(dato_byte)

#CONVERTIR TIPOS DE DATOS
texto="convirtiendo de nro a string para concatenar con la funcion STR"
numerito= 2022   
# ESTO DARIA ERROR
#print(texto + numerito)
#PONER COMO PREFIJO EL TIPO DE DATO AL QUE SE DESEA CONVERTIR EJEMPLO NUMERO=FLOAT(125)
texto="convirtiendo de nro a string para concatenar con la funcion STR"
numerito= str(2022)   
print(f"{texto} {numerito}")
num= 99
print(type(num))
print(num)
num = float(99)
print (type(num))
print (num)
