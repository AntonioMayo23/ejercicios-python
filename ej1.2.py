'''1.2. Realizar un programa que sea capaz de convertir los grados
centígrados en grados Farenheit y viceversa
'''
grados = 0
farenheit = 0
grados = float(input("Dime los grados: "))
farenheit = 1.8 * grados + 32
print("Los grados en farenheit son: ", farenheit)

farenheit = float(input("Dime los farenheit: "))
grados = (farenheit - 32) / 1.8
print("Los farenheit en grados son: ", grados)