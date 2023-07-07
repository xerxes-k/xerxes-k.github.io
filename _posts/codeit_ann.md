**Table of contents**<a id='toc0_'></a>    
- [artificial neural network ann 인공 신경망과 deep learning dl 딥러닝](#toc1_)    
  - [정의](#toc1_1_)    
  - [뉴런처럼 설계한다?](#toc1_2_)    
  - [용어](#toc1_3_)    
  - [층과 뉴런](#toc1_4_)    
    - [가중치와 편향의 표준 오차 조절](#toc1_4_1_)    
  - [신경망 학습](#toc1_5_)    
      - [합성함수: 함수의 인풋이 또다른 함수인 함수](#toc1_5_1_1_)    
      - [연쇄법칙을 쓸 수 있다](#toc1_5_1_2_)    
    - [순전파 vs 역전파](#toc1_5_2_)    
  - [신경망의 비선형성 nonliearity](#toc1_6_)    
  - [각 층별 주요 함수](#toc1_7_)    
      - [은닉층](#toc1_7_1_1_)    
      - [출력층](#toc1_7_1_2_)    
    - [신경망 손실함수](#toc1_7_2_)    
    - [신경망 경사 하강법](#toc1_7_3_)    
  - [수료증](#toc1_8_)    

<!-- vscode-jupyter-toc-config
	numbering=false
	anchor=true
	flat=false
	minLevel=1
	maxLevel=6
	/vscode-jupyter-toc-config -->
<!-- THIS CELL WILL BE REPLACED ON TOC UPDATE. DO NOT WRITE YOUR TEXT IN THIS CELL -->

# <a id='toc1_'></a>[artificial neural network ann 인공 신경망과 deep learning dl 딥러닝](#toc0_)

## <a id='toc1_1_'></a>[정의](#toc0_)
---
- 딥러닝은 머신 러닝ml과 인공지능ai의 결합
    - 인공지능은 기계, 프로그램이 사람처럼 행동하거나 생각하게 만드는 학문
        - 인공지능 중에서도 사람의 신경계가 작동하는 방법을 본떠서 알고리즘으로 구현하는 분야가 ann

예제 활용 자료: MINST data  
- Modified National Institute of Standards and Technology database
- 6만개 학습 / 1만개 테스트
- 손글씨 자료 28*28 픽셀
- 0~255 회색
    - min-max normalization으로 0~1(회색척도)로 변환해서 사용
        - 모델 학습 속도, 정확도 향상을 위해        

예시로 로지스틱 회귀 logistic regression 모델을 사용해 분류한다
- 시그모이드 함수
- 0.5 기준 넘으면 1, 작으면 0

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3990&directory=Screen%20Shot%202020-12-03%20at%209.46.42%20AM.png&name=Screen+Shot+2020-12-03+at+9.46.42+AM.png)

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3990&directory=Screen%20Shot%202020-12-03%20at%209.49.18%20AM.png&name=Screen+Shot+2020-12-03+at+9.49.18+AM.png)

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3990&directory=Screen%20Shot%202022-09-26%20at%2010.24.12%20AM.png&name=Screen+Shot+2022-09-26+at+10.24.12+AM.png)

## <a id='toc1_2_'></a>[뉴런처럼 설계한다?](#toc0_)
---

뉴런(신경세포)는 자극을 받으면 전달한다  

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3995&directory=Screen%20Shot%202020-12-03%20at%209.55.35%20AM.png&name=Screen+Shot+2020-12-03+at+9.55.35+AM.png)

하나의 로지스틱 모델이 하나의 뉴런과 같다?  
입력값을 받으면 예측값을 전달하므로  

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3995&directory=Screen%20Shot%202020-12-03%20at%209.56.18%20AM.png&name=Screen+Shot+2020-12-03+at+9.56.18+AM.png)

뉴런이랑 비슷하다고 하기엔 말이 안되는데?

## <a id='toc1_3_'></a>[용어](#toc0_)
---
ann 분야에서는 theta를 weight이라 부른다. 상수항은 bias b라 부른다. 함수(로지스틱에선 시그모이드)는 활성함수라 부른다

그러므로 활성 함수를 수식으로 표현하면

$h_w(x) = \sigma (w^T x+b) $

여기서 시그마는 시그모이드 함수를 말한다



![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3995&directory=Screen%20Shot%202020-12-03%20at%209.58.24%20AM.png&name=Screen+Shot+2020-12-03+at+9.58.24+AM.png)

여러 단계를 거치면서 분류하면 각 단계를 층이라 부른다

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3995&directory=Screen%20Shot%202020-12-03%20at%2010.00.03%20AM.png&name=Screen+Shot+2020-12-03+at+10.00.03+AM.png)

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3995&directory=Screen%20Shot%202020-12-03%20at%2010.03.16%20AM.png&name=Screen+Shot+2020-12-03+at+10.03.16+AM.png)

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3995&directory=Screen%20Shot%202020-12-03%20at%2010.07.33%20AM.png&name=Screen+Shot+2020-12-03+at+10.07.33+AM.png)

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3995&directory=Screen%20Shot%202020-12-03%20at%2010.09.36%20AM.png&name=Screen+Shot+2020-12-03+at+10.09.36+AM.png)

가장 잘 분류하는 가중치w와 편향b을 찾는 걸 학습한다라고 표현한다

다양한 층이 있는 만큼 각 층에서는 아주 작은 패턴을 찾아내는 데 특화한다

## <a id='toc1_4_'></a>[층과 뉴런](#toc0_)
---

- 층: input layer입력층(0번층), hidden layer 은닉층, output layer 출력층으로 구분하며 층의 수를 L = n으로 표기한다
    - 각 층의 뉴런의 수는 $n[L]$로 표기한다
- 뉴런의 출력: activation a. 뉴런이 얼마나 활성화 됐는지 값을 표현하므로 a라 부른다
    - 몇번 층의 출력인지에 따라 $a^{[L]}$로 표기한다
    - 각 층의 몇번째 출력인지에 따라 $a^{[L]}_i$라 표기한다 $a^{[layer]}_{index}$
        - 2번째 층의 마지막 출력: $a^{[2]}_{n[2]}$
        - 데이터프레임의 표에선 $x^{[row]}_{column}$ 형식일 수 있으니 주의
            - 5번째 이미지의 3번 픽셀 $x^{[5]}_{3}$
- 가중치(신경): 뒤의 층(L)에 속한다고 표현한다 그러므로 $w^{[1]}$부터 시작한다
    - $W^{[L]}_{i,j}$로 i는 앞의 층에서 몇번째, j는 뒤의 층의 몇번째와 연결하는지 나타낸다
- 편향: $b^{[L]}_i$라 표현

L = 3인 신경망(입력층은 0번이므로)


![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3999&directory=Screen%20Shot%202020-12-03%20at%2010.00.03%20AM.png&name=Screen+Shot+2020-12-03+at+10.00.03+AM.png)


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```


```python
# numpy 임의성 조절
np.random.seed(42)

def initialize_parameters(neurons_per_layer):
    """신경망의 가중치와 편향을 초기화해주는 함수"""
    L = len(neurons_per_layer) - 1  # 층 개수 저장
    parameters = {}
    
        # 1층 부터 L층까지 돌면서 가중치와 편향 초기화
    for l in range(1, L+1):
        parameters['W' + str(l)] = np.random.randn(neurons_per_layer[l], neurons_per_layer[l-1]) * np.sqrt(1/neurons_per_layer[l]) # 여기에 코드를 작성하세요
        parameters['b' + str(l)] = np.random.randn(neurons_per_layer[l]) * np.sqrt(1/neurons_per_layer[l]) # 여기에 코드를 작성하세요
        
    return parameters

# 테스트 코드
neurons_per_layer = [10, 5, 5, 3]
initialize_parameters(neurons_per_layer)




```




    {'W1': array([[ 0.22213732, -0.06183368,  0.28965512,  0.68111966, -0.10471657,
             -0.10470923,  0.70624544,  0.34320724, -0.20995533,  0.24264023],
            [-0.20724669, -0.20828068,  0.10820882, -0.85564494, -0.77140671,
             -0.25146263, -0.45295185,  0.14053568, -0.40608071, -0.63160142],
            [ 0.65545806, -0.10097023,  0.03019953, -0.63716676, -0.24345536,
              0.04960609, -0.51473998,  0.16801726, -0.26861379, -0.13044941],
            [-0.26909138,  0.82836399, -0.00603614, -0.47302271,  0.36785327,
             -0.54597788,  0.09340664, -0.87639112, -0.59398286,  0.08803902],
            [ 0.33025229,  0.07663823, -0.05171948, -0.13465767, -0.66121514,
             -0.32192412, -0.20600392,  0.47275943,  0.15367077, -0.78845553]]),
     'b1': array([ 0.14493476, -0.17221403, -0.30272872,  0.27354995,  0.461077  ]),
     'W2': array([[ 0.41648113, -0.37530949, -0.13828398,  0.14814551,  0.43627704],
            [-0.21429323, -0.08302922, -0.49476804, -0.53495987,  0.36337259],
            [ 0.60652898, -0.03220391,  0.44879356,  0.16172855, -0.28850632],
            [ 0.16162103,  0.68783086, -0.01602189,  0.69972991, -1.17158563],
            [ 0.36756597,  0.03892863, -0.13372015,  0.04103667, -0.88886784]]),
     'b2': array([-0.09824025,  0.1597056 ,  0.66093431, -0.23177749, -0.36156933]),
     'W3': array([[-0.28968956,  0.52850766,  0.18980454, -0.3058572 ,  0.29633509],
            [ 0.05604775,  0.55924745, -0.40533054, -0.18917583, -0.22638375],
            [-0.84496075,  0.17096512,  0.15072033,  0.00295226, -0.13543894]]),
     'b3': array([-0.81716468, -0.24285969, -0.19786632])}



### <a id='toc1_4_1_'></a>[가중치와 편향의 표준 오차 조절](#toc0_)
---
> 저희가 randn() 함수로 초기화한 값들은 사실 아무 값이나 갖는 건 아니예요. 평균 0, 표준 오차 1을 갖는 분포도에서 임의로 정해진 값들로 채워집니다.  
신경망의 가중치와 편향의 값들을 초기화할 때는, 값들의 표준 오차를 1 대신 그 층의 뉴런의 개수의 루트 값과 반비례 하는 값을 사용하는 경우가 많습니다. (신경망이 훨씬 더 빠르게, 잘 학습되기 때문입니다)  
이걸 하기 위해서는 임의로 초기화한 L번째 층 가중치와 편향의 모든 원소들에 (1/n[L])**0.5 값을 곱해주죠. (루트는 np.sqrt 함수를 사용하면 됩니다.)

대박 ... np.random.rand로 하고 있어서 np.random.randn으로 하는 문제와 달랐다. 어쩐지 다 맞는 거 같은데 안되더라니. 그래도 예시는 음수도 있는데 왜 내 값은 다 양수지?라는 생각이 퍼뜩 들면서 풀어냈다. 끝내준다

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=4003&directory=Screen%20Shot%202020-12-03%20at%2010.29.24%20AM.png&name=Screen+Shot+2020-12-03+at+10.29.24+AM.png)

그러나 끝에 목표변수 숫자를 정말 숫자로 집어넣으면 모델이 숫자의 크고 작음을 학습에 사용해버릴 수도 있다 따라서 onehot encoding을 해준다

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=4003&directory=Screen%20Shot%202020-12-03%20at%2010.33.34%20AM.png&name=Screen+Shot+2020-12-03+at+10.33.34+AM.png)

계산을 식으로 나타내면 이러하다

z는 뉴런의 입력값. 입력값을 활성함수에 넣어서 나오는 출력값이 a

그러므로

$a^{[L]} = \sigma (z^{[L]}) $



![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=4006&directory=Screen%20Shot%202020-12-03%20at%2010.39.25%20AM.png&name=Screen+Shot+2020-12-03+at+10.39.25+AM.png)


```python
# numpy 임의성 조절
np.random.seed(42)

# 데이터 셋 가지고 오기
dataset = pd.read_csv('MNIST_preprocessed.csv', sep=',', header=None).values

# 입력, 목표 변수 데이터 셋 나누기
X = dataset[:, 0:784]
Y = dataset[:, 784:]

# training, testing 데이터 셋 나누기
X_train, X_test = X[0:250,], X[250:,]
Y_train, Y_test = Y[0:250,], Y[250:,]

def sigmoid(x):
    """시그모이드 함수"""
    return 1/(1 + np.exp(-x))

def initialize_parameters(nodes_per_layer):
    """신경망의 가중치와 편향을 초기화해주는 함수"""
    L = len(nodes_per_layer) - 1  # 층 개수 저장
    parameters = {}
    
    # 1층 부터 L 층까지 돌면서 가중치와 편향 초기화
    for l in range(1, L+1):
        parameters['W' + str(l)] = np.random.randn(nodes_per_layer[l], nodes_per_layer[l-1]) * np.sqrt(1. / nodes_per_layer[l])
        parameters['b' + str(l)] = np.random.randn(nodes_per_layer[l]) * np.sqrt(1. / nodes_per_layer[l])
        
    return parameters

def feed_forward(x, parameters):
    """순전파 함수"""
    cache = {'a0': x}  # 0 번째 층 출력 저장
    L = len(parameters) // 2  # 층 수 저장
    
    for l in range(1, L+1):
        # 전 층 뉴런의 출력, 현재 층 뉴런들의 가중치, 편향 데이터를 가지고 온다 (여기에 코드를 작성하세요)
        a_prev = cache['a' + str(l-1)]
        W = parameters['W' + str(l)]
        b = parameters['b' + str(l)]
        
        # 가지고 온 데이터로 z와 a를 계산한다. (여기에 코드를 작성하세요)
        z = W @ a_prev + b
        a = sigmoid(z)

        # 결과 값을 캐시에 저장한다.
        cache['z' + str(l)] = z
        cache['a' + str(l)] = a
                
    return a, cache

# 테스트 코드
neurons_per_layer = [784, 128, 64, 10]
parameters = initialize_parameters(neurons_per_layer)
feed_forward(X_train[0], parameters)[0]
```




    array([0.39847348, 0.63079802, 0.79832892, 0.93056447, 0.67941405,
           0.67578969, 0.05318435, 0.37468117, 0.12677036, 0.6419338 ])



## <a id='toc1_5_'></a>[신경망 학습](#toc0_)
---

- 가중치와 편향으로 예측을 하고
- 해당 예측이 얼마나 잘 예측하는지 평가해야 한다 (손실함수)

손실함수는 평균제곱오차를 사용해본다  
손실함수 최소화에는 경사하강법을 적용한다  
변수가 많아서 극소점을 구할 순 있으나 최소점이라고 확신할 순 없을 듯? 그렇다고 한다

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=4011&directory=Screen%20Shot%202020-12-03%20at%2010.49.55%20AM.png&name=Screen+Shot+2020-12-03+at+10.49.55+AM.png)

게다가 신경망에서는 하나의 가중치/편향을 바꿨을 때 손실함수에 미치는 영향이 복잡해서  
편미분을 계산하는 게 복잡하다  
합성함수라서 그렇다고 한다 알아보자  
복잡한 수학개념이 나올 거라 한다

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=4014&directory=Screen%20Shot%202020-12-03%20at%2011.03.01%20AM.png&name=Screen+Shot+2020-12-03+at+11.03.01+AM.png)

#### <a id='toc1_5_1_1_'></a>[합성함수: 함수의 인풋이 또다른 함수인 함수](#toc0_)
---
$f(y) = y ~~~$ 
$y(x) = x ~$  
이렇게 f는 y에 대한 함수인데 y는 x에 대한 함수인 관계 등  
이럴 땐 y를 x로 치환해서 f를 x에 대한 함수로 $f(y(x))$로 표현해버릴 수 있다

#### <a id='toc1_5_1_2_'></a>[연쇄법칙을 쓸 수 있다](#toc0_)
---


미분을 여러번 하는 거구나 미분으로 구하는 기울기의 의미는 변수가 단위 1만큼 증가했을 때 함수값이 얼만큼 변하느냐이므로 추적추적해서 따라가면 결국 구할 수 있다  


${dy \over dx} \cdot {df \over dy} $


### <a id='toc1_5_2_'></a>[순전파 vs 역전파](#toc0_)
---

순전파(Forward Propagation)란 입력 데이터를 기반으로 신경망을 따라 입력층(Input Layer)부터 출력층(Output Layer)까지 차례대로 변수들을 계산하고 추론(Inference)한 결과를 의미합니다.

모델(Model)에 입력값을 입력하여 순전파(Forward) 연산을 진행합니다.

이 과정에서 계층(Layer)마다 가중치(Weight)와 편향(Bias)으로 계산된 값이 활성화 함수(Activation Function)에 전달됩니다.

최종 활성화 함수에서 출력값이 계산되고 이 값을 손실 함수(Loss Function)에 실젯값과 함께 연산하여 오차(Cost)를 계산합니다.

역전파(Back Propagation)란 순전파(Forward Propagation)의 방향과 반대로 연산이 진행됩니다.

순전파(Forward Propagation) 과정을 통해 나온 오차(Cost)를 활용해 각 계층(Layer)의 가중치(Weight)와 편향(Bias)을 최적화합니다.

역전파 과정에서는 각각의 가중치와 편향을 최적화 하기 위해 연쇄 법칙(Chain Rule)을 활용합니다.

새로 계산된 가중치는 최적화(Optimization) 알고리즘을 통해 실젯값과 예측값의 차이를 계산하여 오차를 최소로 줄일 수 있는 가중치(Weight)와 편향(Bias)을 계산하게 됩니다.

역전파의 과정을 정리하고 나면 다음과 같다 (연산과정을 못 알아들었다 수학 배우고 와야 할 듯)

$db^{[l]} = \sigma ' (z^{[l]}) \circ da^{[l]} $  

$dW^{[l]} = db^{[l]} \otimes a^{[l-1]}$

$da^{[l-1]} = (W^{[l]})^T \times db^{[l]} $


```python
# numpy 임의성 조절
np.random.seed(42)

# 데이터 셋 가지고 오기
dataset = pd.read_csv('MNIST_preprocessed.csv', sep=',', header=None).values

# 입력, 목표 변수 데이터 셋 나누기
X = dataset[:, 0:784]
Y = dataset[:, 784:]

# training, testing 데이터 셋 나누기
X_train, X_test = X[0:250,], X[250:,]
Y_train, Y_test = Y[0:250,], Y[250:,]

def sigmoid(x):
    """시그모이드 함수"""
    return 1/(1 + np.exp(-x))

def d_sigmoid(x):
    """시그모이드 미분 함수"""
    return (np.exp(-x))/((np.exp(-x)+1)**2)

def initialize_parameters(neurons_per_layer):
    """신경망의 가중치와 편향을 초기화해주는 함수"""
    L = len(neurons_per_layer) - 1  # 입력층을 포함함 층 개수 저장
    parameters = {}
    
    # 1층 부터 L 층까지 돌면서 가중치와 편향 초기화
    for l in range(1, L+1):
        parameters['W' + str(l)] = np.random.randn(neurons_per_layer[l], neurons_per_layer[l-1]) * np.sqrt(1. / neurons_per_layer[l])
        parameters['b' + str(l)] = np.random.randn(neurons_per_layer[l]) * np.sqrt(1. / neurons_per_layer[l])
        
    return parameters

def feed_forward(x, parameters):
    """순전파 함수"""
    cache = {'a0': x}
    L = len(parameters) // 2
    
    for l in range(1, L+1):
        # 전 층 뉴런의 출력, 현재 층 뉴런들의 가중치, 편향 데이터를 가지고 온다
        a_prev = cache['a' + str(l-1)]
        W = parameters['W' + str(l)]
        b = parameters['b' + str(l)]
        
        # 데이터로 z와 a를 계산한다
        z = W @ a_prev + b
        a = sigmoid(z)

        # 결과 값을 캐쉬에 저장한다
        cache['z' + str(l)] = z
        cache['a' + str(l)] = a
                
    return a, cache

def compute_accuracy(x_val, y_val, parameters):
    """테스트 데이터에서 예측값들의 성능을 계산하는 함수"""
    predictions = []

    for x, y in zip(x_val, y_val):
        output, _ = feed_forward(x, parameters)
        pred = np.argmax(output)
        predictions.append(pred == np.argmax(y))

    return np.mean(predictions)

def compute_loss(x_val, y_val, parameters):
    """학습 데이터에서 현재 모델의 손실을 계산하는 함수"""
    loss = 0
    
    for x, y in zip(x_val, y_val):
        output, _ = feed_forward(x, parameters)
        loss += np.mean((output - y)**2) / 2
        
    return loss / len(x_val)

def back_prop(prediction, y, cache, parameters):
    """역전파 함수"""
    gradients = {}
    L = len(cache) // 2
    da = (prediction - y) / y.shape[0]
    
    for layer in range(L, 0, -1):
        # 역전파 행렬 연산을 사용해서 각 요소에 대한 편미분 계산
        # 여기에 코드를 작성하세요------------------------------------------
        db = d_sigmoid(cache['z'+ str(layer)]) * da
        dW = np.outer(db, cache['a'+ str(layer-1)])
        da = parameters['W'+ str(layer)].T @ db
        ## 힌트1을 열어봤는데 이미 내가 한 그대로다
        
        # 계산한 편미분 값들을 저장
        gradients['dW' + str(layer)] = dW
        gradients['db' + str(layer)] = db
    
    # 계산한 편미분 값들 리턴
    return gradients

def update(parameters, gradients, alpha, m):
    """계산한 경사로 가중치와 편향을 업데이트 하는 함수"""
    L = len(parameters) // 2
    
    for layer in range(1, L+1):
        parameters['W'+str(layer)] -= alpha * gradients['dW'+str(layer)] / m
        parameters['b'+str(layer)] -= alpha * gradients['db'+str(layer)] / m
    
    return parameters

def train_nn(X_train, Y_train, X_test, Y_test, neurons_per_layer, epoch, alpha):
    """신경망을 학습시키는 함수"""
    parameters = initialize_parameters(neurons_per_layer)
    loss_list = []
    m = X_train.shape[0]
    
    # epoch 번 경사 하강을 한다
    for i in range(epoch):
        parameters_copy = parameters.copy()
        
        # 모든 이미지에 대해서 경사 계산 후 평균 계산
        for x, y in zip(X_train, Y_train):
            prediction, cache = feed_forward(x, parameters)
            gradients = back_prop(prediction, y, cache, parameters)
            parameters_copy = update(parameters_copy, gradients, alpha, m)
        
        # 가중치와 편향 실제로 업데이트
        parameters = parameters_copy
        loss_list.append(compute_loss(X_train, Y_train, parameters))
        print('{}번째 경사 하강, 테스트 셋에서 성능: {}'.format(i+1, round(compute_accuracy(X_test, Y_test, parameters), 2)))     
            
    return loss_list, parameters




# 테스트 코드
neurons_per_layer = [784, 128, 64, 10]
parameters = initialize_parameters(neurons_per_layer)

loss_list, parameters = train_nn(X_train, Y_train, X_test, Y_test, neurons_per_layer, 25, 300)

# """디버깅을 위한 시각화 코드(쥬피터를 사용하시면 실행 코드 가장 아래줄에 넣어주세요!)
plt.plot(loss_list)
plt.show()
# """

```

    1번째 경사 하강, 테스트 셋에서 성능: 0.16
    2번째 경사 하강, 테스트 셋에서 성능: 0.18
    3번째 경사 하강, 테스트 셋에서 성능: 0.36
    4번째 경사 하강, 테스트 셋에서 성능: 0.54
    5번째 경사 하강, 테스트 셋에서 성능: 0.64
    6번째 경사 하강, 테스트 셋에서 성능: 0.64
    7번째 경사 하강, 테스트 셋에서 성능: 0.64
    8번째 경사 하강, 테스트 셋에서 성능: 0.68
    9번째 경사 하강, 테스트 셋에서 성능: 0.68
    10번째 경사 하강, 테스트 셋에서 성능: 0.7
    11번째 경사 하강, 테스트 셋에서 성능: 0.7
    12번째 경사 하강, 테스트 셋에서 성능: 0.7
    13번째 경사 하강, 테스트 셋에서 성능: 0.7
    14번째 경사 하강, 테스트 셋에서 성능: 0.7
    15번째 경사 하강, 테스트 셋에서 성능: 0.76
    16번째 경사 하강, 테스트 셋에서 성능: 0.76
    17번째 경사 하강, 테스트 셋에서 성능: 0.78
    18번째 경사 하강, 테스트 셋에서 성능: 0.8
    19번째 경사 하강, 테스트 셋에서 성능: 0.8
    20번째 경사 하강, 테스트 셋에서 성능: 0.8
    21번째 경사 하강, 테스트 셋에서 성능: 0.8
    22번째 경사 하강, 테스트 셋에서 성능: 0.8
    23번째 경사 하강, 테스트 셋에서 성능: 0.8
    24번째 경사 하강, 테스트 셋에서 성능: 0.8
    25번째 경사 하강, 테스트 셋에서 성능: 0.8
    


    
![png](output_31_1.png)
    


구현 예제에서 일단 수식을 코딩하는 수준으로 입력해보긴 했는데 이걸 내가 실제로 쓸 수 있을까? 만들 수 있을까? 읽어서 이해나 할 수 있을까?

## <a id='toc1_6_'></a>[신경망의 비선형성 nonliearity](#toc0_)
---

linearly inseperable data 선형 분리 불가능한 데이터도 있다

이럴 때 신경망을 쓰면 복잡한 모양을 분류할 수 있다

활성함수에 비선형 함수를 쓰면 복잡한 비선형 합성 함수를 쓸 수 있다

## <a id='toc1_7_'></a>[각 층별 주요 함수](#toc0_)
---

#### <a id='toc1_7_1_1_'></a>[은닉층](#toc0_)
---

- 시그모이드 함수: 인풋을 0과 1사이의 숫자로 바꿔준다. 그러나 입력값이 크거나 작을 때 경사가 사라지는 vanishing gradient problem이 있다. 경사하강법 적용이 힘들어진다.

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=4032&directory=Screen%20Shot%202020-12-03%20at%2012.18.26%20PM.png&name=Screen+Shot+2020-12-03+at+12.18.26+PM.png)


- reLu Rectified Linear Unit 함수: 사라지는 경사를 해결하기 위해 나왔으나 인풋이 0보다 작을 땐 아예 기울기가 없다

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=4032&directory=Screen%20Shot%202020-12-03%20at%2012.20.05%20PM.png&name=Screen+Shot+2020-12-03+at+12.20.05+PM.png)


- leaky reLu: reLu가 입력값이 0보다 작을 때도 경사를 갖게 변형

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=4032&directory=Screen%20Shot%202020-12-03%20at%2012.20.45%20PM.png&name=Screen+Shot+2020-12-03+at+12.20.45+PM.png)

#### <a id='toc1_7_1_2_'></a>[출력층](#toc0_)
---

- 시그모이드: 분류 결과가 셋 이상일 때는 각 예측 값의 합이 1을 초과하는 경우가 있다. 그럴 땐 확률의 의미가 퇴색된다
- softmax: 출력의 합을 1로 만들어준다.
- 선형함수: 비선형성은 은닉층에서 이미 해결됐으므로 출력값을 회귀함수로 풀어낼 수 있다

나는 ann에는 그다지 큰 관심이 없고 아주 열심히 활용할 생각도 많지 않기 때문에 겉만 햝는 정도로 머신러닝 연습, 관련 지식 습득 정도로 해도 그 목표에 충분히 도움이 되지만 부트캠프 커리큘럼을 보면 ann이 빠지지 않는다. 만약 이걸 한다고 하면 수학부터 빡세게 해야 할 거다

### <a id='toc1_7_2_'></a>[신경망 손실함수](#toc0_)

다양한 손실함수가 있다 ...

### <a id='toc1_7_3_'></a>[신경망 경사 하강법](#toc0_)

- batch 경사하강법은 신경망의 크기가 커질수록 느려진다는 단점이 있다. 가장 가파르게 내려가는 방향을 계산하고 내려간다.
- stochastic gradient descent 확률적 경사하강법: 임의로 하나의 데이터만 사용해 경사하강을 한다 부정확하지만 빠르게 진행할 수 있다.
- mini batch: 임의로 데이터셋을 쪼갠 후 한번 하강에 하나의 데이터셋을 돌린다

## <a id='toc1_8_'></a>[수료증](https://www.codeit.kr/certificates/kk2UB-XbRHm-55wy5-2m3zv) [&#8593;](#toc0_)
