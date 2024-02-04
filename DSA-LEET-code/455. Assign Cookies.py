class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count=0
        s.sort()
        g.sort()
        i=0
        while(i<len(g)):
            for j in s:
                if ((j>=g[i]) and len(s)!=0):
                    count+=1
                    s.remove(j)
                    break

            i+=1
        return(count)