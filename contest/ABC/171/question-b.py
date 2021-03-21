n, k = map( int, input().split() )
p = list( map( int, input().split() ) )

p.sort()

cost = 0
for i in range( k ):
    cost += p[ i ]

print( cost )