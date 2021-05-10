import math

t, N = map( int, input().split() )

# if t == 1:
#     print( 101 * N - 1 )
#     exit()

skipped = []
b = 0
i = 0
c = 0
for i in range( 1, 100 * t + 1 ):
    c = math.floor( i * ( 100 + t ) / 100 )
    if c > b + 1:
        for j in range( b + 1, c ):
            skipped.append( j )
    
    b = c
    i += 1

print( skipped )

p = len( skipped )
m = N // p
r = N % p
print( 100 * t * m + skipped[ r - 1 ] )

print( 100999999999 - 100 )