# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese tres palabras y arme un acrónimo con ellas
# Si desea puede modificar el código para ingresar más palabras
from platform import python_branch
from xml.dom.minidom import CharacterData, ReadOnlySequentialNamedNodeMap


print('Ingrese palabra 1:')
palabra_1 = str(input())

print('Ingrese palabra 2:')
palabra_2 = str(input())

print('Ingrese palabra 3:')
palabra_3 = str(input())

# De cada palabra debe tomar la primera letra y armar el acrónimo
# Ejemplo: Alumbrado, barrido y limpieza --> ABL
# Imprimir el resultado en pantalla

# se especifica con un indice con ":" --> inicio:final
# el intervalo va desde el inicio inclusive hasta
# el anterior al marcado con el final
sub_text_1= palabra_1[:1]  
sub_text_2=palabra_2[:1] 
sub_text_3=palabra_3[:1]
print(sub_text_1+sub_text_2+sub_text_3)#operamos la suma
# imprimimos en la consola la suma
suma= sub_text_1+sub_text_2+sub_text_3
print("el resultado de la suuma es",suma)

caracter_inicial_1= sub_text =palabra_1[:1]
caracter_inicial_2= sub_txet =palabra_2[:1]
caracter_inicial_3= sub_text =palabra_3[:1]
print(caracter_inicial_1,caracter_inicial_2,caracter_inicial_3) #operamos la suma
# imprimir en la consola la suma
suma = caracter_inicial_1+caracter_inicial_2+caracter_inicial_3 
print("el resultado de la suma es", suma)

