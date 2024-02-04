class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count1=0
        count2=0
        for i in range(len(word)):
            if (ord(word[i])<97):
                count1+=1
            elif(ord(word[i])>96):
                count2+=1
        if (count1==len(word)or count2==len(word) or len(word)==1):
            return True
        elif((ord(word[0])<97) and count2==len(word)-1):
            return True
        else:
            return False
        