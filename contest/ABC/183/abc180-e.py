H, W = map( int, input().split() )
S = []
for _ in range( H ):
    S_i = list( input())
    S.append( S_i )

MOD = 10 ** 9 + 7
dp = [ [ 0 for _ in range( W ) ] for _ in range( H ) ]
ruisekiwa = [ [ [ 0, 0, 0 ] for _ in range( W ) ] for _ in range( H ) ] # タテヨコナナメ
dp[ 0 ][ 0 ] = 1
# ruisekiwa[ 0 ][ 0 ] = [ 0, 0, 0 ]
for i in range( H ):
    for j in range( W ):
        if S[ i ][ j ] == "#":
            continue

        if i > 0:
            dp[ i ][ j ] += ruisekiwa[ i - 1 ][ j ][ 0 ]
            dp[ i ][ j ] %= MOD
        if j > 0:
            dp[ i ][ j ] += ruisekiwa[ i ][ j - 1 ][ 1 ]
            dp[ i ][ j ] %= MOD
        if i > 0 and j > 0:
            dp[ i ][ j ] += ruisekiwa[ i - 1 ][ j - 1 ][ 2 ]
            dp[ i ][ j ] %= MOD
        
        ruisekiwa[ i ][ j ][ 0 ] += dp[ i ][ j ]
        ruisekiwa[ i ][ j ][ 0 ] %= MOD
        ruisekiwa[ i ][ j ][ 1 ] += dp[ i ][ j ]
        ruisekiwa[ i ][ j ][ 1 ] %= MOD
        ruisekiwa[ i ][ j ][ 2 ] += dp[ i ][ j ]
        ruisekiwa[ i ][ j ][ 2 ] %= MOD
        if i > 0:
            ruisekiwa[ i ][ j ][ 0 ] += ruisekiwa[ i - 1 ][ j ][ 0 ]
            ruisekiwa[ i ][ j ][ 0 ] %= MOD
        if j > 0:
            ruisekiwa[ i ][ j ][ 1 ] += ruisekiwa[ i ][ j - 1 ][ 1 ]
            ruisekiwa[ i ][ j ][ 1 ] %= MOD
        if i > 0 and j > 0:
            ruisekiwa[ i ][ j ][ 2 ] += ruisekiwa[ i - 1 ][ j - 1 ][ 2 ]
            ruisekiwa[ i ][ j ][ 2 ] %= MOD
        
print( dp[ H - 1 ][ W - 1 ] )