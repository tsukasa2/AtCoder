# h, n = map( int, input().split() )
# a = []
# b = []
# for _ in range( n ):
#     a_i, b_i = map( int, input().split() )
#     a.append( a_i )
#     b.append( b_i )

# best_eff = -1
# best_i = -1
# for i in range( n ):
#     eff = a[ i ] / b[ i ]
#     if best_eff < eff:
#         best_eff = eff
#         best_i = i

# mana = ( h // a[ best_i ] ) * b[ best_i ]

# rem = h % a[ best_i ]
# best_rem_cost = 10 ** 18 + 1
# best_rem_i = -1
# for i in range( n ):
#     if rem % a[ i ] == 0:
#         rem_cost = ( rem // a[ i ] ) * b[ i ]
#     else:
#         rem_cost = ( rem // a[ i ] + 1 ) * b[ i ]
#     print( "rem_cost : " + str( rem_cost ) )
#     if best_rem_cost > rem_cost:
#         best_rem_cost = rem_cost
#         best_rem_i = i

# mana += best_rem_cost

# print( mana )
# print( best_i, best_rem_i )

##以下ググった
h, n = map( int, input().split() )
a = []
b = []
for _ in range( n ):
    a_i, b_i = map( int, input().split() )
    a.append( a_i )
    b.append( b_i )

dp = [ float( "Inf" ) ] * ( h + 1 )
# dp[ d ] = dを与える最小マナ
dp[ 0 ] = 0
for i in range( h ):
    for j in range( n ):
        update_index = min( i + a[ j ], h )
        dp[ update_index ] = min( dp[ update_index ], dp[ i ] + b[ j ] )

print( dp[ h ] )