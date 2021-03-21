n = int( input() )
out_sum = 0

for i in range(1, n+1):
    if i % 3 != 0 and i % 5 != 0:
        out_sum += i

print( out_sum )