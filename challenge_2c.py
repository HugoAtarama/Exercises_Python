"""
3)Escribir un programa que pregunte por una muestra de 
números, separados por comas, los guarde en una lista y 
muestre por pantalla su media.
"""
myMuestra = []
numeroMuestra = int(input('Cuantos numeros desea ingresar? '))
for i in range(0,numeroMuestra):
    valor = float(input('ingrese una muestra de numeros: '))
    myMuestra.append(valor)
valorSuma = sum(myMuestra)
lenMuestra = len(myMuestra)
promedio = valorSuma/lenMuestra
print('El promedio es', promedio)
