N = int( input() )
W = list( map( int, input().split() ) )

S_1 = 0
S_2 = sum( W )

ans = 10 ** 18
for w in W:
    S_1 += w
    S_2 -= w
    ans = min( ans, abs( S_1 - S_2 ) )

print( ans )