N = int( input() )
ST = [ tuple( map( str, input().split() ) ) for _ in range( N ) ]

from collections import Counter
count = Counter()

for S, T in ST:
    if count[ str( S ) + "-" + str( T ) ] > 0:
        print( "Yes" )
        break
    else:
        count[ str( S ) + "-" + str( T ) ] += 1
else:
    print( "No" )