N = int( input() )
xy = [ tuple( map( int, input().split() ) ) for _ in range( N ) ]

args = []
for x, y in xy:
    if x > 1:
        l = 10 ** 19 * ( y - 1 ) // x
        r = 10 ** 19 * y // ( x - 1 )
    else:
        l = 10 ** 19 * ( y - 1 ) // x
        r = 10 ** 38

    args.append( ( r, ( l, r ) ) )

args.sort()

ans = 0
R_max = -1
for _, ( l, r ) in args:
    if R_max <= l:
        ans += 1
        R_max = r

print( ans )