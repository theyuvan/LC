# Question : 
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
# If the input is [1,2,2,1], then the output should be true.

# Answer

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        stack = []
        current = head
        while current:
            stack.append(current.val) 
            current = current.next
        
        current = head
        while current:
            if current.val != stack.pop():
                return False
            current = current.next
        return True


def linked_list(arr):
    head = ListNode()
    current = head

    for val in arr:
        current.next = ListNode(val)
        current = current.next
    
    return head.next

sol = Solution()
head = linked_list([1,2,2,1])
res = sol.isPalindrome(head)
print(res)