N = int( input() )
AB = [ tuple( map( int, input().split() ) ) for _ in range( N ) ]

L = [ 0.0 ]
prev = 0.0
for a, b in AB:
    L.append( prev + a / b )
    prev += a / b

R = [ 0.0 ]
prev = 0.0
for a, b in reversed( AB ):
    R.append( prev + a / b )
    prev += a / b

R = R[ :: -1 ]

L = [ ( L[ i ], L[ i + 1 ] ) for i in range( N ) ]
R = [ ( R[ i + 1 ], R[ i ] ) for i in range( N ) ]

i = 0
while i < N:
    L_l, L_r = L[ i ]
    R_l, R_r = R[ i ]
    if L_l <= R_l and R_l <= L_r:
        break
    elif R_l <= L_l and L_l <= R_r:
        break
    else:
        i += 1

ans = sum( [ a for a, _ in AB[ : i ] ] )
if L[ i ][ 0 ] < R[ i ][ 0 ]:
    d = AB[ i ][ 1 ] * ( R[ i ][ 0 ] - L[ i ][ 0 ] )
    ans += d
    ans += ( AB[ i ][ 0 ] - d ) / 2
else:
    d = AB[ i ][ 1 ] * ( L[ i ][ 0 ] - R[ i ][ 0 ] )
    ans += ( AB[ i ][ 0 ] - d ) / 2

print( ans )