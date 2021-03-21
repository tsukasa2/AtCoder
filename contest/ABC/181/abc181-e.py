N, M = map( int, input().split() )
H = list( map( int, input().split() ) )
W = list( map( int, input().split() ) )

H_sorted = [ 0 ] + sorted( H ) + [ 10 ** 10 ]
W_sorted = sorted( W )

# print( H_sorted, W_sorted )

insert = []
index = 0

for i in range( N + 1 ):
    if index == M:
        break
    while H_sorted[ i ] <= W_sorted[ index ] and W_sorted[ index ] <= H_sorted[ i + 1 ]:
        insert.append( i )
        index += 1
        if index == M:
            break

# print( insert )

l_ruisekiwa = [ 0 ]
r_ruisekiwa = [ 0 ]
for i in range( ( N + 1 ) // 2 ):
    l_ruisekiwa.append( l_ruisekiwa[ -1 ] - H_sorted[ 2 * i + 1 ] + H_sorted[ 2 * i + 2 ] )
    r_ruisekiwa.append( r_ruisekiwa[ -1 ] - H_sorted[ 2 * i ] + H_sorted[ 2 * i + 1 ] )

# print( l_ruisekiwa, r_ruisekiwa )

ans_cand = []

for i in range( M ):
    ans_i = l_ruisekiwa[ insert[ i ] // 2 ]
    if insert[ i ] % 2 == 0:
        ans_i += abs( W_sorted[ i ] - H_sorted[ insert[ i ] + 1 ] )
    else:
        ans_i += abs( W_sorted[ i ] - H_sorted[ insert[ i ] ] )
    ans_i += r_ruisekiwa[ -1 ] - r_ruisekiwa[ insert[ i ] // 2 + 1]
    ans_cand.append( ans_i )
    # print( insert[ i ], l_ruisekiwa[ insert[ i ] // 2 ], abs( W_sorted[ i ] - H_sorted[ insert[ i ] + 1 ] ), r_ruisekiwa[ insert[ i ] // 2 ] )

print( min( ans_cand ) )