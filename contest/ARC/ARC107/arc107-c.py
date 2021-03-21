N, K = map( int, input().split() )
a = []
for _ in range( N ):
    a_i = list( map( int, input().split() ) )
    a.append( a_i )

MOD = 998244353

swappable_line, swappable_raw = [], []
connected_line = [ [] for _ in range( N ) ]
connected_raw = [ [] for _ in range( N ) ]

for x in range( N - 1 ):
    for y in range( x + 1, N ):
        flag = True
        for i in range( N ):
            if a[ x ][ i ] + a[ y ][ i ] > K:
                flag = False
        
        if flag == True:
            swappable_line.append( ( x, y ) )
            connected_line[ x ].append( y )
            connected_line[ y ].append( x )

for x in range( N - 1 ):
    for y in range( x + 1, N ):
        flag = True
        for i in range( N ):
            if a[ i ][ x ] + a[ i ][ y ] > K:
                flag = False
        
        if flag == True:
            swappable_raw.append( ( x, y ) )
            connected_raw[ x ].append( y )
            connected_raw[ y ].append( x )

group_line = [ -1 for _ in range( N ) ]
group_line_id = 0

def search_line( v, group_line_id ):
    group_line[ v ] = group_line_id
    for w in connected_line[ v ]:
        if group_line[ w ] == -1:
            search_line( w, group_line_id )

for v in range( N ):
    if group_line[ v ] > -1:
        continue
    search_line( v, group_line_id )
    group_line_id += 1

group_raw = [ -1 for _ in range( N ) ]
group_raw_id = 0

def search_raw( v, group_raw_id ):
    group_raw[ v ] = group_raw_id
    for w in connected_raw[ v ]:
        if group_raw[ w ] == -1:
            search_raw( w, group_raw_id )

for v in range( N ):
    if group_raw[ v ] > -1:
        continue
    search_raw( v, group_raw_id )
    group_raw_id += 1

group_line_nums = [ 0 for _ in range( group_line_id ) ]
group_raw_nums = [ 0 for _ in range( group_raw_id ) ]
for i in range( N ):
    group_line_nums[ group_line[ i ] ] += 1
for i in range( N ):
    group_raw_nums[ group_raw[ i ] ] += 1

fact = [ 1 ]
for i in range( 1, N + 1 ):
    fact.append( fact[ -1 ] * i % MOD )

# print( group_line_nums, group_raw_nums )
# print( fact )

ans = 1
for i in range( group_line_id ):
    ans = ans * fact[ group_line_nums[ i ] ] % MOD
for i in range( group_raw_id ):
    ans = ans * fact[ group_raw_nums[ i ] ] % MOD

print( ans )