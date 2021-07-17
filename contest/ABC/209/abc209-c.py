N = int( input() )
C = list( map( int, input().split() ) )

MOD = 10 ** 9 + 7

C.sort()
ans = 1
for i, c in enumerate( C ):
    ans *= ( c - i )
    ans %= MOD

print( ans )