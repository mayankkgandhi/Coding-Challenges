N = int(raw_input())
for j in range(N):
    s = raw_input()
    even = ""
    odd = ""

    for i, c in enumerate(s):   
        if (i & 1) == 0:          
            even += c
            
        else:
            odd += c
            
    print even,odd
