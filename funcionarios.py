def print():
  print("hola hola, este es un print")

print()

def suma():
  print("para sumar pides al usuario un numero")
  print("para eso necesitas un input()")
  suma1 = input("agrega el primer numero")
  suma2 = input("agrega el segundo numero")
  resultado = float(suma1 + suma2)
  print("la suma de esos numeros es", resultado)
  print("para multiplicar puedes usar ese numero y otro")
  mult = input("pon otro numero")
  multi = float(resultado*mult)
  print("la multiplicacion sería", multi)

suma()
