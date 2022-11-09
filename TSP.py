# Python3 program to implement traveling salesman 
# problem using naive approach. 
#from point import point
from sys import maxsize 
from itertools import permutations
import matplotlib.pyplot as pt
#cities
Ludhiana=(0,61,140,106,93)
Jalandhar=(61,0,80,149,154)
Amritsar=(140,80,0,229,235)
Chandigar=(106,149,229,0,75)
Patiala=(93,154,235,75,0)

V = 5
 

# implementation of traveling Salesman Problem 
def travellingSalesmanProblem(graph, s): 
 
    # store all vertex apart from source vertex 
    vertex = [] 
    for i in range(V): 
        if i != s: 
            vertex.append(i) 
 
    # store minimum weight Hamiltonian Cycle 
    min_path = maxsize 
    next_permutation=permutations(vertex)
    for i in next_permutation:
 
        # store current Path weight(cost) 
        current_pathweight = 0
 
        # compute current path weight 
        k = s 
        for j in i: 
            current_pathweight += graph[k][j] 
            k = j 
        current_pathweight += graph[k][s] 
 
        # update minimum 
        min_path = min(min_path, current_pathweight) 
         
    return min_path 

print('Shortest path between cities: ')
 
 
if __name__ == "__main__": 
 
    # __matrix representation of graph__
    graph = [[0, 61, 140, 106,93], [61,0,80,149,154], 
            [140,80,0,229,235], [106, 149, 229, 0,75],[93,154,235,75,0]] 
    s = 0
    
    print(travellingSalesmanProblem(graph, s))
 ## Graph implementation using matplotlib
    pt.plot([0,61,140,106,93],[61,0,80,149,154],[140,800,229,0,75],[93,154,235,75,0],)
    pt.title('Implementation of traveling Salesman Problem')
