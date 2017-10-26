# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy_head = ListNode(-1)
        cur = dummy_head
        while head and head.next:
            cur.next = head.next
            temp = head.next.next
            head.next.next = head
            head.next = temp
            cur = cur.next.next
            head = head.next
        return dummy_head.next
