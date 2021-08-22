S, K = input().split()
K = int( K )

words = set()

import itertools
for p in itertools.permutations( S ):
    words.add( "".join( p ) )

words = list( words )
words.sort()
print( words[ K - 1 ] )