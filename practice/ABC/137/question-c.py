n = int( input() )
s = []
for _ in range( n ):
    s.append( input() )

#print( s )

for i in range( n ):
    s[i] = "".join( sorted( s[i] ) )

#print( s )

found = {}
cnt = 0
for s_i in s:
    if s_i in found:
        found[ s_i ] = found[ s_i ] + 1
    else:
        found[ s_i ] = 0

#print( found )

for key in found:
    c = found[key]
    cnt = cnt + c * ( c + 1 ) // 2

print( cnt ) 