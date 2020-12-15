import pandas as pd
from collections import defaultdict

class Graph():

    def __init__(self, vertices):

        self.graph = defaultdict(list)

        self.V = vertices

  

    def addEdge(self, u, v):

        self.graph[u].append(v)

  

    def isCyclicUtil(self, v, visited, recStack):

  

        # Отметить текущий узел как посещенный и

        # добавляет в стек рекурсии

        visited[v] = True

        recStack[v] = True

  

        # Повтор для всех соседей

        # если любой сосед посещен и в

        # recStack, то график циклический

        for neighbour in self.graph[v]:

            if visited[neighbour] == False:

                if self.isCyclicUtil(neighbour, visited, recStack) == True:

                    return True

            elif recStack[neighbour] == True:

                return True

  

        # Узел должен быть извлечен из

        # стек рекурсии до завершения функции

        recStack[v] = False

        return False

  

    # Возвращает true, если график циклический, иначе false

    def isCyclic(self):

        visited = [False] * self.V

        recStack = [False] * self.V

        for node in range(self.V):

            if visited[node] == False:

                if self.isCyclicUtil(node, visited, recStack) == True:

                    return True

        return False

graf = pd.read_excel("input_table.xlsx")
print(graf.size)
for i in range(0,graf['process'].size):
    print(graf["process"][i])
