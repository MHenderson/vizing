import networkx as nx
import vizing as vz

def test_edge_list_colouring_problem():
  G = nx.complete_graph(3)
  permissible_dict_edge = {(0, 1): [0, 1], (0, 2): [1, 2], (1, 2): [2, 4]}
  nx.set_edge_attributes(G, permissible_dict_edge, "permissible")
  nx.set_edge_attributes(G, None, "colour")
  P = vz.edge_list_colouring_problem(G)
  assert P._variables == {(0, 1): [0, 1], (0, 2): [1, 2], (1, 2): [2, 4]}

def test_edge_list_colouring_solution():
  G = nx.complete_graph(3)
  permissible_dict_edge = {(0, 1): [0, 1], (0, 2): [1, 2], (1, 2): [2, 4]}
  nx.set_edge_attributes(G, permissible_dict_edge, "permissible")
  nx.set_edge_attributes(G, None, "colour")
  G = vz.edge_list_colouring_solution(G)
  assert G.edges()[(0, 1)]['colour'] == 1
  assert G.edges()[(0, 2)]['colour'] == 2
  assert G.edges()[(1, 2)]['colour'] == 4
