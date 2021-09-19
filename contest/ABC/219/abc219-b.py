S_1 = str( input() )
S_2 = str( input() )
S_3 = str( input() )
T = str( input() )

ans = ""
for t in T:
    if t == "1":
        ans += S_1
    elif t == "2":
        ans += S_2
    else:
        ans += S_3

print( ans )