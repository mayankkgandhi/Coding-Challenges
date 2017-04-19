   def removeDuplicates(self,head):
        temp = head
        if head is None :
            return head        
        while temp.next:              
            if (temp.data == temp.next.data):                
                temp.next = temp.next.next  
            else:
                temp = temp.next
        return head
  
