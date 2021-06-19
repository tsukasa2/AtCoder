N = int( input() )
A = list( map( int, input().split() ) )

minus_count = 0
abs_A = []
for a in A:
    if a < 0:
        minus_count += 1
    
    abs_A.append( abs( a ) )

if minus_count % 2 == 0:
    print( sum( abs_A ) )
else:
    abs_A.sort()
    print( sum( abs_A[ 1 : ] ) - abs_A[ 0 ] )