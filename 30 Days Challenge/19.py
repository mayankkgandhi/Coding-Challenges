
class Solution:
    # Write your code here
    def __init__(self):
        self.stack=[]
        self.queue=[]
        
    def pushCharacter(self,item):
        self.stack.append(item)
      
    def enqueueCharacter(self,item):
        self.queue.append(item)
        
    def popCharacter(self):
        return self.stack.pop()
    
    def dequeueCharacter(self):       
        return self.queue.pop(0)
        
