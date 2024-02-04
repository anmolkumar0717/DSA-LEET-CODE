class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if (n==0):
            return False
        else:
            n=n&(n-1)
            if(n==0):
                return True
            else:
                False