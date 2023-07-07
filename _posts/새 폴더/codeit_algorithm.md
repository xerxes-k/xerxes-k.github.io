**Table of contents**<a id='toc0_'></a>    
- [algorithm 알고리즘](#toc1_)    
  - [좋은 알고리즘이란?](#toc1_1_)    
  - [정렬과 선택 알고리즘](#toc1_2_)    
    - [탐색](#toc1_2_1_)    
      - [linear search 선형 탐색](#toc1_2_1_1_)    
      - [binary search 이진 탐색](#toc1_2_1_2_)    
  - [정렬](#toc1_3_)    
  - [알고리즘 평가법](#toc1_4_)    
    - [시간복잡도](#toc1_4_1_)    
    - [공간복잡도](#toc1_4_2_)    
  - [수료증](#toc1_5_)    

<!-- vscode-jupyter-toc-config
	numbering=false
	anchor=true
	flat=false
	minLevel=1
	maxLevel=6
	/vscode-jupyter-toc-config -->
<!-- THIS CELL WILL BE REPLACED ON TOC UPDATE. DO NOT WRITE YOUR TEXT IN THIS CELL -->

# <a id='toc1_'></a>[algorithm 알고리즘](#toc0_)
---
컴퓨터 알고리즘이란, (컴퓨터로 어떤 문제를 해결하기 위해서) 컴퓨터가 이해할 수 있는 방식으로 정리한 일련의 절차이다

a process or set of rules to be followed in calculations or other problem-solving operations, especially by a computer.

이렇게 보면 프로그래밍이랑 정의가 엄청 비슷하다. 생각해보면 이렇게 정리되는 듯 하다:  
컴퓨터한테 "이거 이거 해"라고 할 수 없으니 작업을 순서대로 묶어주는 걸 프로그래밍이라 하고 그 정리된 작업, 즉 작업 수행 절차를 알고리즘이라 한다

## <a id='toc1_1_'></a>[좋은 알고리즘이란?](#toc0_)
---
1. 문제를 정확하게 해결하고
2. 문제를 효율적으로 해결하는 알고리즘


```python
def is_palindrome(word):
    list_word=list(word)

    for i in range(len(word)//2):
        if list_word[i] == list_word[-i-1]:
            continue
        else:
            return False
            # print(False)
    return True

print(is_palindrome("racecar"))
print(is_palindrome("starsaaa"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
```

    True
    False
    True
    True
    False
    

## <a id='toc1_2_'></a>[정렬과 선택 알고리즘](#toc0_)
---

### <a id='toc1_2_1_'></a>[탐색](#toc0_)
---
- 선형 탐색 linear search
- 이진 탐색 binary search

#### <a id='toc1_2_1_1_'></a>[linear search 선형 탐색](#toc0_)
---
순차적으로 쭉 보는 걸 선형 탐색linear search이라고 한다


```python

def linear_search(element, some_list):
    # 여기에 코드를 작성하세요
    for e in range(len(some_list)):
        if some_list[e] == element:
            return e
    else:
        return None
    
        

print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))
```

    0
    None
    2
    1
    4
    

#### <a id='toc1_2_1_2_'></a>[binary search 이진 탐색](#toc0_)
---
만약 값이 정렬돼 있다면 중간 값을 열어보고 필요한 한쪽 방향만 찾아보는 이진 탐색binary search을 쓸 수 있다

아래 문제를 푸느라 1시간 넘게 걸렸다. 풀긴 풀었는데 해설 답안이 훨씬 낫다


```python
def binary_search(element, some_list):
    # 여기에 코드를 작성하세요
    st = 0 #처음 인덱스
    ed = len(some_list) - 1 #마지막 인덱스
    md = (st + ed) // 2 #중간 인덱스
    if some_list[md] == element: #중간 인덱스의 값이 찾는 값과 일치
        return md
    elif some_list[md] > element: #중간 인덱스의 값이 찾는 값보다 크다
        #왼쪽 탐색        
        return binary_search(element, some_list[:md])
    elif some_list[md] < element: #중간 인덱스의 값이 찾는 값보다 작다
        #오른쪽 탐색
        return binary_search(element, some_list[md + 1:])
    #원래 인덱스를 잊어버린다
    #None값 처리가 없다

print(binary_search(2, [2, 3, 5, 7, 11]))
# print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
```

    0
    2
    0
    0
    


```python
def binary_search(element, some_list):
    # 여기에 코드를 작성하세요
    st = 0 #처음 인덱스
    ed = len(some_list) - 1 #마지막 인덱스
    md = (st + ed) // 2 #중간 인덱스
    if element not in some_list:
        return None
    while some_list[md] != element:    
        if some_list[md] > element: #중간 인덱스의 값이 찾는 값보다 크다
            ed = md
            md = (st + ed) // 2 #중간 인덱스
        elif some_list[md] < element: #중간 인덱스의 값이 찾는 값보다 작다
            st = md + 1
            md = (st + ed) // 2 #중간 인덱스
    if some_list[md] == element: #중간 인덱스의 값이 찾는 값과 일치
        return md    
        
print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
```

    0
    None
    2
    1
    4
    

- start 와 end가 같아질 때까지 찾아서 없으면 없는 거라고 하면 된다
    - not in을 쓴 건 사실상 반칙이다
- 여기선 리스트를 쓰지 않으므로 end가 md가 될 필요가 없다 mid - 1까지로 해놓아도 된다
    - **어차피 md만 찾는 형식이다!**


```python
def binary_search(element, some_list):
    start_index = 0
    end_index = len(some_list) - 1
    
    while start_index <= end_index:
        midpoint = (start_index + end_index) // 2
        if some_list[midpoint] == element:
            return midpoint
        elif some_list[midpoint] > element:
            end_index = midpoint - 1
        else:
            start_index = midpoint + 1
    return None

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
```

    0
    None
    2
    1
    4
    

## <a id='toc1_3_'></a>[정렬](#toc0_)
---
- 선택 정렬 selection sort이란 리스트 전체를 순회하면서 최솟값을 찾아서 맨 앞으로 보내는 정렬 방법이다
- 삽입 정렬 insertion sort 카드 정리하듯이 각 값이 어떤 위치에 들어가야 할지 찾는다  


이 외에도 다양한 정렬 알고리즘이 있다 다음 사이트들에서 정렬 알고리즘을 비교해서 볼 수 있다  
[알고리즘 비교](https://www.toptal.com/developers/sorting-algorithms)  
[알고리즘 포크 댄스](https://www.youtube.com/@AlgoRythmics)

## <a id='toc1_4_'></a>[알고리즘 평가법](#toc0_)
---
알고리즘은 자원을 효율적으로 쓸수록 좋다고 판단한다. 그렇다면 자원은 무엇일까?  
시간과 공간이다  

예를 들어  
선형 탐색과 이진 탐색 모두 최소 반복 회수는 1번이다. 1번 만에 값을 찾을 수도 있기 때문  
그러나 최대 반복 회수는 선형 탐색은 n번, 이진 탐색은 log2n번이다  
이진 탐색은 리스트의 반을 버리면서 탐색하기 때문에 반복 회수가 log2n이 된다  
따라서 이진 탐색이 선형 탐색에 비해 효율적일 수 있다. 그러나 이진 탐색은 리스트가 정렬돼있어야 한다는 조건이 있다

시간과 공간 소모를 어떤 식으로 표기해서 비교할까?  
점근표기법 漸近 表記法 asymptotic notation으로 표기해서 비교한다  
점근표기법을 빅오노테이션 Big O notation이라고 한다

### <a id='toc1_4_1_'></a>[시간복잡도](#toc0_)

시간 복잡도는 알고리즘의 시간 효율을 측정하는 지표 중 하나로 알고리즘의 반복 횟수를 입력 데이터 크기 n의 함수로 표현한 것이다  
the time complexity is generally expressed as a function of the size of the input  
데이터가 증가해도 소요시간이 덜 증가하는 게 좋은 알고리즘이다

걸리는 시간을 수식으로 표현한 값에서 상수는 무시하고 가장 큰 영향을 주는 n만 남겨서 표시한다  
그러므로 (1000000000000n + 1000000000)이든 (n + 1)이든 둘 다 O(n)으로 표기법은 동일하다  
이러한 이유는 최악의 케이스를 가정해 데이터 사이즈가 무한히 크다고(n을 무한대로) 가정하기 때문이다  

알고리즘 시간 복잡도는 대체로  
- O(1) < O(logn) < O(n) < O(nlogn) < O(n^2) < O(2^n) < O(n!) 순이다

최악의 경우 몇번 n을 돌려야 하지?를 떠올리면 대체로 알 수 있다

### <a id='toc1_4_2_'></a>[공간복잡도](#toc0_)
공간 복잡도 역시 마찬가지다 데이터가 n개 일 때 얼마의 공간이 필요한지 n에 대한 함수로 표현한다

## <a id='toc1_5_'></a>[수료증](https://www.codeit.kr/certificates/SU9aO-UJ6Yc-z8jbT-MaBqR) [&#8593;](#toc0_)
