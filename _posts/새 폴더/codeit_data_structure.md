**Table of contents**<a id='toc0_'></a>    
- [Data Structure 자료구조](#toc1_)    
  - [정의](#toc1_1_)    
  - [컴퓨터가 데이터를 저장 하는 방법](#toc1_2_)    
    - [그중에서도 자료구조에서 빠른 처리가 중요한 건 메모리](#toc1_2_1_)    
  - [배열 Array](#toc1_3_)    
    - [배열 시간복잡도](#toc1_3_1_)    
  - [링크트 리스트 linked list](#toc1_4_)    
    - [linked list의 시간 복잡도 time complexity](#toc1_4_1_)    
  - [더블 링크드 리스트 doubly linked list](#toc1_5_)    
    - [single Vs. double Usage](#toc1_5_1_)    
    - [single Vs. double time complexity](#toc1_5_2_)    
      - [접근 access는 O(n)으로 동일하다](#toc1_5_2_1_)    
      - [탐색: 값으로 탐색하는 것도 O(n)으로 동일하다](#toc1_5_2_2_)    
      - [삽입: O(1)으로 동일하다](#toc1_5_2_3_)    
      - [head, tail에 대한 삽입 삭제 연산은 다르다](#toc1_5_2_4_)    
  - [tbd 원형 연결 리스트 circular linked list](#toc1_6_)    
  - [Hash Table](#toc1_7_)    
    - [hash table 단점](#toc1_7_1_)    
    - [chaining](#toc1_7_2_)    
    - [open addressing](#toc1_7_3_)    
  - [추상자료형 abstract data type](#toc1_8_)    
    - [리스트list](#toc1_8_1_)    
    - [큐, 대기열Queue](#toc1_8_2_)    
    - [스택Stack](#toc1_8_3_)    
    - [dict = map](#toc1_8_4_)    
    - [set](#toc1_8_5_)    
  - [정리](#toc1_9_)    
  - [수료증](#toc1_10_)    

<!-- vscode-jupyter-toc-config
	numbering=false
	anchor=true
	flat=false
	minLevel=1
	maxLevel=6
	/vscode-jupyter-toc-config -->
<!-- THIS CELL WILL BE REPLACED ON TOC UPDATE. DO NOT WRITE YOUR TEXT IN THIS CELL -->

# <a id='toc1_'></a>[Data Structure 자료구조](#toc0_)

## <a id='toc1_1_'></a>[정의](#toc0_)
---
데이터의 효율적 접근 및 조작을 가능하게 하는 저장 및 관리 방식  

## <a id='toc1_2_'></a>[컴퓨터가 데이터를 저장 하는 방법](#toc0_)
---
1. storage: permanent, slow -> warehouse
2. memory: temporary, quick -> desktop drawer

### <a id='toc1_2_1_'></a>[그중에서도 자료구조에서 빠른 처리가 중요한 건 메모리](#toc0_)
---
메모리는 데이터를 저장할 수 있는 칸으로 나누어지고 고유의 주소값을 갖는다  
이 칸을 세는 단위를 byte라고 한다  
RAM: Random Access Memory  
주소가 어디에 있든지 간에 한번에 조회하므로 시간복잡도는 O(1)이다

주소는 메모리의 실질적 주소이고 레퍼런스는 데이터에 접근 할 수 있게 해주는 값이다  
레퍼런스는 주소를 참조하는 값이므로 주소일 수도 있고 아닐 수도 있다

id()로 조회했을 때 같은 주소를 가리키는 다른 객체들을 볼 수 있다 이를 aliasing이라고 한다

## <a id='toc1_3_'></a>[배열 Array](#toc0_)
---
C 언어의 기반. 파이썬의 리스트는 C의 배열에 기반한다

1. 배열의 크기는 정해져있다(정적 배열) : 연속적인 메모리 칸을 선언하는 크기 만큼 미리 할당해둔다 >>> 삽입이 불가능
2. 같은 타입의 데이터만 담을 수 있다
3. 값이 비어있다는 데이터를 넣을 수 없다 >>> 삭제 불가능  

값을 삭제하려고 하면 실제로 지우는 게 아니라 지우려는 값 뒤에 있는 값들을 앞으로 당겨서 덮어씌운다  
파이썬(동적 배열)도 정적 배열을 이용하므로 삭제를 하지는 못 한다. 다만 땡겨지고 나서 끝에 인덱스를 막아버려서 사용하지 못하게 한다

메모리 주소를 규칙적으로 정해놓으니 배열에 값을 저장하거나 불러올 때 O(1)이 된다

동적 배열은 정적 배열에 기반해 만들어진다. 배열이 꽉 찼을 때 값을 추가하려고 하면 크기가 두 배 짜리인 배열을 생성해서 옮기고 추가해서 저장한다  
따로 언급하지 않으면 정적 배열이다 (크기가 정해져있는 배열)

파이썬 리스트는 동적 배열이다 값은 값대로 따로 저장하고 레퍼런스도 리스트로 만든다

### <a id='toc1_3_1_'></a>[배열 시간복잡도](#toc0_)
---

배열 끝에 새 값을 넣는 걸 추가 연산append operation이라 한다  
동적 배열이라도 내부적으로는 정적 배열이므로 경우의 수는  
1. 정적 배열 공간이 남았을 땐, 있는 배열에 넣으면 되므로 O(1)
2. 정적 배열 공간이 없을 땐, 새로운 배열을 만들고 이 전의 값 n개를 복사하고 넣어야 하므로 O(n)


시간 복잡도는 최악의 경우를 가정해서 O(n)이다.  
그러나 동적 배열의 경우 배열이 아예 꽉 찬 경우보다 비어있는 경우가 많으므로 일괄적으로 O(n)이라 하는 건 불합리 할 수 있다  
따라서 다른 방식으로 표기하기도 하는데 분할 상환 분석 Amortized analysis가 그 중 하나다  
분할 상환 분석은 작업이 걸리는 평균시간을 말하는데 동작 n번에 걸린 시간이 x라면 평균시간 x/n를 시간복잡도로 사용한다  
따라서 다음과 같이 표현할 수 있다  
**동적 배열의 추가 연산은 최악의 경우 O(n)이 걸리지만 분할 상환 분석을 하면 O(1)이 걸린다**  
(O(n)/n = O(1)이 되는 거구나 ... ?)

데이터를 추가(append) 말고 삽입(insert) 할 때도
1. 정적 배열 공간이 남았을 땐, 최악의 경우(0 자리에 삽입), 모든 값을 한칸씩 미뤄야 하므로 O(n)
2. 정적 배열 공간이 없을 땐, 새로운 배열을 만들고 나서 한칸씩 미뤄야 하므로 O(n)

배열에서 맨 끝 데이터의 삭제 시
1. 데이터만 삭제하고 배열 크기는 변경이 없는 경우 O(1)
2. 데이터를 삭제하고 배열 크기 대비 담겨있는 데이터가 기준 보다 낮아져서 배열 크기 자체를 줄이는 경우, 작아진 크기 만큼의 배열을 생성하고 거기에 복사해야 하므로 O(n)

동적 배열은 현재 크기가 다 찼을 때 2배 크기의 배열을 생성하므로 최악의 경우 n개의 데이터를 저장할 때 n-2개의 자리가 남는다  
예를 들어 8칸 짜리 8개 데이터 저장된 상태에서 1개 데이터 추가 돼 9개 데이터가 저장된 16칸 배열이 되면 7칸이 남는다 공간이 낭되는 셈이다 낭비되는 양은 O(n)이다

## <a id='toc1_4_'></a>[링크트 리스트 linked list](#toc0_)
---

데이터를 순서대로 저장하고 계속 추가 할 수 있다. 동적 배열과 유사하나 경우에 따라 차이가 있다  
노드node에 데이터를 저장하고 노드들을 연결한다  
노드는 [data | next reference] 모양으로 생겼다. data와 ref를 속성으로 갖는다 a.data, a.next  
linked list에서 첫번째 노드를 head node라고 부른다  
메모리 상에 노드들이 흩어져 저장되어도 next가 있으니 이어진다


```python
class Node:
    """linked list Node"""
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
    
# 노드 생성
head = Node(1)        
node2 = Node(2)
node3 = Node(3)
tail = Node(4)

# 노드 연결
head.next = node2
node2.next = node3
node3.next = tail

iterator = head
while iterator is not None:
    print(iterator.data)
    iterator = iterator.next
```

    1
    2
    3
    4
    


```python
class LinkedList:
    """linked list"""
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def find(self, index):
        """access data. assuming index is there"""
        iterator = self.head
        for _ in range(index):
            iterator = iterator.next
        return iterator
        
    def append(self, data):
        """append"""
        new = Node(data)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new
            
    def __str__(self) -> str:
        """str linked list"""
        res = "|"
        iterator = self.head
        while iterator is not None:
            res += f'{iterator.data}|'
            iterator = iterator.next
        return res
            
#new list
lt = LinkedList()
lt.append(7)
lt.append(8)
lt.append(9)
lt.append(10)

iterator = lt.head
while iterator is not None:
    print(iterator.data)
    iterator = iterator.next
```

    7
    8
    9
    10
    


```python
print(lt)
```

    |7|8|9|10|
    

linked list를 통해 접근할 땐 node를 이용한다  
head부터 시작해서 next를 따라가면서 찾는다


```python
print(lt.find(0).data)
lt.find(3).data = 1
print(lt.find(3).data)
```

    7
    1
    

배열에서는 접근은 O(1)인데 linked list는 접근이 O(n)이다


```python
print(lt.find(5).data)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    Cell In[14], line 1
    ----> 1 print(lt.find(5).data)
    

    Cell In[10], line 12, in LinkedList.find(self, index)
         10 iterator = self.head
         11 for _ in range(index):
    ---> 12     iterator = iterator.next
         13 return iterator
    

    AttributeError: 'NoneType' object has no attribute 'next'


한번에 맞췄다!


```python
class Node:
    """링크드 리스트의 노드 클래스"""
    def __init__(self, data):
        self.data = data  # 실제 노드가 저장하는 데이터
        self.next = None  # 다음 노드에 대한 레퍼런스

class LinkedList:
    """링크드 리스트 클래스"""
    def __init__(self):
        self.head = None  # 링크드 리스트의 가장 앞 노드
        self.tail = None  # 링크드 리스트의 가장 뒤 노드
        
    def find(self, index):
        """access data. assuming index is there"""
        iterator = self.head
        for _ in range(index):
            iterator = iterator.next
        return iterator
    
    def prepend(self, data):
        """링크드 리스트의 가장 앞에 데이터 삽입"""
        # 코드를 쓰세요
        new = Node(data)
        if self.head == None:
            self.append(data)
        else:
            new.next = self.head
            self.head = new
            
    def pop_left(self):
        """링크드 리스트의 가장 앞 노드 삭제 메소드. 단, 링크드 리스트에 항상 노드가 있다고 가정한다"""
        # 코드를 쓰세요     
        gone = self.head.data   
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        return gone

    def find_node_with_data(self, data):
        """링크드 리스트에서 탐색 연산 메소드. 단, 해당 노드가 없으면 None을 리턴한다"""
        # 여기에 코드를 작성하세요
        iterator = self.head
        
        while iterator is not None:
            if iterator.data == data:
                return iterator            
            iterator = iterator.next
        return None
    
    def insert_after(self, prev, data):
        """insert data after prev node"""
        new = Node(data)
        if prev == self.tail:
            self.tail.next = new  # 가장 마지막 노드 뒤에 새로운 노드를 추가하고
            self.tail = new  # 마지막 노드를 추가한 노드로 바꿔준다
        else:
            new.next = prev.next            
            prev.next = new
            
    def delete_after(self, prev):
        """delete node after prev node"""
        #lined list에서 노드를 삭제할 땐 그 데이터를 리턴해주는 게 관습
        gone = prev.next.data
        
        if prev.next == self.tail:
            prev.next = None #prev의 다음이 없어지게 해야 하는 구나
            self.tail = prev
        else:
            prev.next = prev.next.next
            #천재! 역시 쩔었다
            
        return gone

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)
        
        # 링크드 리스트가 비어 있으면 새로운 노드가 링크드 리스트의 처음이자 마지막 노드다
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 링크드 리스트가 비어 있지 않으면
        else:
            self.tail.next = new_node  # 가장 마지막 노드 뒤에 새로운 노드를 추가하고
            self.tail = new_node  # 마지막 노드를 추가한 노드로 바꿔준다

    def __str__(self):
        """링크드  리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        # 링크드  리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드  리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += " {} |".format(iterator.data)
            iterator = iterator.next # 다음 노드로 넘어간다

        return res_str
    
    


    
    
```


```python
# 새로운 링크드 리스트 생성
linked_list = LinkedList()

# 여러 데이터를 링크드 리스트 마지막에 추가
linked_list.append(2)
linked_list.append(3)
linked_list.append(5)
linked_list.append(7)
linked_list.append(11)

# 데이터 2를 갖는 노드 탐색
node_with_2 = linked_list.find_node_with_data(2)

if not node_with_2 is None:
    print(node_with_2.data)
else:
    print("2를 갖는 노드는 없습니다")

# 데이터 11을 갖는 노드 탐색
node_with_11 = linked_list.find_node_with_data(11)

if not node_with_11 is None:
    print(node_with_11.data)
else:
    print("11를 갖는 노드는 없습니다")

# 데이터 6 갖는 노드 탐색
node_with_6 = linked_list.find_node_with_data(6)

if not node_with_6 is None:
    print(node_with_6.data)
else:
    print("6을 갖는 노드는 없습니다")
```

    2
    11
    6을 갖는 노드는 없습니다
    


```python
linked_list.insert_after(node_with_11, 12)
print(linked_list)
```

    | 2 | 3 | 5 | 7 | 11 | 12 |
    


```python
linked_list.insert_after(node_with_2, 2.5)
print(linked_list)
```

    | 2 | 2.5 | 3 | 5 | 7 | 11 | 12 |
    


```python
linked_list.prepend(1)
print(linked_list)
```

    | 1 | 2 | 2.5 | 3 | 5 | 7 | 11 | 12 |
    


```python
lt = LinkedList()
lt.prepend(0)
print(lt)
```

    | 0 |
    


```python
node_with_5 = linked_list.find_node_with_data(5)
linked_list.delete_after(node_with_5)
```




    7




```python
print(linked_list)
```

    | 1 | 2 | 2.5 | 3 | 5 | 11 | 12 |
    


```python
linked_list.delete_after(node_with_11)
```




    12




```python
# 새로운 링크드 리스트 생성
linked_list = LinkedList()

# 여러 데이터를 링크드 리스트 앞에 추가
linked_list.prepend(11)
linked_list.prepend(7)
linked_list.prepend(5)
linked_list.prepend(3)
linked_list.prepend(2)

# 가장 앞 노드 계속 삭제
print(linked_list.pop_left())
print(linked_list.pop_left())
print(linked_list.pop_left())
print(linked_list.pop_left())
print(linked_list.pop_left())

print(linked_list)  # 링크드 리스트 출력
print(linked_list.head)
print(linked_list.tail)
```

    2
    3
    5
    7
    11
    |
    None
    None
    

### <a id='toc1_4_1_'></a>[linked list의 시간 복잡도 time complexity](#toc0_)
---
1. access : O(n)
2. search : O(n)
3. insert/delete : O(1) 직전 노드를 인자로 받아서 바로 처리해버리기 때문
4. search + insert/delete를 붙여놓으면 당연히 O(n+1) = O(n)이 된다

## <a id='toc1_5_'></a>[더블 링크드 리스트 doubly linked list](#toc0_)
---

singly linked list는 바로 다음 노드에 대한 ref만 갖는다  
doubly linked list는 next와 prev를 ref로 갖는다  
코드는 대체로 겹치되 prev 속성을 갖게 해야 한다


```python
class Node:    
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None
        
    
```


```python
class LinkedList:
    """링크드 리스트 클래스"""
    def __init__(self):
        self.head = None  # 링크드 리스트의 가장 앞 노드
        self.tail = None  # 링크드 리스트의 가장 뒤 노드
        
    def find_node_at(self, index):
        """access data. assuming index is there"""
        iterator = self.head
        for _ in range(index):
            iterator = iterator.next
        return iterator
    
    def prepend(self, data):
        """링크드 리스트의 가장 앞에 데이터 삽입"""
        # 코드를 쓰세요
        new = Node(data)
        if self.head == None:
            self.append(data)
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new
            
    # def pop_left(self):
    #     """링크드 리스트의 가장 앞 노드 삭제 메소드. 단, 링크드 리스트에 항상 노드가 있다고 가정한다"""
    #     # 코드를 쓰세요     
    #     gone = self.head.data   
    #     if self.head == self.tail:
    #         self.head = None
    #         self.tail = None
    #     else:
    #         self.head = self.head.next
    #     return gone

    def find_node_with_data(self, data):
        """링크드 리스트에서 탐색 연산 메소드. 단, 해당 노드가 없으면 None을 리턴한다"""
        # 여기에 코드를 작성하세요
        iterator = self.head
        
        while iterator is not None:
            if iterator.data == data:
                return iterator            
            iterator = iterator.next
        return None
    
    def insert_after(self, prev, data):
        """insert data after prev node"""
        new = Node(data)
        if prev == self.tail:
            self.tail.next = new  # 가장 마지막 노드 뒤에 새로운 노드를 추가하고
            new.prev = self.tail
            self.tail = new  # 마지막 노드를 추가한 노드로 바꿔준다
        else: #천재
            prev.next.prev = new #prev's right's left is new
            new.next = prev.next #new's right is prev's right
            prev.next = new #prev's right is new
            new.prev = prev #new's left is prev
                        
    def delete(self, node):
        """delete node after prev node"""
        #lined list에서 노드를 삭제할 땐 그 데이터를 리턴해주는 게 관습
        gone = node.data
        
        if node == self.head == self.tail:
            self.head = None
            self.tail = None
        
        elif node == self.head:
            node.next.prev = None
            self.head = node.next
        
        elif node == self.tail:
            node.prev.next = None #prev의 다음이 없어지게 해야 하는 구나
            self.tail = node.prev
        else: #천재
            node.prev.next = node.next
            node.next.prev = node.prev
        return gone
    

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)
        
        # 링크드 리스트가 비어 있으면 새로운 노드가 링크드 리스트의 처음이자 마지막 노드다
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 링크드 리스트가 비어 있지 않으면
        else:
            self.tail.next = new_node  # 가장 마지막 노드 뒤에 새로운 노드를 추가하고
            new_node.prev = self.tail
            # 요 부분이 다르다 천재!!!
            self.tail = new_node  # 마지막 노드를 추가한 노드로 바꿔준다

    def __str__(self):
        """링크드  리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        # 링크드  리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드  리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += " {} |".format(iterator.data)
            iterator = iterator.next # 다음 노드로 넘어간다

        return res_str
    
    


    
    
```


```python
# 새로운 링크드 리스트 생성
my_list = LinkedList()

# 새로운 노드 5개 추가
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)
my_list.append(11)

print(my_list)

# tail 노드 뒤에 노드 삽입
tail_node = my_list.tail  # 4 번째(마지막)노드를 찾는다
my_list.insert_after(tail_node, 5)  # 4 번째(마지막)노드 뒤에 노드 추가
print(my_list)
print(my_list.tail.data)  # 새로운 tail 노드 데이터 출력

# 링크드 리스트 중간에 데이터 삽입
node_at_index_3 = my_list.find_node_at(3)  # 노드 접근
my_list.insert_after(node_at_index_3, 3)
print(my_list)

# 링크드 리스트 중간에 데이터 삽입
node_at_index_2 = my_list.find_node_at(2)  # 노드 접근
my_list.insert_after(node_at_index_2, 2)
print(my_list)
```

    | 2 | 3 | 5 | 7 | 11 |
    | 2 | 3 | 5 | 7 | 11 | 5 |
    5
    | 2 | 3 | 5 | 7 | 3 | 11 | 5 |
    | 2 | 3 | 5 | 2 | 7 | 3 | 11 | 5 |
    


```python
# 새로운 링크드 리스트 생성
my_list = LinkedList()

# 여러 데이터를 링크드 리스트 앞에 추가
my_list.prepend(11)
my_list.prepend(7)
my_list.prepend(5)
my_list.prepend(3)
my_list.prepend(2)

print(my_list) # 링크드 리스트 출력

# head, tail 노드가 제대로 설정됐는지 확인
print(my_list.head.data)
print(my_list.tail.data)
```

    | 2 | 3 | 5 | 7 | 11 |
    2
    11
    


```python
# 새로운 링크드 리스트 생성
my_list = LinkedList()

# 새로운 노드 4개 추가
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)

print(my_list)

# 두 노드 사이에 있는 노드 삭제
node_at_index_2 = my_list.find_node_at(2)
my_list.delete(node_at_index_2)
print(my_list)

# 가장 앞 노드 삭제
head_node = my_list.head
print(my_list.delete(head_node))
print(my_list)

# 가장 뒤 노드 삭제
tail_node = my_list.tail
my_list.delete(tail_node)
print(my_list)

# 마지막 노드 삭제
last_node  = my_list.head
my_list.delete(last_node)
print(my_list)
```

    | 2 | 3 | 5 | 7 |
    | 2 | 3 | 7 |
    2
    | 3 | 7 |
    | 3 |
    |
    

### <a id='toc1_5_1_'></a>[single Vs. double Usage](#toc0_)
1. single은 한쪽으로만 이동 가능하지만 double은 양쪽으로 이동 가능. 앞에 있는 노드에 접근할 필요가 있는지에 따라 선택 가능
2. 둘 다 memory complexity는 O(n)으로 표기 되지만 실제 single은 n-1개 (tail은 ref가 없으므로), double은 2n-2개가 필요하다

### <a id='toc1_5_2_'></a>[single Vs. double time complexity](#toc0_)

#### <a id='toc1_5_2_1_'></a>[접근 access는 O(n)으로 동일하다](#toc0_)
아래처럼 싹 돌려야 하므로


```python
def find(self, index):
        """access data. assuming index is there"""
        iterator = self.head
        for _ in range(index):
            iterator = iterator.next
        return iterator
```

#### <a id='toc1_5_2_2_'></a>[탐색: 값으로 탐색하는 것도 O(n)으로 동일하다](#toc0_)


```python
def find_node_with_data(self, data):
    """링크드 리스트에서 탐색 연산 메소드. 단, 해당 노드가 없으면 None을 리턴한다"""
    # 여기에 코드를 작성하세요
    iterator = self.head
    
    while iterator is not None:
        if iterator.data == data:
            return iterator            
        iterator = iterator.next
    return None
```

#### <a id='toc1_5_2_3_'></a>[삽입: O(1)으로 동일하다](#toc0_)
위치 값을 받아서 바로 처리하므로


```python
############################################# SINGLE    
    def insert_after(self, prev, data):
        """insert data after prev node"""
        new = Node(data)
        if prev == self.tail:
            self.tail.next = new  # 가장 마지막 노드 뒤에 새로운 노드를 추가하고
            self.tail = new  # 마지막 노드를 추가한 노드로 바꿔준다
        else:
            new.next = prev.next            
            prev.next = new
            
    def delete_after(self, prev):
        """delete node after prev node"""
        #lined list에서 노드를 삭제할 땐 그 데이터를 리턴해주는 게 관습
        gone = prev.next.data
        
        if prev.next == self.tail:
            prev.next = None #prev의 다음이 없어지게 해야 하는 구나
            self.tail = prev
        else:
            prev.next = prev.next.next
            
############################################# DOUBLE            
    def insert_after(self, prev, data):
        """insert data after prev node"""
        new = Node(data)
        if prev == self.tail:
            self.tail.next = new  # 가장 마지막 노드 뒤에 새로운 노드를 추가하고
            new.prev = self.tail
            self.tail = new  # 마지막 노드를 추가한 노드로 바꿔준다
        else: #천재
            prev.next.prev = new #prev's right's left is new
            new.next = prev.next #new's right is prev's right
            prev.next = new #prev's right is new
            new.prev = prev #new's left is prev
                        
    def delete(self, node):
        """delete node after prev node"""
        #lined list에서 노드를 삭제할 땐 그 데이터를 리턴해주는 게 관습
        gone = node.data
        
        if node == self.head == self.tail:
            self.head = None
            self.tail = None
        
        elif node == self.head:
            node.next.prev = None
            self.head = node.next
        
        elif node == self.tail:
            node.prev.next = None #prev의 다음이 없어지게 해야 하는 구나
            self.tail = node.prev
        else: #천재
            node.prev.next = node.next
            node.next.prev = node.prev
        return gone
```

#### <a id='toc1_5_2_4_'></a>[head, tail에 대한 삽입 삭제 연산은 다르다](#toc0_)
- single, double 모두 head의 삽입 삭제(prepend), tail의 추가(append)는 O(1)이다 (접근 1 연산 1)
- 그러나 single은 head에 대한 삽입 삭제는 O(1)이지만 tail에 대한 삭제는 O(n)이다  
single의 삭제는 delete_after 즉 prev node가 필요하다. 따라서 tail 삭제는 tail 직전 노드를 찾아야 하므로 O(n)이다
- double은 delete할 때 삭제할 node만 알면 되므로 tail도 직접 정보를 갖고 있으니 O(1)이다


|| single | double |
| :-- | :-: | :-: |
| access | O(n) | O(n) |
| search | O(n) | O(n) |
| insert/delete | O(1) | O(1) |
| insert/delete head | O(1) | O(1) |
| insert/delete tail | O(n) | O(1) |

## <a id='toc1_6_'></a>[tbd 원형 연결 리스트 circular linked list](#toc0_)
---

## <a id='toc1_7_'></a>[Hash Table](#toc0_)
---

key : value 쌍으로 돼 있는 자료구조  
순서는 없고 키는 중복이 되지 않는다 

direct access table은 key를 index로 사용한다. 마지막 키를 메모리 크기로 정하여 메모리를 확보한 뒤 값을 저장한다.  
그러나 key는 아무 숫자나 될 수 있기 때문에 쓸데없이 큰 값이면 메모리가 낭비된다. 실제로 담긴 값은 적은데 키만 클 수도 있다  
access 가 O(1)인 장점이 있지만 메모리 낭비가 심할 수 있다

hash function은 어떤 값을 지정한 범위의 자연수로 바꿔주는 함수다. 이를 이용해서 key를 index로 변환한다  
먼저 메모리를 확보한 후 메모리 범위에 맞는 hash function에 key를 넣어서 index를 얻는다  
index는 메모리 범위 내에 있으므로 메모리 낭비가 없다. 해당 index에 key와 value를 함께 저장한다

이때 hash function은
1. 결정론적이어야 한다: 같은 key를 넣으면 같은 index를 반환해야 한다
2. 효율적이어야 한다: 빨라야 한다
3. 값이 치우치지 않고 고르게 나와야 한다

파이썬 내장 hash 함수는 불변 자료형에만 쓸 수 있다

### <a id='toc1_7_1_'></a>[hash table 단점](#toc0_)
---
hash table의 문제점은 충돌 collision 가능성이다  
hash function에서 나온 index에 이미 다른 값이 들어있어 중복되는 가능성이다

충돌을 해결하는 방법은 2가지가 있다
1. chaining : linked list를 이용해서 충돌을 해결한다
2. open addressing : 충돌이 일어나면 다른 index를 찾아서 저장한다

### <a id='toc1_7_2_'></a>[chaining](#toc0_)
---

순서가 없기 때문에 access는 없고 search 만 있다  
hash function O(1) + memory access O(1) + search O(n) = O(n)

insert/delete  
hash function O(1) + memory access O(1) + search O(n) + insert/delete O(1) = O(n)

그러나 탐색이 O(n)이 된다는 건 모든 hash 값이 하나의 index로 모이는 worst case라는 뜻이다  
이런 경우는 흔치 않으므로 O(n)이라는 평가는 실용적이지 못할 수 있다  
오로지 search만 O(n)인데 극단적인 경우가 아니라 평균적인 경우를 보려면 하나의 index에 평균적으로 몇 개의 값이 할당되는지 봐야 한다

여기서 하나의 가정을 한다 Simple Uniform Hashing Assumption
SUHA는 모든 key가 index에 배정될 가능성이 1/m이고 서로 독립적이라는 가정이다  
즉 입력할 key가 n개 이고 index가 m개라면 각 index에 할당되리라 예상되는 key의 개수(기대값)는 n/m이다  
n/m은 load factor라고 한다  
이 때 만약 n/m = 1인 상황을 약속한다면 비로소 search의 time complexity는 O(1)이 된다
즉 SUHA와 n = m을 만족하는 경우에 search time complexity는 O(1)이 되는 것이다


```python
class Node:
    """링크드 리스트의 노드 클래스"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  # 다음 노드에 대한 레퍼런스
        self.prev = None  # 전 노드에 대한 레퍼런스


class LinkedList:
    """링크드 리스트 클래스"""
    def __init__(self):
        self.head = None  # 링크드 리스트의 가장 앞 노드
        self.tail = None  # 링크드 리스트의 가장 뒤 노드
        

    def find_node_with_key(self, key):
        """링크드 리스트에서 주어진 데이터를 갖고있는 노드를 리턴한다. 단, 해당 노드가 없으면 None을 리턴한다"""
        iterator = self.head   # 링크드 리스트를 돌기 위해 필요한 노드 변수

        while iterator is not None:
            if iterator.key == key:
                return iterator

            iterator = iterator.next

        return None


    def append(self, key, value):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(key, value)

        # 빈 링크드 리스트라면 head와 tail을 새로 만든 노드로 지정
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 이미 노드가 있으면
        else:
            self.tail.next = new_node  # 마지막 노드의 다음 노드로 추가
            new_node.prev = self.tail
            self.tail = new_node  # 마지막 노드 업데이


    def delete(self, node_to_delete):
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

        return node_to_delete.value


    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = ""

        # 링크드 리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드 리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += "{}: {}\n".format(iterator.key, iterator.value)
            iterator = iterator.next  # 다음 노드로 넘어간다

        return res_str
    
    
```


```python
class HashTable:
    """해시 테이블 클래스"""
    
    def __init__(self, capacity):
        self._capacity = capacity  # 파이썬 리스트 수용 크기 저장
        self._table = [LinkedList() for _ in range(self._capacity)]  # 파이썬 리스트 인덱스에 반 링크드 리스트 저장

    def _hash_function(self, key):
        """
        주어진 key에 나누기 방법을 사용해서 해시된 값을 리턴하는 메소드
        주의: key는 파이썬 불변 타입이여야 한다.
        """
        return hash(key) % self._capacity
    
    def _get_table_index(self, key):
        ind = self._hash_function(key)
        table_index = self._table[ind]
        
        return table_index


    def look_up_value(self, key):
        """
        주어진 key에 해당하는 데이터를 리턴하는 메소드
        """
        # 코드를 쓰세요
        table_index = self._get_table_index(key)        
        node = table_index.find_node_with_key(key)
        return node.value
        
            
    def insert(self, key, value):
        """
        새로운 key - value 쌍을 삽입시켜주는 메소드
        이미 해당 key에 저장된 데이터가 있으면 해당 key에 해당하는 데이터를 바꿔준다
        """
        # 코드를 쓰세요
        table_index = self._get_table_index(key)        
        node = table_index.find_node_with_key(key)
        
        if node is None:
            table_index.append(key, value) # 등록된 적이 없는 key면 등록해준다
        else:
            node.value = value # 등록된 적이 있는 key면 값을 수정한다
            
    def delete_by_key(self, key):
        """주어진 key에 해당하는 key - value 쌍을 삭제하는 메소드"""
        # 코드를 쓰세요            
        table_index = self._get_table_index(key)        
        node = table_index.find_node_with_key(key)
        
        if node is not None:
            table_index.delete(node)
        
        

    def __str__(self):
        """해시 테이블 문자열 메소드"""
        res_str = ""

        for linked_list in self._table:
            res_str += str(linked_list)

        return res_str[:-1]

    
 
```


```python

test_scores = HashTable(50)  # 시험 점수를 담을 해시 테이블 인스턴스 생성

# 여러 학생들 이름과 시험 점수 삽입
test_scores.insert("현승", 85)
test_scores.insert("영훈", 90)
test_scores.insert("동욱", 87)
test_scores.insert("지웅", 99)
test_scores.insert("신의", 88)
test_scores.insert("규식", 97)
test_scores.insert("태호", 90)

print(test_scores)

# key인 이름으로 특정 학생 시험 점수 검색
print(test_scores.look_up_value("현승"))
print(test_scores.look_up_value("태호"))
print(test_scores.look_up_value("영훈"))

# 학생들 시험 점수 수정
test_scores.insert("현승", 10)
test_scores.insert("태호", 20)
test_scores.insert("영훈", 30)

print(test_scores)

```

    영훈: 90
    신의: 88
    동욱: 87
    현승: 85
    규식: 97
    지웅: 99
    태호: 90
    85
    90
    90
    영훈: 30
    신의: 88
    동욱: 87
    현승: 10
    규식: 97
    지웅: 99
    태호: 20
    


```python
test_scores = HashTable(50) # 시험 점수를 담을 해시 테이블 인스턴스 생성

# 여러 학생들 이름과 시험 점수 삽입
test_scores.insert("현승", 85)
test_scores.insert("영훈", 90)
test_scores.insert("동욱", 87)
test_scores.insert("지웅", 99)
test_scores.insert("신의", 88)
test_scores.insert("규식", 97)
test_scores.insert("태호", 90)

# 학생들 시험 점수 삭제
test_scores.delete_by_key("태호")
test_scores.delete_by_key("지웅")
test_scores.delete_by_key("신의")
test_scores.delete_by_key("현승")
test_scores.delete_by_key("규식")

print(test_scores)
```

    영훈: 90
    동욱: 87
    

### <a id='toc1_7_3_'></a>[open addressing](#toc0_)
---

충돌 시 다른 비어있는 인덱스를 찾아서 저장한다

비어있는 인덱스를 찾는 방법은 3가지가 있다
1. linear probing : 다음 인덱스를 찾는다
2. quadratic probing : 다음 인덱스를 찾는데 제곱을 해서 찾는다
3. double hashing : 다른 hash function을 적용한다

이 중에서 linear probing을 쓸 땐 주의해야 한다  
값을 삭제할 때 key, value를 다 없애면 마치 값이 한번도 저장되지 않은 것과 구분되지 않으므로 흔적을 저장해두어야 한다

## <a id='toc1_8_'></a>[추상자료형 abstract data type](#toc0_)
---

기능 Vs. 구현  
기능: 연산이 무엇을 하는지  
구현: 기능을 어떻게 하는지

추상화: 구현을 숨기고 기능만 보여주는 것. 어떻게 구현할지 몰라도 기능을 쓸 수 있다  

"you just type in and it pops out"  
추상화가 잘 돼있는 예. 그때 사용자가 누르는 버튼이 interface

리스트list는 추상자료형이다. 자료구조(동적배열, 링크드 리스트)로 구현할 수 있다  
추상 자료형을 먼저 떠올리고 (어떤 기능이 필요한지 먼저 정의하고) 자료구조(구현)를 정하면 된다

핸드폰이 추상자료형이라면 아이폰, 갤럭시 등등 모델이 자료구조다

### <a id='toc1_8_1_'></a>[리스트list](#toc0_)
---
- 데이터간 순서 유지
- 접근
- 탐색
- 삽입
- 삭제

### <a id='toc1_8_2_'></a>[큐, 대기열Queue](#toc0_)
---
- FIFO 맨 앞에만 삭제되고 맨 뒤에만 추가된다

파이썬에는 deque가 있다 doubly ended queue: 앞뒤로 모두 삽입 삭제가 가능하다


```python
from collections import deque

que = deque()

que.append(1)
que.append(2)
que.append(3)
print(que)
```

    deque([1, 2, 3])
    


```python
que[0]
```




    1




```python
que[1]
```




    2




```python
# 맨앞을 삭제하면서 리턴
que.popleft()
print(que)
```

    deque([2, 3])
    


```python

from collections import deque

class CustomerComplaint:
    """고객 센터 문의를 나타내는 클래스"""
    def __init__(self, name, email, content):
        self.name = name
        self.email = email
        self.content = content

        
class CustomerServiceCenter:
    """고조선 호텔 서비스 센터 클래스"""
    def __init__(self):
        self.queue = deque()  # 대기 중인 문의를 저장할 큐 생성

        
    def process_complaint(self):
        """접수된 고객 센터 문의 내용 처리하는 메소드"""
        # 여기에 코드를 작성하세요
        if not self.queue : ######### BECAUSE VOID IS FALSE ####################
            print('더 이상 대기 중인 문의가 없습니다!')
        else:
            print(f'{self.queue[0].name}님의 {self.queue[0].content} 문의 내용 접수 되었습니다. 담당자가 배정되면 {self.queue[0].email}로 연락드리겠습니다!')
            self.queue.popleft()
            
        ### 마찬가지로 if self.queue로 처리했어도 됐다.
        ### popleft()는 처음 값을 반환하고 삭제하므로 cat = self.queue.popleft()로 했어도 받아올 수 있었다
        


    def add_complaint(self, name, email, content):
        """새로운 문의를 큐에 추가 시켜주는 메소드"""
        # 여기에 코드를 작성하세요
        new = CustomerComplaint(name, email, content)
        self.queue.append(new)


# 고객 문의 센터 인스턴스 생성
center = CustomerServiceCenter()

# 문의 접수한다
center.add_complaint("강영훈", "younghoon@codeit.com", "음식이 너무 맛이 없어요")

# 문의를 처리한다
center.process_complaint()
center.process_complaint()

# 문의 세 개를 더 접수한다
center.add_complaint("이윤수", "yoonsoo@codeit.kr", "에어컨이 안 들어와요...")
center.add_complaint("손동욱", "dongwook@codeit.us", "결제가 제대로 안 되는 거 같군요")
center.add_complaint("김현승", "hyunseung@codeit.ca", "방을 교체해주세요")

# 문의를 처리한다
center.process_complaint()
center.process_complaint()
```

    강영훈님의 음식이 너무 맛이 없어요 문의 내용 접수 되었습니다. 담당자가 배정되면 younghoon@codeit.com로 연락드리겠습니다!
    더 이상 대기 중인 문의가 없습니다!
    이윤수님의 에어컨이 안 들어와요... 문의 내용 접수 되었습니다. 담당자가 배정되면 yoonsoo@codeit.kr로 연락드리겠습니다!
    손동욱님의 결제가 제대로 안 되는 거 같군요 문의 내용 접수 되었습니다. 담당자가 배정되면 dongwook@codeit.us로 연락드리겠습니다!
    


```python
from collections import deque

class CustomerComplaint:
    """고객 센터 문의를 나타내는 클래스"""
    def __init__(self, name, email, content):
        self.name = name
        self.email = email
        self.content = content

class CustomerServiceCenter:
    """고조선 호텔 서비스 센터 클래스"""
    def __init__(self):
        self.queue = deque()   # 대기 중인 문의를 저장할 큐 생성

    def process_complaint(self):
        """접수된 고객 센터 문의 내용 처리하는 메소드"""
        if self.queue:  # 대기 중인 문의가 있는지 확인

            # 가장 오래된 문의 먼저 처리
            complaint = self.queue.popleft()
            print(f"{complaint.name}님의 {complaint.content} 문의 내용 접수 되었습니다. 담당자가 배정되면 {complaint.email}로 연락드리겠습니다!")
        else:
            print("더 이상 대기 중인 문의가 없습니다!")


    def add_complaint(self, name, email, content):
        """새로운 문의를 큐에 추가 시켜주는 메소드"""
        new_complaint = CustomerComplaint(name, email, content)   # 새 문의 인스턴스 생성
        self.queue.append(new_complaint)   # 문의 대기 큐에 추가 시켜준다
```


```python
x = deque()
x.pop()
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    Cell In[31], line 2
          1 x = deque()
    ----> 2 x.pop()
    

    IndexError: pop from an empty deque


### <a id='toc1_8_3_'></a>[스택Stack](#toc0_)
---

- LIFO
- 맨 뒤에만 추가되고 맨 뒤에만 삭제된다 (맨 뒤만 접근)

조금 시간이 걸렸지만 힌트 한 개만 보고 잘 해냈다!


```python

from collections import deque

def parentheses_checker(string):
    """주어진 문자열 인풋의 모든 괄호가 짝이 있는지 확인해주는 메소드"""


    print(f"테스트하는 문자열: {string}")
    stack = deque() # 사용할 스택 정의

    # 여기에 코드를 작성하세요
    
    for x in range(len(string)):
        if string[x] == '(':
            stack.append(x)      
        elif stack and string[x] == ')':
            stack.pop()
        elif not stack and string[x] == ')':
            print(f'문자열 {x} 번째 위치에 있는 닫는 괄호에 맞는 열리는 괄호가 없습니다')
                    
                
    if stack:    
        for x in range(len(stack)):
            index = stack.pop()
            print(f'문자열 {index} 번째 위치에 있는 괄호가 닫히지 않았습니다')

        
            
    # for x in range(len(string)):
    #     if string[x] == ')':
    #         stack.append(x)      
    #     if stack:
    #         if string[x] == '(':
    #             stack.pop()
    # if stack:
    #     for x in range(stack):
    #         index = stack.pop()
    #         print(f'문자열 {index} 번째 위치에 있는 괄호가 닫히지 않았습니다')
    
    
    
    # if index 번째 괄호 안 닫힘:
    #     print(f'문자열 {index} 번째 위치에 있는 괄호가 닫히지 않았습니다')
    # elif index 번째 괄호 안 열림:
    #     print(f'문자열 {index} 번째 위치에 있는 닫는 괄호에 맞는 열리는 괄호가 없습니다')

case1 = "(1+2)*(3+5)"
case2 = "((3*12)/(41-31))"
case3 = "((1+4)-(3*12)/3"
case4 = "(12-3)*(56/3))"
case5 = ")1+14)/3"
case6 = "(3+15(*3"

parentheses_checker(case1)
parentheses_checker(case2)
parentheses_checker(case3)
parentheses_checker(case4)
parentheses_checker(case5)
parentheses_checker(case6)
```

    테스트하는 문자열: (1+2)*(3+5)
    테스트하는 문자열: ((3*12)/(41-31))
    테스트하는 문자열: ((1+4)-(3*12)/3
    문자열 0 번째 위치에 있는 괄호가 닫히지 않았습니다
    테스트하는 문자열: (12-3)*(56/3))
    문자열 13 번째 위치에 있는 닫는 괄호에 맞는 열리는 괄호가 없습니다
    테스트하는 문자열: )1+14)/3
    문자열 0 번째 위치에 있는 닫는 괄호에 맞는 열리는 괄호가 없습니다
    문자열 5 번째 위치에 있는 닫는 괄호에 맞는 열리는 괄호가 없습니다
    테스트하는 문자열: (3+15(*3
    문자열 5 번째 위치에 있는 괄호가 닫히지 않았습니다
    문자열 0 번째 위치에 있는 괄호가 닫히지 않았습니다
    

### <a id='toc1_8_4_'></a>[dict = map](#toc0_)
---
- key, value 쌍으로 저장, 탐색, 삭제
- 순서는 없음
- key의 중복은 안됨

### <a id='toc1_8_5_'></a>[set](#toc0_)
---
- 순서는 없음
- 삽입, 탐색, 삭제
- 중복은 안됨

## <a id='toc1_9_'></a>[정리](#toc0_)
---

||list|deque|dict|set|
|:--|:-:|:-:|:-:|:-:|
|access|O(1)|X|X|X|
|append|O(1)|O(1)|X|X|
|pop|O(1)|O(1)|X|X|
|appendleft|X|O(1)|X|X|
|popleft|X|O(1)|X|X|
|len|O(1)|O(1)|O(1)|O(1)|
|in|O(n)|X|O(1) dict[x]|O(1)|
|insert|O(n)|X|O(1) dict[x] = y|O(1) add|
|del|O(n) del, pop|X|O(1) del, pop|O(1) remove, pop|

자료형을 잘 선택하려면 어떤 기능을 쓰려고 하는지 생각해야 한다  
예를 들어 탐색 in 기능을 자주 쓰려고 한다면 list 보다 set을 쓰는 게 훨씬 빠르다

## <a id='toc1_10_'></a>[수료증](https://www.codeit.kr/certificates/fdvY7-Lm2Lt-AKOmJ-gcXsN) [&#8593;](#toc0_)
