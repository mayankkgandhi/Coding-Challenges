#Array 2 is subset of Array 1. 
#Duplicates are taken care of.

def isSubset(l1,l2,m,n):
    a1 = dict()
    if n>m : 
        return
    
    for i in l1:
        # print i
        if i in a1.keys():
            a1[i] += 1
            # print a1[i]
        else:
            a1[i]= 1
            # print a1[i]

    for i in l2:
        
        if a1[i] != 0:
            a1[i] -= 1
            print a1[i]
        else:
            return False
            
    return True
    print a1

l1= [11, 1, 13, 21, 3, 7,3,3]
l2=[11, 3, 7, 1,3,3]
m = len(l1)
n =len(l2)

if(isSubset(l1,l2,m,n)):
    print "l2 is subset of l1"
else:
     print "l2 is not subset of l1"
    
