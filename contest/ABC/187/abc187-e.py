N = int( input() )
edge = []
connect = [ [] for _ in range( N ) ]
for _ in range( N - 1 ):
    a_i, b_i = map( int, input().split() )
    edge.append( ( a_i, b_i ) )
    connect[ a_i - 1 ].append( b_i - 1 )
    connect[ b_i - 1 ].append( a_i - 1 )
Q = int( input() )
querry = []
for _ in range( Q ):
    t_i, e_i, x_i = map( int, input().split() )
    querry.append( ( t_i, e_i, x_i ) )

queue = [ 0 ]
parent = [ -1 for _ in range( N ) ]
while queue:
    v = queue.pop( 0 )
    for u in connect[ v ]:
        if u != parent[ v ]:
            queue.append( u )
            parent[ u ] = v

c = [ 0 for _ in range( N ) ]
for i in range( Q ):
    t, e, x = querry[ i ]
    a_e_i, b_e_i = edge[ e - 1 ]
    if t == 2:
        a_e_i, b_e_i = b_e_i, a_e_i
    if parent[ b_e_i - 1 ] == a_e_i - 1:
        c[ 0 ] += x
        c[ b_e_i - 1 ] -= x
    else:
        c[ a_e_i - 1 ] += x

queue = [ 0 ]
while queue:
    v = queue.pop( 0 )
    for u in connect[ v ]:
        if u != parent[ v ]:
            queue.append( u )
            c[ u ] += c[ v ]

[ print( c_i ) for c_i in c ]