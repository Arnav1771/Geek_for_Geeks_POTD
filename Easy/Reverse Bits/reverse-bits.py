
#User function Template for python3

class Solution:
    def reversedBits(self, x):
        # code here
        x = bin(x)[2:]
        x = '0' * (32 - len(x)) + x
        x = x[::-1]
        
        return  int(x,2)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        X=int(input())
        
        ob = Solution()
        print(ob.reversedBits(X))
# } Driver Code Ends