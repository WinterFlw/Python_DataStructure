class Node:
    """이진 트리 노드 클래스"""
    def __init__(self, data):
            self.data = data
            self.left_child = None
            self.right_child = None


# root 노드 생성
root_node = Node("A")
# 여기에 코드를 작성하세요
B_node = Node("B")
root_node.left_child = B_node
C_node = Node("C")
root_node.right_child = C_node

D_node = Node("D")
root_node.left_child.left_child = D_node
E_node = Node("E")
root_node.left_child.right_child = E_node
F_node = Node("F")
root_node.right_child.right_child = F_node
G_node = Node("G")
root_node.left_child.right_child.left_child = G_node
H_node = Node("H")
root_node.left_child.right_child.right_child = H_node
# 테스트 코드
test_node = root_node.right_child.right_child
print(test_node.data)

test_node = root_node.left_child.right_child.left_child
print(test_node.data)

test_node = root_node.left_child.right_child.right_child
print(test_node.data)