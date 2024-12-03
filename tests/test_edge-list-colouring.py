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

def test_directed_edge_list_colouring_problem():
  G = nx.complete_graph(3, create_using = nx.DiGraph)
  G.add_edge(0, 0)
  G.add_edge(1, 1)
  G.add_edge(2, 2)
  permissible_dict = {(0, 0): [1], (0, 1): [2], (0, 2): [3], (1, 0): [2, 3], (1, 1): [3], (1, 2): [1], (2, 0): [2, 3], (2, 1): [1, 3], (2, 2): [2, 3]}
  nx.set_edge_attributes(G, permissible_dict, "permissible")
  CP = vz.edge_list_colouring_problem(G, directed = True)
  assert CP._variables == {(0, 1): [2], (0, 2): [3], (0, 0): [1], (1, 0): [2, 3], (1, 2): [1], (1, 1): [3], (2, 0): [2, 3], (2, 1): [1, 3], (2, 2): [2, 3]}

def test_directed_edge_list_colouring_solution():
  G = nx.complete_graph(3, create_using = nx.DiGraph)
  G.add_edge(0, 0)
  G.add_edge(1, 1)
  G.add_edge(2, 2)
  permissible_dict = {(0, 0): [1], (0, 1): [2], (0, 2): [3], (1, 0): [2, 3], (1, 1): [3], (1, 2): [1], (2, 0): [2, 3], (2, 1): [1, 3], (2, 2): [2, 3]}
  nx.set_edge_attributes(G, permissible_dict, "permissible")
  nx.set_edge_attributes(G, None, "colour")
  G = vz.edge_list_colouring_solution(G, directed = True)
  assert G.edges()[(0, 0)]['colour'] == 1
  assert G.edges()[(0, 1)]['colour'] == 2
  assert G.edges()[(0, 2)]['colour'] == 3
  assert G.edges()[(1, 0)]['colour'] == 2
  assert G.edges()[(1, 1)]['colour'] == 3
  assert G.edges()[(1, 2)]['colour'] == 1
  assert G.edges()[(2, 0)]['colour'] == 3
  assert G.edges()[(2, 1)]['colour'] == 1
  assert G.edges()[(2, 2)]['colour'] == 2
