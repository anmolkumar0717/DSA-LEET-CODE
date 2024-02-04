# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        str1=""
        while(head!=None):
            str1+=str(head.val)
            head=head.next
        print(str1)
        return int(str1,2)
