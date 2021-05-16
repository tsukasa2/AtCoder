S = str( input() )

count = { "o": 0, "x": 0, "?": 0 }
for d in S:
    count[ d ] += 1

ans = 0
if count[ "o" ] > 4:
    ans = 0
elif count[ "o" ] == 4:
    ans = 24
elif count[ "o" ] == 3:
    ans += count[ "?" ] * 24
    ans += 3 * 12
elif count[ "o" ] == 2:
    ans += ( count[ "?" ] * ( count[ "?" ] - 1 ) // 2 ) * 24
    ans += count[ "?" ] * 12
    ans += count[ "?" ] * 2 * 12
    ans += 6
    ans += 8
elif count[ "o" ] == 1:
    ans += ( count[ "?" ] + 1 ) ** 4 - count[ "?" ] ** 4
else:
    ans += count[ "?" ] ** 4

print( ans )