# Question : 
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
# Return the linked list sorted as well.

# Answer

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = head
        while temp and temp.next:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head

def linked_list(arr):
    head = ListNode()
    current = head

    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return head.next


sol = Solution()
head = linked_list([1,1,2])
res = sol.deleteDuplicates(head)
print(res)