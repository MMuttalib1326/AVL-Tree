# AVL TREE
import QueueLinkedList1 as queue
class AVLNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
        self.height=1
        
# Preorder Traversal

def preorderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preorderTraversal(rootNode.leftChild)
    preorderTraversal(rootNode.rightChild)    
   

# InorderTraversal

def inorderTraversal(rootNode):
    if not rootNode:
        return
    inorderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inorderTraversal(rootNode.rightChild)

# Post Order Traversal
def postorderTraversal(rootNode):
    if not rootNode:
        return
    postorderTraversal(rootNode.leftChild)
    postorderTraversal(rootNode.rightChild)
    print(rootNode.data) 

# Level Order Traversal
def levelorderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue=queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root=customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)

# Search 

def search(rootNode,nodeValue):
    if rootNode.data==nodeValue:
        print("The value is found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data==nodeValue:
            print("The value is found")
        else:
            search(rootNode.leftChild,nodeValue)
    else:
        if rootNode.rightChild.data==nodeValue:
            print("The value is found")
        else:
            search(rootNode.rightChild,nodeValue)
def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

def rightRotate(disbalancedNode):
    newRoot=disbalancedNode.leftChild
    disbalancedNode.leftChild=disbalancedNode.leftChild.rightChild
    newRoot.rightChild=disbalancedNode
    disbalancedNode.height=1+max(getHeight(disbalancedNode.leftChild),getHeight(disbalancedNode.rightChild))
    newRoot.height=1+max(getHeight(newRoot.leftChild),getHeight(newRoot.rightChild))
    return newRoot

def leftRotate(disbalancedNode):
    newRoot=disbalancedNode.rightChild
    disbalancedNode.rightChild=disbalancedNode.rightChild.leftChild
    newRoot.leftChild=disbalancedNode
    disbalancedNode.height=1+max(getHeight(disbalancedNode.leftChild),getHeight(disbalancedNode.rightChild))
    newRoot.height=1+max(getHeight(newRoot.leftChild),getHeight(newRoot.rightChild))
    return newRoot

def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild)-getHeight(rootNode.rightChild)

def insertNode(rootNode,nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.leftChild=insertNode(rootNode.leftChild,nodeValue)
    else:
        rootNode.rightChild=insertNode(rootNode.rightChild,nodeValue)

    rootNode.height=1+max(getHeight(rootNode.leftChild),getHeight(rootNode.rightChild))  
    balance=getBalance(rootNode)
    if balance>1 and nodeValue<rootNode.leftChild.data:
        return rightRotate(rootNode)
    if balance>1 and nodeValue>rootNode.leftChild.data:
        rootNode.leftChild=leftRotate(rootNode.leftChild)
        return rightRotate()
    if balance<-1 and nodeValue>rootNode.rightChild.data:
        return leftRotate(rootNode)
    if balance <-1 and nodeValue<rootNode.rightChild.data:
        rootNode.rightChild=rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    return rootNode      

def getminValueNode(rootNode):
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return getminValueNode(rootNode.leftChild)

def deleteNode(rootNode,nodeValue):
    if not rootNode:
        return rootNode
    elif nodeValue<rootNode.data:
        rootNode.leftChild=deleteNode(rootNode.leftChild,nodeValue)     
    elif nodeValue>rootNode.data:
        rootNode.rightChild=deleteNode(rootNode.rightChild,nodeValue) 
    else:
        if rootNode.leftChild is None:
            temp=rootNode.rightChild
            rootNode=None
            return temp   
        elif rootNode.rightChild is None:
            temp=rootNode.leftChild
            rootNode=None
            return temp 
        temp=getminValueNode(rootNode.rightChild)
        rootNode.data=temp.data
        rootNode.rightChild=deleteNode(rootNode.rightChild,temp.data)
    balance=getBalance(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild)>=0:
        return rightRotate(rootNode)
    if balance > -1 and getBalance(rootNode.rightChild)<=0:
        return leftRotate(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild)<0:
        rootNode.leftChild=leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balance <-1 and getBalance(rootNode.rightChild)>0:
        rootNode.rightChild=rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    return rootNode
def deleteAVL(rootNode):
    rootNode.data=None
    rootNode.leftChild=None
    rootNode.rightChild=None
    return "The AVL has been succefully deleted"    









newAVL=AVLNode(5)
newAVL=insertNode(newAVL,10)
newAVL=insertNode(newAVL,15)
newAVL=insertNode(newAVL,20)
#newAVL=deleteNode(newAVL,15)
deleteAVL(newAVL)
levelorderTraversal(newAVL)  
           