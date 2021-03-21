n = int( input() )
s = []
for _ in range( n ):
    s_i = str( input() )
    s.append( s_i )

cnt = { "AC" : 0, "WA" : 0, "TLE" : 0, "RE" : 0 }

for s_i in s:
    cnt[ s_i ] += 1

print( "AC x " + str( cnt[ "AC" ] ) )
print( "WA x " + str( cnt[ "WA" ] ) )
print( "TLE x " + str( cnt[ "TLE" ] ) )
print( "RE x " + str( cnt[ "RE" ] ) )