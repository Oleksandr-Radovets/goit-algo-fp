
# реверсування однозв'язного списку
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


# Сортування вставками для однозв'язного списку
def insertion_sort_linked_list(head):
    if not head or not head.next:
        return head

    dummy = Node(0)
    dummy.next = head
    curr = head

    while curr.next:
        if curr.next.data < curr.data:
            temp = curr.next
            prev = dummy
            while prev.next.data < temp.data:
                prev = prev.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
        else:
            curr = curr.next

    return dummy.next

# Об'єднання двох відсортованих списків
def merge_sorted_lists(head1, head2):
    dummy = Node(0)
    curr = dummy

    while head1 and head2:
        if head1.data < head2.data:
            curr.next = head1
            head1 = head1.next
        else:
            curr.next = head2
            head2 = head2.next
        curr = curr.next

    if head1:
        curr.next = head1
    if head2:
        curr.next = head2

    return dummy.next

