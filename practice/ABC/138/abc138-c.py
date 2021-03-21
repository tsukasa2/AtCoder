N = int( input() )
v = list( map( int, input().split() ) )

v.sort()
ans = v[ 0 ]
for v_i in v:
    ans = ( ans + v_i ) / 2

print( ans )