#User function Template for python3

class Solution:
    def isPossible(self, paths):
		# Code here
		row = len(paths)
		col = len(paths[0])
		count = 0
		
		for i in range(row):
			for j in range(col):
				if paths[i][j] == 1:
					count += 1
			if count % 2 != 0:
				return 0
		return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		paths = []
		for _ in range(n):
			cur = list(map(int, input().split()))
			paths.append(cur)
		obj = Solution()
		ans = obj.isPossible(paths)
		print(ans)

# } Driver Code Ends