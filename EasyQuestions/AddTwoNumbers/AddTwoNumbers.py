#Definition for singly-linked list.
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
        while l1 is not None or l2 is not None:
            temp1 = 0
            temp2 = 0

            if l1.val == None:
                temp1 = l1.val
            else:
                temp1 = 0

            if l2.val == None:
                temp2 = l1.val
            else:
                temp2 = 0