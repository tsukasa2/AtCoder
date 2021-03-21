l, r = map( int, input().split() )

r = min( r, l + 2019 )

min_ixj = 2019
for i in range( l, r ): 
    for j in range( i+1, r+1 ):
        ixj = ( i % 2019 ) * ( j % 2019 ) % 2019
        if ixj < min_ixj:
            min_ixj = ixj

print( min_ixj )