S = str( input() )

first = S
last = S
s = S
for _ in range( len( S ) ):
    if s < first:
        first = s
    
    if s > last:
        last = s
    
    s = s[ 1 : ] + s[ 0 ]

print( first )
print( last )