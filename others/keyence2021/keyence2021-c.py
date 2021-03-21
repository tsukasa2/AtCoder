H, W, K = map( int, input().split() )

grid = [ [ 0 ] * W for _ in range( H ) ]

c_dict = { "R" : 1, "D" : 2, "X": 3 }
for _ in range( K ):
    h, w, c = input().split()
    h, w = int( h ), int( w )
    grid[ h - 1 ][ w - 1 ] = c_dict[ c ]

# print( "\n".join( [ " ".join( grid[ h ] ) for h in range( H ) ] ) )

MOD = 998244353
inv = [ 1, 1 ]
fact = [ 1, 1 ]
inv_fact = [ 1, 1 ]
for k in range( 2, 4 ):
    inv_k = ( -inv[ MOD % k ] * ( MOD // k ) ) % MOD
    inv.append( inv_k )
    fact.append( fact[ -1 ] * k % MOD )
    inv_fact.append( inv_fact[ -1 ] * inv[ k ] % MOD )
inv3 = inv[ 3 ]

dp = [ [ 0 ] * W for _ in range( H ) ]
dp[ 0 ][ 0 ] = pow( 3, H * W - K, MOD )
for i in range( H ):
    for j in range( W ):
        c = grid[ i ][ j ]
        dp[ i ][ j ] %= MOD
        p = dp[ i ][ j ]
        if i < H - 1:
            if c == 0:
                dp[ i + 1 ][ j ] += p * 2 * inv3
            elif c == 3 or c == 2:
                dp[ i + 1 ][ j ] += p
        
        if j < W - 1:
            if c == 0:
                dp[ i ][ j + 1 ] += p * 2 * inv3
            elif c == 3 or c == 1:
                dp[ i ][ j + 1 ] += p

print( dp[ H - 1 ][ W - 1 ] )