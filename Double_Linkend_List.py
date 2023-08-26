class Node:
    """링크드 리스트의 노드 클래스"""
    def __init__(self, data):
        self.data = data  # 실제 노드가 저장하는 데이터
        self.next = None  # 다음 노드에 대한 레퍼런스
        self.prev = None  # 전 노드에 대한 레퍼런스


class LinkedList:
    """링크드 리스트 클래스"""
    def __init__(self):
        self.head = None  # 링크드 리스트의 가장 앞 노드
        self.tail = None  # 링크드 리스트의 가장 뒤 노드

    def insert_after(self, previous_node, data):
        new_node = Node(data)  # 새로운 노드 생성
        if previous_node.next is None:
            self.tail.next = new_node  # 마지막 노드의 다음 노드로 추가
            new_node.prev = self.tail
            self.tail = new_node  # 마지막 노드 업데이트
        else:
            temp_node = previous_node.next
            previous_node.next = new_node
            new_node.prev = previous_node
            new_node.next = temp_node
            temp_node.prev = new_node

    def modelanswer_insert_after(self, previous_node, data):
        new_node = Node(data)  # 새로운 노드 생성

        # tail 노드 다음에 노드를 삽입할 때
        if previous_node is self.tail:
            self.tail.next = new_node  # 새로운 노드를 tail 노드의 다음 노드로 지정한다
            new_node.prev = self.tail  # tail 노드를 새로운 노드의 전 노드로 지정한다
            self.tail = new_node  # 새로운 노드를 tail 노드로 지정한다

        else:
            # 새롭게 생성한 노드를 이미 있는 링크드 리스트에 연결시키고
            new_node.prev = previous_node 
            new_node.next = previous_node.next

            # 이미 있는 노드들의 앞과 다음 레퍼런스를 새롭게 생성한 노드로 지정한다
            previous_node.next.prev = new_node
            previous_node.next = new_node

    def prepend(self, data):
        """링크드 리스트 가장 앞에 데이터를 추가시켜주는 메소드"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            temp_node = self.head
            new_node.next = temp_node
            temp_node.prev = new_node
            self.head = new_node

    def modelanswer_prepend(self, data):
        """연결 리스트 가장 앞에 데이터를 추가시켜주는 메소드"""
        new_node = Node(data)  # 새로운 노드 생성

        # head와 tail을 새로 만든 노드로 지정
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # 이미 노드가 있으면
        else:
            new_node.next = self.head  # 새로운 노드의 다음 노드를 head 노드로 지정
            self.head.prev = new_node  # head 노드의 전 노드를 새로운 노드로 지정
            self.head = new_node  # head 노드 업데이트

    def delete(self, node_to_delete):
        """더블리 링크드 리스트 삭제 연산 메소드"""
        return_node = node_to_delete.data

        if node_to_delete is self.head and node_to_delete is self.tail:
            self.head = None
            self.tail = None
        elif node_to_delete is self.head:
            self.head = self.head.next
        elif node_to_delete is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            next_temp_node = node_to_delete.next
            perv_temp_node = node_to_delete.prev
            next_temp_node.prev = perv_temp_node
            perv_temp_node.next = next_temp_node
        return return_node

    def modelanswer_delete(self, node_to_delete):
        """더블리 링크드 리스트 삭제 연산 메소드"""
        # 링크드 리스트에서 마지막 남은 데이터를 삭제할 때
        if node_to_delete is self.head and node_to_delete is self.tail:
            self.tail = None
            self.head = None

        # 링크드 리스트 가장 앞 데이터 삭제할 때
        elif node_to_delete is self.head:
            self.head = self.head.next
            self.head.prev = None

        # 링크드 리스트 가장 뒤 데이터 삭제할 떄
        elif node_to_delete is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None

        # 두 노드 사이에 있는 데이터 삭제할 때
        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev

        # 삭제하는 노드 데이터 리턴
        return node_to_delete.data

    def find_node_at(self, index):
        """링크드 리스트 접근 연산 메소드. 파라미터 인덱스는 항상 있다고 가정한다"""
        # 링크드 리스트를 돌기 위해 필요한 노드 변수
        iterator = self.head
        # index 번째 있는 노드로 간다
        for _ in range(index):
            iterator = iterator.next

        return iterator

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)  # 새로운 노드 생성

        # 빈 링크드 리스트라면 head와 tail을 새로 만든 노드로 지정
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 이미 노드가 있으면
        else:
            self.tail.next = new_node  # 마지막 노드의 다음 노드로 추가
            new_node.prev = self.tail
            self.tail = new_node  # 마지막 노드 업데이

    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        # 링크드 리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드 리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += " {} |".format(iterator.data)
            iterator = iterator.next  # 다음 노드로 넘어간다

        return res_str
