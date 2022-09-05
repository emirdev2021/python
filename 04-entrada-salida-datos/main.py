#entrada
nombre= input("cual es tu nombre?")
edad= input("cual es tu edad?")
#salida
print(f"bienvenido {nombre} veo que tenes {int(edad)} primaveras") #se convierte el string edad en entero para sumarle un numero

print("\n##### birth year ####")
birth_year= input("birth year:")
age= 2022 - int(birth_year)
print(age)
print("*" * 10)
