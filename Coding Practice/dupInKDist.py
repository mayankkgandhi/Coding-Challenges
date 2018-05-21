# Check if a given array contains duplicate elements within k distance from each other


def duplicateinArray(a,l,k):
    m = dict()
    for i in range (0,l):
        if a[i] in m.keys():
            print m
            return True
        
        m[a[i]] = 1
            
        # print m
        if(i>=k):
            print a[i]
            m.pop(a[i])
        
        
    return False
            

A= [10, 5, 3, 4, 3, 5, 6]

if duplicateinArray(A,len(A),3):
    print "YES"
else:
    print "NO"
