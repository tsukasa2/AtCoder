S = str( input() )

T = ""
reverse = False
for c in S:
    if c == "R":
        reverse = not reverse
    else:
        if len( T ) == 0:
            T += c
        else:
            if reverse == False:
                if T[ -1 ] == c:
                    T = T[ : -1 ]
                else:
                    T += c
            else:
                if T[ 0 ] == c:
                    T = T[ 1 : ]
                else:
                    T = c + T

if reverse == False:
    print( T )
else:
    print( T[ :: -1 ] )