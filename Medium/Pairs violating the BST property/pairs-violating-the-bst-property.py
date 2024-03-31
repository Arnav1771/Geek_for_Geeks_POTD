
from typing import Optional
from collections import deque



class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def pairsViolatingBST(self, n: int, root: Optional[Node]) -> int:
        # Function to perform inorder traversal and count inversions
        def inorder(root):
            if root is None:
                return []
            return inorder(root.left) + [root.data] + inorder(root.right)

        def merge(arr, left, mid, right):
            i, j, k = left, mid + 1, 0
            temp = [0] * (right - left + 1)
            inversion_count = 0

            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp[k] = arr[i]
                    i += 1
                else:
                    temp[k] = arr[j]
                    j += 1
                    inversion_count += (mid - i + 1)
                k += 1

            while i <= mid:
                temp[k] = arr[i]
                i += 1
                k += 1

            while j <= right:
                temp[k] = arr[j]
                j += 1
                k += 1

            for idx in range(left, right + 1):
                arr[idx] = temp[idx - left]

            return inversion_count

        def merge_sort(arr, left, right):
            inversion_count = 0
            if left < right:
                mid = (left + right) // 2
                inversion_count += merge_sort(arr, left, mid)
                inversion_count += merge_sort(arr, mid + 1, right)
                inversion_count += merge(arr, left, mid, right)
            return inversion_count

        # Get the inorder traversal of the tree
        inorder_list = inorder(root)
        
        # Count inversions using merge sort
        inversions = merge_sort(inorder_list, 0, len(inorder_list) - 1)

        return inversions
        



#{ 
 # Driver Code Starts

class Node:
    def __init__(self,val):
        self.data=val
        self.right=None
        self.left=None

# Function to Build Tree
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip=list(map(str,s.split()))

    # Create the root of the tree
    root=Node(int(ip[0]))
    size=0
    q=deque()

    # Push the root to the queue
    q.append(root)
    size=size+1

    # Starting from the second element
    i=1
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1

        # Get the current node's value from the string
        currVal=ip[i]

        # If the left child is not null
        if(currVal!="N"):

            # Create the left child for the current node
            currNode.left=Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]

        # If the right child is not null
        if(currVal!="N"):

            # Create the right child for the current node
            currNode.right=Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

def inputTree():
    treeString=input().strip()
    root = buildTree(treeString)
    return root
def inorder(root):
    if (root == None):
       return
    inorder(root.left);
    print(root.data,end=" ")
    inorder(root.right)

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        root = inputTree();
        
        obj = Solution()
        res = obj.pairsViolatingBST(n, root)
        
        print(res)
        

# } Driver Code Ends