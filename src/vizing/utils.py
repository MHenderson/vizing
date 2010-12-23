def to_colouring(assignment):
    """Fix this awful code."""
    def f(y):
        return [x for x in assignment.keys() if assignment[x]==y]
    P = list(set(assignment.values()))
    Q = dict(zip(assignment.keys(), map(f, assignment)))
    R = {}
    for q in Q:
        if len(Q[q])>0:
            R[q] = Q[q]
    return R
