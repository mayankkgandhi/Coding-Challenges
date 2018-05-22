# Group multiple occurrence of array elements ordered by first occurrence using Hashing

def orderedCount(a,l):
    m = dict()
    
    for i in range(0,l):
        if a[i] in m.keys():
            m[a[i]] += 1
        else:
            m[a[i]] = 1
    # print m
    # {1: 1, 10: 3, 3: 2, 4: 1, 5: 1}
    
    for i in range(0,l):
        count = m[a[i]]
        if count !=0:
            for j in range(0,count):
                print a[i] 
            m[a[i]] =0
        

A=[10, 5, 3, 10, 10, 4, 1, 3]
orderedCount(A,len(A))
