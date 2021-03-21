H, W = map( int, input().split() )
S = [ str( input() ) for _ in range( H ) ]

S = [ "." * W ] + S + [ "." * W ]
S = [ "." + s + "." for s in S ]

ans = 0
for i in range( H + 2 ):
    for j in range( W + 2 ):
        if S[ i ][ j ] == "#":
            if S[ i ][ j - 1 ] != "#":
                if S[ i - 1 ][ j ] != "#":
                    ans += 2
                    # print( i, j )
                elif S[ i - 1 ][ j - 1 ] == "#":
                    ans += 2
                    # print( i, j )
            if S[ i ][ j + 1 ] != "#":
                if S[ i - 1 ][ j ] != "#":
                    ans += 2
                    # print( i, j )
                elif S[ i - 1 ][ j + 1 ] == "#":
                    ans += 2
                    # print( i, j )

print( ans )