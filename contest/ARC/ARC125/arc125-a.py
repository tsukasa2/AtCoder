N, M = map( int, input().split() )
S = list( map( int, input().split() ) )
T = list( map( int, input().split() ) )

# TがS[ 0 ]のみからなるとき
for t in T:
    if not t == S[ 0 ]:
        break
else:
    print( M )
    exit()

# SにS[ 0 ]と異なる文字が存在しないとき
if sum( S ) == 0 or sum( S ) == N:
    print( -1 )
    exit()

# そうでないとき
# SのなかでS[ 0 ]と異なる文字のうち，最も左をx，最も右をyとする
x = 10 ** 5 + 100
y = -1
for i in range( N ):
    if not S[ i ] == S[ 0 ]:
        x = min( x, i )
        y = max( y, i )

ans = min( x, N - y ) - 1
now = S[ 0 ]
for t in T:
    if t == now:
        ans += 1
    else:
        now = t
        ans += 2

print( ans )