import math

a, b, x = map( int, input().split() )

if x > a * a * b / 2:
    tan_ans = 2 * ( a * a * b - x ) / ( a * a * a )
else:
    tan_ans = a * b * b / ( 2 * x )

print( math.atan( tan_ans ) * 180 / math.pi )