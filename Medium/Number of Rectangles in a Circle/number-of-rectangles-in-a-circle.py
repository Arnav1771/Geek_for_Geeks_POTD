#User function template for Python

class Solution:
    def rectanglesInCircle(self,r):
        #code here
        count = 0
        R = 2 * r
        radius_squared = r*r
        
        for length in range(1,R + 1):
            for width in range(1,R + 1):
                half_length = length/2
                half_width =  width/2
                
                if (half_length**2 + half_width**2) <= radius_squared:
                    count+=1
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python

import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.rectanglesInCircle(N)
        print(ans)

# } Driver Code Ends