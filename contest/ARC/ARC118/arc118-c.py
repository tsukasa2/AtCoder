N = int( input() )

A = [ 6, 10, 15 ]

i = 16
len_A = 3
while len_A < N:
    if i % 6 == 0:
        A.append( i )
        len_A += 1
    elif i % 10 == 0:
        A.append( i )
        len_A += 1
    elif i % 15 == 0:
        A.append( i )
        len_A += 1
    
    i += 1

print( " ".join( map( str, A ) ) )