---
layout: single
title:  "tree data structure "
---

**Table of contents**<a id='toc0_'></a>    
- [data structure: tree](#toc1_)    
  - [트리의 종류](#toc1_1_)    
    - [정 이진 트리 full binary tree :](#toc1_1_1_)    
    - [완전 이진 트리 complete binary tree :](#toc1_1_2_)    
    - [포화 이진 트리 perfect binary tree :](#toc1_1_3_)    
  - [트리 순회](#toc1_2_)    
  - [heap tree 힙 트리](#toc1_3_)    
    - [heap sorting](#toc1_3_1_)    
  - [binary search tree 이진 탐색 트리](#toc1_4_)    
  - [수료증](#toc1_5_)    

<!-- vscode-jupyter-toc-config
	numbering=false
	anchor=true
	flat=false
	minLevel=1
	maxLevel=6
	/vscode-jupyter-toc-config -->
<!-- THIS CELL WILL BE REPLACED ON TOC UPDATE. DO NOT WRITE YOUR TEXT IN THIS CELL -->

# <a id='toc1_'></a>[data structure: tree](#toc0_)
---

데이터의 계층관계를 표시하는 방법

linked list가 next를 담고 있는 node로 만들어졌다면, tree는 child를 담고 있는 node로 만들어진다.

처음 시작하는 node를 root라고 부른다. root를 알면 tree의 모든 node를 알 수 있다.

정렬과 압축 등의 문제를 해결하는 데 유용하게 쓰인다

![img](https://bakey-api.codeit.kr/files/2369/TM643U?name=1.png)


```python
class Node:
    """binary tree node"""
    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data
        
n1 = Node(1)
n2 = Node(2)
n3, n4 = Node(3), Node(4)
n1.left = n2
n1.right = n3
n2.left = n4
n2.left.data
```




    4




```python
class Node:
    """이진 트리 노드 클래스"""
    def __init__(self, data):
            self.data = data
            self.left_child = None
            self.right_child = None


# root 노드 생성
root_node = Node("A")

# 여기에 코드를 작성하세요
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")
h = Node("H")

root_node.right_child = c
c.right_child = f
root_node.left_child = b
b.left_child = d
b.right_child = e
e.left_child = g
e.right_child = h

# 테스트 코드
test_node = root_node.right_child.right_child
print(test_node.data)

test_node = root_node.left_child.right_child.left_child
print(test_node.data)

test_node = root_node.left_child.right_child.right_child
print(test_node.data)
```

    F
    G
    H
    

## <a id='toc1_1_'></a>[트리의 종류](#toc0_)
---
### <a id='toc1_1_1_'></a>[정 이진 트리 full binary tree :](#toc0_)
---
이진 트리임 즉, 자식이 하나인 노드가 없음. every node has zero or two child nodes  

![](https://bakey-api.codeit.kr/files/2372/W2dJf5?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-05-28+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+5.19.38.png)

### <a id='toc1_1_2_'></a>[완전 이진 트리 complete binary tree :](#toc0_)
---
이 빠지지 않고 왼쪽부터 잘 채워지고 있음. every level except possibly the last is completely filled, and all nodes in the last level are as far left as possible  

![](https://bakey-api.codeit.kr/files/2372/c2zngI?name=2.png)
![](https://bakey-api.codeit.kr/files/2372/k4yiH5?name=3.png)

### <a id='toc1_1_3_'></a>[포화 이진 트리 perfect binary tree :](#toc0_)
---
꽉참. full binary tree + complete binary tree. therefore all levels are filled with nodes

![](https://bakey-api.codeit.kr/files/2372/Suu7QL?name=5.png)

완전 이진 트리의 높이는 저장된 노드의 개수가 n일 때 lg(n)이다.

![](https://bakey-api.codeit.kr/files/2372/NRFEzr?name=4.png)


```python
def get_parent_index(complete_binary_tree, index):
    """배열로 구현한 완전 이진 트리에서 index번째 노드의 부모 노드의 인덱스를 리턴하는 함수"""
    # 여기에 코드를 작성하세요
    if index == 1:
        return None
    elif index % 2 == 0:
        return index/2
    else:
        return int((index-1)/2)


def get_left_child_index(complete_binary_tree, index):
    """배열로 구현한 완전 이진 트리에서 index번째 노드의 왼쪽 자식 노드의 인덱스를 리턴하는 함수"""
    # 여기에 코드를 작성하세요
    
    limit = len(complete_binary_tree)
    id = None
    
    if index == 1:
        id = index + 1
    else:
        id= index * 2
    
    if id > limit:
        return None
    else:
        return id
    



def get_right_child_index(complete_binary_tree, index):
    """배열로 구현한 완전 이진 트리에서 index번째 노드의 오른쪽 자식 노드의 인덱스를 리턴하는 함수"""
    # 여기에 코드를 작성하세요
    
    #인덱스가 리스트에 있으면 인덱스를 리턴하고 아니면 None 리턴 
    # 인덱스가 있느냐고 리스트[인덱스]하는 순간 오류 난다
    #
    limit = len(complete_binary_tree)
    id = None
    
    if index == 1:
        id = index + 2
    else:
        id = index * 2 + 1
    
    if id > limit:
        return None
    else:
        return id
 
# 테스트 코드
root_node_index = 1 # root 노드

tree = [None, 1, 5, 12, 11, 9, 10, 14, 2, 10]  # 과제 이미지에 있는 완전 이진 트리

# root 노드의 왼쪽과 오른쪽 자식 노드의 인덱스를 받아온다
left_child_index = get_left_child_index(tree, root_node_index)
right_child_index = get_right_child_index(tree,root_node_index)

print(tree[left_child_index])
print(tree[right_child_index])

# 9번째 노드의 부모 노드의 인덱스를 받아온다
parent_index = get_parent_index(tree, 9)

print(tree[parent_index])

# 부모나 자식 노드들이 없는 경우들
parent_index = get_parent_index(tree, 1)  # root 노드의 부모 노드의 인덱스를 받아온다
print(parent_index)

left_child_index = get_left_child_index(tree, 6)  # 6번째 노드의 왼쪽 자식 노드의 인덱스를 받아온다
print(left_child_index)

right_child_index = get_right_child_index(tree, 8)  # 8번째 노드의 오른쪽 자식 노드의 인덱스를 받아온다
print(right_child_index)
```

    5
    12
    11
    None
    None
    None
    


```python
def get_parent_index(complete_binary_tree, index):
    """배열로 구현한 완전 이진 트리에서 index번째 노드의 부모 노드의 인덱스를 리턴하는 함수"""
    # 여기에 코드를 작성하세요
    ######## 2로 나눈 정수 부분만 반환을 해주면 된다 홀수든 짝수든!
    limit = len(complete_binary_tree)
    id = index // 2
    if 0 < id < limit:
        return id
    else:
        return None


def get_left_child_index(complete_binary_tree, index):
    """배열로 구현한 완전 이진 트리에서 index번째 노드의 왼쪽 자식 노드의 인덱스를 리턴하는 함수"""
    # 여기에 코드를 작성하세요
    
    limit = len(complete_binary_tree)
    id = index * 2 ##### 첫번째든 나머지든 인덱스의 2배
    
    if id > limit:
        return None
    else:
        return id
    



def get_right_child_index(complete_binary_tree, index):
    """배열로 구현한 완전 이진 트리에서 index번째 노드의 오른쪽 자식 노드의 인덱스를 리턴하는 함수"""
    # 여기에 코드를 작성하세요
    
    #인덱스가 리스트에 있으면 인덱스를 리턴하고 아니면 None 리턴 
    # 인덱스가 있느냐고 리스트[인덱스]하는 순간 오류 난다
    #
    limit = len(complete_binary_tree)
    id = index * 2 + 1 ##### 첫번째든 나머지든 인덱스의 2배 + 1
    
    if id > limit:
        return None
    else:
        return id
 
# 테스트 코드
root_node_index = 1 # root 노드

tree = [None, 1, 5, 12, 11, 9, 10, 14, 2, 10]  # 과제 이미지에 있는 완전 이진 트리

# root 노드의 왼쪽과 오른쪽 자식 노드의 인덱스를 받아온다
left_child_index = get_left_child_index(tree, root_node_index)
right_child_index = get_right_child_index(tree,root_node_index)

print(tree[left_child_index])
print(tree[right_child_index])

# 9번째 노드의 부모 노드의 인덱스를 받아온다
parent_index = get_parent_index(tree, 9)

print(tree[parent_index])

# 부모나 자식 노드들이 없는 경우들
parent_index = get_parent_index(tree, 1)  # root 노드의 부모 노드의 인덱스를 받아온다
print(parent_index)

left_child_index = get_left_child_index(tree, 6)  # 6번째 노드의 왼쪽 자식 노드의 인덱스를 받아온다
print(left_child_index)

right_child_index = get_right_child_index(tree, 8)  # 8번째 노드의 오른쪽 자식 노드의 인덱스를 받아온다
print(right_child_index)
```

    5
    12
    11
    None
    None
    None
    

## <a id='toc1_2_'></a>[트리 순회](#toc0_)
---

트리는 순서가 없기 때문에 반복 보다는 재귀로 순회한다  
왼쪽 자식 순회, 오른쪽 자식 순회, 출력 세 부분으로 구성된다

pre order  
- 출력
- 왼쪽
- 오른쪽

- 입력된 노드의 정보 출력
- 노드의 왼쪽, 오른쪽이 있는 경우
 - 왼쪽 순회
 - 오른쪽 순회
- 노드 왼쪽이 없는 경우
 - 오른쪽 순회
- 노드 오른쪽이 없는 경우
 -왼쪽 순회

post order
- 왼쪽
- 오른쪽
- 출력

in order
- 왼쪽
- 출력
- 오른쪽

계층 관계 나타내는 데이터도 순회를 하면 선형으로 표시할 수 있다


```python
class Node:
    """이진 트리 노드를 나타내는 클래스"""

    def __init__(self, data):
        """이진 트리 노드는 데이터와 두 자식 노드에 대한 레퍼런스를 갖는다"""
        self.data = data
        self.left_child = None
        self.right_child = None

# def traverse_inorder(node):
#     """in-order 순회 함수"""
#     # 여기에 코드를 작성하세요
#     if node.left_child and node.right_child:
        
#         traverse_inorder(node.left_child)
#         print(node.data)
#         traverse_inorder(node.right_child)
#     elif node.left_child:
        
#         traverse_inorder(node.left_child)
#         print(node.data)
#     elif node.right_child:        
#         print(node.data)

#         traverse_inorder(node.right_child)
        
#     else:
#         print(node.data)

###### 그렇네 재귀함수니까 베이스부터 생각했어야 한다
# 베이스는 더이상 내려갈 노드가 없는 경우. 그럴 경우엔 출력하고
# 그렇지 않은 경우엔 왼쪽 출력 오른쪽 순으로 반복하게 하면 되는 구나
# 멋지다

def traverse_inorder(node):
    """in-order 순회 함수"""
    if node is not None:
        traverse_inorder(node.left_child)  # 재귀적으로 왼쪽 부분 트리 순회
        print(node.data)  # 데이터 출력
        traverse_inorder(node.right_child)  # 재귀적으로 오른쪽 부분 트리 순회
        

# 여러 노드 인스턴스 생성
node_A = Node("A")
node_B = Node("B")
node_C = Node("C")
node_D = Node("D")
node_E = Node("E")
node_F = Node("F")
node_G = Node("G")
node_H = Node("H")
node_I = Node("I")

# 생성한 노드 인스턴스들 연결
node_F.left_child = node_B
node_F.right_child = node_G

node_B.left_child = node_A
node_B.right_child = node_D

node_D.left_child = node_C
node_D.right_child = node_E

node_G.right_child = node_I

node_I.left_child = node_H

# 노드 F를 root 노드로 만든다
root_node = node_F

# 만들어 놓은 트리를 in-order로 순회한다
traverse_inorder(root_node)
```

    A
    B
    C
    D
    E
    F
    G
    H
    I
    


```python
a = None
if a:
    print('y')
else:
    print('n')
```

    n
    

## <a id='toc1_3_'></a>[heap tree 힙 트리](#toc0_)
---
- 형태 속성: complete binary tree, height = O(lg(n))
  - 완전 이진 트리를 가정하기 때문에 배열이나 파이썬 리스트로 표현한다
- 힙 속성: 모든 노드는 자식 노드 데이터보다 크거나 같다

정렬 알고리즘: 데이터를 재배치하는 구체적인 방법
- 삽입
- 퀵
- 선택
- 합병  
- https://www.youtube.com/@AlgoRythmics


```python
def swap(tree, index_1, index_2):
    """완전 이진 트리의 노드 index_1과 노드 index_2의 위치를 바꿔준다"""
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp


def heapify(tree, index, tree_size):
    """heapify 함수"""

    # 왼쪽 자식 노드의 인덱스와 오른쪽 자식 노드의 인덱스를 계산
    left_child_index = 2 * index
    right_child_index = 2 * index + 1

    # 여기에 코드를 작성하세요
    up = tree[index]
    peak = max(tree[index])
    


# 테스트 코드
tree = [None, 15, 5, 12, 14, 9, 10, 6, 2, 11, 1]  # heapify하려고 하는 완전 이진 트리
heapify(tree, 2, len(tree))  # 노드 2에 heapify 호출
print(tree) 
```


```python
def swap(tree, index_1, index_2):
    """완전 이진 트리의 노드 index_1과 노드 index_2의 위치를 바꿔준다"""
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp


def heapify(tree, index, tree_size):
    """heapify 함수"""

    # 왼쪽 자식 노드의 인덱스와 오른쪽 자식 노드의 인덱스를 계산
    left_child_index = 2 * index
    right_child_index = 2 * index + 1

    # 여기에 코드를 작성하세요
    up = tree[index]
    left = 0 if left_child_index > tree_size else tree[left_child_index]
    right = 0 if right_child_index > tree_size else tree[right_child_index] 
    
    peak = max(up, left, right)
    if peak == up:
        return
    elif peak == left:
        swap(tree, index, left_child_index)
        heapify(tree, left_child_index, tree_size)
    elif peak == right:
        swap(tree, index, right_child_index)
        heapify(tree, right_child_index, tree_size)
        
    


# 테스트 코드
tree = [None, 15, 5, 12, 14, 9, 10, 6, 2, 11, 1]  # heapify하려고 하는 완전 이진 트리
heapify(tree, 2, len(tree))  # 노드 2에 heapify 호출
print(tree) 
```

    [None, 15, 14, 12, 11, 9, 10, 6, 2, 5, 1]
    


```python
def heapify(tree, index, tree_size):
    """heapify 함수"""

    # 왼쪽 자식 노드의 인덱스와 오른쪽 자식 노드의 인덱스를 계산
    left_child_index = 2 * index
    right_child_index = 2 * index + 1

    largest = index  # 일단 부모 노드의 값이 가장 크다고 설정

    # 왼쪽 자식 노드의 값과 비교
    if 0 < left_child_index < tree_size and tree[largest] < tree[left_child_index]:
        largest = left_child_index

    # 오른쪽 자식 노드의 값과 비교
    if 0 < right_child_index < tree_size and tree[largest] < tree[right_child_index]:
        largest = right_child_index
    
    if largest != index: # 부모 노드의 값이 자식 노드의 값보다 작으면
        swap(tree, index, largest)  # 부모 노드와 최댓값을 가진 자식 노드의 위치를 바꿔준다
        heapify(tree, largest, tree_size)  # 자리가 바뀌어 자식 노드가 된 기존의 부모 노드를대상으로 또 heapify 함수를 호출한다
```


```python
def heapify(tree, index, tree_size):
    """heapify 함수"""

    # 왼쪽 자식 노드의 인덱스와 오른쪽 자식 노드의 인덱스를 계산
    left_child_index = 2 * index
    right_child_index = 2 * index + 1

    # 여기에 코드를 작성하세요
    # up = tree[index]   
    # left = 0 if left_child_index > tree_size else tree[left_child_index]
    # right = 0 if right_child_index > tree_size else tree[right_child_index] 
    
    if left_child_index <= tree_size and right_child_index <= tree_size:
        up = tree[index]
        left = tree[left_child_index]
        right = tree[right_child_index]
    
        peak = max(up, left, right)
        if peak == up:
            return
        elif peak == left:
            swap(tree, index, left_child_index)
            heapify(tree, left_child_index, tree_size)
        elif peak == right:
            swap(tree, index, right_child_index)
            heapify(tree, right_child_index, tree_size)
```


```python
# 테스트 코드
tree = [None, 15, 5, 12, 14, 9, 10, 6, 2, 11, 1]  # heapify하려고 하는 완전 이진 트리
heapify(tree, 2, len(tree))  # 노드 2에 heapify 호출
print(tree) 
```

    [None, 15, 14, 12, 11, 9, 10, 6, 2, 5, 1]
    

각 노드 별로 모두 heapify를 한다고 하면? 시간복잡도는 O(nlg(n))이 된다  
- 왜 모든 노드에 그래야 하는 거지 최상위 노드에만 하면 되지 않나?
 - 최상위에만 하면 subtree 중에 숨어있는 애들이 있을 수 있다

### <a id='toc1_3_1_'></a>[heap sorting](#toc0_)

root node와 마지막 노드를 바꾸고 마지막 노드가 없는 셈 친다  
오름 차순 정렬이 된다

min heap을 하면 내림 차순이 된다


```python
def swap(tree, index_1, index_2):
    """완전 이진 트리의 노드 index_1과 노드 index_2의 위치를 바꿔준다"""
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp


def heapify(tree, index, tree_size):
    """heapify 함수"""

    # 왼쪽 자식 노드의 인덱스와 오른쪽 자식 노드의 인덱스를 계산
    left_child_index = 2 * index
    right_child_index = 2 * index + 1

    largest = index  # 일단 부모 노드의 값이 가장 크다고 설정

    # 왼쪽 자식 노드의 값과 비교
    if 0 < left_child_index < tree_size and tree[largest] < tree[left_child_index]:
        largest = left_child_index

    # 오른쪽 자식 노드의 값과 비교
    if 0 < right_child_index < tree_size and tree[largest] < tree[right_child_index]:
        largest = right_child_index
    
    if largest != index: # 부모 노드의 값이 자식 노드의 값보다 작으면
        swap(tree, index, largest)  # 부모 노드와 최댓값을 가진 자식 노드의 위치를 바꿔준다
        heapify(tree, largest, tree_size)  # 자리가 바뀌어 자식 노드가 된 기존의 부모 노드를대상으로 또 heapify 함수를 호출한다

def heapsort(tree):
    """힙 정렬 함수"""
    tree_size = len(tree)

    # 여기에 코드를 작성하세요
    # heapify
    # count = tree_size
    # while count > 0:
    #     heapify(tree, count, tree_size)
    #     count -= 1
    
    ############## range도 step이 된다!!!! ##################
    for index in range(tree_size-1, 0, -1):
        heapify(tree, index, tree_size)
    
    # for x in range(tree_size-1):
    #     swap(tree, 1, tree_size - x - 1)
    #     heapify(tree, 1, len(tree[:tree_size - x - 1]))
    
    ############## range도 step이 된다!!!! ##################
    for i in range(tree_size-1, 0, -1):
        swap(tree, 1, i)  # root 노드와 마지막 인덱스를 바꿔준 후
        heapify(tree, 1, i)  # root 노드에 heapify를 호출한다
        # i를 거꾸로 가게 해놓으니 이렇게 되는 구나 깔끔하고 멋지다!


# 테스트 코드
data_to_sort = [None, 6, 1, 4, 7, 10, 3, 8, 5, 1, 5, 7, 4, 2, 1]
heapsort(data_to_sort)
print(data_to_sort)
```

    [None, 1, 1, 1, 2, 3, 4, 4, 5, 5, 6, 7, 7, 8, 10]
    

range 함수도 step을 적용할 수 있다!!!


```python
for i in range(10, 1, -1):
    print(i)
```

    10
    9
    8
    7
    6
    5
    4
    3
    2
    

|정렬|시간복잡도|
|:-:|:-:|
|선택|O(n^2)|
|삽입|O(n^2)|
|합병|O(nlg(n))|
|퀵|O(n^2) 평균O(nlg(n))|
|힙|O(nlg(n))|

heap 정렬로 우선순위 큐를 구현할 수 있다  
일반 큐는 FIFO라면 우선순위 큐는 priority 순으로 나간다

heap 데이터 삽입


```python
def swap(tree, index_1, index_2):
    """완전 이진 트리의 노드 index_1과 노드 index_2의 위치를 바꿔준다"""
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp


def reverse_heapify(tree, index):
    """삽입된 노드를 힙 속성을 지키는 위치로 이동시키는 함수"""
    parent_index = index // 2  # 삽입된 노드의 부모 노드의 인덱스 계산
    # 여기에 코드를 작성하세요
    if parent_index > 0:
        if tree[index] <= tree[parent_index]:
            return
        else:
            swap(tree, index, parent_index)
            reverse_heapify(tree, parent_index)

class PriorityQueue:
    """힙으로 구현한 우선순위 큐"""
    def __init__(self):
        self.heap = [None]  # 파이썬 리스트로 구현한 힙


    def insert(self, data):
        """삽입 메소드"""
        # 여기에 코드를 작성하세요
        self.heap.append(data)
        reverse_heapify(self.heap, len(self.heap) - 1)


    def __str__(self):
        return str(self.heap)


# 테스트 코드
priority_queue = PriorityQueue()

priority_queue.insert(6)
priority_queue.insert(9)
priority_queue.insert(1)
priority_queue.insert(3)
priority_queue.insert(10)
priority_queue.insert(11)
priority_queue.insert(13)

print(priority_queue)
```

    [None, 13, 9, 11, 3, 6, 1, 10]
    


```python
def reverse_heapify(tree, index):
    """삽입된 노드를 힙 속성을 지키는 위치로 이동시키는 함수"""
    parent_index = index // 2  # 삽입된 노드의 부모 노드의 인덱스 계산

    # 부모 노드가 존재하고, 부모 노드의 값이 삽입된 노드의 값보다 작을 때
    if 0 < parent_index < len(tree) and tree[index] > tree[parent_index]:
        swap(tree, index, parent_index)  # 부모 노드와 삽입된 노드의 위치 교환
        reverse_heapify(tree, parent_index)  # 삽입된 노드를 대상으로 다시 reverse_heapify 호출


class PriorityQueue:
    """힙으로 구현한 우선순위 큐"""
    def __init__(self):
        self.heap = [None]  # 파이썬 리스트로 구현한 힙


    def insert(self, data):
        """삽입 메소드"""
        self.heap.append(data)  # 힙의 마지막에 데이터 추가
        reverse_heapify(self.heap, len(self.heap)-1) # 삽입된 노드(추가된 데이터)의 위치를 재배치


    def __str__(self):
        return str(self.heap)
```


```python
def swap(tree, index_1, index_2):
    """완전 이진 트리의 노드 index_1과 노드 index_2의 위치를 바꿔준다"""
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp


def heapify(tree, index, tree_size):
    """heapify 함수"""

    # 왼쪽 자식 노드의 인덱스와 오른쪽 자식 노드의 인덱스를 계산
    left_child_index = 2 * index
    right_child_index = 2 * index + 1

    largest = index  # 일단 부모 노드의 값이 가장 크다고 설정

    # 왼쪽 자식 노드의 값과 비교
    if 0 < left_child_index < tree_size and tree[largest] < tree[left_child_index]:
        largest = left_child_index

    # 오른쪽 자식 노드의 값과 비교
    if 0 < right_child_index < tree_size and tree[largest] < tree[right_child_index]:
        largest = right_child_index
    
    if largest != index: # 부모 노드의 값이 자식 노드의 값보다 작으면
        swap(tree, index, largest)  # 부모 노드와 최댓값을 가진 자식 노드의 위치를 바꿔 준다
        heapify(tree, largest, tree_size)  # 자리가 바뀌어 자식 노드가 된 기존의 부모 노드를대상으로 또 heapify 함수를 호출한다


def reverse_heapify(tree, index):
    """삽입된 노드를 힙 속성을 지키는 위치로 이동시키는 함수"""
    parent_index = index // 2  # 삽입된 노드의 부모 노드의 인덱스 계산

    # 부모 노드가 존재하고, 부모 노드의 값이 삽입된 노드의 값보다 작을 때
    if 0 < parent_index < len(tree) and tree[index] > tree[parent_index]:
        swap(tree, index, parent_index)  # 부모 노드와 삽입된 노드의 위치 교환
        reverse_heapify(tree, parent_index)  # 삽입된 노드를 대상으로 다시 reverse_heapify 호출


```


```python
class PriorityQueue:
    """힙으로 구현한 우선순위 큐"""
    def __init__(self):
        self.heap = [None]  # 파이썬 리스트로 구현한 힙

    def insert(self, data):
        """삽입 메소드"""
        self.heap.append(data)  # 힙의 마지막에 데이터 추가
        reverse_heapify(self.heap, len(self.heap)-1) # 삽입된 노드(추가된 데이터)의 위치를 재배치

    def extract_max(self):
        """최우선순위 데이터 추출 메소드"""
        # 코드를 쓰세요
        swap(self.heap, 1, len(self.heap) - 1)
        rst = self.heap[len(self.heap) - 1]
        self.heap = self.heap[:-1]
        heapify(self.heap, 1, len(self.heap))
        # reverse_heapify(self.heap, len(self.heap)-1)
        
        return rst

    def __str__(self):
        return str(self.heap)

# 출력 코드
priority_queue = PriorityQueue()

priority_queue.insert(6)
priority_queue.insert(9)
priority_queue.insert(1)
priority_queue.insert(3)
priority_queue.insert(10)
priority_queue.insert(11)
priority_queue.insert(13)

print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())
```

    13
    11
    10
    9
    6
    3
    1
    

||삽입|추출|
|:-:|:-:|:-:|
|배열|O(n)|O(1)|
|연결 리스트|O(n)|O(1)|
|힙|O(lg(n))|O(lg(n))|

## <a id='toc1_4_'></a>[binary search tree 이진 탐색 트리](#toc0_)
---

어떤 노드의 왼쪽 서브트리에는 그 노드의 값보다 작은 값들을, 오른쪽 서브트리에는 그 노드의 값보다 큰 값들을 가진다

- 값을 찾는 데 유리하다
- 완전 이진 트리가 아니어도 되기 때문에 노드로 구성한다

1시간 정도 고민했다. 힌트 1개 정도 보고 풀었는데 답안과 거의 똑같아서 놀랐다


```python
class Node:
    """이진 탐색 트리 노드 클래스"""
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.right_child = None
        self.left_child = None


def print_inorder(node):
    """주어진 노드를 in-order로 출력해주는 함수"""
    if node is not None:
        print_inorder(node.left_child)
        print(node.data)
        print_inorder(node.right_child)


class BinarySearchTree:
    """이진 탐색 트리 클래스"""
    def __init__(self):
        self.root = None


    def insert(self, data):
        new_node = Node(data)  # 삽입할 데이터를 갖는 새 노드 생성

        # 트리가 비었으면 새로운 노드를 root 노드로 만든다
        if self.root is None:
            self.root = new_node
            return

        # 여기에 코드를 작성하세요
        # comp = self.root
        # while new_node.data <= comp.data:            
        #     if comp.left_child is not None:
        #         comp = comp.left_child
        #     else:
        #         comp.left_child = new_node
        #         new_node.parent = comp
        # while new_node.data > comp.data:
        #     if comp.right_child is not None:
        #         comp = comp.right_child
        #     else:
        #         comp.right_child = new_node
        
        # if new_node.data <= self.root.data and self.root.left_child is None:
        #     self.root.left_child = new_node
        # elif new_node.data > self.root.data and self.root.right_child is None:
        #     self.root.right_child = new_node
        
        comp = self.root
        while comp is not None:
            if comp.data <= new_node.data:
                if comp.right_child is None:
                    new_node.parent = comp ############ 아참 parent 속을 넣어줘야 하지!
                    comp.right_child = new_node
                    # comp = None ##################### return을 시키면 while을 빠져나갈 수 있구나?
                    return
                else:
                    comp = comp.right_child
            else:                            
                if comp.left_child is None:
                    new_node.parent = comp
                    comp.left_child = new_node                    
                    # comp = None
                    return
                else:
                    comp = comp.left_child
########################################################## 아래가 해설
        # # 원하는 위치를 찾아간다
        # while temp is not None:
        #     if data > temp.data:  # 삽입하려는 데이터가 현재 노드 데이터보다 크다면
        #         # 오른쪽 자식이 없으면 새로운 노드를 현재 노드 오른쪽 자식으로 만듦
        #         if temp.right_child is None:
        #             new_node.parent = temp
        #             temp.right_child = new_node
        #             return
        #         # 오른쪽 자식이 있으면 오른쪽 자식으로 간다
        #         else:
        #             temp = temp.right_child
        #     else:  # 삽입하려는 데이터가 현재 노드 데이터보다 작다면
        #         # 왼쪽 자식이 없으면 새로운 노드를 현재 노드 왼쪽 자식으로 만듦
        #         if temp.left_child is None:
        #             new_node.parent = temp
        #             temp.left_child = new_node
        #             return
        #         # 왼쪽 자식이 있다면 왼쪽 자식으로 간다
        #         else:
        #             temp = temp.left_child
                
        
        
            

    def print_sorted_tree(self):
        """이진 탐색 트리 내의 데이터를 정렬된 순서로 출력해주는 메소드"""
        print_inorder(self.root)  # root 노드를 in-order로 출력한다


# 빈 이진 탐색 트리 생성
bst = BinarySearchTree()

# 데이터 삽입
bst.insert(7)
bst.insert(11)
bst.insert(9)
bst.insert(17)
bst.insert(8)
bst.insert(5)
bst.insert(19)
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.insert(14)

# 이진 탐색 트리 출력
bst.print_sorted_tree()
```

    2
    3
    4
    5
    7
    8
    9
    11
    14
    17
    19
    


```python
class Node:
    """이진 탐색 트리 노드 클래스"""
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.right_child = None
        self.left_child = None


def print_inorder(node):
    """주어진 노드를 in-order로 출력해주는 함수"""
    if node is not None:
        print_inorder(node.left_child)
        print(node.data)
        print_inorder(node.right_child)


class BinarySearchTree:
    """이진 탐색 트리 클래스"""
    def __init__(self):
        self.root = None


    def search(self, data):
        """이진 탐색 트리 탐색 메소드, 찾는 데이터를 갖는 노드가 없으면 None을 리턴한다"""
        # 여기에 코드를 작성하세요
        


    def insert(self, data):
        """이진 탐색 트리 삽입 메소드"""
        new_node = Node(data)  # 삽입할 데이터를 갖는 노드 생성

        # 트리가 비었으면 새로운 노드를 root 노드로 만든다
        if self.root is None:
            self.root = new_node
            return

        # 여기에 코드를 작성하세요
        temp = self.root  # 저장하려는 위치를 찾기 위해 사용할 변수. root 노드로 초기화한다

        # 원하는 위치를 찾아간다
        while temp is not None:
            if data > temp.data:  # 삽입하려는 데이터가 현재 노드 데이터보다 크다면
                # 오른쪽 자식이 없으면 새로운 노드를 현재 노드 오른쪽 자식으로 만듦
                if temp.right_child is None:
                    new_node.parent = temp
                    temp.right_child = new_node
                    return
                # 오른쪽 자식이 있으면 오른쪽 자식으로 간다
                else:
                    temp = temp.right_child
            else:  # 삽입하려는 데이터가 현재 노드 데이터보다 작다면
                # 왼쪽 자식이 없으면 새로운 노드를 현재 노드 왼쪽 자식으로 만듦
                if temp.left_child is None:
                    new_node.parent = temp
                    temp.left_child = new_node
                    return
                # 왼쪽 자식이 있다면 왼쪽 자식으로 간다
                else:
                    temp = temp.left_child
            

    def print_sorted_tree(self):
        """이진 탐색 트리 내의 데이터를 정렬된 순서로 출력해주는 메소드"""
        print_inorder(self.root)  # root 노드를 in-order로 출력한다


# 빈 이진 탐색 트리 생성
bst = BinarySearchTree()

# 데이터 삽입
bst.insert(7)
bst.insert(11)
bst.insert(9)
bst.insert(17)
bst.insert(8)
bst.insert(5)
bst.insert(19)
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.insert(14)

# 노드 탐색과 출력
print(bst.search(7).data)
print(bst.search(19).data)
print(bst.search(2).data)
print(bst.search(20))
```

## <a id='toc1_5_'></a>[수료증](https://www.codeit.kr/certificates/FEx0l-WniUc-8D6x6-WPOO3) [&#8593;](#toc0_)
