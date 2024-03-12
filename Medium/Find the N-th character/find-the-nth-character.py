#User function Template for python3

class Solution:
    def nthCharacter(self, s, r, n):
        odd_cnt = 0
        while r > 0:
            odd_cnt += n % 2
            n //= 2
            r -= 1
        if odd_cnt % 2 == 0:
            return s[n]
        else:
            return '1' if s[n] == '0' else '0'








#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        snr = input().split()
        S, R, N = snr[0], int(snr[1]), int(snr[2])
        ob = Solution()
        print(ob.nthCharacter(S, R, N))
# } Driver Code Ends