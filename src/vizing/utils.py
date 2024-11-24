import itertools

from networkx import complement, node_clique_number

def graph_clique_number(graph):
    return max(node_clique_number(graph))

def is_independent(graph, nodes):
    """Decides whether of not the subgraph of 'graph' induced by nodes in 
    'nodes' is an independent set or not."""
    if len(nodes) == 0:
        return True
    else:
        return graph_clique_number(graph.subgraph(nodes)) == 1

def is_exact(graph, colouring):
    """Decides whether exactly every vertex of 'graph' is coloured."""
    coloured_vertices = list(itertools.chain.from_iterable(list(colouring.values())))
    coloured_vertices.sort()
    return coloured_vertices == graph.nodes()

def is_proper(graph, colouring):
    """Decides whether or not 'colouring' is a proper colouring of the vertices
    of 'graph'."""
    return is_exact(graph, colouring) and all([is_independent(graph, nodes) for nodes in list(colouring.values())])

def has_colour(list_assignment, vertex, colour):
    """Decides whether or not 'colour' is a member of the list assigned to 
    'vertex' by the 'list_assignment'."""
    return colour in list_assignment.get(vertex)

def is_list_colouring(graph, list_assignment, colouring):
    """Decides whether or not 'colouring' is a list colouring of 'graph', 
    according to the 'list_assignment' given."""
    return all([has_colour(list_assignment, vertex, colour) for colour in colouring for vertex in colouring.get(colour)])

def is_proper_list_colouring(graph, list_assignment, colouring):
    """Decides whether or not 'colouring' is a proper list colouring of 
    'graph', according to the 'list_assignment' given."""
    return is_proper(graph, colouring) and is_list_colouring(graph, list_assignment, colouring)

def grange(vtc_colouring):
    """The colours used by a colouring (vertex-to-color map)."""
    return list(set((list(vtc_colouring.values()))))

def inverse(vtc_colouring, colour):
    """The vertices where a colour appears in a vertex-to-colour map."""
    return [v for v in vtc_colouring if vtc_colouring[v] == colour]

def vtc_to_ctv(vtc):
    """Translate a vertex-to-colour map into a colour-to-vertices map."""
    return dict([(colour, inverse(vtc, colour)) for colour in grange(vtc)])

def support(list_assignment, nodes, colour):
    """
    A list of those vertices in 'nodes' which have 'colour' in the list 
    associated with that vertex by 'list_assignment'.
    """
    return [vertex for vertex in nodes if has_colour(list_assignment, vertex, colour)]

def support_subgraph(graph, list_assignment, colour):
    """
    The subgraph induced by those vertices of 'graph' which have 'colour' 
    in the list associated by 'list_assignment'.
    """
    return graph.subgraph(support(list_assignment, graph.nodes(), colour))

def independence_number(graph):
    """
    Compute the independence number of 'graph'.
    """
    if graph.number_of_nodes() == 0:
        return 0
    else:
        return graph_clique_number(complement(graph))

def powerset(iterable):
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))

