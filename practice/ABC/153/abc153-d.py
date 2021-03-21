h = int( input() )

ans = 0
k = 1
while k <= h:
    ans += k
    k *= 2

print( ans )