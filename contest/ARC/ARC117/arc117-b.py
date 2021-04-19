N = int( input() )
A = list( map( int, input().split() ) )

MOD = 10 ** 9 + 7

A.sort()
ans = A[ 0 ] + 1
for i in range( N - 1 ):
    ans *= ( A[ i + 1 ] - A[ i ] + 1 )
    ans %= MOD

print( ans )