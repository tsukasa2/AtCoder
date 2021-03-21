import copy
D = int( input() )
c = list( map( int, input().split() ) )
s = []
for _ in range( D ):
    s_i = list( map( int, input().split() ) )
    s.append( s_i )

def next_satisfy( d, c, s, next_t, last,  pre_satisfy ):
    ans = pre_satisfy + s[ d ][ next_t ]
    last_d = copy.deepcopy( last[ -1 ] )
    last_d[ next_t ] = d
    last.append( last_d )
    for i in range( 26 ):
        ans -= c[ i ] * ( d - last[ d ][ i ] )
    return ans

t = []
last = [ [ -1 for _ in range( 26 ) ] ]
last_i = [ -1 for _ in range( 26 ) ]
for d in range( D ):
    max_satisfy = - 10 ** 10
    next_t = -1
    for i in range( 26 ):
        satisfy_i = next_satisfy( d, c, s, i, last, 0 )
        if max_satisfy < satisfy_i:
            max_satisfy = satisfy_i
            next_t = i
    last_i[ next_t ] = d
    last.append( copy.deepcopy( last_i ) )
    t.append( next_t + 1 )

for t_i in t:
    print( t_i )
    