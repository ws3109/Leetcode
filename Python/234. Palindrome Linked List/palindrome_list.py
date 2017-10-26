# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def find_mid(node):
            fast = node
            slow = node
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        def reverse(node):
            pre = None
            while node:
                temp = node.next
                node.next = pre
                pre = node
                node = temp
            return pre
        
        if not head or not head.next:
            return True
        mid = find_mid(head)
        head2 = reverse(mid)
        while head and head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        return True
        
        
