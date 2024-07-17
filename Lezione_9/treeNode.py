class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def crea_treeNode(self) -> list[int]:

        treeNode: list[int] = []

        for i in range(1,3):

            treeNode.append(self.val)

            self.left = 2*i+1
            self.right = 2*(i+1)

        
        
def symmetric(tree: list[int]) -> bool:
    
    
    for i in range(len(tree)):

        if tree[2*i+1] == tree[2(i+1)]:

            print("ciao")
        else: 
            
            return False

    return True


print(symmetric([1,2,2,3,4,4,3]))