S = str( input() )

ans = "Yes"

i = 0
while i < len( S ):
    if S[ i ] == "L":
        ans = "No"
    i += 2

i = 1
while i < len( S ):
    if S[ i ] == "R":
        ans = "No"
    i += 2

print( ans )