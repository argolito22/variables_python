# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese dos palabras y arme combinaciones con ella
print('Ingrese palabra 1:')
palabra_1 = str(input())

print('Ingrese palabra 2:')
palabra_2 = str(input())

# De la primera palabra tome las primeras tres letras, utilice el operador :
# De la segunda palabra tome las primeras dos letras, utilice el operador :
# Formar una nueva palabra con los recortes solicitados
# Imprima en pantalla los resultados

# se especifica con un indice con ":" --> inicio:final
# el intervalo va desde el inicio inclusive hasta
# el anterior marcado con el final
sub_text_1= palabra_1[0:3]
sub_text_2= palabra_2[0:2]
print(sub_text_1+sub_text_2) # operamos la suma 
# imprimimos en la pantalla la suma
suma= sub_text_1+sub_text_2
print("el rersultado de la suma es", suma)
