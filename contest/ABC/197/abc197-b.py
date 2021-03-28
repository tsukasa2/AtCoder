H, W, X, Y = map( int, input().split() )
S = [ str( input() ) for _ in range( H ) ]

ans = 1

x, y = X - 1 , Y - 1
while x > 0:
    if S[ x - 1 ][ y ] == ".":
        ans += 1
        x -= 1
    else:
        break

x, y = X - 1 , Y - 1
while x < H - 1:
    if S[ x + 1 ][ y ] == ".":
        ans += 1
        x += 1
    else:
        break

x, y = X - 1 , Y - 1
while y > 0:
    if S[ x ][ y - 1 ] == ".":
        ans += 1
        y -= 1
    else:
        break

x, y = X - 1 , Y - 1
while y < W - 1:
    if S[ x ][ y + 1 ] == ".":
        ans += 1
        y += 1
    else:
        break

print( ans )