import networkx
import vizing

from vizing.utils import graph_clique_number

def test_clique_number():
    G = networkx.complete_graph(3)
    assert graph_clique_number(G) == 2
