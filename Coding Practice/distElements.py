#Count distinct elements in every window of size k

def findDistinct(arr,l,k):
    m=dict()
    dist_count = 0 
    for i in range (0,k):

        if arr[i] in m.keys():
            # print m[arr[i]]
            m[arr[i]] +=1
        else:
            m[arr[i]] = 1
            dist_count += 1
            
    print "First Window is", m  
    print " Dist Count =",dist_count
    # print k
    for i in range(k,l):
        if m[arr[i-k]] == 1:
            dist_count -= 1
            m.pop(arr[i-k])
        else:
            m[arr[i-k]] -= 1
        # print m
        # print arr[i]
        if arr[i] in m.keys():
            m[arr[i]] +=1
        else:
            m[arr[i]] = 1
            dist_count += 1
        
        print "Current Window is", m   
        print " Dist Count =",dist_count


A=[1, 2, 1, 3, 4, 2, 3]
print A
findDistinct(A,len(A),4)
