N, X = map( int, input().split() )
A = list( map( int, input().split() ) )

ans = []
for a in A:
    if a != X:
        ans.append( a )

print( " ".join( map( str, ans ) ) )