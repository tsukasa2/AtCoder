n = int( input() )
s = []
for _ in range( n ):
    s_i = str( input() )
    s.append( s_i )

count = {}
for s_i in s:
    try:
        count[ s_i ] += 1
    except KeyError:
        count[ s_i ] = 1

max_count = 0
for t in count.keys():
    if count[ t ] > max_count:
        max_count = count[ t ]

max_t = []
for t in count.keys():
    if count[ t ] == max_count:
        max_t.append( t )

max_t.sort()

for t in max_t:
    print( t )