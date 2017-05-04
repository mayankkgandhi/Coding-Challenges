from __future__ import print_function
import sys
import re

lst=[]
N = int(raw_input().strip())
for a0 in xrange(N):
    firstName,emailID = raw_input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    if re.search('@gmail\.com$',emailID):      
        lst.append(firstName)
        
print(*sorted(lst),sep='\n')
