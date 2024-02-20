#User function Template for python3

def solve(s, d, n, i, memo):
    if i >= n:
        return True
    if i in memo:
        return memo[i]
    res = False
    for j in range(i, n):
        res = res or ((s[i:j+1] in d) and solve(s, d, n, j+1, memo))
    memo[i] = res
    return res

class Solution:
    def wordBreak(self, n, s, dictionary):
        d = set(dictionary)
        return solve(s, d, len(s), 0, {})


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		n = int(input())
		dictionary = [word for word in input().strip().split()]
		s = input().strip()
		ob = Solution()
		res = ob.wordBreak(n, s, dictionary)
		if res:
			print(1)
		else:
			print(0)
# } Driver Code Ends