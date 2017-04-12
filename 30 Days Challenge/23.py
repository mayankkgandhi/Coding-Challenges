    def getHeight(self,root):
        
        if root is None:
            return -1
        else:
            leftheight = 1+ self.getHeight(root.left)
            rightheight = 1 +self.getHeight(root.right)
            
            return max(leftheight,rightheight) 
