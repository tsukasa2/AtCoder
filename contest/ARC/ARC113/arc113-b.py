A, B, C = map( int, input().split() )

found = [ False for _ in range( 10 ) ]
a = A % 10
k = 0
while found[ a ] == False:
    found[ a ] = True
    a = a * A % 10
    k += 1

r = pow( B, C, k )
if r == 0:
    r += k
print( pow( A, r, 10 ) )

# print( r, k )