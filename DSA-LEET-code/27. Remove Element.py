class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        while (i<len(nums)):
            if(nums[i]==val):
                if(i==0):
                    nums.pop(i)
                    continue

                else:
                    nums.pop(i)
                    i-=1

            else:
                i+=1
            
                
            
       
