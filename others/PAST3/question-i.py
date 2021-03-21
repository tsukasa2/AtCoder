import copy
n = int( input() )
q = int( input() )
query = []
for _ in range( q ):
    query_i = list( map( int, input().split() ) )
    query.append( query_i )

a = []
for i in range( 1, n+1 ):
    line = []
    for j in range( 1, n+1 ):
        line.append( n * ( i - 1 ) + ( j - 1 ) )
    a.append( line )

b = copy.deepcopy( a )

for query_i in query:
    if query_i[0] == 1:
        tmp = copy.deepcopy( b[ query_i[1] - 1 ] )
        b[ query_i[1] - 1 ] = copy.deepcopy( b[ query_i[2] - 1 ] )
        b[ query_i[2] - 1 ] = tmp
    elif query_i[0] == 2:
        for j in range( n ):
            tmp = copy.deepcopy( b[ j ][ query_i[1] - 1 ] )
            b[ j ][ query_i[1] - 1 ] = copy.deepcopy( b[ j ][ query_i[2] - 1 ] )
            b[ j ][ query_i[2] - 1 ] = tmp
    elif query_i[0] == 3:
        b_0 = copy.deepcopy( b )
        for i in range( n ):
            for j in range( n ):
                b[ i ][ j ] = copy.deepcopy( b_0[ j ][ i ] )
    else:
        print( b[ query_i[1] - 1 ][ query_i[ 2 ] - 1 ] )
