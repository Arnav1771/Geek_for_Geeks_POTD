#User function Template for python3

class Solution:
    def minRow(self,n,m,a):
        #code here
        min_cnt = float('inf')
        index = -1
        for i in range(N):
            count = 0
            for j in range(M):
                if A[i][j] == 1:
                    count +=1
            if count < min_cnt:
                min_cnt = count
                index = i + 1
        return index


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(" "))
        A=[]
        for i in range(N):
            B=list(map(int,input().strip().split(" ")))
            A.append(B)
        ob=Solution()
        print(ob.minRow(N,M,A))
# } Driver Code Ends