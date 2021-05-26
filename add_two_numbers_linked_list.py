# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2 ,c = 0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = ListNode(0)
        ret_tail = ret
        while(l1 or l2 or c):
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0 )
            value = val1 + val2 + c
            c = value // 10
            cur_add = value % 10
            ret_tail.next = ListNode(cur_add)
            ret_tail = ret_tail.next
       
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
            
        return ret.next
            
            
