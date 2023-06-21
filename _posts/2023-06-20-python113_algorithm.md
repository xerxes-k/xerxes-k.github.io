---
layout: single
title:  "알고리즘이란?"
---

# 알고리즘이란?

컴퓨터 알고리즘이란, 컴퓨터가 어떤 문제를 해결하기 위해서 컴퓨터가 이해할 수 있는 방식으로 정리되어 있는 해결 방법이다

좋은 알고리즘이란?
1. 문제를 정확하게 해결하고
2. 문제를 효율적으로 해결하는 알고리즘

알고리즘은 결국 프로그램으로 구현한다


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
```


```python
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
    

## 탐색

순차적으로 쭉 보는 걸 선형 탐색linear search이라고 한다

만약 값이 정렬돼 있다면 중간 값을 열어보고 한쪽 방향만 찾아보는 이진 탐색binary search을 쓸 수 있다


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
    

아래 문제를 푸느라 1시간 넘게 걸렸다. 풀긴 풀었는데 해설 답안이 훨씬 낫다


```python
# def binary_search(element, some_list):
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


    Cannot execute code, session has been disposed. Please try restarting the Kernel.



    The Kernel crashed while executing code in the the current cell or a previous cell. Please review the code in the cell(s) to identify a possible cause of the failure. Click <a href='https://aka.ms/vscodeJupyterKernelCrash'>here</a> for more info. View Jupyter <a href='command:jupyter.viewOutput'>log</a> for further details.



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
    

선형 탐색과 이진 탐색 모두 최소 반복 회수는 1번이다. 1번 만에 값을 찾을 수도 있기 때문  
그러나 최대 반복 회수는 선형 탐색은 n번, 이진 탐색은 log2n번이다  
이진 탐색은 리스트의 반을 버리면서 탐색하기 때문에 반복 회수가 log2n이 된다  
따라서 이진 탐색이 선형 탐색에 비해 효율적일 수 있지만 이진 탐색은 리스트가 정렬돼있어야 한다는 조건이 있다

정렬은 문제 해결의 기본 도구 중 하나이므로 꼭 알아야 한다

선택 정렬 selection sort란 리스트 전체를 순회하면서 최솟값을 찾아서 맨 앞으로 보내는 정렬 방법이다

삽입 정렬 insertion sort 카드 정리하듯이 각 값이 어떤 위치에 들어가야 할지 찾는다

아래 사이트에서 각 정렬 알고리즘의 정렬 속도를 확인할 수 있다

https://www.toptal.com/developers/sorting-algorithms

알고리즘이 효율적이어야 하는 이유는 시간과 공간이 한정적이기 때문이다

시간 복잡도는 알고리즘의 시간 효율을 측정하는 지표 중 하나로  
알고리즘의 반복 횟수를 입력 데이터의 크기 n의 함수로 표현한 것이다  
데이터가 증가해도 소요시간이 덜 증가하는 게 좋은 알고리즘이다

the time complexity is generally expressed as a function of the size of the input

알고리즘을 평가할 때 점근표기법 asymptotic notation을 사용한다  
이를 빅오노테이션 Big O notation이라고 한다

걸리는 시간을 수식으로 표현한 값에서 상수는 무시하고 가장 큰 영향을 주는 n만 남긴다  
고로 1000000000000n + 1000000000이든 n + 1이든 동일하다  
n을 극한값으로 가정하기 때문이다 (최악의 케이스 가정)  
O(n), O(n^2), O(logn) 등이 그 꼴이다

알고리즘 시간 복잡도는 대체로  
- O(1) < O(logn) < O(n) < O(nlogn) < O(n^2) < O(2^n) < O(n!) 순이다

최악의 경우 몇번 n을 돌려야 하지?를 떠올리면 대체로 알 수 있다

공간 복잡도 역시 마찬가지다 데이터가 n개 일 때 얼마의 공간이 필요한지 n에 대한 함수로 표현한다
