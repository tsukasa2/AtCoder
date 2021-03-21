import math

X, Y, A, B = map( int, input().split() )

ans = 0

# if B / ( A - 1 ) < Y:
#     ans += math.ceil( math.log( ( B / ( A - 1 ) / X ), A ) )
#     # print( ans )
#     ans += ( Y - 1 - X * pow( A, ans ) ) // B
#     print( ans )
# else:
#     ans += math.floor( math.log( ( ( Y - 1 ) / X ), A ) )
#     print( ans )

power = X

while power * A < Y and power < B / ( A - 1 ):
    power = power * A
    ans += 1

ans += ( Y - 1 - power ) // B

print( ans )