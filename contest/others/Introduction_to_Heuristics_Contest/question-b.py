import copy
D = int( input() )
c = list( map( int, input().split() ) )
s = []
for _ in range( D ):
    s_i = list( map( int, input().split() ) )
    s.append( s_i )
t = []
for _ in range( D ):
    t_i = int( input() )
    t.append( t_i - 1 )

last = []
last_i = [ -1 for _ in range( 26 ) ]
for i in range( D ):
    last_i[ t[ i ] ] = i
    last.append( copy.deepcopy( last_i ) )

# def satisfy( D, c, s, t, last, d ):
satisfy = [ 0 for _ in range( D ) ]
for d in range( D ):
    satisfy[ d ] += s[ d ][ t[ d ] ]
    for i in range( 26 ):
        satisfy[ d ] -= c[ i ] * ( d - last[ d ][ i ] )

v = 0
for v_i in satisfy:
    v += v_i
    print( v )
