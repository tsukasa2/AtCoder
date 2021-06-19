import math

N = int( input() )
A = list( map( int, input().split() ) )

left_gcd = [ A[ 0 ] ]
right_gcd = [ A[ -1 ] ]

for a in A[ 1 : ]:
    left_gcd.append( math.gcd( left_gcd[ -1 ], a ) )

for a in reversed( A[ : -1 ] ):
    right_gcd.append( math.gcd( right_gcd[ -1 ], a ) )

ans = right_gcd[ -2 ]
for i in range( 1, N - 1 ):
    g = math.gcd( left_gcd[ i - 1 ], right_gcd[ - ( i + 2 ) ] )
    ans = max( ans, g )

g = left_gcd[ -2 ]
ans = max( ans, g )

print( ans )