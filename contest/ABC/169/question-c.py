a, b = input().split()
a = int( a )
b = int( 1000 * float( b ) )
m = a * b
m = m // 1000

print( m )