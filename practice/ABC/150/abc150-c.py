n = int( input() )
p = tuple( map( int, input().split() ) )
q = tuple( map( int, input().split() ) )

import itertools
permutations = list( itertools.permutations( range( 1, n + 1 ) ) )
p_order = permutations.index( p )
q_order = permutations.index( q )

print( abs( p_order - q_order ) )

# kaijo = [ 1 ]
# for k in range( n ):
#     kaijo.append( kaijo[ -1 ] * ( k + 1 ) )

# print( kaijo )

# import copy

# def make_list( s, used, length ):
#     if length == n:
#         seq_list.append( s )
#         return
#     else:
#         for k in range( n ):
#             print( s, used, length )
#             if used[ k ] == 1:
#                 continue
#             else:
#                 next_used = copy.deepcopy( used )
#                 next_used[ k ] = 1
#                 make_list( s + str( k + 1 ), next_used, length + 1 )

# make_list( "", [ 0 for _ in range( n ) ], 0 )

# print( seq_list )