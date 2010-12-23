import networkx 

import vizing

V1 = ['a','b','c','d']
E1 = [('a','b'),('a','d'),('b','c'),('c','d')]
L1 = {'a':['p','q'], 'b':['p','r'], 'c':['q','r'], 'd':['p','q','r']}

V2 = [1,2,3,4]
E2 = [(1,2),(1,4),(2,3),(3,4)]
L2 = {1:[1,2],2:[1,3],3:[2,3],4:[1,2,3]}

G1 = networkx.Graph()
G1.add_nodes_from(V1)
G1.add_edges_from(E1)

G2 = networkx.Graph()
G2.add_nodes_from(V2)
G2.add_edges_from(E2)

G3 = networkx.complete_graph(10)
lists_3 = dict([(node, range(10)) for node in G3.nodes()])

C1 = vizing.list_colouring(G3, lists_3, model = 'CP')
C2 = vizing.list_colouring(G3, lists_3, model = 'or')

#assert vizing.is_proper_list_colouring(G1, C1, L1)
#assert vizing.is_proper_list_colouring(G2, C2, L2)
#assert vizing.is_proper_list_colouring(G3, C3, L3)

