# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Accepted
# 1568/1568 cases passed (64 ms)
# Your runtime beats 83.45 % of python3 submissions
# Your memory usage beats 31.88 % of python3 submissions (15 MB)


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        first_cur = l1
        second_cur = l2
        sum_cur = dummy_head = ListNode(None,None)
        add = 0
        while first_cur or second_cur:
            if first_cur:
                first_num, first_cur = first_cur.val, first_cur.next
            else:
                first_num = 0
            if second_cur:
                second_num, second_cur = second_cur.val, second_cur.next
            else:
                second_num = 0
            sum, add = (first_num + second_num + add)%10, (first_num + second_num + add)//10
            sum_cur.next = ListNode(sum,None)
            sum_cur = sum_cur.next
        if add > 0:
            sum_cur.next = ListNode(add,None)      
        return dummy_head.next