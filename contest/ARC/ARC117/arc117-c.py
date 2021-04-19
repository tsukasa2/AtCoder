N = int( input() )
c = str( input() )

def next_block( x, y ):
    if x == "B":
        if y == "B":
            return "B"
        elif y == "R":
            return "W"
        else:
            return "R"
    elif x == "W":
        if y == "R":
            return "B"
        elif y == "W":
            return "W"
        else:
            return "R"
    else:
        if y == "W":
            return "B"
        elif y == "B":
            return "W"
        else:
            return "R"

# N *= 10
# c = c * 10
for _ in range( N ):
    next_c = ""
    for i in range( len( c ) - 1 ):
        next_c += next_block( c[ i ], c[ i + 1 ] )
    c = next_c
    print( c )