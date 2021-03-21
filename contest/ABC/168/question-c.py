import math
a, b, h, m = map( float, input().split() )

theta_a = 2 * math.pi * ( h + m / 60 ) / 12
theta_b = 2 * math.pi * m / 60

print( math.sqrt( a ** 2 + b ** 2 - 2 * a * b * math.cos( theta_a - theta_b ) ) )