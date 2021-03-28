import math

N = int( input() )
x_0, y_0 = map( int, input().split() )
x_H, y_H = map( int, input().split() )

x_M = ( x_0 + x_H ) / 2
y_M = ( y_0 + y_H ) / 2

a = x_0 - x_M
b = y_0 - y_M

x_1 = a * math.cos( 2 * math.pi / N ) - b * math.sin( 2 * math.pi / N )
y_1 = b * math.cos( 2 * math.pi / N ) + a * math.sin( 2 * math.pi / N )

x_1 += x_M
y_1 += y_M

print( x_1, y_1 )