class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Binary_Search_Tree:
    def __init__(self, head): #트리 생성(head/root node 필요)
        self.head = head
    def insert(self, value): #노드 추가
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left #비교 대상을 바꿔서 while문 사이클 반복
                else:
                    self.current_node.left = Node(value)
                    break
            else: #value가 현재 노드의 값보다 같거나 클때(같아도 오른쪽으로 보냄)
                if self.current_node.right !=None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break
    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False

head = Node(1)
BST = Binary_Search_Tree(head)
BST.insert(4)
BST.insert(12)
BST.insert(8)
print(BST.search(11))
