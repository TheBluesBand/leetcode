# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        comp1, comp2 = 0, 0
        multiplier = 1
        while l1 != None or l2 != None:
            comp1 += (l1.val if l1 else 0) * multiplier
            comp2 += (l2.val if l2 else 0) * multiplier
            multiplier *= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        output = [int(char) for char in str(comp1 + comp2)[::-1]]
        
        head = None
        tail = None
        for value in output:
            new_node = ListNode(value)
            if not head:  # Initialize head and tail on first iteration
                head = tail = new_node
            else:
                tail.next = new_node
                tail = new_node

        return head