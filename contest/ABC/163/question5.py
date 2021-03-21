import math
n = input()
n = int(n)
a = input().split()
kept_a = a
out = 0 
move = [-1] * n
    
def max_move(a):
    maximum = -1
    i = -1
    for a_i in a:
        move_i = a_i * max( a.index(a_i), len(a)-a.index(a_i) )
        if move_i >= 0 and move_i > maximum:
            maximum = move_i
            #i = 0 if a.index(a_i) > len(a)-a.index(a_i) else len(a)
            i = a.index(a_i)
    return maximum, i

for k in range( len(a) ):
    plus, i = max_move(a)
    out += plus
    a[i] = str(-1)

print(out)