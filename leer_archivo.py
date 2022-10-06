archivo = open('prueba.txt','r') #r = read lee un archivo
# print(archivo.read())

# leer algunos caracteres
# print(archivo.read(5))
# print(archivo.read(3))


# leer lineas completas
# print(archivo.readline())
# print(archivo.readline())

#iterar el archivo
# for linea in archivo:
#     print(linea)


# leer lineas
# print(archivo.readlines()) # regresa una lista

# acceder a una linea de la lista
# print(archivo.readlines()[0]) #  accede al elemento indice 0 de la lista

# abrimos un nuevo archivo
# a - anexar informacion
archivo2 = open('copia.txt','a')
archivo2.write(archivo.read()) # archivo2 copia lo que leyo archivo.read()

archivo2.close()
archivo.close()



