#UTILIZANDO PYTHON3

#utilizando as relações de girard, tendo n raizes do polinomio, sabemos que:
#o termo independente do polinomio é a0 = RAIZn * RAIZn-1 * ... RAIZ0 se o an for 1
#ou seja, a multiplicação das raizes é igual ao termo independente para an = 1

import numpy as np

n = int(input("Input the number of roots: "))

listRoots = []
for i in range(0,n):
    print("Insert your","{0}st root:".format(i), end = '')
    listRoots.append(float(input()))

print("The roots of polynomial are: ", listRoots)

#multiplica todos os termos da "listRoots", ou seja, todas as raizes

if n%2 == 0:
    independentTerm = np.prod(listRoots)
else:
    independentTerm = (-1)*np.prod(listRoots)
#sabendo que as raizes de um polinomio sao valores de x que resultam em 0
#podemos fazer o seguinte: depois de obter o valor do termo independente
#"passar" ele para o outro lado da igualdade e com isso criar um sistema de equações lineares
#para cada valor da raiz avera uma equação, assim, é possível utilizar uma matriz para resolver

matrix = np.zeros(shape=(n, n), dtype=float)

col = 0

for i in listRoots:
    for j in range(0,n):
        matrix[col][j] = (i**(n-j))
    col = col+1


#colunaB é a coluna q multiplicara a matriz 
colB = []
for i in range(0,n):
    colB = np.insert(colB, i, (-1)*independentTerm)

#resolvendo o sistema de equações lineares a partir das matrizes:

result = np.linalg.solve(matrix, colB)
print("The coefficients of polynomial are: ", end = '')
print(result)

result = np.append(result, [independentTerm])

p = np.poly1d(result)
print(p)