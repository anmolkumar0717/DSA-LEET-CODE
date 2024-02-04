class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i=0
        length=len(s)//2
        while(i<length):
            s[i],s[len(s)-i-1]=s[len(s)-i-1],s[i]
            i+=1
            
            