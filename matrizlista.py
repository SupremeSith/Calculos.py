#valores do enunciado 
valores = [3,1,4,6,2,5]

#matriz da lista
matriz = {}

#formação do tamanho da matriz 
for i in range(4):
    for v in range(4):
        matriz[(i, v)] =0 

#valores e posições iniciais da matriz 
matriz[( 3, 1)] = valores[0]

matriz[(1, 2)] = valores[ 1]

matriz[(0, 0)] = valores[2]

matriz[(0, 3)] = valores[3]

matriz [(2, 2 )] = valores[4]

matriz [(3, 3)] = valores[5]

#determinação de valores da matriz
for i in range(4):

#print dos valores + posições iniciais da matriz
    for v in range(4):

        print(matriz[(i, v)], end="")
        print()