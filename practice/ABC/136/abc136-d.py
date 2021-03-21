S = str( input() )

substrings = S.split( "LR" )
for i in range( len( substrings ) ):
    substrings[ i ] = "R" + substrings[ i ] + "L"

substrings[ 0 ] = substrings[ 0 ][1:]
substrings[ -1 ] = substrings[ -1 ][:-1]
# S = "RRLLLLRLRRLL"のときsubstrings = [ "RRLLLL", "RL", "RRLL" ]

# print( substrings )

ans = []
for s in substrings:
    r = 0
    while s[ r + 1 ] != "L":
        r += 1
    l = r + 1
    # s = "RRLLLL"のときr = 1，l = 2

    ans_s = [ 0 for _ in range( len( s ) ) ]
    for i, c in enumerate( s ):
        if c == "R" and ( r - i ) % 2 == 0:
            ans_s[ r ] += 1
        elif c == "L" and ( i - l ) % 2 == 1:
            ans_s[ r ] += 1
        else:
            ans_s[ l ] += 1
    # s = "RRLLLL"のときans_s = [ 0, 3, 3, 0, 0, 0 ]
    
    ans.append( " ".join( map( str, ans_s ) ) )

print( " ".join( ans ) )