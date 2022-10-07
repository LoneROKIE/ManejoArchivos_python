from Manejo_archivos import ManejoArchivos

# context manager con el uso de with se abre y se cierra de forma
# automatica el archivo

# with open('prueba.txt','r',encoding='utf-8') as archivo:
#     print(archivo.read())


with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())