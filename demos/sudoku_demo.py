import sudoku, vizing

s = '1....7.9.\
     .3..2...8\
     ..96..5..\
     ..53..9..\
     .1..8...2\
     6....4...\
     3......1.\
     .4......7\
     ..7...3..'
d = sudoku.string_to_dict(s, 3)
P = sudoku.puzzle_as_graph(d, 3)
print P.order(), P.size()
print P.nodes()
# create Sudoku list assignment
# solve via list colouring
