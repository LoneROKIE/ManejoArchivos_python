
# es comun que el manejo de archivos este dentro de un bloque try catch
try:

    archivo = open('prueba.txt','w') # si no existe el archivo entonces se crea, 'w' = write nos permite modficar el archiv
    archivo.write('agregamos informacion al archivo') # write metodo para escribir info en el archivo
    archivo.write('\nadios')
except Exception as e:
    print(e)
finally:
   archivo.close()
   print('Fin del archivo')
# despues de cerrado logicamento ya no podemos trabajar con el archivo