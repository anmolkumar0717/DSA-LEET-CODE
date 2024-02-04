# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp1=temp=head
        temp_next=head.next
        link_len=1
        while(temp.next!=None):
            temp=temp.next
            link_len+=1

        new_n=link_len-n

        if (new_n==0):

            if(link_len==1):
                return None
            else:
                return head.next

        elif(new_n==1):
            temp1.next=temp_next.next
            return head
        else:
            i=0
            while(i<new_n-1):
                temp1=temp1.next
                temp_next=temp_next.next
                i+=1
                
            temp1.next=temp_next.next
            return head


        


        
        
            


            
        