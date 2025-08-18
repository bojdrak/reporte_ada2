import matplotlib.pyplot as plt

# Función que determina si un cuerpo está en equilibrio
def equilibrio(vectores):
    xSum, ySum, zSum = 0, 0, 0
    for x, y, z in vectores:
        xSum += x
        ySum += y
        zSum += z
    return xSum == 0 and ySum == 0 and zSum == 0

casos = [
    ([(4,1,7), (-2,4,-1), (1,-5,-3)], "NO"),  
    ([(3,-1,7), (-5,2,-4), (2,-1,-3)], "YES"), 
    ([(0,0,0)], "YES") 
]

print("Pruebas de código:\n")
for i in range(len(casos)):
    # 'entrada' es una lista de vectores, 'esperado' es un string que expresa el resultado deseado
    entrada, esperado = casos[i] 
    
    if equilibrio(entrada):
        salida = "YES"
    else:
        salida = "NO"
    
    print(f"Caso {i + 1}: Entrada={entrada}")
    print(f"Salida obtenida={salida}, Salida esperada={esperado}\n")

# Medir iteraciones para distintos tamaños de entrada
tamanos = list(range(1, 101))  # n de 1 a 100
iteraciones = []

for n in tamanos:
    vectores = [(0,0,0)] * n
    count = 0
    for v in vectores:
        count += 1
    iteraciones.append(count)

# Graficar
plt.plot(tamanos, iteraciones, marker='o')
plt.xlabel("Tamaño de entrada (n)")
plt.ylabel("Iteraciones del bucle")
plt.title("Iteraciones vs tamaño de entrada")
plt.grid(True)
plt.show()
