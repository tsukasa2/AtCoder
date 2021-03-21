N = int( input() )
A = [ int( input() ) for _ in range( N ) ]

max_1st = -1
max_2nd = -1
for a in A:
    if a >= max_1st:
        max_2nd = max_1st
        max_1st = a
    elif a >= max_2nd:
        max_2nd = a

for a in A:
    if a == max_1st:
        print( max_2nd )
    else:
        print( max_1st )