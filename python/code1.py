# Question : 
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.


# Answer

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        head = ListNode()
        temp = head

        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            
            else:
                temp.next = list2
                list2 = list2.next

            temp = temp.next
        
        temp.next = list1 or list2

        return head.next


def linked_list(arr):
    head = ListNode()
    current = head

    for val in arr:
        current.next = ListNode(val)
        current = current.next

    return head.next

sol = Solution()
list1 = linked_list([1,2,4])
list2 = linked_list([1,3,4])
res = sol.mergeTwoLists(list1,list2)
print(res)