# Question : 
# Given the head of a linked list and an integer val,
# remove all the nodes of the linked list that has Node.val == val, and return the new head.
# If the input is [1,2,6,3,4,5,6] and val = 6, then the output should be [1,2,3,4,5].

# Answer

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        temp = ListNode(0)
        temp.next = head
        current = temp
        while current and current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next      
        return temp.next

        
def linked_list(arr):
    head = ListNode()
    current = head

    for val in arr:
        current.next = ListNode(val)
        current = current.next

    return head.next

sol = Solution()
head = linked_list([1,2,6,3,4,5,6])
val = 6
res = sol.removeElements(head, val)
print(res)