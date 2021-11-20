S = str( input() )
T = str( input() )

move_S = { c : set() for c in "abcdefghijklmnopqrstuvwxyz" }
move_T = { c : set() for c in "abcdefghijklmnopqrstuvwxyz" }
for i in range( len( S ) ):
    move_S[ S[ i ] ].add( T[ i ] )
    move_T[ T[ i ] ].add( S[ i ] )

ans = "Yes"
for c in "abcdefghijklmnopqrstuvwxyz":
    if len( move_S[ c ] ) > 1 or len( move_T[ c ] ) > 1:
        ans = "No"

print( ans )