import constraint

def list_colouring_problem(G):
  """
  Return a constraint problem representing a node list-colouring instance.

  :param G: A graph with lists of permissible colours assigned to nodes.
  :return A node list-colouring constraint problem.
  """
  P = constraint.Problem()
  for node in G.nodes():
    P.addVariable(node, G.nodes[node]['permissible'])
  for edge in G.edges():
    P.addConstraint(constraint.AllDifferentConstraint(), edge)
  return(P)

def list_colouring_solution(G):
  """
  Return a list-coloured graph.

  :param G: A graph with lists of permissible colours assigned to nodes.
  :return A properly list-coloured graph.
  """
  P = list_colouring_problem(G)
  S = P.getSolution()
  for node in S:
    G.nodes[node]['colour'] = S[node]
  return(G)

