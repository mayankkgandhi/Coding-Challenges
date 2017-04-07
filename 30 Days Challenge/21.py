import sys


n = int(raw_input().strip())
a =map(int,raw_input().strip().split(' '))

numswaps=0
for i in range (n):
    for j in range (n-i-1):
        if a[j]> a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            numswaps=numswaps+1
           
        
print 'Array is sorted in %d swaps.'  % (numswaps)
print 'First Element: %d' % (a[0])
print 'Last Element: %d '%  (a[-1])
