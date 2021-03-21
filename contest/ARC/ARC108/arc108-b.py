N = int( input() )
s = str( input() )

prev_c = ""
ans = N

queue = [ "none" ]

for c in s:
    s = queue[ -1 ]
    if c == "f":
        queue.append( "f" )
    elif c == "o":
        if s == "f":
            queue[ -1 ] = "fo"
        else:
            queue = [ "none" ]
    elif c == "x":
        if s == "fo":
            ans -= 3
            queue.pop( -1 )
        else:
            queue = [ "none" ]
    else:
        queue = [ "none" ]

    prev_c = c
    # print( c,  queue )


print( ans )

        