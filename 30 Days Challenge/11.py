
import sys

n = int(raw_input().strip())
count = 0;
binnum = bin(n)[2:].split('0')
print (binnum )
for i in range(len(binnum )):
    leni = len(binnum [i])
    if (leni>count):
        count = leni
print count
    
    
