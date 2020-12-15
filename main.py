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

vertex = set()

for i in range(0,graf['onResource'].size):
    vertex.add(graf['process'][i])
    if graf['onResource'][i] != 0:
        vertex.add(graf['onResource'][i])
    if graf['needResource'][i] != 0:
        if len(graf['needResource'][i]) > 1:
            vertex.add(graf['needResource'][i][0])
            vertex.add(graf['needResource'][i][3])
        else:
            vertex.add(graf['needResource'][i])
            print("addV"+" "+graf['needResource'][i])

print(vertex)
g = Graph(len(vertex))

list_vert = list(vertex)

for i in range(0, len(list_vert)):
    print(list_vert[i])

for i in range(0,graf['onResource'].size):
    if graf['onResource'][i] != 0:
        g.addEdge(list_vert.index(graf['onResource'][i]), list_vert.index(graf['process'][i]))
        print("on "+graf['onResource'][i]+","+graf['process'][i])
    if graf['needResource'][i] != 0:
        if len(graf['needResource'][i]) > 1:
            g.addEdge(list_vert.index(graf['process'][i]),list_vert.index(graf['needResource'][i][0]))
            g.addEdge(list_vert.index(graf['process'][i]),list_vert.index(graf['needResource'][i][3]))
            print("need "+graf['process'][i]+","+graf['needResource'][i][0])
            print("need "+graf['process'][i]+","+graf['needResource'][i][3])
        else:
            g.addEdge(list_vert.index(graf['process'][i]),list_vert.index(graf['needResource'][i]))
            print("need "+graf['process'][i]+","+graf['needResource'][i])

if g.isCyclic() == 1:
    print("Обнаружена взаимная блокировка")
else:
    print("Взаимной блокировки не обнаружено")
