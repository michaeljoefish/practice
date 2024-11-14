# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        outp = head

        np1 = l1
        np2 = l2

        while np1 != None or np2 != None:
            if np1 != None and np2 == None:
                temp = np1.value + carry
                if temp > 9:
                    outp.val = 1
                    carry = temp%10
                else:
                    outp.val = temp
                    carry = 0
                outp.next = ListNode()