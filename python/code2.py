# Question : 
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.


# Answer

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)
    
class Solution:
    def mergeKLists(self, lists):
        head = ListNode()
        temp = head

        while True:
            min_val = float('inf')
            min_index = -1
            for i in range(len(lists)):

                if lists[i] and lists[i].val < min_val:
                    min_val = lists[i].val

                    # print(min_val)
                    min_index = i
                    print(min_index)
            if min_index == -1:
                break
            temp.next = lists[min_index]
            temp = temp.next
            lists[min_index] = lists[min_index].next
        return head.next

def linked_list(arr):
    head = ListNode()
    current = head

    for val in arr:
        current.next = ListNode(val)
        current = current.next

    return head.next

sol = Solution()
lists = [linked_list([1,4,5]), linked_list([1,3,4]), linked_list([2,6])]
res = sol.mergeKLists(lists)
print(res)
