N = int( input() )
f = list( map( int, input().split() ) )

INF = 2 * 10 ** 5 + 100
log_ans = 0

found = [ INF for _ in range( N ) ]
for i in range( N ):
    v = i
    if found[ v ] < INF:
        continue

    if found[ f[ v ] - 1 ] < INF:
        continue
    
    found[ v ] = i
    v = f[ v ] - 1

    while True:
        found[ v ] = i
        if found[ f[ v ] - 1 ] < i:
            break
        elif found[ f[ v ] - 1 ] == i:
            log_ans += 1
            break
        else:
            v = f[ v ] - 1

MOD = 998244353
ans = 1
for _ in range( log_ans ):
    ans = ans * 2 % MOD

print( ans - 1 )   