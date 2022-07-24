# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese primero su nombre y luego su apellido
# Capture ambos datos e imprima su nombre completo
print('Ingrese por consola su nombre/s:')
nombre = str(input())

print('Ingrese por consola su apellido/s:')
apellido = str(input())

# Imprima su nombre completo

# Almacenar su nombre completo en una variable
# nombre_completo = .....

# Imprimir la cantidad de letras que posee su nombre completo
# cantidad_letras = len(....)

#nombre de la persona a evaluar
nombre_completo = nombre + "" + apellido 
nombre_completo_len = len(nombre_completo)
print(nombre_completo , "tiene" , nombre_completo_len , "caracteres") 

#el carcter inicial , el indice siempre empieza con [0]
caracter_inicial = nombre_completo [0]
print(caracter_inicial)

# accedo al cararter final , si la palabra tiene 12 letras ,
#el indice de la letra final sera 11
caracter_final = nombre_completo [11]
caracter_final = nombre_completo [nombre_completo_len -1] # len=12, len=-1 =11
caracter_final = nombre_completo [-1] # indice negativo recorre la lista al reves
print =(caracter_final)


# puedo acceder a todos los caracteres indibidualmente
print(nombre_completo[0],nombre_completo[1],nombre_completo[2],
nombre_completo[3],nombre_completo[4]
)
# puedes acceder a una serie de caracteres todos juntos 
# se especifica el intervalo de indices con ":" inicial:final
# El intervalo va desde le inicial inclusive hasta
# el anterior al marcado como el final
sub_text = nombre_completo [0:5] # obtendras los primeros caracteres
sub_text = nombre_completo[:5]   # obtendras los primeros caracteres 


sub_text = nombre_completo[1:9] # obtendras desde el segundo caracter hasta el 8


#obtendras desde el segundo caracter hasta el final
sub_text = nombre_completo[1:nombre_completo_len]
# obtendras desde el segundo caracter hasta el final
sub_text = nombre_completo[1:len(nombre_completo)]
# obtendras desde el segundo caracter hasta el final
sub_text = nombre_completo [1:] 
print(sub_text)

