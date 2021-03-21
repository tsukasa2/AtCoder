n, m = input().split()
a = input().split()
total = 0

for a_i in a:
    total = total + int(a_i)

print( max( int(n)-total, -1 ) )