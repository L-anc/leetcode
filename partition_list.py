# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def list_to_listNode(self, lst):
        if type(list) is not list:
            return None
        head = self
        current = head
        for value in lst:
            current.next = ListNode(value)
            current = current.next
        return head
    
    def print(self):
        current = self
        while current:
            print(f"{current.val} -> ")
            current = current.next
        print("None")

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        new_head = head

        end_first = None
        beg_next = None
        found_beg_next = False
        found_end_first = False
        
        node = head
        while node != None:
            if node.val >= x:
                if not found_beg_next:
                    beg_next = node
                    found_beg_next = True
                else:
                    node = node.next

            else:
                if not found_end_first:
                    end_first = node
                    found_end_first = True
                    new_head = end_first
                else:
                    end_first.next = node
                    temp = node.next
                    node.next = beg_next
                    node = temp

        return new_head

t = ListNode(1)
t.list_to_listNode([1, 4, 3, 2, 5, 2])
t.print()  # Expected output: 1 -> 4 -> 3 -> 2 -> 5 -> 2 -> None

sol = Solution()
result = sol.partition(test, 3)
result.print()  # Expected output: 1 -> 2 -> 2 -> 4 -> 3 -> 5 -> None
        