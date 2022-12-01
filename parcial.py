import random

# Dimensiones de la matriz
m = int(input("No. de filas de la Matriz: "))
n = m

# Creación de la matriz
M = []

for i in range(m):
  M.append([])
  for j in range(n):
    M[i].append(random.randint(1,9))

# Mostrar matriz
for k in range(m):
  print()
  for j in range(n):
    print(M[k][j], end= "\t")
