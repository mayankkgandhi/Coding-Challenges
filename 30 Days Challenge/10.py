#1) Basic sol
def factorial(n):
    if n is 1:
        return n
    else:
        return (n * factorial(n-1))
if __name__ == '__main__':
    
    N=int(raw_input())        
    print(factorial(N))
    
# Advance sol
factorial = lambda x : 1 if x<=1 else x*factorial(x-1)
print(factorial(int(raw_input()))
