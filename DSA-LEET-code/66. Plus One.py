class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0


        digits1 = []
        for i in range(-1, -(len(digits) + 1), -1):
            if digits[-1] < 9:
                digits[-1] += 1
                return(digits)
            elif len(digits) == 1 and digits[i] == 9:
                digits1.insert(0, 0)
                digits1.insert(0, 1)
            elif (digits[i]==9):
                if i == -1:
                    digits1.insert(0, 0)
                    carry += 1
                elif (i == -len(digits) and carry == 1):
                    digits1.insert(0, 0)
                    digits1.insert(0, 1)
                elif(carry==1):
                    digits1.insert(0, 0)
                else:
                    digits1.insert(0,9)

            else:
                if carry == 1:
                    digits1.insert(0, digits[i] + 1)
                    carry = 0
                else:
                    digits1.insert(0, digits[i])
        return(digits1)
