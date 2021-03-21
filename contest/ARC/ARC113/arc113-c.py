S = str( input() )

length = len( S )

start = []
chara = { S[ 0 ] : 0 }
for i in range( len( S ) - 2 ):
    if ( S[ i ] == S[ i + 1 ] ) and ( not S[ i + 1 ] == S[ i + 2 ] ):
        start.append( ( i, S[ i ] ) )
    chara[ S[ i ] ] = 0

# print( start )
count = [ chara ]
import copy
for i, c in enumerate( S ):
    try:
        count[ i ][ c ] += 1
    except KeyError:
        count[ i ][ c ] = 1
    count.append( copy.deepcopy( count[ -1 ] ) )

# print( count )

if not start:
    print( 0 )
    exit()

prev_i, prev_c = start[ -1 ]
ans = length - ( prev_i + 1 ) - ( count[ length ][ prev_c ] - count[ prev_i ][ prev_c ] )
for i, c in reversed( start[ :-1 ] ):
    if prev_c != c:
        ans += length - ( i + 1 ) - ( count[ prev_i ][ c ] - count[ i ][ c ] )
    prev_i, prev_c = i, c

print( ans )
