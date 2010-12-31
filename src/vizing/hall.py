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

def hall_inequality(graph, list_assignment, colours):
    """
    Decide whether the Hall inequality for graph is satisfied
    """
    return halls_sum(graph, list_assignment, colours) >= len(graph.nodes())

def hall_inequality_induced_by(graph, list_assignment, colours, vertices):
    """
    Check Hall's inequality for a subgraph of 'graph' induced by 'vertices'.
    """
    return hall_inequality(graph.subgraph(vertices), list_assignment, colours)

