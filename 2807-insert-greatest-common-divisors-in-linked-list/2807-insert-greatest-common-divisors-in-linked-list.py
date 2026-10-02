# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a,b):
            while(b):
                a,b=b,a%b
            return a
        temp=head
        while(temp.next):
            val1=temp.val
            val2=temp.next.val
            maxy=max(val1,val2)
            miny=min(val1,val2)
            val3=gcd(miny,maxy)
            new=ListNode(val3)
            new.next=temp.next
            temp.next=new
            temp=temp.next.next
        return head
        