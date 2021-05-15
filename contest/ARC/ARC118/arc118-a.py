import math

t, N = map( int, input().split() )

skipped = []
b = 0
i = 0
c = 0
for i in range( 1, 100 + t ):
    c = math.floor( i * ( 100 + t ) / 100 )
    if c > b + 1:
        for j in range( b + 1, c ):
            skipped.append( j )
    
    b = c
    i += 1

N -= 1
m = N // t
r = N % t
print( ( 100 + t ) * m + skipped[ r ] )