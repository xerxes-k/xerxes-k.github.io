**Table of contents**<a id='toc0_'></a>    
- [알고리즘 패러다임 Algorithm Paradigm](#toc1_)    
  - [Brute Force 무차별 대입법](#toc1_1_)    
  - [Divide and Conquer 분할 정복법](#toc1_2_)    
  - [Dynamic Programming 동적 계획법](#toc1_3_)    
    - [memoization = topdown = recursive](#toc1_3_1_)    
    - [tabulation = bottom up = iterative](#toc1_3_2_)    
  - [Greedy Algorithm 탐욕 알고리즘](#toc1_4_)    
  - [수료증](#toc1_5_)    

<!-- vscode-jupyter-toc-config
	numbering=false
	anchor=true
	flat=false
	minLevel=1
	maxLevel=6
	/vscode-jupyter-toc-config -->
<!-- THIS CELL WILL BE REPLACED ON TOC UPDATE. DO NOT WRITE YOUR TEXT IN THIS CELL -->

# <a id='toc1_'></a>[알고리즘 패러다임 Algorithm Paradigm](#toc0_)

자주 등장하는 알고리즘들을 분류해서 정리하고 패러다임이라 부른다  
패러다임은 원래 현재까지 정립된 세계관을 말할텐데?

## <a id='toc1_1_'></a>[Brute Force 무차별 대입법](#toc0_)
가능한 경우의 수를 모두 대입해보는 방식


```python
def max_product(left_cards, right_cards):
    # 여기에 코드를 작성하세요
    card = []
    for l in left_cards:
        for r in right_cards:
            card.append(l * r)
    return max(card)
    
# 테스트 코드
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))
```

    24
    32
    28
    


```python
# 제곱근 사용을 위한 sqrt 함수
from math import sqrt

# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(coordinates):
    # 여기에 코드를 작성하세요
    pair = []
    dist = distance(coordinates[0], coordinates[1])
    for a in coordinates:
        for b in coordinates:
            if a == b:
                pass
            elif distance(a, b) < dist:
                pair = [a, b]
                dist = distance(a, b)
            else:
                dist = dist
    
    return pair

# 테스트 코드
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))
```

    [(2, 3), (3, 4)]
    


```python
def trapping_rain(buildings):
    # 여기에 코드를 작성하세요
    # 자기보다 크거나 같은 수가 자기 이후에 있으면
    # 그 수가 나오기 전까지 모든 수는 자기와 같다
    # ------- 이렇게 하려면 자기보다 큰 수의 인덱스를 알아야 한다
    #---
    # 다음 수가 현재 수 보다 작거나 같으면 (현재 수 - 다음 수)를 더한다
    # 다음 수가 현재 수 보다 크면  --------- 이렇게 하면 물이 안 가둬진 것도 더하게 된다
    # 힌트를 보니 왼쪽 오른쪽의 최대 값을 모두 보란다
    # 물 양은 가장 높은 양 건물 중 작은 값으로 제한되니 문제 없겠구나
    
    water = 0
    for x in range(len(buildings) - 1):
        left = max(buildings[:x + 1] )
        right = max(buildings[x:])
        water += min(left, right) - buildings[x]
    return water
            
        
# 테스트 코드
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
```

    10
    6
    

## <a id='toc1_2_'></a>[Divide and Conquer 분할 정복법](#toc0_)

0. find base case
1. divdie
2. conquer
3. combine

In data structures and algorithms, Divide and Conquer is a recursive problem-solving approach that divides the problem into smaller subproblems, recursively solves each subproblem, and combines the subproblem's solutions to get the solution of the original problem. So, there are four steps in the divide and conquer algorithm

문제를 쪼개서 재귀적으로 풀고 다시 결과들을 합쳐서 해결한다


```python
def consecutive_sum(start, end):
    # 여기에 코드를 작성하세요
    if start == end:
        return start
    else:
        return consecutive_sum(start, end - 1) + end

# 테스트 코드
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))
```

    55
    5050
    32131
    75466
    

아래처럼 반환 값에서 나란히 놓으면 되는 구나. 이렇게 나란히 놓는 걸 몰랐다


```python
def consecutive_sum(start, end):
    # 여기에 코드를 작성하세요
    if start == end:
        return start
    else:
        tmp = (start + end) // 2
        return consecutive_sum(start, tmp) + consecutive_sum(tmp + 1, end)

# 테스트 코드
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))
```

    55
    5050
    32131
    75466
    

아래 merge는 1시간 넘게 걸렸다 힌트도 다 봤다 영상 설명과 문제 질문이 조금 달랐다


```python
def merge(list1, list2):
    # 여기에 코드를 작성하세요
    merged = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1
    if i != len(list1):
        merged += list1[i:]
    if j != len(list2):
        merged += list2[j:]
    return merged
                
    
# 테스트 코드
print(merge([1],[]))
print(merge([],[1]))
print(merge([2],[1]))
print(merge([1, 2, 3, 4],[5, 6, 7, 8]))
print(merge([5, 6, 7, 8],[1, 2, 3, 4]))
print(merge([4, 7, 8, 9],[1, 3, 6, 10]))
```

    [1]
    [1]
    [1, 2]
    [1, 2, 3, 4, 5, 6, 7, 8]
    [1, 2, 3, 4, 5, 6, 7, 8]
    [1, 3, 4, 6, 7, 8, 9, 10]
    

while 조건 안에 i, j를 동시에 넣는다?


```python
i = 0
j = 0
while i < 5:    
    while j < 5:
        i += 1
        print(i, j)                
        j += 1
```

    1 0
    2 1
    3 2
    4 3
    5 4
    


```python
i = 0
j = 0
while i < 5 and j < 5:
    i += 1
    print(i, j)    
    j += 1
```

    1 0
    2 1
    3 2
    4 3
    5 4
    

힌트도 다 봤다 한참 걸렸다


```python
# 합병 정렬
def merge_sort(my_list):
    # 여기에 코드를 작성하세요
    # 각 리스트가 정렬이 될 때까지
    if len(my_list) <= 1:
        return my_list
    left = merge_sort(my_list[:len(my_list)//2])
    right = merge_sort(my_list[len(my_list)//2:])
    
    return merge(left, right)

# 테스트 코드
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))

```

    [1, 3, 5, 7, 9, 11, 11, 13]
    [1, 5, 7, 9, 13, 15, 28, 30, 48]
    [1, 1, 2, 2, 4, 4, 4, 5, 6, 6, 7, 7, 10, 11, 13, 15]
    


```python
# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    # 여기에 코드를 작성하세요
    tmp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = tmp
list1 = [1, 2, 3, 4, 5, 6]
swap_elements(list1, 2, 5)  # 2번 인덱스 값과 5번 인덱스 값 위치 바꿈
print(list1)
```

    [1, 2, 6, 4, 5, 3]
    

아래 예제는 모범 답안을 보고 수정함  
while 문 안에서 해야 하는 것과 밖에서 해야 하는 것을 구분해야 하고  
while 문 안에 있는 if 조건문 안에서 해야 하는 것과 밖에서 해야 하는 걸 구분해야 한다  
이래도 이래야 하고 저래도 이래야 하는 건 if 조건문으로 나눌 필요 없이 if가 끝나고 어차피 하게 하면 된다 (i += 1)  
b, p 요소를 바꾸는 건 상황이 종결되고 나서 따로 해주면 되므로 while이 끝나고 어차피 하게 하면 된다


```python
# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    # 여기에 코드를 작성하세요
    b = start
    i = start
    p = end    
    while i < p: #리스트의 길이는 그대로인데 끝지점이 달라지는 거라 끝지점을 직접 써줘야 한다
    # while i < len(my_list) - 1:  
        if my_list[i] <= my_list[p]:            
            swap_elements(my_list, i, b)
            b += 1
        i += 1
    swap_elements(my_list, b, p)
    p = b                            
    return p


# 테스트 코드 1
list1 = [4, 3, 6, 2, 7, 1, 5]
pivot_index1 = partition(list1, 0, len(list1) - 1)
print(list1)
print(pivot_index1)

# 테스트 코드 2
list2 = [6, 1, 2, 6, 3, 5, 4]
pivot_index2 = partition(list2, 0, len(list2) - 1)
print(list2)
print(pivot_index2)

```

    [4, 3, 2, 1, 5, 6, 7]
    4
    [1, 2, 3, 4, 6, 5, 6]
    3
    


```python
# 퀵 정렬
def quicksort(my_list, start, end):
    # 여기에 코드를 작성하세요
    if end - start < 1:
        return    
    p = partition(my_list, start, end)
    quicksort(my_list, start, p-1) 
    quicksort(my_list, p+1, end)
    
    #새로운 리스트를 반환하는 게 아니기 때문에 한번 받은 리스트를 계속 돌려먹어야 한다는 걸
    #알아차리는 게 가장 중요한 포인트구나
    
    # left = my_list[:p]
    # right = my_list[p:]
    # quicksort(left, 0, len(left) - 1)
    # quicksort(right, 0, len(right) - 1)


# 테스트 코드 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1, 0, len(list1) - 1)
print(list1)

# 테스트 코드 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2, 0, len(list2) - 1)
print(list2)

# 테스트 코드 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3, 0, len(list3) - 1)
print(list3)
```

    [1, 3, 5, 7, 9, 11, 11, 13]
    [1, 5, 7, 9, 13, 15, 28, 30, 48]
    [1, 1, 2, 2, 4, 4, 4, 5, 6, 6, 7, 7, 10, 11, 13, 15]
    


```python
list1 = [1]
partition(list1, 0, len(list1)-1)
```




    0




```python
def quicksort(my_list, start=-1, end=-1):
    # 여기에 코드를 작성하세요
    if end == -1:
        end = len(my_list) - 1
    if start == -1:
        start = 0
    if end - start < 1:
        return    
    p = partition(my_list, start, end)
    quicksort(my_list, start, p-1) 
    quicksort(my_list, p+1, end)
```


```python
# 테스트 코드 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1) # start, end 파라미터 없이 호출
print(list1)

# 테스트 코드 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2) # start, end 파라미터 없이 호출
print(list2)

# 테스트 코드 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3) # start, end 파라미터 없이 호출
print(list3)
```

    [1, 3, 5, 7, 9, 11, 11, 13]
    [1, 5, 7, 9, 13, 15, 28, 30, 48]
    [1, 1, 2, 2, 4, 4, 4, 5, 6, 6, 7, 7, 10, 11, 13, 15]
    

이번 예제를 푸는 데 있어서도 리스트를 슬라이싱하면 새로운 리스트를 만들어서 기존 리스트는 수정이 안된다든지, 리스트를 줄이지 않기 때문에 while의 끝값을 지정해줘야 한다든지, 한번 받은 리스트를 시작점과 끝점을 바꿔가면서 조작해줘야 한다는 등 "파이썬 상식"이 부족했다  
바꿔 말하면 문제에서 설명하는 내용만으로 문제를 풀기가 어려웠다  
여러 문제를 풀고 실제로 개발하면서 경험치를 쌓아야 하는 부분이다  
문제풀이를 많이 하자

## <a id='toc1_3_'></a>[Dynamic Programming 동적 계획법](#toc0_)

Dynamic Programming is mainly an optimization over plain recursion. Wherever we see a recursive solution that has repeated calls for same inputs, we can optimize it using Dynamic Programming. The idea is to simply store the results of subproblems, so that we do not have to re-compute them when needed later. This simple optimization reduces time complexities from exponential to polynomial.

재귀함수의 최적화 버전이라고 할 수 있다. 단순히 자기 스스로를 반복해서 불러내는 재귀함수가 있다면 이전 계산 결과를 저장해둠으로써 계산을 반복하지 않게 만드는 게 핵심이다. overlapping subproblem 중복되는 부분 문제를 매번 다시 푸는 것이 아니라 한 번만 풀고 기록해두고 다음에는 기록된 값을 사용하는 것

그러려면 두 가지 전제가 필요하다
- optimal substructure 최적 부분 구조가 있다
- overlapping subproblem 중복되는 하위 문제가 있다

크게 두가지 방법이 있다
1. memoization 메모이제이션: 사전 + 재귀함수. 결국 재귀함수라 call stack이 넘칠 수 있다
2. tabulation 타뷸레이션: 리스트 + 반복문. 반복문이라 불필요한 계산을 할 수도 있다

### <a id='toc1_3_1_'></a>[memoization = topdown = recursive](#toc0_)


```python
def fib_memo(n, cache):
    # 여기에 코드를 작성하세요


def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}

    return fib_memo(n, fib_cache)


# 테스트 코드
print(fib(10))
print(fib(50))
print(fib(100))
```

이 모양을 봤을 때 이게 뭔지 확 와닿지가 않는다. 코딩 경험이 부족한 거다  
힌트를 5개 다 까봤는데 이미 고민하고 있는 내용만 나온다 ㅠㅠ  
거의 1시간 반 걸렸다 ... 그래도 결국 풀었다 짜릿하다 ㅠㅠ


```python
def fib_memo(n, cache):
    # 여기에 코드를 작성하세요    
    # cache |= cache
    # cache[n] = cache[n]
    # 사전에서 n의 값을 반환하기
    #base case
    if n < 3:
        return 1
    if n in cache:
        return cache[n]
    cache[n] = fib_memo(n-1, cache) + fib_memo(n-2, cache)    #값이 없으면 계산해서 사전에 넣기
    return cache[n]
    
def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}
    #값이 있는지 찾기

    return fib_memo(n, fib_cache)


# 테스트 코드
print(fib(10))
print(fib(50))
print(fib(500))
```

    55
    12586269025
    139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125
    

### <a id='toc1_3_2_'></a>[tabulation = bottom up = iterative](#toc0_)

here we go again  
다행히 이건 좀 덜 걸렸다


```python
def fib_tab(n):
    # 여기에 코드를 작성하세요
    table = [0, 1, 1]
    for x in range(3, n+1):
        table.append(table[x-1] + table[x-2])
    return table[n]

# 테스트 코드
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))
```

    55
    225851433717
    1725375039079340637797070384
    

공간 최적화 -> tabulation은 모든 값을 저장하고 있으니 저장하는 메모리를 최소화해보자  
기존 tabulation은 n개를 저장하니까 O(n)이었다  
아래 변수 2개만 저장하는 코드는 메모리 복잡도가 O(1)이다


```python
def fib_optimized(n):
    # 여기에 코드를 작성하세요
    cur = 1
    prev = 0
    
    for x in range(1, n):
        cp = cur + prev
        prev = cur
        cur = cp
    
    return cp


# 테스트 코드
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))

```

    987
    53316291173
    146178119651438213260386312206974243796773058
    

이 아래도 몇 시간 고민하고 해설을 봤다


```python
def max_profit_memo(price_list, count, cache):
    # 여기에 코드를 작성하세요
    if count < 2:
        cache[count] = price_list[count]
        return cache[count]
    
    if count in cache:
        return cache[count]
    
    ## 문제를 해결하는 데 중요한 발상은 세 가지로 보인다
    ## range에서 (1, count // 2 + 1) 범위로 돌리는 것
    ## (max_profit_memo(price_list, count - x, cache) + max_profit_memo(price_list, x, cache) 으로 재귀를 돌리는 것
    ## 마지막으로 리스트에 있는 최대값과 직접 비교하는 걸 분리하는 것
    ##   최대값과 직접 비교하는 걸 분리하는 부분 빼고는 다 왔다. 잘했다.
    ##    변수를 만들어서 케이스들을 몽땅 묶어서 그 중에 최대값을 빼야 하나 하고 있었는데 리스트 최대값만 분리하면 되다니
    ##      if 조건문을 여러개로 나누는 게 중요하구나. 문제를 작게 쪼개고 분리해내 게 중요하다.      
    
    if count < len(price_list):
        maximo = price_list[count]
    else:
        maximo = 0  
    
    for x in range(1, count//2 + 1):
        maximo = max(maximo, max_profit_memo(price_list, count - x, cache) + max_profit_memo(price_list, x, cache))
            
    cache[count] = maximo
    return cache[count]

    
#################################이전 시도
    # maximo = 0
    # for x in range(1, count//2 + 1):
    #     if count < len(price_list):
    #         sep = (max_profit_memo(price_list, count - x, cache) + max_profit_memo(price_list, x, cache))
    #         maximo = max(maximo, price_list[count], sep)            
    #     else:
    #         maximo = (max_profit_memo(price_list, count - x, cache) + max_profit_memo(price_list, x, cache))
    
        
    # cache[count] = max(price_list[count], (max_profit_memo(price_list, [count - 1], cache) + max_profit_memo(price_list, 1, cache)))
    
    # print(count, maximo)
    
####################################


    
def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트 코드
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))
```

    1200
    2500
    2400
    


```python
def max_profit(price_list, count):
    # 여기에 코드를 작성하세요
    table = [0]
    if count < len(price_list):
        maximo = price_list[count]
    else:
        maximo = 0  
        
    for x in range(1, count + 1):
        table.append(0)
        
    for x in range(1, count + 1):        
        maximo = max(maximo, (table[x]+table[count-x]))
    table[count] = maximo
    return table[count]


# 테스트 코드
print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))

```

    2000
    0
    1800
    

답의 방향으로 생각했다는 게 굉장히 중요하다  
(table[i]+table[x-i])이런 패턴이나 range(1, x //2 + 1) 이런 걸 스스로 생각해냈다  
그리고 중첩 반복문을 쓸 생각도 했었다(memoization에서였지만)  
이제 경험치를 쌓아서 그걸 구체화해낼 수 있게 되는 거다  
옛날에는 코드잇 기본 문제도 1시간씩 걸렸던 걸 생각하면 확실히 연습을 하면  
파이썬 도구들에 익숙해지면서 이런 발상은 이렇게 구체화 시킬 수 있겠다 하는 감이 온다  
그런 감을 이제 기르면 되는 거다


```python
def max_profit(price_list, count):
    # 여기에 코드를 작성하세요
    table = [0]
    for x in range(1, count + 1):
        if x < len(price_list):
            maximo = price_list[x]
        else:
            maximo = 0  
            
        for i in range(1, x //2 + 1):
            maximo = max(maximo, (table[i]+table[x-i]))
        table.append(maximo)
    
    return table[count]


# 테스트 코드
print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))

```

    2000
    2400
    1800
    

## <a id='toc1_4_'></a>[Greedy Algorithm 탐욕 알고리즘](#toc0_)

간단하고 빠르되 최적해를 보장하지는 않는다

그러나 최적해를 구할 수 있는 경우가 있는데 두 가지 조건을 갖춰야 한다

- greedy choice property: If an optimal solution to the problem can be found by choosing the best choice at each step without reconsidering the previous steps once chosen, the problem can be solved using a greedy approach. This property is called greedy choice property. 이전 상황의 선택을 재고하지 않아도 현재 상황에서 최적의 선택이 가능하다. 혹은 각 단계에서의 최선의 선택이 최종 답을 선택하는 데 최선인지

- optimal substructure: If the optimal overall solution to the problem corresponds to the optimal solution to its subproblems, then the problem can be solved using a greedy approach.
Dynamic Programming에서도 필요했던 조건. 하위 문제를 해결하는 방법이 전체 문제를 해결하는 방법과 동일한지

쩔었따. 아래 문제는 나 스스로 맞췄다. sorted(coin_list, reverse= True) 이걸 아는 게 포인트였다  
그러니까 위에서 내가 좌절을 느꼈던 것도 정당하다. sorted를 모르면 못 푸는 문제를 sorted를 알려주지 않고 풀라고 하니  
풀릴 리가 없다. 그래도 고민하고 나서 보면 무릎을 탁 치게 된다. 더 나은 부분 내가 생각지 못한 부분을 발견하고 감탄하고 성장하는 거다


```python
def min_coin_count(value, coin_list):
    # 여기에 코드를 작성하세요
    coin_list = sorted(coin_list, reverse= True)
    num = 0
    rest = 0
    for i in range(len(coin_list)):
        num += value // coin_list[i]
        rest = value % coin_list[i]        
        value = rest
    return num

# 테스트 코드
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))
```

    10
    5
    49
    70
    


```python
default_coin_list = [100, 500, 10, 50]
sorted(default_coin_list, reverse= True)
```




    [500, 100, 50, 10]




```python
1440%500
```




    440




```python
def min_coin_count(value, coin_list):
    # 누적 동전 개수
    count = 0

    # coin_list의 값들을 큰 순서대로 본다
    for coin in sorted(coin_list, reverse=True):
        ## 리스트에서 굳이 참조하지 않아도 되는 구나 어차피 원소를 가져올 거니까!
        # 현재 동전으로 몇 개 거슬러 줄 수 있는지 확인한다
        count += (value // coin)

        # 잔액을 계산한다
        value %= coin
        ## 그렇구나 이런 연산자도 이렇게 표현할 수 있구나

    return count
```

아래도 스스로 풀었다. 사실 대부분 스스로 푸는데 알고리즘에서만 두 개나 해설을 보았고 대부분 힌트를 보아서 약간 좌절했었다 ㅠㅠ


```python
def max_product(card_lists):
    # 여기에 코드를 작성하세요
    nlt = []
    peak = 1
    for x in range(len(card_lists)):
        nlt.append(max(card_lists[x]))
    
    for x in range(len(nlt)):
        peak *= nlt[x]
        
    return peak


# 테스트 코드
test_cards1 = [[1, 6, 5], [4, 2, 3]]
print(max_product(test_cards1))

test_cards2 = [[9, 7, 8], [9, 2, 3], [9, 8, 1], [2, 8, 3], [1, 3, 6], [7, 7, 4]]
print(max_product(test_cards2))

test_cards3 = [[1, 2, 3], [4, 6, 1], [8, 2, 4], [3, 2, 5], [5, 2, 3], [3, 2, 1]]
print(max_product(test_cards3))

test_cards4 = [[5, 5, 5], [4, 3, 5], [1, 1, 1], [9, 8, 3], [2, 8, 4], [5, 7, 4]]
print(max_product(test_cards4))

```

    24
    244944
    10800
    12600
    


```python
def max_product(card_lists):
    # 누적된 곱을 저장하는 변수
    product = 1

    # 반복문을 돌면서 카드 뭉치를 하나씩 본다
    for card_list in card_lists:
        # product에 각 뭉치의 최댓값을 곱해 준다
        product *= max(card_list)
        ## 그냥 이렇게 안에 있는 리스트 중에서 최대값을 뽑은 다음 곱하는 걸 할 수 있구나!?
        ## for x in card_lists라고 리스트에서 내부 리스트를 데려오게 한 다음에
        ## x 자체가 리스트니까 x의 max를 가져오라고 하면 끝나는 구나!!!
        ## 무릎 탁!

    return product
```

아래는 심지어 해설과 거의 같다! pages_to_print.sort() 이 부분을 sorted_list = sorted(pages_to_print) 이렇게 한 것과 빼고  
근디 sort로 이렇게 해버린 건 사실 알고리즘이 min fee를 구하는 게 아니라 내가 알아내고 적용한 느낌인데


```python
def min_fee(pages_to_print):
    # 여기에 코드를 작성하세요
    fee = 0
    pages_to_print.sort()
    for i in range(len(pages_to_print)):
        fee += pages_to_print[i] * (len(pages_to_print) - i)
    
    return fee

# 테스트 코드
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))

```

    39
    10
    32
    188
    

oh yeah ... 이 맛이지!

검색해서 풀었고 그게 맞는 거 같긴 한데 여전히 유효한 포인트는 sort(key = lambda x: x[1]) 이런 거 아예 몰라서 발상을 못 하는 사람은 못 푼다. 미리 알려준 것도 아니고 말이지  

잘 모르는 게 당연할 수 밖에 없다고 봅니다

수업 내용만 듣고 답안처럼 유추해내는 건 사실 힘들어보여요

파이썬 내장함수를 이미 알아서 사용할 줄 알아야 문제풀이가 가능한 부분입니다

이런 부분에 대해선 힌트에서 이런 함수는 이런 기능이 있다라고 풀이를 유도하는 게 더 적합해 보입니다

여기서 배우고자 하는 건 알고리즘이므로 함수를 모른다고 문제 풀이가 막히게 해선 안 될 거 같아요
라고 남겼다


```python
def course_selection(course_list):
    # 여기에 코드를 작성하세요
    course_list.sort(key = lambda x: x[1])
    x = 1
    while x < len(course_list):
        if course_list[x][0] <= course_list[x-1][1]:
            del course_list[x]
            x -= 1
        x += 1
    return course_list


# 테스트 코드
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))

```

    [(2, 3), (4, 5), (6, 8), (9, 10)]
    [(1, 2), (3, 4), (5, 7), (8, 9)]
    [(1, 3), (4, 7), (8, 10), (13, 16)]
    


```python
lt = [(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]
lt[0][1]
```




    10




```python
lt.sort(key = lambda x: x[1])
lt
```




    [(2, 3), (4, 5), (1, 7), (6, 8), (6, 10), (9, 10)]




```python
del lt[0]
lt
```




    [(4, 5), (1, 7), (6, 8), (6, 10), (9, 10)]



## <a id='toc1_5_'></a>[수료증](https://www.codeit.kr/certificates/YvabT-rp7D6-N3B4m-Kjw2k) [&#8593;](#toc0_)
