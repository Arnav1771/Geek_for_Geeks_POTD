#User function Template for python3


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class Solution:
    def sort(self, head):
        if not head or not head.next:
            return head
        
        st = head
        temp = st.next
        
        while temp:
            if temp.data >= st.data:
                st = temp
                temp = temp.next
            else:
                st.next = temp.next
                prev = None
                curr = head
                while curr != st and curr.data <= temp.data:
                    prev = curr
                    curr = curr.next
                if prev is None:
                    temp.next = head
                    head = temp
                else:
                    temp.next = curr
                    prev.next = temp
            temp = st.next
        
        return head


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Llist:
    def __init__(self):
        self.head=None
    
    def insert(self,data,tail):
        node=Node(data)
        
        if not self.head:
            self.head=node
            return node
        
        tail.next=node
        return node
        

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        
        n1=int(input())
        arr1=[int(x) for x in input().split()]
        ll1=Llist()
        tail=None
        for nodeData in arr1:
            tail=ll1.insert(nodeData,tail)
            
        
        ob = Solution()
        resHead=ob.sort(ll1.head)
        printList(resHead)
        print()
        
    
    
# } Driver Code Ends