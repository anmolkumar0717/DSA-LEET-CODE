class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n=len(skill)
        i=0
        j=n-1
        count=0
        while(j-i!=1):
            if((skill[i]+skill[j])==(skill[i+1]+skill[j-1])):
                count+=(skill[i]*(skill[j]))
            else:
                return -1
            i+=1
            j-=1
        return count+(skill[i]*skill[j])
