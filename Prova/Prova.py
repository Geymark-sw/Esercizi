lista_invertita: list[int] = []

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverse_list(head: ListNode) -> list[int]:
    
    
    
    while head.next != None:

        reverse_list(head.next)
        head.next = None
    
    
    lista_invertita.append(head.val)
    

    return lista_invertita

head = ListNode(val=1, next=ListNode(val=2,))
print(reverse_list(head))