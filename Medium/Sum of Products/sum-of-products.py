#User function Template for python3

class Solution:
    def pairAndSum(self, N, Arr):
        #code here
        ans = 0
        for i in range(31, -1, -1):
            count = 0
            for j in range(N):
                r = Arr[j]
                x = 1
                p = x << i
                if r & p:
                    count += 1
            ans += (((count * (count - 1)) // 2) * (2 ** i))
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        Arr=list(map(int,input().strip().split(' ')))
        ob=Solution()
        print(ob.pairAndSum(N,Arr))
# } Driver Code Ends