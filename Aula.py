# 1. A implementação do algoritmo K-Means vista em aula somente permite que as médias finais
# sejam visualizadas. Ajuste o algoritmo para que todos os elementos de cada grupo sejam
# armazenados em uma estrutura de dados apropriada. Adicione uma função à classe que exibe a
# coleção.

from collections import defaultdict

#multiplica um vetor por um escalar
def scalar_multiply (escalar, vetor):
    return [escalar * i for i in vetor]

#soma n vetores
def vector_sum (vetores):
    resultado = vetores[0]
    for vetor in vetores[1:]:
        resultado = [resultado[i] + vetor[i] for i in range(len(vetor))]
    return resultado

#calcula a média de n vetores
def vector_mean (vetores):
    return scalar_multiply(1/len(vetores), vector_sum(vetores))

#produto escalar
def dot (v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

#subtração de vetores
def vector_subtract (v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]

#soma dos quadrados
def sum_of_squares(v):
    return dot(v, v)

#distância ao quadrado
def squared_distance (v, w):
    return sum_of_squares(vector_subtract(v, w))


class KMeans:
    def __init__ (self, k, means = None):
        self.k = k
        self.means = means
        self.result = defaultdict(list)
    
    def classify (self, ponto):
        return min (range (self.k), key = lambda i: squared_distance(ponto, self.means[i]))
    
    def train (self, pontos):
        #escolha de k elementos
        #self.means = random,sample (pontos, self.k)
        #nenhuma atribuição para começar
        assignments = None
        while True:
            #associa cada instância a um inteiro 0 <= i < k
            new_assignments = list(map(self.classify, pontos))
            #se não houver mudança, termina
            if new_assignments == assignments:
                self.salvaResultado(new_assignments, pontos)
                return
            #atribuição atual se torna a nova
            assignments = new_assignments
            #cálculo das novas médias
            for i in range (self.k):
                #pontos associados ao agrupamento i
                #note que pontos e assignments estão na ordem
                #por exemplo pontos = [1, 2, 3] e assignments = [1, 2, 2]
                #indicam que a primeira instância está no grupo 1 e as demais
                #no grupo 2
                i_points = [p for p, a in zip (pontos, assignments) if a == i]
                #tem alguém nesse grupo?
                if i_points:
                    self.means[i] = vector_mean (i_points)
    
    def salvaResultado (self, vector1, vector2):
        lista = [(x, y) for x, y in zip (vector1, [n[0] for n in vector2])]
        l2 = [(a[0], b) for a, b in zip(self.means, set(vector1))]
        for i, j in lista:
            for x, y in l2:
                if i == y:
                    self.result[x].append(j)

    def mostraResultado (self):
        print(f'Resultado: {self.result}')

    
def test_k_means():
    dados = [[1], [3], [6], [7], [10], [11]]
    kmeans = KMeans(3, [[1], [3], [11]])
    kmeans.train(dados)
    print (kmeans.means)
    kmeans.mostraResultado()

test_k_means()