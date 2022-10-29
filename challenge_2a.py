"""
1) Escribir un programa que guarde en una variable el 
diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
pregunte al usuario por una divisa y muestre su símbolo 
o un mensaje de aviso si la divisa no está en el diccionario.
"""
divisa = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
valorDivisa = input("Ingrese una divisa: ")
#recorrer un diciconario con sus llaves
if valorDivisa in divisa:
    for key, value in divisa.items():
        if valorDivisa == key:
            print('Su simbolo es: '+ value)
else:
    print('Divisa no encontrada')




