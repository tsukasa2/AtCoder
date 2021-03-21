N = int( input() )
P = list( map( int, input().split() ) )

locate = [ -1 for _ in range( N + 1 ) ]
# xはPのlocate[ x ]文字目にいる．0 <= locate[ x ] <= N - 1

for k in range( N ):
    locate[ P[ k ] ] = k

used = [ False for _ in range( N - 1) ]
# used[ i ] = P[ i ]とP[ i + 1 ]を入れ替える操作は使われているか

ans = []
n = 1
while n <= N:
    if locate[ n ] == n - 1:
        n += 1
    elif locate[ n ] > n - 1:
        m = P[ locate[ n ] - 1 ]
        P[ locate[ n ] ], P[ locate[ n ] - 1 ] = m, n
        locate[ n ] -= 1
        locate[ m ] += 1
        ans.append( locate[ n ] + 1 )
        if used[ locate[ n ] ] == True:
            print( -1 )
            exit()
        else:
            used[ locate[ n ] ] = True
    elif locate[ n ] < n - 1:
        m = P[ locate[ n ] + 1 ]
        P[ locate[ n ] ], P[ locate[ n ] + 1 ] = m, n
        locate[ n ] += 1
        locate[ m ] -= 1
        ans.append( locate[ m ] + 1 )
        if used[ locate[ m ] ] == True:
            print( -1 )
            exit()
        else:
            used[ locate[ m ] ] = True

for b in used:
    if b == False:
        print( -1 )
        exit()

for a in ans:
    print( a )