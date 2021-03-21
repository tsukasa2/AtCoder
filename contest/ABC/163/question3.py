n = input()
a = input().split()
out = [0] * int(n)

#for i in range( int(n) ):
#    print( a.count(str(i+1)) )

for a_i in a:
    a_i = int(a_i)
    out[a_i-1] += 1

for out_i in out:
    print( out_i )
