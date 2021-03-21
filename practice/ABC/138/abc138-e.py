s = str( input() )
t = str( input() )

l_s = len( s )
INF = 10 ** 5 + 100
komoji = "abcdefghijklmnopqrstuvwxyz"

first_found = [ {} for _ in range( l_s ) ]
# first_found[ i ][ c ] = sのi文字目以降でcが初めて出現するところ

import copy
first_found[ -1 ][ s[ -1 ] ] = l_s - 1
for i in reversed( range( l_s - 1 ) ):
    first_found[ i ] = copy.deepcopy( first_found[ i + 1 ] )
    first_found[ i ][ s[ i ] ] = i

# print( first_found )

ans = 0
i = 0
for t_j in t:
    # print( "PRINT_DEBUG", i, t_j, ans )
    try:
        next_i = first_found[ i ][ t_j ]
        ans += next_i - ( i - 1 )
        i = ( next_i + 1 ) % l_s
    except KeyError:
        ans += ( l_s - 1 ) - ( i - 1 )
        i = 0
        # print( "PRINT_DEBUG", i, t_j, ans )
        try:
            next_i = first_found[ i ][ t_j ]
            ans += next_i - ( i - 1 )
            i = ( next_i + 1 ) % l_s
        except KeyError:
            print( -1 )
            break
else:
    print( ans )