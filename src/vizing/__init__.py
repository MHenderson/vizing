import constraint

def list_colouring_problem(G):
  P = constraint.Problem()
  for node in G.nodes():
    P.addVariable(node, G.nodes[node]['permissible'])
  for edge in G.edges():
    P.addConstraint(constraint.AllDifferentConstraint(), edge)
  return(P)

def list_colouring_solution(G):
  P = list_colouring_problem(G)
  S = P.getSolution()
  for node in S:
    G.nodes[node]['colour'] = S[node]
  return(G)

