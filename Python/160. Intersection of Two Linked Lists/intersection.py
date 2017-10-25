# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lA, lB = 0, 0
        nodeA, nodeB = headA, headB
        while nodeA != None:
            nodeA = nodeA.next
            lA = lA + 1
        while nodeB != None:
            nodeB = nodeB.next
            lB = lB + 1
        if lB < lA:
            headA, headB, lA, lB = headB, headA, lB, lA
        for i in range(lB - lA):
            headB = headB.next
        while headA != None and headB != None:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
        
