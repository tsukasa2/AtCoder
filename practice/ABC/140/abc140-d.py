N, K = map( int, input().split() )
S = str( input() )

def happiness( s ):
    happy = 0
    for i in range( len( s ) ):
        if s[ i ] == "L":
            if i > 0:
                if s[ i - 1 ] == "L":
                    happy += 1
        else: # s[ i ] == "R"
            if i < len( s ) - 1:
                if s[ i + 1 ] == "R":
                    happy += 1
    return happy

def count_RL( s ):
    count = 0
    for i in range( len( s ) - 1 ):
        if s[ i ] == "R" and s[ i + 1 ] == "L":
            count += 1
    return count

def count_LR( s ):
    count = 0
    for i in range( len( s ) - 1 ):
        if s[ i ] == "L" and s[ i + 1 ] == "R":
            count += 1
    return count

print( happiness( S ) + min( count_RL( S ) + count_LR( S ), K * 2 ) )