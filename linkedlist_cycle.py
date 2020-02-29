# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 普通查找
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        searched = {}
        while head:
            searched[id(head)] = head
            if id(head.next) in searched:
                return True
            else:
                if head.next:
                    head = head.next
                else:
                    return False
        return False


# 快慢指针
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return head
        slow = head
        quick = head
        while quick and slow:
            slow = slow.next
            if quick.next:
                quick = quick.next.next
            else:
                return False
            if quick is slow:
                return True
        return False