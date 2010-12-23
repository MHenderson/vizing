import networkx 

import vizing

nodes_1 = ['a','b','c','d']
edges_1 = [('a','b'),('a','d'),('b','c'),('c','d')]
lists_1 = {'a':['p','q'], 'b':['p','r'], 'c':['q','r'], 'd':['p','q','r']}

nodes_2 = [1,2,3,4]
edges_2 = [(1,2),(1,4),(2,3),(3,4)]
lists_2 = {1:[1,2],2:[1,3],3:[2,3],4:[1,2,3]}

G1 = networkx.Graph()
G1.add_nodes_from(nodes_1)
G1.add_edges_from(edges_1)

G2 = networkx.Graph()
G2.add_nodes_from(nodes_2)
G2.add_edges_from(edges_2)

G3 = networkx.complete_graph(10)
lists_3 = dict([(node, range(10)) for node in G3.nodes()])

print vizing.list_colouring(G3, lists_3, model = 'CP')
print vizing.list_colouring(G3, lists_3, model = 'or')

