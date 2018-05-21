# Given an array A[] and a number x, check for pair in A[] with sum as x

# 1. Sorting based solution

# def pairHasSum(A,length,sum):
#     print A
#     l=0
#     r=length-1
#
#     while(l<r):
#         if (A[l] + A[r] == sum):
#             return A[l],A[r]
#         elif(A[l] + A[r]  < sum):
#             l +=1
#         else:
#             r -= 1
#     return False
#
# A = [1,4,45,6,10,-8]
# n = 16
# result = pairHasSum(sorted(A),len(A),n);
# if (result):
#     print result
#     print "YES"
# else:
#     print "NO"

# 1. Hashing based solution

def printPairs(a,l,n):
    m=dict()
    for i in range(0,l):
        temp= n - a[i]
        if(temp>=0 and temp in m.keys()):
            print "Pairs are " , temp ," and ", a[i]
        m[a[i]] =1
        # print m
A = [1,4,45,6,10,-8]
n = 16
printPairs(A,len(A),n)
