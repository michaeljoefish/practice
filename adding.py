# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = ListNode()
        lagp = None
        outp = head

        np1 = l1
        np2 = l2

        while (np1 != None) and (np2 != None):
            temp = np1.val + np2.val + outp.val
            if temp > 9:
                print('i',temp)
                outp.val = temp%10
                carry = 1
            else:
                print('e',temp)
                outp.val = temp
                carry = 0
            np1 = np1.next
            np2 = np2.next
            outp.next = ListNode(carry)

            lagp = outp
            outp = outp.next

        while (np1 != None):
            temp = np1.val + outp.val
            if temp > 9:
                print('i',temp)
                outp.val = temp%10
                carry = 1
            else:
                print('e',temp)
                outp.val = temp
                carry = 0
            np1 = np1.next
            outp.next = ListNode(carry)

            lagp = outp
            outp = outp.next

        while (np2 != None):
            temp = np2.val + outp.val
            if temp > 9:
                print('i',temp)
                outp.val = temp%10
                carry = 1
            else:
                print('e',temp)
                outp.val = temp
                carry = 0
            np2 = np2.next
            outp.next = ListNode(carry)

            lagp = outp
            outp = outp.next

        if lagp.next.val == 0:
            lagp.next = None
        return head

def main():
    bob = Solution()

    l4 = ListNode(val=5)
    l3 = ListNode(val=3, next=l4)
    l2 = ListNode(val=4, next=l3)
    l1 = ListNode(val=2, next=l2)

    b3 = ListNode(val=7)
    b2 = ListNode(val=6, next=b3)
    b1 = ListNode(val=5, next=b2)

    head = bob.addTwoNumbers(l1, b1)

    np = head
    print('hv', head.val)
    print('hn', head.next)
    print("fuck")
    while np != None:
        print(np.val)
        np = np.next

if __name__ == "__main__":
    main()