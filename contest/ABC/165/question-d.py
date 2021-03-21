a, b, n = input().split()
a = int( a )
b = int( b )
n = int( n )
f_max = 0

x = 0
x_per_b = 0
d = 1 / b
for x in range( n + 1 ):
    f_x = int( a * x_per_b ) - a * int( x_per_b )
    if x == 0 or f_max < f_x:
        f_max = f_x
    x_per_b = x_per_b + d

print( f_max )