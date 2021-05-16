H, W, M = map( int, input().split() )
bombs = [ tuple( map( int, input().split() ) ) for _ in range( M ) ]

is_bomb = { ( i - 1, j - 1 ) : True for ( i, j ) in bombs }
bomb_v = [ 0 for _ in range( W ) ]
bomb_h = [ 0 for _ in range( H ) ]
for ( i, j ) in bombs:
    bomb_h[ i - 1 ] += 1
    bomb_v[ j - 1 ] += 1

i_cand = []
max_h = max( bomb_h )
for i in range( H ):
    if bomb_h[ i ] == max_h:
        i_cand.append( i )

j_cand = []
max_v = max( bomb_v )
for j in range( W ):
    if bomb_v[ j ] == max_v:
        j_cand.append( j )

ans = -1
for i in i_cand:
    for j in j_cand:
        if is_bomb.get( ( i, j ), False ):
            ans = max_h + max_v - 1
        else:
            ans = max_h + max_v
            break
    else:
        continue
    
    break

print( ans )