class Solution:
    def addBinary(self, a: str, b: str) -> str:
        str_int=int(a,2)
        str_int2=int(b,2)

        sum1=str_int2+str_int

        rep=bin(sum1).replace("0b","")
        return (str(rep))