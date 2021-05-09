N = int( input() )
A = list( map( int, input().split() ) )

count = [ 0 for _ in range( 200 ) ]

for a in A:
    count[ a % 200 ] += 1

ans = 0
for c in count:
    ans += c * ( c - 1 ) // 2

print( ans )