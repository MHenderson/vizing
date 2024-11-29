import listcolouring as lc
import networkx as nx
import vizing as vz

def test_total_list_colouring_problem():
  G = nx.complete_graph(3)
  permissible_dict_edge = {(0, 1): [0, 1], (0, 2): [1, 2], (1, 2): [2, 4]}
  nx.set_edge_attributes(G, permissible_dict_edge, "permissible")
  nx.set_edge_attributes(G, None, "colour")
  permissible_dict_node = {0: [0, 1], 1: [1, 2], 2: [2, 4]}
  nx.set_node_attributes(G, permissible_dict_node, "permissible")
  nx.set_node_attributes(G, None, "colour")
  P = vz.total_list_colouring_problem(G)
  assert P._variables == {0: [0, 1], 1: [1, 2], 2: [2, 4], (0, 1): [0, 1], (0, 2): [1, 2], (1, 2): [2, 4]}

def test_total_list_colouring_solution():
  G = nx.petersen_graph()
  n_colours = 6
  G = lc.list_init_node(G, range(n_colours - 1), 3, 0)
  G = lc.list_init(G, range(n_colours - 1), 3, 0)
  G = vz.total_list_colouring_solution(G)
  assert G.nodes()[0]['colour'] == 0

