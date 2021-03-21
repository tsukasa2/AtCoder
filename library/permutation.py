import itertools

l = [ 1, 2, 3, 4 ]
for p in itertools.permutations( l, 3 ):
    print( p )