N = int( input() )
A = list( map( int, input().split() ) )

dA = []
for i in range( N - 1 ):
    if A[ i ] < A[ i + 1 ]:
        dA.append( 1 )
    else:
        dA.append( -1 )

dA.append( 1 )
# print( dA )

hand = "gold"
last_trade = -1
prev_dA = 1
ans = []
for i in range( N ):
    if hand == "gold":
        if prev_dA == 1 and dA[ i ] == -1:
            ans.append( 1 )
            last_trade = i
            hand = "silver"
        else:
            ans.append( 0 )
    else:
        if prev_dA == -1 and dA[ i ] == 1:
            ans.append( 1 )
            last_trade = i
            hand = "gold"
        else:
            ans.append( 0 )
    
    prev_dA = dA[ i ]

if hand == "silver":
    ans[ last_trade ] = 0

print( " ".join( map( str, ans ) ) )