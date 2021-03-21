n = int( input() )
c = list( input() )

c = [ "R" ] + c + [ "W" ]
l = 1
r = n
ans = 0
while l < r:
    while c[ l ] == "R":
        l += 1
    while c[ r ] == "W":
        r -= 1
    if l < r:
        c[ l ] = "R"
        c[ r ] = "W"
        ans += 1

print( ans )