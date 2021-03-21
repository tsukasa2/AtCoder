N = int( input() )
S = str( input() )

ans = N
for i in range( N - 1 ):
    if S[ i ] == S[ i + 1 ]:
        ans = ans - 1

print( ans )