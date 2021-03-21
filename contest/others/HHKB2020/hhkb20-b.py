h, w = map( int, input().split() )
s = []
for _ in range( h ):
    s_i = list( input() )
    s.append( s_i )

# print( s )

futon = 0
for i in range( h ):
    for j in range( w ):
        if s[ i ][ j ] == ".":
            if i < h - 1:
                if s[ i + 1 ][ j ] == ".":
                    futon += 1
            if j < w - 1:
                if s[ i ][ j + 1 ] == ".":
                    futon += 1

print( futon )