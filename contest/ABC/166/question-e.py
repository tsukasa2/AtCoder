n = int( input() )
array_a = input().split()

set_a = []

for i in range( n ):
    d = i - int( array_a[i] )
    if d >= 0:
        set_a.append(d)

cnt = 0
#for i in range( n ):
#    h_i = int( array_a[i] )
#    for j in range( i + h_i, n ):
#        h_j = int( array_a[j] )
#        if j - i == h_i + h_j:
#            cnt = cnt + 1

for i in range( n ):
    h_i = int( array_a[i] )
    if ( h_i + i ) in set_a:
        cnt = cnt + 1

print( cnt )