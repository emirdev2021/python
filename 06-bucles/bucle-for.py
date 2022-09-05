#BUCLE FOR 
"""
FOR VARIABLE IN ELEMENTO_ITERABLE (LISTA,RANGO,ETC)
    BLOQUE INSTRUCCIONES

"""
contador= 0
resultado= 0
for contador in range(1,10):
    print("voy por el "+ str(contador))
    resultado += contador
    print(f"el resultado es: {resultado}")

#TABLA DE MULTIPLICAR
    print("\n##### ejemplo FOR ####")

numero_usuario = int(input("de que numero quieres ver la tabla?: "))
if numero_usuario < 1:
    numero_usuario = 1

print (f"### TABLA DEL {numero_usuario} ###")

for numero_tabla in range (1,11):
    print(f"{numero_usuario} X {numero_tabla} = {numero_usuario* numero_tabla}   ")