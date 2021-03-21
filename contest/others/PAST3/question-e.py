n, m, q = map( int, input().split() )
adj_list = []
for _ in range( n+1 ):
    adj_list.append( [] )

for _ in range( m ):
    u, v = map( int, input().split() )
    adj_list[u].append( v )
    adj_list[v].append( u )

c = list( map( int, input().split() ) )
c = [ 0 ] + c

s = []
for _ in range( q ):
    s_i = list( map( int, input().split() ) )
    s.append( s_i )

for s_i in s: 
    print( c[ s_i[1] ] )
    if s_i[0] == 1:        
        for v in adj_list[ s_i[1] ]:
            c[ v ] = c[ s_i[1] ]
    else:
        c[ s_i[1] ] = s_i[2]