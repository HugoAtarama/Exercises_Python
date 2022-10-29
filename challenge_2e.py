"""
5)Escribir un programa que almacene el diccionario con 
los créditos de las asignaturas de un curso 
{'Matemáticas': 6, 'Física': 4, 'Química': 5} y 
después muestre por pantalla los créditos de cada 
asignatura en el formato <asignatura> tiene <créditos> créditos,
donde <asignatura> es cada una de las asignaturas del curso,
y <créditos> son sus créditos. Al final debe mostrar también
el número total de créditos del curso.
"""
from multiprocessing.sharedctypes import Value


myDiccionario = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
sumaCreditos = 0
for key, value in myDiccionario.items():
    print('Asignatura '+str(key)+' tiene '+str(value)+' creditos')
    sumaCreditos += value
print('Total creditos: '+str(sumaCreditos))