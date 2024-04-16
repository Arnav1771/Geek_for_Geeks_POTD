#User function Template for python3
#User function Template for 

class Solution:
    def countElements(self, a, b, n, query, q):
        size = max(max(a),max(b))
        memo = [0]*(size+1)
        ans = []
        for i in range(n):
            memo[b[i]] +=1
        
        for i in range(1,size+1):
            memo[i] += memo[i-1]
        for i in range(q):
            ans.append(memo[a[query[i]]])
        return ans

        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    q = int(input())
    query = []
    ob = Solution()
    for i in range(q):
        query.append(int(input()))
    ans = ob.countElements(a, b, n, query, q)
    for i in range(q):
        print(ans[i])

# } Driver Code Ends