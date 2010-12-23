import constraint
from constraint_solver import pywrapcp

class CP_model:
    """ 
        XXX doc XXX 
    """
    
    def __init__(self, graph, list_assignment):
        """ XXX doc XXX """
        self.graph = graph
        self.list_assignment = list_assignment
        self.problem = constraint.Problem()
        for node in self.graph.nodes():
            self.problem.addVariable(node, self.list_assignment.get(node)) 
        for edge in self.graph.edges():
            self.problem.addConstraint(constraint.AllDifferentConstraint(), edge)
 
    def first_solution(self):
        """ XXX doc XXX """
        return self.problem.getSolution()

class or_CP_model:
    """ 
        XXX doc XXX 
    """

    def __init__(self, graph, list_assignment):
        """ XXX doc XXX """
        self.graph = graph
        self.list_assignment = list_assignment
        self.solver = pywrapcp.Solver('xxxNAMExxx')
        self.var = {}
        self.solution = {}
        for node in self.graph.nodes():
            self.var[node] = self.solver.IntVar(self.list_assignment.get(node))
        for edge in self.graph.edges():
            self.solver.Add(self.solver.AllDifferent([self.var[node] for node in edge], False))

    def first_solution(self):
        """ XXX doc XXX """
        var_list = self.var.values()
        vars_phase = self.solver.Phase(var_list,
                            self.solver.INT_VAR_SIMPLE,
                            self.solver.INT_VALUE_SIMPLE)
        solution = self.solver.Assignment()
        solution.Add(var_list)
        collector = self.solver.FirstSolutionCollector(solution)
        self.solver.Solve(vars_phase, [collector])
        current = collector.solution(0)
        if collector.solution_count() == 1:
            for var in self.var:  
                self.solution[var] = current.Value(self.var[var])
        return self.solution

def list_colouring(graph, list_assignment, model = 'CP'):
    """ XXX doc XXX """
    if model == 'CP':
        return CP_model(graph, list_assignment).first_solution()
    if model == 'or':
        return or_CP_model(graph, list_assignment).first_solution()
    else:
        raise Exception('No such model')

