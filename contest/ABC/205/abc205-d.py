N, Q = map( int, input().split() )
A = list( map( int, input().split() ) )
K = [ int( input() ) for _ in range( Q ) ]

A.sort()
c = 0
borders = []
borders.append( ( 0, 0 ) )
for a in A:
    borders.append( ( a - c, c ) )
    c += 1

_, c = borders[ -1 ]
borders.append( ( 10 ** 18 + 100, c + 1 ) )

for k in K:
    L = 0
    R = len( borders ) - 1
    while R - L > 1:
        M = ( L + R ) // 2
        b, c = borders[ M ]
        if k < b:
            R = M
        else:
            L = M
    
    print( k + borders[ R ][ 1 ] )
