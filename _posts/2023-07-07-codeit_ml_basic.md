---
layout: single
title:  "machine learning basic "
---

**Table of contents**<a id='toc0_'></a>    
- [machine learning 기초 상식](#toc1_)    
  - [정의](#toc1_1_)    
  - [ML과 프로그래밍의 차이](#toc1_2_)    
  - [ML이 핫해진 이유](#toc1_3_)    
  - [분류 정리](#toc1_4_)    
  - [카테고리](#toc1_5_)    
  - [ML Vs. DL](#toc1_6_)    
  - [수학 개념](#toc1_7_)    
    - [선형 대수학](#toc1_7_1_)    
      - [행렬과 벡터](#toc1_7_1_1_)    
      - [numpy를 이용한 행렬](#toc1_7_1_2_)    
      - [행렬의 덧셈은 같은 위치의 요소끼리 더해주면 된다](#toc1_7_1_3_)    
      - [행렬과 스칼라의 곱셈은 각 원소에 곱해주면 된다](#toc1_7_1_4_)    
      - [행렬 간의 곱셈은 내적곱, 외적곱 그리고 요소별 곱하기로 나뉜다](#toc1_7_1_5_)    
    - [행렬 matrix](#toc1_7_2_)    
    - [벡터 vector](#toc1_7_3_)    
    - [행렬 연산](#toc1_7_4_)    
    - [특수행렬](#toc1_7_5_)    
      - [역행렬은 없을 수도 있다](#toc1_7_5_1_)    
    - [미분](#toc1_7_6_)    
      - [함수](#toc1_7_6_1_)    
      - [그래프](#toc1_7_6_2_)    
      - [기울기가 의미하는 두 가지](#toc1_7_6_3_)    
      - [순간변화율이 0인 지점들](#toc1_7_6_4_)    
    - [편미분](#toc1_7_7_)    
  - [수료증](#toc1_8_)    

<!-- vscode-jupyter-toc-config
	numbering=false
	anchor=true
	flat=false
	minLevel=1
	maxLevel=6
	/vscode-jupyter-toc-config -->
<!-- THIS CELL WILL BE REPLACED ON TOC UPDATE. DO NOT WRITE YOUR TEXT IN THIS CELL -->

# <a id='toc1_'></a>[machine learning 기초 상식](#toc0_)

## <a id='toc1_1_'></a>[정의](#toc0_)
Machine Learning (ML) is a subset of Artificial Intelligence (AI) which enable computers to learn from data and improve themselves without being explicitly programmed.

Tom Mitchell (1998) — Well-posed Learning Problem: A computer program is said to learn from experience E with respect to some task T and some performance measure P, if its performance on T, as measured by P, improves with experience E

작업T을 할 때 경험E이 늘어남에 따라 성능P이 나아진다면 머신 러닝 프로그램이다  
예: 데이터가 늘어남으로써 성능이 좋아진다

## <a id='toc1_2_'></a>[ML과 프로그래밍의 차이](#toc0_)

- 프로그램 : 인간이 판단하고 규칙을 알려준다
- 머신러닝 : 데이터를 통해 규칙을 학습하고 모델을 만든다

## <a id='toc1_3_'></a>[ML이 핫해진 이유](#toc0_)
- 데이터 증가
- 컴퓨터 성능 증가
- 추천 알고리즘 등 수익 창출 경로 증가

## <a id='toc1_4_'></a>[분류 정리](#toc0_)
![ai-ml-dl-ds](https://14535109.fs1.hubspotusercontent-na1.net/hub/14535109/hubfs/DevIQ%20website%20active%20images/ai-ml-dl-ds-venn-diagram-deviq.png?width=575&name=ai-ml-dl-ds-venn-diagram-deviq.png)

## <a id='toc1_5_'></a>[카테고리](#toc0_)
![category](https://cdn-images-1.medium.com/max/800/1*rbaxTrB_CZCqbty_zv2bEg.png)

- 지도 학습: 정답을 포함한 데이터로 학습
- 비지도 학습: 정답 없이 군집화 한다. 지도 학습에 쓸 feature를 파악하기 위해 전처리 과정에서 사용하기도 한다
- 강화 학습: 자신 agent가 환경 environment에서 갖는 행동 action에 따라 현황 state이 달라지는데 현황에 따라 점수 reward를 부여하여 높은 점수를 보상으로 학습. 지도 학습이 모든 상황 가능성에 정답이라는 라벨을 붙여야 하는 반면 강화 학습은 상태에 대한 보상 규칙을 설계함으로써 필요한 예제의 데이터가 줄어든다

## <a id='toc1_6_'></a>[ML Vs. DL](#toc0_)
feature를 사람이 지정해주느냐 스스로 판단하느냐 차이


![mlvsdl](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FLYTie%2FbtqDp12Zbvq%2FYyvsPGwZYfnvVcHfi9kTE0%2Fimg.jpg)

## <a id='toc1_7_'></a>[수학 개념](#toc0_)
- 선형대수학: 행렬. 많은 데이터를 효율적으로 계산 가능
- 미분: 최적화 작업에 사용
- 통계: 수치화 작업에 사용
- 확률: 가능성 작업에 사용

### <a id='toc1_7_1_'></a>[선형 대수학](#toc0_)
- 일차식, 일차 함수에 대한 학문
  - f(x) = ax + b
  - x가 여러개여도 1차항이면 된다

#### <a id='toc1_7_1_1_'></a>[행렬과 벡터](#toc0_)
- 행렬 matrix: 수를 직사각형 형태로 나열 row, column
  - A(i,j) = i행 j열 원소
- vetocr : 행이나 열이 1인 벡터
  - 그냥 벡터라고 하면 열 column이 하나인 열 벡터 a(i, 1)
  - 원소의 개수가 곧 벡터의 차원

#### <a id='toc1_7_1_2_'></a>[numpy를 이용한 행렬](#toc0_)


```python
import numpy as np
```


```python
#행과 열이 3개인 행렬 A(3,3)
A = np.zeros((3,3))
A
```




    array([[0., 0., 0.],
           [0., 0., 0.],
           [0., 0., 0.]])




```python
#열이 1개인 벡터 a(10, 1)
a = np.zeros(10)
a
```




    array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])




```python
B = np.random.rand(5,5)
B
```




    array([[0.82606596, 0.69863289, 0.16105202, 0.40375735, 0.17790336],
           [0.42554986, 0.96419337, 0.68932391, 0.406969  , 0.9401609 ],
           [0.82612563, 0.20573045, 0.74927203, 0.44439312, 0.52298137],
           [0.88661827, 0.46285522, 0.26786482, 0.64451089, 0.19692272],
           [0.73865738, 0.45712483, 0.45393201, 0.52411184, 0.45950078]])




```python
B[0][4]
```




    0.1779033566340631




```python
A = np.array([
    [0, 1, -1],
    [1, 2, 3],
    [2, 1, 0],
    [-1, 2, -4]]
)
A
```




    array([[ 0,  1, -1],
           [ 1,  2,  3],
           [ 2,  1,  0],
           [-1,  2, -4]])




```python
B = np.array([
    [0, 2],
    [1, 1],
    [-1, -2]
])
B
```




    array([[ 0,  2],
           [ 1,  1],
           [-1, -2]])



#### <a id='toc1_7_1_3_'></a>[행렬의 덧셈은 같은 위치의 요소끼리 더해주면 된다](#toc0_)
그러므로 더할 수 있으려면 같은 차원이어야 한다

#### <a id='toc1_7_1_4_'></a>[행렬과 스칼라의 곱셈은 각 원소에 곱해주면 된다](#toc0_)
행렬에서 행렬 원소가 아닌 일반 수를 스칼라라고 부른다


```python
C = np.random.rand(3,2)
C
```




    array([[0.5530029 , 0.46776339],
           [0.62338118, 0.37394191],
           [0.00987416, 0.19955162]])




```python
D = B + C
D
```




    array([[ 0.5530029 ,  2.46776339],
           [ 1.62338118,  1.37394191],
           [-0.99012584, -1.80044838]])




```python
5*A
```




    array([[  0,   5,  -5],
           [  5,  10,  15],
           [ 10,   5,   0],
           [ -5,  10, -20]])



#### <a id='toc1_7_1_5_'></a>[행렬 간의 곱셈은 내적곱, 외적곱 그리고 요소별 곱하기로 나뉜다](#toc0_)
- 내적곱(행렬의 곱셈) A@B np.dot()
    - 결과 AB의 1,1 에는 A의 1행과 B의 1열 원소들을 각각 곱한 값의 합이 부여된다
    - 앞의 행렬이 행을, 뒤의 행렬이 열을 제공한다
    - 그러므로 A가 (x,y)고 B가 (a,b)라면 결과 AB는 (x,b)가 된다
    - __그러므로 A의 열 y와 B의 행 a는 같아야 한다 y = a__
    - 일반화하면 A(x,**y**) B(**y**,b)일 때 내적곱이 가능하며 결과는 AB(x,b)가 된다
    - 또한 AB와 BA의 결과가 달라지며 AB가 계산이 가능해도 BA는 불가능 할 수 있다
- 요소별 곱하기 element-wise multiplication A∘B 아다마르 곱(Hadamard product) A*B
    - 마치 행렬간 덧셈처럼 각 요소별로 곱한다  
    - 그러므로 행렬간 덧셈과 같이 차원이 같은 경우에만 가능하다
- 외적곱 np.outer() 수식은 $A\otimes B$
    - 외적곱의 결과 행렬은 행렬A와 B의 모든 product를 갖는다
      - 행렬 크기가 더 커진다


```python
B * C
```




    array([[ 0.        ,  0.93552677],
           [ 0.62338118,  0.37394191],
           [-0.00987416, -0.39910325]])



외적곱을 강의에서 설명하지 않아 내용을 찾아보던 중 수학을 더 배워야겠다는 생각이 들었다

---

### <a id='toc1_7_2_'></a>[행렬 matrix](#toc0_)
---

행렬 matrix는 수나 다항식 등을 직사각형 모양으로 배열한 것이다

In mathematics, a matrix is a rectangular array or table of numbers, symbols, or expressions, arranged in rows and columns, which is used to represent a mathematical object or a property of such an object.

역사적으로 본다면 행렬은 연립 일차 방정식의 풀이를 어떻게 하면 될까라고 고민한 데서 시작했다. 제임스 조지프 실베스터(James Joseph Sylvester)와 아서 케일리(Arthur Cayley)등이 연구하다가 (ad−bc)의 값에 따라 연립 방정식의 해가 다르게 나오는 것을 보고 이 값이 해의 존재 여부(궁극적으로는 행렬의 가역 여부)를 '판별'한다는 뜻에서 determinant라는 용어가 탄생했고, 윌리엄 로원 해밀턴이 '그러면 연립 방정식의 계수랑 변수를 따로 떼어내서 쓰면 어떨까?'라는 생각에서 행렬이 탄생했다. 즉 교육과정에서 배우는 것과는 달리, 역사적으로 보면 행렬식이 행렬보다 먼저 탄생했다.

- $A(i,j)$의 전치행렬 transposal matrix는 $A^T (j,i)$이다. 각 행을 열로 바꾼 행렬이다.
- $A(i,j)$와 그 전치행렬 $A^T (j,i)$가 동일하다면 A는 **대칭행렬**이라 부른다
  - 대칭행렬이 되려면 정사각형이어야 한다
- 대각성분이 아닌 모든 성분이 0인 정사각형 행렬을 **대각행렬**이라 부른다
  - 대각행렬은 기본적으로 대칭행렬이다
- 대각행렬이면서 대각선의 모든 성분이 1인 행렬을 **단위행렬 I**라 부른다
- 모든 성분이 0인 행렬을 **영행렬**이라 부른다

### <a id='toc1_7_3_'></a>[벡터 vector](#toc0_)
---
크기와 방향을 가진 대상

- 크기와 방향이 같은 벡터는 모두 같다(위치 무관)
- 그러므로 모든 벡터는 0,0을 원점으로 하고 a,b를 종점으로 한다고 표현할 수 있다
  - $v(a,b)$
  - 그러므로 평면벡터와 좌표평면 위의 점은 일대일 대응한다 (벡터를 좌표평면 위에 표시할 수 있다)
  - 시점a와 종점b가 주어진다면 a(x,y) b(a,b) a에서 b로 가는 벡터 ab를 표현할 때는 시점을 0으로 만들어서 표시한다
  - 즉 ab(a-x, b-y)로 만들어낸다 >>> 0에서부터 출발하는 모양으로 만든다
  - 이렇게 만들면 다시 좌표평면 위의 한 점으로 표현할 수 있다
  - 이를 점 o에 대한 위치 벡터라 부른다

정의를 넘어 연산으로 가다보니 지금 배우려고 하는 행렬 연산과는 점점 거리가 멀어진다 차후에 필요시 보충한다

### <a id='toc1_7_4_'></a>[행렬 연산](#toc0_)

numpy에서 행렬의 곱은 np.dot()으로 쓸 수도 있고 연산자 @로도 쓸 수 있다


```python
A = np.random.rand(2,3)
B = np.random.rand(3,4)
np.dot(A,B)
```




    array([[1.15241185, 0.91000418, 0.47187929, 0.68972416],
           [0.45706849, 0.74090877, 0.60775145, 0.41322287]])




```python
A@B
```




    array([[1.15241185, 0.91000418, 0.47187929, 0.68972416],
           [0.45706849, 0.74090877, 0.60775145, 0.41322287]])




```python
A = np.array([
    [1, -1, 2],
    [3, 2, 2]
])

B = np.array([
    [0, 1],
    [-1, 1],
    [5, 2]
])

C = np.array([
    [2, -1],
    [-3, 3]
])

D = np.array([
    [-5, 1],
    [2, 0]
])
```


```python
((2*A)@((-1)*B))@(3*C+D)
```




    array([[  34,  -28],
           [ 110, -130]])



헐 띄어쓰기로 하면 된다


```python
2*A @ -B @ (3*C + D)
```




    array([[  34,  -28],
           [ 110, -130]])



### <a id='toc1_7_5_'></a>[특수행렬](#toc0_)
- 전치행렬: 곱셈 하려고 모양 맞추거나 할 때 유용하다
- 단위행렬
- 역행렬 inverse matrix: 곱했을 때 단위행렬이 나오게 하는 행렬
  - 정사각형만 가능(왜지?)
  - 역행렬이 없는 경우도 있다

따로 배워봤더니 역시나 배우기는 한다 따로 배워둬서 이해가 더 수월하다


```python
A
```




    array([[ 1, -1,  2],
           [ 3,  2,  2]])




```python
np.transpose(A)
```




    array([[ 1,  3],
           [-1,  2],
           [ 2,  2]])




```python
A.T
```




    array([[ 1,  3],
           [-1,  2],
           [ 2,  2]])




```python
np.identity(3)
```




    array([[1., 0., 0.],
           [0., 1., 0.],
           [0., 0., 1.]])




```python
A @ np.identity(3)
```




    array([[ 1., -1.,  2.],
           [ 3.,  2.,  2.]])



#### <a id='toc1_7_5_1_'></a>[역행렬은 없을 수도 있다](#toc0_)
그러므로 넘파이로 역행렬을 만들 때 역행렬에 가깝게 만들어달라고 할 수 있다 np.pinv()


```python
np.linalg.pinv(A)
```




    array([[ 0.02597403,  0.16883117],
           [-0.35064935,  0.22077922],
           [ 0.31168831,  0.02597403]])




```python
A @ np.linalg.pinv(A)
# pinv as in pseudo inverse
```




    array([[1.00000000e+00, 1.38777878e-17],
           [0.00000000e+00, 1.00000000e+00]])




```python
A = np.array([
    [1, -1, 2],
    [3, 2, 2]
])

B = np.array([
    [0, 1],
    [-1, 1],
    [5, 2]
])

C = np.array([
    [2, -1],
    [-3, 3]
])

D = np.array([
    [-5, 1],
    [2, 0]
])
```


```python
B.T @ (2*(A.T)) @ (3*(np.linalg.pinv(C)) + D.T)
```




    array([[20., 98.],
           [56., 60.]])



### <a id='toc1_7_6_'></a>[미분](#toc0_)

#### <a id='toc1_7_6_1_'></a>[함수](#toc0_)
- 하나의 입력값에 하나의 결과값
- $y = ax + b$ 라면 y는 x에 대한 함수

#### <a id='toc1_7_6_2_'></a>[그래프](#toc0_)

수학 식을 그림으로 보는 방법  
함수의 특징을 시각적으로 파악할 수 있다

평균변화율: y 증가량 / x 증가량.  
기울기 : x에 움직임에 따라 y가 얼만큼 빠르게 변하는가  
접선의 기울기. 순간변화율을 알고 싶다면 x를 극히 작은 하나의 단위로 만들면 된다 = 점  
(기울기, 평균변화율, 순간변화율, 미분 차례로 설명하니 이해가 쉽다)

x가 a에서 b만큼 증가 할 때 y가 얼만큼 빠르게 증가하는지 그 기울기를 수식으로 표현하면

$(f(b) - f(a)) \over (b - a)$ 

여기서 b = a + h 로 치환한다

$(f(a+h) - f(a)) \over h$  


for a general case, replace a with x 상수 a를 미지수 x로 치환해서 일반화 한다  

$(f(x+h) - f(x)) \over h$  


$limit(h) \rarr 0$, 위 식에서 h를 극한으로 0값에 가깝게 하면 접선의 기울기를 알 수 있다  
이 때 f(x)를 풀어서 정리하고 h를 0으로 보내야 한다  
그렇게 정리하면 식이 나오는데 이를 f'(x)라 쓰고 f prime이라 읽으며 이를 f(x)의 미분이라 한다 x에 값을 넣으면 나오는 결과는 x일 때의 기울기이다. 즉 f'(x) 미분은 함수의 순간 변화율을 구하는 함수다

#### <a id='toc1_7_6_3_'></a>[기울기가 의미하는 두 가지](#toc0_)
- 그래프가 해당 지점에서 얼마나 기울어져 있는가
- 어떤 방향으로 가야 가장 가파르게 "올라갈 수 있는가"
  - 음수면 숫자가 작아지는 방향
  - 양수면 숫자가 커지는 방향
  - 즉, x의 절대값이 커지는 방향으로 가야 가파르게 "올라갈 수 있다"
  - 내려가는 건 반대로 절대값이 작아지는 방향으로 가면 된다

![기울기](https://bakey-api.codeit.kr/files/3005/M24v5W?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-04-30+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+7.03.22.png)

#### <a id='toc1_7_6_4_'></a>[순간변화율이 0인 지점들](#toc0_)
- 최소점, 극소점 / 최대점, 극대점 global/local minimum/maximum
  - 기울기 부호가 바뀌면서 거쳐가는 순간변화율 0
- 안장점 saddle point
  - 기울기 부호는 그대로인데 순간변화율 0을 지나는 모습

### <a id='toc1_7_7_'></a>[편미분](#toc0_)
변수가 2개 이상일 때, 즉 3차원 이상일 때에 대한 미분

함수를 변수 하나에 대해서만 미분한다  
미분하지 않는 변수는 상수 취급한다

그 결과는 $▽f(x,y) = [[ax],[by]]$ 로 표현한다  
y를 고정했을 때 x가 1증가할 때 f(x,y)는 a만큼 증가하고  
x를 고정했을 때 y가 1증가할 때 f(x,y)는 b만큼 증가한다고 해석한다

![편미분](https://bakey-api.codeit.kr/files/3008/DQCV0L?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-04-30+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+7.35.21.png)

![편미분2](https://bakey-api.codeit.kr/files/3008/9H0ix0?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-04-30+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+7.35.29.png)

기울기가 가장 가파르게 올라가는 경로를 알려주었듯이 벡터에서도 이를 알 수 있다

예를 들어 위 그림에서 ▽f(1,1)의 기울기는 [[2], [4]]인데 이는 (2, 4)로 갈 때 가장 가파르게 올라갈 수 있음을 뜻한다

![편미분3](https://bakey-api.codeit.kr/files/3007/4Pv2lh?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-04-30+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+7.21.06.png)

![편미분4](https://bakey-api.codeit.kr/files/3007/HMGdkp?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-04-30+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+7.23.07.png)

![편미분5](https://bakey-api.codeit.kr/files/3007/Zk5oCg?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-04-30+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+7.23.55.png)

함수의 경사는 함수 결과값이 늘어나는 방향을 가리킨다

## <a id='toc1_8_'></a>[수료증](https://www.codeit.kr/certificates/BFSn7-cTgSh-InAfT-4uLJW) [&#8593;](#toc0_)
