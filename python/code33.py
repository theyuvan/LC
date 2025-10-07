# Question : 
# Given the head of a singly linked list, reverse the list, and return the reversed list.
# If the input is [1,2,3,4,5], then the output should be [5,4,3,2,1].

# Answer

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None

        stack = []
        current = head
        while current:
            stack.append(current)
            current = current.next

        new_head = stack.pop()
        current = new_head
        while stack:
            node = stack.pop()
            current.next = node
            current = node
        
        current.next = None
        return new_head
        

def linked_list(arr):
    head = ListNode()
    current = head

    for val in arr:
        current.next = ListNode(val)
        current = current.next
    
    return head.next

sol = Solution()
head = linked_list([1,2,3,4,5])
res = sol.reverseList(head)
print(res)