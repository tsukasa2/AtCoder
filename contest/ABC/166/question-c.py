n, m = input().split()
n = int( n )
m = int( m )
h = input().split()
tower = [ 1 ] * n

for i in range( m ):
    a, b = input().split()
    a = int( a )
    b = int( b )
    if int( h[a-1] ) < int( h[b-1] ):
        tower[a-1] = 0
    elif int( h[a-1] ) == int( h[b-1] ):
        tower[a-1] = 0
        tower[b-1] = 0
    else:
        tower[b-1] = 0

cnt = 0
for tower_i in tower:
    if tower_i == 1:
        cnt = cnt + 1

print( cnt )