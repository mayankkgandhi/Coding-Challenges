    def levelOrder(self, root):
        traversal = ''
        
        if root is not None:
            queue = [root]
            while queue:
                traversal += str(queue[0].data) + ' '
                if queue[0].left :
                    queue.append(queue[0].left)
                if queue[0].right :
                    queue.append(queue[0].right)
                queue.pop(0)
        print(traversal)
