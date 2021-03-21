n, m, q = map( int, input().split() )
s = []
for _ in range( q ):
    s_i = list( map( int, input().split() ) )
    s.append( s_i )

solved = []  # solved[i] = iさんが解いた問題
for _ in range( n+1 ):
    solved.append( [] )
score = [ n ] * ( m+1 )     # score[i] = 問題iの得点

for s_i in s:
    if s_i[ 0 ] == 1:
        tmp = 0
        for j in range( 1, m+1 ):
            if j in solved[ s_i[ 1 ] ]:
                tmp += score[ j ]
        print( tmp )
    else:
        score[ s_i[ 2 ] ] -= 1
        solved[ s_i[ 1 ] ].append( s_i[ 2 ] )
