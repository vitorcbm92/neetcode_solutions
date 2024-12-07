from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:

    reversed_node = None
    current_node = head

    while current_node is not None:
        next_node = current_node.next
        current_node.next = reversed_node
        reversed_node = current_node
        current_node = next_node

    return reversed_node  

if __name__ == '__main__':
    

    head = ListNode(val = 1, next = ListNode(val = 2, next = ListNode(val = 3, next = ListNode(val = 4, next = ListNode(val = 5, next = None)))))
    result = reverseList(head)
    print(result)
    
    # result = reverseList([1,2])
    # print(result)

    # result = reverseList([])
    # print(result)

