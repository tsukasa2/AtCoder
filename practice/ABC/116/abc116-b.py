from collections import Counter

s = int( input() )

def f( x ):
    if x % 2 == 0:
        return x // 2
    else:
        return 3 * x + 1

count = Counter()
x = 1
m = s
count[ m ] += 1
while True:
    x += 1
    m = f( m )
    count[ m ] += 1
    if count[ m ] == 2:
        break

print( x )