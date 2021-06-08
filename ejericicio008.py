"""
STRING y mas!!!
"""
esto_es_una_string= "Hola"
esto_es_otra_string= "Mundo"

#concatenar
print (esto_es_una_string + ' '+  esto_es_otra_string) #CADENA REFERENCIAL + CADENA LITERAL + CADENA REFERENCIAL
#Hola Mundo

#MAYUS
print(esto_es_una_string.upper()) #upper es mayuscula 
print(esto_es_una_string.lower()) #lower es la minuscula 
print(esto_es_una_string.capitalize()) #capitaliza la primera letra
print (esto_es_una_string.title())
print(len(esto_es_una_string))


#Busca un caracter y muestra su ubicacion
print(esto_es_una_string.find('a'))
#rebanar
print(esto_es_una_string[0:2])
#palindroma
print(esto_es_una_string[::-1])

