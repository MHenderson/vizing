import listcolouring
import networkx as nx

import vizing

from listcolouring import list_init_node

def test_list_colouring_solution():
  G = nx.petersen_graph()
  G = list_init_node(G, range(1, 10), 3, 0)
  G = vizing.list_colouring_solution(G)
