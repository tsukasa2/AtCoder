n, m, q = input().split()
n = int( n )
m = int( m )
q = int( q )
a = []
b = []
c = []
d = []
for i in range( int( q ) ):
    a_i, b_i, c_i, d_i = input().split()
    a.append( int( a_i ) )
    b.append( int( b_i ) )
    c.append( int( c_i ) )
    d.append( int( d_i ) )

array = [ 1 ] * n
array_list = [ array ]

i = 0
while True:
    for k in range( array_list[i][-1], m + 1 ):
        array_list.append( array_list[i][1:] + [ k ] )
        #print( array_list[i][1:] + [ k ] )
    i = i + 1
    if len( array_list ) > 100000:
        break

max_score = 0
for array in array_list:
    score = 0
    for i in range( q ):
        #print( i, a[i], b[i], c[i], array )
        if array[b[i]-1] - array[a[i]-1] == c[i]:
            score = score + d[i]
    if max_score < score:
        max_score = score

print( max_score )