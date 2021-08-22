N = int( input() )

ans = 0
b = 1
while b * 2 <= N:
    b *= 2
    ans += 1

print( ans )