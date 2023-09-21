# primer-parcial_plc
def suma(a,b):
  x = a + b
  return x

def resta(a,b):
  x = a - b
  return x

print("dame el primer numero:")
a = int(input())
print("dame el segundo numero")
b = int(input())
print("la suma da", suma(a,b), "y la resta da", resta(a,b))
suma()
resta()

def multiplicación(a,b):
x = (a * b)
 return x

def division(a,b):
  x = (a/b)
  return x
  
print("dame el primer numero:")
a = int(input())
print("dame el segundo numero")
b = int(input())
print("la multiplicacion da", multiplicación(a,b), "y la división da", division(a,b))
multiplicación()
division()
