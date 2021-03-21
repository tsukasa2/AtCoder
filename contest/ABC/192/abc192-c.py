N, K = map( int, input().split() )

def g_1( n ):
    l = list( str( n ) )
    l.sort()
    return int( "".join( l ) )

def g_2( n ):
    l = list( str( n ) )
    l.sort( reverse=True )
    return int( "".join( l ) )

def f( n ):
    return g_2( n ) - g_1( n )

for _ in range( K ):
    if N == f( N ):
        print( N )
        break
    N = f( N )
else:
    print( N )