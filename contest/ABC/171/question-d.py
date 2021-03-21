n = int( input() )
a_array = list( map( int, input().split() ) )
q = int( input() )
bc_array = []
for _ in range( q ):
    bc_i = list( map( int, input().split() ) )
    bc_array.append( bc_i )

a_list = [ 0 for _ in range( 10 ** 5 + 1 ) ]
for a in a_array:
    a_list[ a ] += 1

s = 0
for i in range( 10 ** 5 + 1 ):
    s += i * a_list[ i ]

for b, c in bc_array:
    s = s + ( c - b ) * a_list[ b ]
    a_list[ c ] += a_list[ b ]
    a_list[ b ] = 0
    print( s )