#User function Template for python3

class Solution:
    def canPair(self, nums, k):
        if len(nums) % 2 != 0:
            return False
        
        cnt = [0] * k
        
        for i in nums:
            cnt[i % k] += 1
        
        l, r = 1, k - 1
        
        while l < r:
            if cnt[l] != cnt[r]:
                return False
            l += 1
            r -= 1
        
        if (l == r and cnt[l] % 2 != 0) or cnt[0] % 2 != 0:
            return False
        
        return True
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, k = input().split()
		n = int(n)
		k = int(k)
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.canPair(nums, k)
		if(ans):
			print("True")
		else:
			print("False")
# } Driver Code Ends