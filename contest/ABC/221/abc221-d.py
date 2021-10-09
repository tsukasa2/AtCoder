N = int( input() )
AB = [ tuple( map( int, input().split() ) ) for _ in range( N ) ]

if N == 1:
    a, b = AB[ 0 ]
    print( b )
    exit()

d_dict = {}
for a, b in AB:
    if a in d_dict.keys():
        d_dict[ a ] += 1
    else:
        d_dict[ a ] = 1
    
    if a + b in d_dict.keys():
        d_dict[ a + b ] -= 1
    else:
        d_dict[ a + b ] = -1

delta = [ ( k, d_dict[ k ] ) for k in d_dict.keys() ]
delta.sort()

on = [ 0 ] * N
prev_k, s = delta[ 0 ]
for k, d in delta[ 1 : ]:
    if s >= 1 and s <= N:
        on[ s - 1 ] += k - prev_k
    prev_k = k
    s += d

print( " ".join( map( str, on ) ) )