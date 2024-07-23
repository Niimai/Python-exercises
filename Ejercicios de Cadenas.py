# Ejercicio 1 - Escribir un programa que pregunte el nombre del usuario en la consola y un número entero 
# e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

nombre = input("¿Cómo te llamas? ")
n = input("Introduce un número entero: ")
print((nombre + "\n") * int(n))

# Ejercicio 2 - Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre 
# por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las 
# letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede 
# introducir su nombre combinando mayúsculas y minúsculas como quiera.