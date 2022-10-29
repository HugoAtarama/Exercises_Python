
"""
2)Escribir un programa que almacene las asignaturas de 
un curso (por ejemplo Matemáticas, Física, Química, 
Historia y Lengua) en una lista, pregunte al 
usuario la nota que ha sacado en cada asignatura y elimine 
de la lista las asignaturas aprobadas. Al final el programa 
debe mostrar por pantalla las asignaturas que el usuario 
tiene que repetir.
"""
myList = ['Matemáticas','Física','Química','Historia','Lengua']
myNotas = []
myDesaprobadas = []
for i in myList:
    print(i)
    nota = float(input('Ingresar nota: '))
    myNotas.append((nota))
#print(list(myTuple))
for i in range(0,len(myList)-2,+1):
    if myNotas[i] < 10.5:
       myDesaprobadas.append((myList[i]))
#imprimir asignaturas a repetir
for i in myDesaprobadas:
    print('Asignatura a repetir: '+i)
