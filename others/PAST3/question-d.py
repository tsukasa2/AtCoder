n = int( input() )
s = []
for _ in range( 5 ):
    s_i = str( input() )
    s.append( s_i )

num = []

for m in range( n ):
    d1 = s[0][ 4*m+1 : 4*m+4 ]
    d2 = s[1][ 4*m+1 : 4*m+4 ]
    d3 = s[2][ 4*m+1 : 4*m+4 ]
    d4 = s[3][ 4*m+1 : 4*m+4 ]
    if d1 == ".#.":
        num.append( "1" )
        continue
    elif d1 == "#.#":
        num.append( "4" )
        continue
    else:
        if d2 == "#..":
            if d4 == "..#":
                num.append( "5" )
                continue
            else:
                num.append( "6" )
                continue
        elif d2 == "#.#":
            if d3 == "#.#":
                num.append( "0" )
                continue
            else:
                if d4 == "#.#":
                    num.append( "8" )
                    continue
                else:
                    num.append( "9" )
                    continue
        else:
            if d3 == "..#":
                num.append( "7" )
                continue
            else:
                if d4 == "#..":
                    num.append( "2" )
                    continue
                else:
                    num.append( "3" )
                    continue

print( "".join( num ) )