"""Haciendo uso de la función input en python usted es capaz de recibir textos
 (no son datos numéricos hay que transformarlos como en castle.py) por la consola
 y almacenarlos en variables con las cuales se pueden hacer diferentes tipos de
 operaciones; pida al usuario ingresar 2 números para realizar la operación.

 Nota: Tenga en cuenta que se pueden ingresar números enteros y flotantes;
 y que la función input siempre retorna un String; por lo cual puede ayudarse de
 .isdigit() que retorna True solo en caso de ser entero y false en caso de ser flotante.
,ejemplo: """

print("MI PRIMERA CALCULADORA")

#Recibiendo variables a operar
variable_number = input("Digite el primer número:") 
variable_number2 = input("Digite el segundo número:")

#Menú
print("Escoja entre: SUMA, RESTA, MULTIPLICACION, DIVISION, POTENCIACION y MODULO")

#Recibir operación
variable_escoger = input("Escoja la operación:")

#Pasar de texto a número
variable_number = float(variable_number)
variable_number2 = float(variable_number2)

if (variable_escoger == "SUMA" or variable_escoger == "+"):
   variable_resultado = variable_number + variable_number2

elif (variable_escoger == "RESTA" or variable_escoger == "-"):   
   variable_resultado = variable_number - variable_number2

elif (variable_escoger == "MULTIPLICACION" or variable_escoger == "*"):   
   variable_resultado = variable_number * variable_number2

elif (variable_escoger == "DIVISION" or variable_escoger == "/"):   
   variable_resultado = variable_number / variable_number2

elif (variable_escoger == "POTENCIACION" or variable_escoger == "**"):   
   variable_resultado = variable_number ** variable_number2

elif (variable_escoger == "MODULO" or variable_escoger == "%"):   
   variable_resultado = variable_number % variable_number2

else: 
   print("Operación no válida") 
   variable_resultado = False 

#Verdadero si es válida   o falso (no válido, null o False)
if (variable_resultado):

   print(f"El resultado es: {variable_resultado}")

   variable_other_operation = input("¿Deseas hacer una operación con el resultado? y/n")

   if ( variable_other_operation.lower() == ['y','yes'}):
      variable_escoger = input("Escoja la operación:")
   else:
      print('gracias por usar la calculadora')





  


   print(f"{variable_other_operation}")