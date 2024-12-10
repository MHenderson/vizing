import listcolouring as lc
import networkx as nx
import vizing as vz

def test_node_list_colouring_problem():
  G = nx.petersen_graph()
  G = lc.list_init_node(G, range(1, 10), 3, 0)
  G = vz.node_list_colouring_problem(G)

def test_node_list_colouring_solution():
  G = nx.complete_graph(3)
  permissible_dict = {0: [0, 1], 1: [1, 2], 2: [2, 3]}
  nx.set_node_attributes(G, permissible_dict, "permissible")
  G = vz.node_list_colouring_solution(G)
  assert G.nodes[0]['colour'] == 1
  assert G.nodes[1]['colour'] == 2
  assert G.nodes[2]['colour'] == 3
