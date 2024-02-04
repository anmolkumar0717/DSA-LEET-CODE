# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        temp=head
        temp1=head.next
        while(temp1!=None):
            if (temp.val==temp1.val):
                temp.next=temp1.next
                temp1=temp1.next
            else:
                temp1=temp1.next
                temp=temp.next
        return head
            
