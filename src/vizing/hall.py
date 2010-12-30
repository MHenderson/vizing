# Matthew Henderson, 2010.12.30 (Chandler's Ford)

from utils import support_subgraph, independence_number 

def hall_number(graph, list_assignment, colour):
    """
    Compute the independence number of the subgraph induced by those 
    vertices in 'graph' having 'colour' in their list.
    """
    return independence_number(support_subgraph(graph, colour, list_assignment))

def halls_sum(graph, list_assignment, colours):
    """
    Sum Hall numbers over all monochromatic subgraphs.
    """
    return sum([hall_number(graph, list_assignment, colour) for colour in colours])

def halls_condition(graph, list_assignment, colours):
    """
    Decide whether Hall's condition is satisfied.
    """
    return halls_sum(graph, list_assignment, colours) >= len(graph.nodes())

def halls_condition_induced_by(graph, size, list_assignment, colours, vertices):
    """
    Check Hall's condition for a subgraph of 'graph' induced by 'vertices'.
    """
    H = graph.subgraph(vertices)
    return halls_condition(H, list_assignment, colours)

