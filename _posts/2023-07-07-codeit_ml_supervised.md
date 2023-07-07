---
layout: single
title:  "supervised ml "
---

**Table of contents**<a id='toc0_'></a>    
- [ML: supervised algorithms](#toc1_)    
  - [표기법](#toc1_1_)    
    - [손실 함수 loss function (또는 비용 함수 cost function)](#toc1_1_1_)    
    - [경사하강법 gradiant descent](#toc1_1_2_)    
  - [linear regression](#toc1_2_)    
    - [학습률](#toc1_2_1_)    
    - [모델 평가](#toc1_2_2_)    
  - [다중 선형 회귀](#toc1_3_)    
    - [정규방정식 normal equation](#toc1_3_1_)    
    - [경사하강법 Vs. 정규방정식](#toc1_3_2_)    
    - [그러나 경사하강법, 정규방정식 모두 global이 아니라 local minimum을 찾을 수 있다](#toc1_3_3_)    
  - [다항회귀 polynomial regression](#toc1_4_)    
  - [단일 속성 다항회귀](#toc1_5_)    
  - [다중 다항 회귀](#toc1_6_)    
  - [분류 cluster](#toc1_7_)    
    - [logistic regression](#toc1_7_1_)    
  - [수료증](#toc1_8_)    

<!-- vscode-jupyter-toc-config
	numbering=false
	anchor=true
	flat=false
	minLevel=1
	maxLevel=6
	/vscode-jupyter-toc-config -->
<!-- THIS CELL WILL BE REPLACED ON TOC UPDATE. DO NOT WRITE YOUR TEXT IN THIS CELL -->

# <a id='toc1_'></a>[ML: supervised algorithms](#toc0_)

- linear regression
- multiple linear regression
- polynomial regression
- logistic regression

**특히 수학 부분 복습 하자**

- 연속적인 값을 예측해야 할 때는 회귀를 쓴다
- 객관식처럼 몇개 뭉치로 나눠야 할 때는 분류를 쓴다

## <a id='toc1_1_'></a>[표기법](#toc0_)

- 입력 변수 x input variable, feature
- 목표 변수 y target varibable, output variable
- 인덱스 i에 따라 x(i), y(i)로 표현한다
- 시도하는 함수 : 가설함수 hypothesis function y = ax + b

### <a id='toc1_1_1_'></a>[손실 함수 loss function (또는 비용 함수 cost function)](#toc0_)
- **가설 함수를 평가하는 방법**
- 손실이 작을수록 가설 함수가 데이터에 잘 맞는다
- $J(a)$로 표기
  - 실제 변수 x는 이미 입력값들이 정해져있으므로 바꿀 수 있는 건 x를 제외한 상수값 세트다
- 선형 회귀에서는 평균제곱오차가 손실함수다

### <a id='toc1_1_2_'></a>[경사하강법 gradiant descent](#toc0_)
- 선형 회귀에서 손실 함수 결과를 최소화 하기 위해 쓰는 방법 중 하나
- 손실 함수 J(a)의 극소점을 찾는다
  - 손실이 작을수록 좋은 가설 함수라고 정의했으므로
    - 선형 회귀에서 손실 함수는 평균 제곱 오차이므로
    - 평균 제곱 오차가 최소가 되게 하는 상수 세트를 찾는 격
- a를 계속해서 업데이트한다
  - a에 대한 편미분 결과에 학습률L이라는 가중치를 곱한 후 a에서 차감한다 (기울기가 값이 커지는 방향을 가리키니 **차감**)
    - $a = a - L * ▽J(a)$
    - a가 여러개 일 때는 한번 업데이트 진행할 땐 업데이트 대상인 a만 고려한다
      - 앞에 거 업데이트하고 그 값을 넣어서 두번째를 업데이트 하듯 순차적으로 업데이트 하는 게 아니라
      - 모든 a에 대해서 업데이트가 하나도 진행되지 않은 세트로 계산한다
- 선형 회귀에서는 $J(a)$가 MSE 이므로 MSE를 넣고 편미분 하면 ...
  - 갑자기 과정은 안 보여주고 건너 뛴다

## <a id='toc1_2_'></a>[linear regression](#toc0_)
---
일차함수로 만들어진 직선 관계를 찾는다

회귀선을 찾는 방법
- 평균 제곱 오차 MSE mean squared error가 최소인 선을 찾는다

우선 이런 개념이 있다는 걸 인지하고 수학 개념은 천천히 파고들자


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing as cali
from sklearn.datasets import load_iris
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
import seaborn as sns
```


```python
def prediction(theta_0, theta_1, x):
    """주어진 학습 데이터 벡터 x에 대해서 예측 값을 리턴하는 함수"""
    # 코드를 쓰세요
    rst = theta_0 + theta_1 * x
    return rst
    


# 테스트 코드

# 입력 변수(집 크기) 초기화 (모든 집 평수 데이터를 1/10 크기로 줄임)
house_size = np.array([0.9, 1.4, 2, 2.1, 2.6, 3.3, 3.35, 3.9, 4.4, 4.7, 5.2, 5.75, 6.7, 6.9])
theta_0 = -3
theta_1 = 2

prediction(theta_0, theta_1, house_size)

```




    array([-1.2, -0.2,  1. ,  1.2,  2.2,  3.6,  3.7,  4.8,  5.8,  6.4,  7.4,
            8.5, 10.4, 10.8])




```python
def prediction_difference(theta_0, theta_1, x, y):
    """모든 예측 값들과 목표 변수들의 오차를 벡터로 리턴해주는 함수"""
    # 여기에 코드를 작성하세요
    h = prediction(theta_0, theta_1, x)
    rst = h - y
    return rst
    
    
# 입력 변수(집 크기) 초기화 (모든 집 평수 데이터를 1/10 크기로 줄임)
house_size = np.array([0.9, 1.4, 2, 2.1, 2.6, 3.3, 3.35, 3.9, 4.4, 4.7, 5.2, 5.75, 6.7, 6.9])

# 목표 변수(집 가격) 초기화 (모든 집 값 데이터를 1/10 크기로 줄임)
house_price = np.array([0.3, 0.75, 0.45, 1.1, 1.45, 0.9, 1.8, 0.9, 1.5, 2.2, 1.75, 2.3, 2.49, 2.6])

theta_0 = -3
theta_1 = 2

prediction_difference(-3, 2, house_size, house_price)
```




    array([-1.5 , -0.95,  0.55,  0.1 ,  0.75,  2.7 ,  1.9 ,  3.9 ,  4.3 ,
            4.2 ,  5.65,  6.2 ,  7.91,  8.2 ])




```python
def gradient_descent(theta_0, theta_1, x, y, iterations, alpha):
    """주어진 theta_0, theta_1 변수들을 경사 하강를 하면서 업데이트 해주는 함수"""
    for _ in range(iterations):  # 정해진 번만큼 경사 하강을 한다
        error = prediction_difference(theta_0, theta_1, x, y)  # 예측값들과 입력 변수들의 오차를 계산
        # 여기에 코드를 작성하세요
        theta_0 = theta_0 - alpha * error.mean()
        theta_1 = theta_1 - alpha * (error * x).mean()
        ################# 아다마르 곱을 한 다음 평균값을 낸다
        
    return theta_0, theta_1

# 입력 변수(집 크기) 초기화 (모든 집 평수 데이터를 1/10 크기로 줄임)
house_size = np.array([0.9, 1.4, 2, 2.1, 2.6, 3.3, 3.35, 3.9, 4.4, 4.7, 5.2, 5.75, 6.7, 6.9])

# 목표 변수(집 가격) 초기화 (모든 집 값 데이터를 1/10 크기로 줄임)
house_price = np.array([0.3, 0.75, 0.45, 1.1, 1.45, 0.9, 1.8, 0.9, 1.5, 2.2, 1.75, 2.3, 2.49, 2.6])

# theta 값들 초기화 (아무 값이나 시작함)
theta_0 = 2.5
theta_1 = 0

# 학습률 0.1로 200번 경사 하강
theta_0, theta_1 = gradient_descent(theta_0, theta_1, house_size, house_price, 200, 0.1)

theta_0, theta_1    
```




    (0.16821801417752186, 0.3438032402351199)




```python
# visualize
def gradient_descent(theta_0, theta_1, x, y, iterations, alpha):
    """주어진 theta_0, theta_1 변수들을 경사 하강를 하면서 업데이트 해주는 함수"""
    m = len(x)
    cost = []
    
    for _ in range(iterations):  # 정해진 번만큼 경사 하강을 한다
        error = prediction_difference(theta_0, theta_1, x, y)  # 예측값들과 입력 변수들의 오차를 계산
        cost.append(error@error / 2*m)
        # 여기에 코드를 작성하세요
        theta_0 = theta_0 - alpha * error.mean()
        theta_1 = theta_1 - alpha * (error * x).mean()
        ################# 아다마르 곱을 한 다음 평균값을 낸다
        
        if _ % 10 == 0:
            plt.scatter(house_size, house_price)
            plt.plot(house_size, prediction(theta_0, theta_1, x), color = 'red')
        
    return theta_0, theta_1, cost

# 입력 변수(집 크기) 초기화 (모든 집 평수 데이터를 1/10 크기로 줄임)
house_size = np.array([0.9, 1.4, 2, 2.1, 2.6, 3.3, 3.35, 3.9, 4.4, 4.7, 5.2, 5.75, 6.7, 6.9])

# 목표 변수(집 가격) 초기화 (모든 집 값 데이터를 1/10 크기로 줄임)
house_price = np.array([0.3, 0.75, 0.45, 1.1, 1.45, 0.9, 1.8, 0.9, 1.5, 2.2, 1.75, 2.3, 2.49, 2.6])

# theta 값들 초기화 (아무 값이나 시작함)
theta_0 = 2.5
theta_1 = 0

# 학습률 0.1로 200번 경사 하강
theta_0, theta_1, cost = gradient_descent(theta_0, theta_1, house_size, house_price, 200, 0.1)

theta_0, theta_1
```




    (0.16821801417752186, 0.3438032402351199)




    
![png](output_13_1.png)
    



```python
plt.plot(cost)
```




    [<matplotlib.lines.Line2D at 0x1b05080d090>]




    
![png](output_14_1.png)
    


### <a id='toc1_2_1_'></a>[학습률](#toc0_)

0~1 사이 값으로 설정하는데 너무 크거나 작으면 문제가 있다

### <a id='toc1_2_2_'></a>[모델 평가](#toc0_)

- 평균 제곱근 오차 RMSE root mean square error를 쓰기도 한다. MSE가 아니라 root을 씌우는 이유는 단위가 제곱이 되는 걸 방지하기 위해서다?
- 학습용 데이터 training set와 평가용 데이터 test set로 나누고 평가한다


```python
print(cali.__doc__)
```

    Load the California housing dataset (regression).
    
        ==============   ==============
        Samples total             20640
        Dimensionality                8
        Features                   real
        Target           real 0.15 - 5.
        ==============   ==============
    
        Read more in the :ref:`User Guide <california_housing_dataset>`.
    
        Parameters
        ----------
        data_home : str, default=None
            Specify another download and cache folder for the datasets. By default
            all scikit-learn data is stored in '~/scikit_learn_data' subfolders.
    
        download_if_missing : bool, default=True
            If False, raise a IOError if the data is not locally available
            instead of trying to download the data from the source site.
    
        return_X_y : bool, default=False
            If True, returns ``(data.data, data.target)`` instead of a Bunch
            object.
    
            .. versionadded:: 0.20
    
        as_frame : bool, default=False
            If True, the data is a pandas DataFrame including columns with
            appropriate dtypes (numeric, string or categorical). The target is
            a pandas DataFrame or Series depending on the number of target_columns.
    
            .. versionadded:: 0.23
    
        Returns
        -------
        dataset : :class:`~sklearn.utils.Bunch`
            Dictionary-like object, with the following attributes.
    
            data : ndarray, shape (20640, 8)
                Each row corresponding to the 8 feature values in order.
                If ``as_frame`` is True, ``data`` is a pandas object.
            target : numpy array of shape (20640,)
                Each value corresponds to the average
                house value in units of 100,000.
                If ``as_frame`` is True, ``target`` is a pandas object.
            feature_names : list of length 8
                Array of ordered feature names used in the dataset.
            DESCR : str
                Description of the California housing dataset.
            frame : pandas DataFrame
                Only present when `as_frame=True`. DataFrame with ``data`` and
                ``target``.
    
                .. versionadded:: 0.23
    
        (data, target) : tuple if ``return_X_y`` is True
            A tuple of two ndarray. The first containing a 2D array of
            shape (n_samples, n_features) with each row representing one
            sample and each column representing the features. The second
            ndarray of shape (n_samples,) containing the target samples.
    
            .. versionadded:: 0.20
    
        Notes
        -----
    
        This dataset consists of 20,640 samples and 9 features.
        
    


```python
print(cali().DESCR)
```

    .. _california_housing_dataset:
    
    California Housing dataset
    --------------------------
    
    **Data Set Characteristics:**
    
        :Number of Instances: 20640
    
        :Number of Attributes: 8 numeric, predictive attributes and the target
    
        :Attribute Information:
            - MedInc        median income in block group
            - HouseAge      median house age in block group
            - AveRooms      average number of rooms per household
            - AveBedrms     average number of bedrooms per household
            - Population    block group population
            - AveOccup      average number of household members
            - Latitude      block group latitude
            - Longitude     block group longitude
    
        :Missing Attribute Values: None
    
    This dataset was obtained from the StatLib repository.
    https://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.html
    
    The target variable is the median house value for California districts,
    expressed in hundreds of thousands of dollars ($100,000).
    
    This dataset was derived from the 1990 U.S. census, using one row per census
    block group. A block group is the smallest geographical unit for which the U.S.
    Census Bureau publishes sample data (a block group typically has a population
    of 600 to 3,000 people).
    
    A household is a group of people residing within a home. Since the average
    number of rooms and bedrooms in this dataset are provided per household, these
    columns may take surprisingly large values for block groups with few households
    and many empty houses, such as vacation resorts.
    
    It can be downloaded/loaded using the
    :func:`sklearn.datasets.fetch_california_housing` function.
    
    .. topic:: References
    
        - Pace, R. Kelley and Ronald Barry, Sparse Spatial Autoregressions,
          Statistics and Probability Letters, 33 (1997) 291-297
    
    


```python
cali()
```




    {'data': array([[   8.3252    ,   41.        ,    6.98412698, ...,    2.55555556,
               37.88      , -122.23      ],
            [   8.3014    ,   21.        ,    6.23813708, ...,    2.10984183,
               37.86      , -122.22      ],
            [   7.2574    ,   52.        ,    8.28813559, ...,    2.80225989,
               37.85      , -122.24      ],
            ...,
            [   1.7       ,   17.        ,    5.20554273, ...,    2.3256351 ,
               39.43      , -121.22      ],
            [   1.8672    ,   18.        ,    5.32951289, ...,    2.12320917,
               39.43      , -121.32      ],
            [   2.3886    ,   16.        ,    5.25471698, ...,    2.61698113,
               39.37      , -121.24      ]]),
     'target': array([4.526, 3.585, 3.521, ..., 0.923, 0.847, 0.894]),
     'frame': None,
     'target_names': ['MedHouseVal'],
     'feature_names': ['MedInc',
      'HouseAge',
      'AveRooms',
      'AveBedrms',
      'Population',
      'AveOccup',
      'Latitude',
      'Longitude'],
     'DESCR': '.. _california_housing_dataset:\n\nCalifornia Housing dataset\n--------------------------\n\n**Data Set Characteristics:**\n\n    :Number of Instances: 20640\n\n    :Number of Attributes: 8 numeric, predictive attributes and the target\n\n    :Attribute Information:\n        - MedInc        median income in block group\n        - HouseAge      median house age in block group\n        - AveRooms      average number of rooms per household\n        - AveBedrms     average number of bedrooms per household\n        - Population    block group population\n        - AveOccup      average number of household members\n        - Latitude      block group latitude\n        - Longitude     block group longitude\n\n    :Missing Attribute Values: None\n\nThis dataset was obtained from the StatLib repository.\nhttps://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.html\n\nThe target variable is the median house value for California districts,\nexpressed in hundreds of thousands of dollars ($100,000).\n\nThis dataset was derived from the 1990 U.S. census, using one row per census\nblock group. A block group is the smallest geographical unit for which the U.S.\nCensus Bureau publishes sample data (a block group typically has a population\nof 600 to 3,000 people).\n\nA household is a group of people residing within a home. Since the average\nnumber of rooms and bedrooms in this dataset are provided per household, these\ncolumns may take surprisingly large values for block groups with few households\nand many empty houses, such as vacation resorts.\n\nIt can be downloaded/loaded using the\n:func:`sklearn.datasets.fetch_california_housing` function.\n\n.. topic:: References\n\n    - Pace, R. Kelley and Ronald Barry, Sparse Spatial Autoregressions,\n      Statistics and Probability Letters, 33 (1997) 291-297\n'}




```python
cali().feature_names
```




    ['MedInc',
     'HouseAge',
     'AveRooms',
     'AveBedrms',
     'Population',
     'AveOccup',
     'Latitude',
     'Longitude']




```python
cali().data.shape
```




    (20640, 8)




```python
cali().target.shape
```




    (20640,)




```python
df = pd.DataFrame(cali().data, columns=cali().feature_names)
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MedInc</th>
      <th>HouseAge</th>
      <th>AveRooms</th>
      <th>AveBedrms</th>
      <th>Population</th>
      <th>AveOccup</th>
      <th>Latitude</th>
      <th>Longitude</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8.3252</td>
      <td>41.0</td>
      <td>6.984127</td>
      <td>1.023810</td>
      <td>322.0</td>
      <td>2.555556</td>
      <td>37.88</td>
      <td>-122.23</td>
    </tr>
    <tr>
      <th>1</th>
      <td>8.3014</td>
      <td>21.0</td>
      <td>6.238137</td>
      <td>0.971880</td>
      <td>2401.0</td>
      <td>2.109842</td>
      <td>37.86</td>
      <td>-122.22</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7.2574</td>
      <td>52.0</td>
      <td>8.288136</td>
      <td>1.073446</td>
      <td>496.0</td>
      <td>2.802260</td>
      <td>37.85</td>
      <td>-122.24</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5.6431</td>
      <td>52.0</td>
      <td>5.817352</td>
      <td>1.073059</td>
      <td>558.0</td>
      <td>2.547945</td>
      <td>37.85</td>
      <td>-122.25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3.8462</td>
      <td>52.0</td>
      <td>6.281853</td>
      <td>1.081081</td>
      <td>565.0</td>
      <td>2.181467</td>
      <td>37.85</td>
      <td>-122.25</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>20635</th>
      <td>1.5603</td>
      <td>25.0</td>
      <td>5.045455</td>
      <td>1.133333</td>
      <td>845.0</td>
      <td>2.560606</td>
      <td>39.48</td>
      <td>-121.09</td>
    </tr>
    <tr>
      <th>20636</th>
      <td>2.5568</td>
      <td>18.0</td>
      <td>6.114035</td>
      <td>1.315789</td>
      <td>356.0</td>
      <td>3.122807</td>
      <td>39.49</td>
      <td>-121.21</td>
    </tr>
    <tr>
      <th>20637</th>
      <td>1.7000</td>
      <td>17.0</td>
      <td>5.205543</td>
      <td>1.120092</td>
      <td>1007.0</td>
      <td>2.325635</td>
      <td>39.43</td>
      <td>-121.22</td>
    </tr>
    <tr>
      <th>20638</th>
      <td>1.8672</td>
      <td>18.0</td>
      <td>5.329513</td>
      <td>1.171920</td>
      <td>741.0</td>
      <td>2.123209</td>
      <td>39.43</td>
      <td>-121.32</td>
    </tr>
    <tr>
      <th>20639</th>
      <td>2.3886</td>
      <td>16.0</td>
      <td>5.254717</td>
      <td>1.162264</td>
      <td>1387.0</td>
      <td>2.616981</td>
      <td>39.37</td>
      <td>-121.24</td>
    </tr>
  </tbody>
</table>
<p>20640 rows × 8 columns</p>
</div>




```python
x = df[['HouseAge']]
y = pd.DataFrame(cali().target, columns=cali().target_names)
```


```python
x
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>HouseAge</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>41.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>52.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>52.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>52.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>20635</th>
      <td>25.0</td>
    </tr>
    <tr>
      <th>20636</th>
      <td>18.0</td>
    </tr>
    <tr>
      <th>20637</th>
      <td>17.0</td>
    </tr>
    <tr>
      <th>20638</th>
      <td>18.0</td>
    </tr>
    <tr>
      <th>20639</th>
      <td>16.0</td>
    </tr>
  </tbody>
</table>
<p>20640 rows × 1 columns</p>
</div>




```python
y
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MedHouseVal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4.526</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3.585</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.521</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3.413</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3.422</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>20635</th>
      <td>0.781</td>
    </tr>
    <tr>
      <th>20636</th>
      <td>0.771</td>
    </tr>
    <tr>
      <th>20637</th>
      <td>0.923</td>
    </tr>
    <tr>
      <th>20638</th>
      <td>0.847</td>
    </tr>
    <tr>
      <th>20639</th>
      <td>0.894</td>
    </tr>
  </tbody>
</table>
<p>20640 rows × 1 columns</p>
</div>




```python
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=5)
```


```python
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)
```

    (16512, 1)
    (16512, 1)
    (4128, 1)
    (4128, 1)
    


```python
model = LinearRegression()
```


```python
model.fit(x_train, y_train)
```




<style>#sk-container-id-1 {color: black;background-color: white;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id="sk-container-id-1" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>LinearRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-1" type="checkbox" checked><label for="sk-estimator-id-1" class="sk-toggleable__label sk-toggleable__label-arrow">LinearRegression</label><div class="sk-toggleable__content"><pre>LinearRegression()</pre></div></div></div></div></div>




```python
model.coef_
```




    array([[0.0089758]])




```python
model.intercept_
```




    array([1.80742009])




```python
y_predict = model.predict(x_test)
y_predict
```




    array([[1.93308132],
           [1.96898453],
           [2.04079095],
           ...,
           [2.10362156],
           [2.20235539],
           [2.14850057]])




```python
mean_squared_error(y_test, y_predict) ** 0.5
```




    1.1650449718027613



## <a id='toc1_3_'></a>[다중 선형 회귀](#toc0_)

- 여러 개의 입력 변수를 사용해서 목표 변수를 예측하는 알고리즘
  - 1차식인데 x가 여러개다 즉 $x^{(n)}$
- 다중 선형 회귀에서도 손실함수는 MSE로 동일하다 


```python
def prediction(X, theta):
    """다중 선형 회귀 가정 함수. 모든 데이터에 대한 예측 값을 numpy 배열로 리턴한다"""
    # 여기에 코드를 작성하세요
    # rst = X * theta ######### numpy에서 *는 elementwise multiplication이다 행렬의 곱은 @다
    rst = X @ theta
    return rst
    
    
# 입력 변수
house_size = np.array([1.0, 1.5, 1.8, 5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 6.0, 7.0, 8.0, 8.5, 9.0, 10.0])  # 집 크기
distance_from_station = np.array([5, 4.6, 4.2, 3.9, 3.9, 3.6, 3.5, 3.4, 2.9, 2.8, 2.7, 2.3, 2.0, 1.8, 1.5, 1.0])  # 지하철역으로부터의 거리 (km)
number_of_rooms = np.array([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4])  # 방 수

# 설계 행렬 X 정의
X = np.array([
    np.ones(16),
    house_size,
    distance_from_station,
    number_of_rooms
]).T

# 파라미터 theta 값 정의
theta = np.array([1, 2, 3, 4])

prediction(X, theta)
```




    array([22. , 21.8, 21.2, 26.7, 24.7, 24.8, 25.5, 26.2, 29.7, 31.4, 33.1,
           33.9, 39. , 39.4, 39.5, 40. ])



하나만 있을 때, 시리즈일 때, 벡터 일 땐 열이 1이다


```python
house_size.shape
```




    (16,)



시리즈는 열이 1인데 array로 포개면 눕혀서 쌓는다  
한 시리즈가 한 행을 이룬다


```python
y = np.array([
    np.ones(16),
    house_size,
    distance_from_station,
    number_of_rooms
])
y.shape
```




    (4, 16)



그래서 .T 했다?


```python
X.shape
```




    (16, 4)



쎄타는 4행 1열 벡터다


```python
theta.shape
```




    (4,)




```python
X * theta
```




    array([[ 1. ,  2. , 15. ,  4. ],
           [ 1. ,  3. , 13.8,  4. ],
           [ 1. ,  3.6, 12.6,  4. ],
           [ 1. , 10. , 11.7,  4. ],
           [ 1. ,  4. , 11.7,  8. ],
           [ 1. ,  5. , 10.8,  8. ],
           [ 1. ,  6. , 10.5,  8. ],
           [ 1. ,  7. , 10.2,  8. ],
           [ 1. ,  8. ,  8.7, 12. ],
           [ 1. , 10. ,  8.4, 12. ],
           [ 1. , 12. ,  8.1, 12. ],
           [ 1. , 14. ,  6.9, 12. ],
           [ 1. , 16. ,  6. , 16. ],
           [ 1. , 17. ,  5.4, 16. ],
           [ 1. , 18. ,  4.5, 16. ],
           [ 1. , 20. ,  3. , 16. ]])




```python
(X * theta).shape
```




    (16, 4)




```python
X * theta.T
```




    array([[ 1. ,  2. , 15. ,  4. ],
           [ 1. ,  3. , 13.8,  4. ],
           [ 1. ,  3.6, 12.6,  4. ],
           [ 1. , 10. , 11.7,  4. ],
           [ 1. ,  4. , 11.7,  8. ],
           [ 1. ,  5. , 10.8,  8. ],
           [ 1. ,  6. , 10.5,  8. ],
           [ 1. ,  7. , 10.2,  8. ],
           [ 1. ,  8. ,  8.7, 12. ],
           [ 1. , 10. ,  8.4, 12. ],
           [ 1. , 12. ,  8.1, 12. ],
           [ 1. , 14. ,  6.9, 12. ],
           [ 1. , 16. ,  6. , 16. ],
           [ 1. , 17. ,  5.4, 16. ],
           [ 1. , 18. ,  4.5, 16. ],
           [ 1. , 20. ,  3. , 16. ]])



이러면 16, 1이 나와야 하는 거 아닌가?  
라고 고민했었는데 __numpy에서 *은 element wise multiplication이다__  
행렬의 곱은 @로 해야 한다


```python
prediction(X, theta).shape
```




    (16,)




```python
def gradient_descent(X, theta, y, iterations, alpha):
    """다중 선형 회귀 경사 하강법을 구현한 함수"""
    m = len(X)  # 입력 변수 개수 저장
    
    for _ in range(iterations):
        # 여기에 코드를 작성하세요
        predict = prediction(X, theta)
        theta = theta - alpha / m * X.T @ (predict - y)
        
    return theta
    

# 입력 변수
house_size = np.array([1.0, 1.5, 1.8, 5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 6.0, 7.0, 8.0, 8.5, 9.0, 10.0])  # 집 크기
distance_from_station = np.array([5, 4.6, 4.2, 3.9, 3.9, 3.6, 3.5, 3.4, 2.9, 2.8, 2.7, 2.3, 2.0, 1.8, 1.5, 1.0])  # 지하철역으로부터의 거리 (km)
number_of_rooms = np.array([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4])  # 방 수

# 목표 변수
house_price = np.array([3, 3.2, 3.6 , 8, 3.4, 4.5, 5, 5.8, 6, 6.5, 9, 9, 10, 12, 13, 15])  # 집 가격

# 설계 행렬 X 정의
X = np.array([
    np.ones(16),
    house_size,
    distance_from_station,
    number_of_rooms
]).T

# 입력 변수 y 정의
y = house_price

# 파라미터 theta 초기화
theta = np.array([0, 0, 0, 0])

# 학습률 0.01로 100번 경사 하강
theta = gradient_descent(X, theta, y, 100, 0.01)

theta
```




    array([0.11484521, 1.21120425, 0.18270523, 0.30060782])



### <a id='toc1_3_1_'></a>[정규방정식 normal equation](#toc0_)
---
손실 함수를 최소화하기 위해 경사하강법 말고도 정규방정식을 쓰기도 한다  
정규방정식은 손실함수를 미분해서 구했다 그 과정은 tbd


수식으로 표현하면  


$\theta = {(X^T X)^{-1}}{X^T y} $

손실함수 J를 미분해서 기울기가 0이 되는 지점을 찾는다


```python
def normal_equation(X, y):
    """설계 행렬 X와 목표 변수 벡터 y를 받아 정규 방정식으로 최적의 theta를 구하는 함수"""
    # 여기에 코드를 작성하세요
    first = np.linalg.inv(X.T @ X)
    second = X.T @ y
    theta = first @ second
    
    
    return theta
    
# 입력 변수
house_size = np.array([1.0, 1.5, 1.8, 5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 6.0, 7.0, 8.0, 8.5, 9.0, 10.0])  # 집 크기
distance_from_station = np.array([5, 4.6, 4.2, 3.9, 3.9, 3.6, 3.5, 3.4, 2.9, 2.8, 2.7, 2.3, 2.0, 1.8, 1.5, 1.0])  # 지하철역으로부터의 거리 (km)
number_of_rooms = np.array([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4])  # 방 수

# 목표 변수
house_price = np.array([3, 3.2, 3.6 , 8, 3.4, 4.5, 5, 5.8, 6, 6.5, 9, 9, 10, 12, 13, 15])  # 집 가격

# 입력 변수 파라미터 X 정의
X = np.array([
    np.ones(16),
    house_size,
    distance_from_station,
    number_of_rooms
]).T

# 입력 변수 y 정의
y = house_price

# 정규 방적식으로 theta 계산
theta = normal_equation(X, y)
theta
```




    array([ 5.24706322,  1.30727421, -0.68881811, -0.8709494 ])



### <a id='toc1_3_2_'></a>[경사하강법 Vs. 정규방정식](#toc0_)

|경사하강법|정규방정식|
|:-:|:-:|
|학습률 alpha 필요| 불필요
|반복문 필요| 불필요
|n이 커도 효율적|n이 크면 행렬 연산 복잡
||역행렬 부재 시 pseudo inverse 하게 됨


따라서 대체로 n이 1000을 넘어가면 경사하강법을 선호한다

### <a id='toc1_3_3_'></a>[그러나 경사하강법, 정규방정식 모두 global이 아니라 local minimum을 찾을 수 있다](#toc0_)

![경사](https://bakey-api.codeit.kr/files/3045/M9Jmn5?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-05-12+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+12.36.22.png)

![정규](https://bakey-api.codeit.kr/files/3045/fqn4hH?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-05-12+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+12.36.29.png)

손실함수가 아래로 볼록한 2차 함수면 경사하강, 정규방정식 모두 최소점을 찾을 수 있는데  
선형 회귀에서 사용하는 MSE는 오차의 제곱에 관한 식이라 다행히 2차 함수이며 따라서 적용 가능하다


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MedInc</th>
      <th>HouseAge</th>
      <th>AveRooms</th>
      <th>AveBedrms</th>
      <th>Population</th>
      <th>AveOccup</th>
      <th>Latitude</th>
      <th>Longitude</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8.3252</td>
      <td>41.0</td>
      <td>6.984127</td>
      <td>1.023810</td>
      <td>322.0</td>
      <td>2.555556</td>
      <td>37.88</td>
      <td>-122.23</td>
    </tr>
    <tr>
      <th>1</th>
      <td>8.3014</td>
      <td>21.0</td>
      <td>6.238137</td>
      <td>0.971880</td>
      <td>2401.0</td>
      <td>2.109842</td>
      <td>37.86</td>
      <td>-122.22</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7.2574</td>
      <td>52.0</td>
      <td>8.288136</td>
      <td>1.073446</td>
      <td>496.0</td>
      <td>2.802260</td>
      <td>37.85</td>
      <td>-122.24</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5.6431</td>
      <td>52.0</td>
      <td>5.817352</td>
      <td>1.073059</td>
      <td>558.0</td>
      <td>2.547945</td>
      <td>37.85</td>
      <td>-122.25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3.8462</td>
      <td>52.0</td>
      <td>6.281853</td>
      <td>1.081081</td>
      <td>565.0</td>
      <td>2.181467</td>
      <td>37.85</td>
      <td>-122.25</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>20635</th>
      <td>1.5603</td>
      <td>25.0</td>
      <td>5.045455</td>
      <td>1.133333</td>
      <td>845.0</td>
      <td>2.560606</td>
      <td>39.48</td>
      <td>-121.09</td>
    </tr>
    <tr>
      <th>20636</th>
      <td>2.5568</td>
      <td>18.0</td>
      <td>6.114035</td>
      <td>1.315789</td>
      <td>356.0</td>
      <td>3.122807</td>
      <td>39.49</td>
      <td>-121.21</td>
    </tr>
    <tr>
      <th>20637</th>
      <td>1.7000</td>
      <td>17.0</td>
      <td>5.205543</td>
      <td>1.120092</td>
      <td>1007.0</td>
      <td>2.325635</td>
      <td>39.43</td>
      <td>-121.22</td>
    </tr>
    <tr>
      <th>20638</th>
      <td>1.8672</td>
      <td>18.0</td>
      <td>5.329513</td>
      <td>1.171920</td>
      <td>741.0</td>
      <td>2.123209</td>
      <td>39.43</td>
      <td>-121.32</td>
    </tr>
    <tr>
      <th>20639</th>
      <td>2.3886</td>
      <td>16.0</td>
      <td>5.254717</td>
      <td>1.162264</td>
      <td>1387.0</td>
      <td>2.616981</td>
      <td>39.37</td>
      <td>-121.24</td>
    </tr>
  </tbody>
</table>
<p>20640 rows × 8 columns</p>
</div>




```python
target_y = pd.DataFrame(cali().target, columns=cali().target_names)
```


```python
x_train, x_test, y_train, y_test = train_test_split(df, target_y, test_size=0.2, random_state=5)
```


```python
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)
```

    (16512, 8)
    (4128, 8)
    (16512, 1)
    (4128, 1)
    


```python
model = LinearRegression()
```


```python
model.fit(x_train, y_train)
```




<style>#sk-container-id-2 {color: black;background-color: white;}#sk-container-id-2 pre{padding: 0;}#sk-container-id-2 div.sk-toggleable {background-color: white;}#sk-container-id-2 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-2 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-2 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-2 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-2 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-2 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-2 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-2 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-container-id-2 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-2 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-2 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-2 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-2 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-2 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-2 div.sk-item {position: relative;z-index: 1;}#sk-container-id-2 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-2 div.sk-item::before, #sk-container-id-2 div.sk-parallel-item::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-2 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-2 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-2 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-2 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-2 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-2 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-2 div.sk-label-container {text-align: center;}#sk-container-id-2 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-2 div.sk-text-repr-fallback {display: none;}</style><div id="sk-container-id-2" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>LinearRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-2" type="checkbox" checked><label for="sk-estimator-id-2" class="sk-toggleable__label sk-toggleable__label-arrow">LinearRegression</label><div class="sk-toggleable__content"><pre>LinearRegression()</pre></div></div></div></div></div>




```python
model.coef_
```




    array([[ 4.38384807e-01,  9.17273492e-03, -1.11793600e-01,
             6.79331516e-01, -3.04158117e-06, -4.12179113e-03,
            -4.19560244e-01, -4.33473567e-01]])




```python
model.intercept_
```




    array([-36.89554297])




```python
y_prediction = model.predict(x_test)
```


```python
y_prediction
```




    array([[1.69422277],
           [1.94022419],
           [1.00866627],
           ...,
           [2.0254698 ],
           [2.07781354],
           [1.06749589]])




```python
mean_squared_error(y_test, y_prediction) ** 0.5
```




    0.7323542382277797




```python
sns.lineplot(data = model.predict(x_test))
sns.lineplot(data = y_test, palette='bright')
```




    <Axes: >




    
![png](output_70_1.png)
    



```python
df.columns
```




    Index(['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup',
           'Latitude', 'Longitude'],
          dtype='object')




```python
target_y
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MedHouseVal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4.526</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3.585</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.521</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3.413</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3.422</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>20635</th>
      <td>0.781</td>
    </tr>
    <tr>
      <th>20636</th>
      <td>0.771</td>
    </tr>
    <tr>
      <th>20637</th>
      <td>0.923</td>
    </tr>
    <tr>
      <th>20638</th>
      <td>0.847</td>
    </tr>
    <tr>
      <th>20639</th>
      <td>0.894</td>
    </tr>
  </tbody>
</table>
<p>20640 rows × 1 columns</p>
</div>




```python
tf = df
tf['target'] = target_y['MedHouseVal']
tf
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MedInc</th>
      <th>HouseAge</th>
      <th>AveRooms</th>
      <th>AveBedrms</th>
      <th>Population</th>
      <th>AveOccup</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>target</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8.3252</td>
      <td>41.0</td>
      <td>6.984127</td>
      <td>1.023810</td>
      <td>322.0</td>
      <td>2.555556</td>
      <td>37.88</td>
      <td>-122.23</td>
      <td>4.526</td>
    </tr>
    <tr>
      <th>1</th>
      <td>8.3014</td>
      <td>21.0</td>
      <td>6.238137</td>
      <td>0.971880</td>
      <td>2401.0</td>
      <td>2.109842</td>
      <td>37.86</td>
      <td>-122.22</td>
      <td>3.585</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7.2574</td>
      <td>52.0</td>
      <td>8.288136</td>
      <td>1.073446</td>
      <td>496.0</td>
      <td>2.802260</td>
      <td>37.85</td>
      <td>-122.24</td>
      <td>3.521</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5.6431</td>
      <td>52.0</td>
      <td>5.817352</td>
      <td>1.073059</td>
      <td>558.0</td>
      <td>2.547945</td>
      <td>37.85</td>
      <td>-122.25</td>
      <td>3.413</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3.8462</td>
      <td>52.0</td>
      <td>6.281853</td>
      <td>1.081081</td>
      <td>565.0</td>
      <td>2.181467</td>
      <td>37.85</td>
      <td>-122.25</td>
      <td>3.422</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>20635</th>
      <td>1.5603</td>
      <td>25.0</td>
      <td>5.045455</td>
      <td>1.133333</td>
      <td>845.0</td>
      <td>2.560606</td>
      <td>39.48</td>
      <td>-121.09</td>
      <td>0.781</td>
    </tr>
    <tr>
      <th>20636</th>
      <td>2.5568</td>
      <td>18.0</td>
      <td>6.114035</td>
      <td>1.315789</td>
      <td>356.0</td>
      <td>3.122807</td>
      <td>39.49</td>
      <td>-121.21</td>
      <td>0.771</td>
    </tr>
    <tr>
      <th>20637</th>
      <td>1.7000</td>
      <td>17.0</td>
      <td>5.205543</td>
      <td>1.120092</td>
      <td>1007.0</td>
      <td>2.325635</td>
      <td>39.43</td>
      <td>-121.22</td>
      <td>0.923</td>
    </tr>
    <tr>
      <th>20638</th>
      <td>1.8672</td>
      <td>18.0</td>
      <td>5.329513</td>
      <td>1.171920</td>
      <td>741.0</td>
      <td>2.123209</td>
      <td>39.43</td>
      <td>-121.32</td>
      <td>0.847</td>
    </tr>
    <tr>
      <th>20639</th>
      <td>2.3886</td>
      <td>16.0</td>
      <td>5.254717</td>
      <td>1.162264</td>
      <td>1387.0</td>
      <td>2.616981</td>
      <td>39.37</td>
      <td>-121.24</td>
      <td>0.894</td>
    </tr>
  </tbody>
</table>
<p>20640 rows × 9 columns</p>
</div>




```python
sns.set(style = 'whitegrid', context = 'notebook')
sns.pairplot(tf, height= 2.5)
```




    <seaborn.axisgrid.PairGrid at 0x1b034a5bd90>




    
![png](output_74_1.png)
    



```python
cor = np.corrcoef(tf.values.T)
cor
```




    array([[ 1.        , -0.11903399,  0.32689543, -0.06204013,  0.00483435,
             0.01876625, -0.07980913, -0.01517587,  0.68807521],
           [-0.11903399,  1.        , -0.15327742, -0.07774728, -0.29624424,
             0.01319136,  0.01117267, -0.10819681,  0.10562341],
           [ 0.32689543, -0.15327742,  1.        ,  0.84762133, -0.07221285,
            -0.00485229,  0.10638897, -0.02754005,  0.15194829],
           [-0.06204013, -0.07774728,  0.84762133,  1.        , -0.0661974 ,
            -0.0061812 ,  0.06972113,  0.01334439, -0.04670051],
           [ 0.00483435, -0.29624424, -0.07221285, -0.0661974 ,  1.        ,
             0.06986273, -0.10878475,  0.09977322, -0.02464968],
           [ 0.01876625,  0.01319136, -0.00485229, -0.0061812 ,  0.06986273,
             1.        ,  0.00236618,  0.00247582, -0.02373741],
           [-0.07980913,  0.01117267,  0.10638897,  0.06972113, -0.10878475,
             0.00236618,  1.        , -0.92466443, -0.14416028],
           [-0.01517587, -0.10819681, -0.02754005,  0.01334439,  0.09977322,
             0.00247582, -0.92466443,  1.        , -0.04596662],
           [ 0.68807521,  0.10562341,  0.15194829, -0.04670051, -0.02464968,
            -0.02373741, -0.14416028, -0.04596662,  1.        ]])




```python
sns.heatmap(cor, annot=True, square=True, fmt='.2f', yticklabels=tf.columns, xticklabels=tf.columns)
```




    <Axes: >




    
![png](output_76_1.png)
    



```python
print(cali().DESCR)
```

    .. _california_housing_dataset:
    
    California Housing dataset
    --------------------------
    
    **Data Set Characteristics:**
    
        :Number of Instances: 20640
    
        :Number of Attributes: 8 numeric, predictive attributes and the target
    
        :Attribute Information:
            - MedInc        median income in block group
            - HouseAge      median house age in block group
            - AveRooms      average number of rooms per household
            - AveBedrms     average number of bedrooms per household
            - Population    block group population
            - AveOccup      average number of household members
            - Latitude      block group latitude
            - Longitude     block group longitude
    
        :Missing Attribute Values: None
    
    This dataset was obtained from the StatLib repository.
    https://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.html
    
    The target variable is the median house value for California districts,
    expressed in hundreds of thousands of dollars ($100,000).
    
    This dataset was derived from the 1990 U.S. census, using one row per census
    block group. A block group is the smallest geographical unit for which the U.S.
    Census Bureau publishes sample data (a block group typically has a population
    of 600 to 3,000 people).
    
    A household is a group of people residing within a home. Since the average
    number of rooms and bedrooms in this dataset are provided per household, these
    columns may take surprisingly large values for block groups with few households
    and many empty houses, such as vacation resorts.
    
    It can be downloaded/loaded using the
    :func:`sklearn.datasets.fetch_california_housing` function.
    
    .. topic:: References
    
        - Pace, R. Kelley and Ronald Barry, Sparse Spatial Autoregressions,
          Statistics and Probability Letters, 33 (1997) 291-297
    
    


```python
sns.boxenplot(y_prediction, palette='bright')
sns.boxenplot(y_test, palette='flare')
# sns.scatterplot(target_y, palette='pastel')
####### 산점도로 봤더니 x축이 인덱스가 된다. 그래서 순간 왜 데이터가 서로 안 맞지 하고 오해했다
```




    <Axes: >




    
![png](output_78_1.png)
    



```python
af = pd.DataFrame(y_prediction, columns=['predict'])
af['real'] = y_test
```


```python
sns.boxplot(af, palette='flare')
```




    <Axes: >




    
![png](output_80_1.png)
    



```python
sns.boxenplot(af, palette='flare')
```




    <Axes: >




    
![png](output_81_1.png)
    



```python
print(len(y_test))
print(len(y_prediction))
```

    4128
    4128
    

## <a id='toc1_4_'></a>[다항회귀 polynomial regression](#toc0_)

데이터에 가장 잘 맞는 선은 직선이 아니라 곡선이 맞을 수도 있다

![다항](https://bakey-api.codeit.kr/files/3065/89Stmf?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-05-14+%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB+10.50.14.png)

- 단일 속성 다항회귀
- 다중 속성 다항회귀

## <a id='toc1_5_'></a>[단일 속성 다항회귀](#toc0_)

![단일다형](https://bakey-api.codeit.kr/files/3063/LuibNw?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-05-14+%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB+10.40.58.png)

$x^2$을 $x^{(2)}$라고 취급한다 >>> 다중선형회귀와 같아진다

## <a id='toc1_6_'></a>[다중 다항 회귀](#toc0_)

![다중다항](https://bakey-api.codeit.kr/files/3064/zn2Is9?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-05-14+%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB+10.45.19.png)

$x_1, x_2, x_3$이 있을 때 (다중 속성일 때) 2차항으로서 가능한 경우의 수를 모두 포함시킨다 >>> 다중선형회귀와 같다


```python
tf
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MedInc</th>
      <th>HouseAge</th>
      <th>AveRooms</th>
      <th>AveBedrms</th>
      <th>Population</th>
      <th>AveOccup</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>target</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8.3252</td>
      <td>41.0</td>
      <td>6.984127</td>
      <td>1.023810</td>
      <td>322.0</td>
      <td>2.555556</td>
      <td>37.88</td>
      <td>-122.23</td>
      <td>4.526</td>
    </tr>
    <tr>
      <th>1</th>
      <td>8.3014</td>
      <td>21.0</td>
      <td>6.238137</td>
      <td>0.971880</td>
      <td>2401.0</td>
      <td>2.109842</td>
      <td>37.86</td>
      <td>-122.22</td>
      <td>3.585</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7.2574</td>
      <td>52.0</td>
      <td>8.288136</td>
      <td>1.073446</td>
      <td>496.0</td>
      <td>2.802260</td>
      <td>37.85</td>
      <td>-122.24</td>
      <td>3.521</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5.6431</td>
      <td>52.0</td>
      <td>5.817352</td>
      <td>1.073059</td>
      <td>558.0</td>
      <td>2.547945</td>
      <td>37.85</td>
      <td>-122.25</td>
      <td>3.413</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3.8462</td>
      <td>52.0</td>
      <td>6.281853</td>
      <td>1.081081</td>
      <td>565.0</td>
      <td>2.181467</td>
      <td>37.85</td>
      <td>-122.25</td>
      <td>3.422</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>20635</th>
      <td>1.5603</td>
      <td>25.0</td>
      <td>5.045455</td>
      <td>1.133333</td>
      <td>845.0</td>
      <td>2.560606</td>
      <td>39.48</td>
      <td>-121.09</td>
      <td>0.781</td>
    </tr>
    <tr>
      <th>20636</th>
      <td>2.5568</td>
      <td>18.0</td>
      <td>6.114035</td>
      <td>1.315789</td>
      <td>356.0</td>
      <td>3.122807</td>
      <td>39.49</td>
      <td>-121.21</td>
      <td>0.771</td>
    </tr>
    <tr>
      <th>20637</th>
      <td>1.7000</td>
      <td>17.0</td>
      <td>5.205543</td>
      <td>1.120092</td>
      <td>1007.0</td>
      <td>2.325635</td>
      <td>39.43</td>
      <td>-121.22</td>
      <td>0.923</td>
    </tr>
    <tr>
      <th>20638</th>
      <td>1.8672</td>
      <td>18.0</td>
      <td>5.329513</td>
      <td>1.171920</td>
      <td>741.0</td>
      <td>2.123209</td>
      <td>39.43</td>
      <td>-121.32</td>
      <td>0.847</td>
    </tr>
    <tr>
      <th>20639</th>
      <td>2.3886</td>
      <td>16.0</td>
      <td>5.254717</td>
      <td>1.162264</td>
      <td>1387.0</td>
      <td>2.616981</td>
      <td>39.37</td>
      <td>-121.24</td>
      <td>0.894</td>
    </tr>
  </tbody>
</table>
<p>20640 rows × 9 columns</p>
</div>



2차 함수로 가정한다


```python
poly_transformer = PolynomialFeatures(2)
```


```python
poly_data = poly_transformer.fit_transform(cali().data)
```


```python
poly_data
```




    array([[ 1.00000000e+00,  8.32520000e+00,  4.10000000e+01, ...,
             1.43489440e+03, -4.63007240e+03,  1.49401729e+04],
           [ 1.00000000e+00,  8.30140000e+00,  2.10000000e+01, ...,
             1.43337960e+03, -4.62724920e+03,  1.49377284e+04],
           [ 1.00000000e+00,  7.25740000e+00,  5.20000000e+01, ...,
             1.43262250e+03, -4.62678400e+03,  1.49426176e+04],
           ...,
           [ 1.00000000e+00,  1.70000000e+00,  1.70000000e+01, ...,
             1.55472490e+03, -4.77970460e+03,  1.46942884e+04],
           [ 1.00000000e+00,  1.86720000e+00,  1.80000000e+01, ...,
             1.55472490e+03, -4.78364760e+03,  1.47185424e+04],
           [ 1.00000000e+00,  2.38860000e+00,  1.60000000e+01, ...,
             1.54999690e+03, -4.77321880e+03,  1.46991376e+04]])



가상의 열들이 추가되면서 열이 늘었다


```python
poly_data.shape
```




    (20640, 45)




```python
cali()
```




    {'data': array([[   8.3252    ,   41.        ,    6.98412698, ...,    2.55555556,
               37.88      , -122.23      ],
            [   8.3014    ,   21.        ,    6.23813708, ...,    2.10984183,
               37.86      , -122.22      ],
            [   7.2574    ,   52.        ,    8.28813559, ...,    2.80225989,
               37.85      , -122.24      ],
            ...,
            [   1.7       ,   17.        ,    5.20554273, ...,    2.3256351 ,
               39.43      , -121.22      ],
            [   1.8672    ,   18.        ,    5.32951289, ...,    2.12320917,
               39.43      , -121.32      ],
            [   2.3886    ,   16.        ,    5.25471698, ...,    2.61698113,
               39.37      , -121.24      ]]),
     'target': array([4.526, 3.585, 3.521, ..., 0.923, 0.847, 0.894]),
     'frame': None,
     'target_names': ['MedHouseVal'],
     'feature_names': ['MedInc',
      'HouseAge',
      'AveRooms',
      'AveBedrms',
      'Population',
      'AveOccup',
      'Latitude',
      'Longitude'],
     'DESCR': '.. _california_housing_dataset:\n\nCalifornia Housing dataset\n--------------------------\n\n**Data Set Characteristics:**\n\n    :Number of Instances: 20640\n\n    :Number of Attributes: 8 numeric, predictive attributes and the target\n\n    :Attribute Information:\n        - MedInc        median income in block group\n        - HouseAge      median house age in block group\n        - AveRooms      average number of rooms per household\n        - AveBedrms     average number of bedrooms per household\n        - Population    block group population\n        - AveOccup      average number of household members\n        - Latitude      block group latitude\n        - Longitude     block group longitude\n\n    :Missing Attribute Values: None\n\nThis dataset was obtained from the StatLib repository.\nhttps://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.html\n\nThe target variable is the median house value for California districts,\nexpressed in hundreds of thousands of dollars ($100,000).\n\nThis dataset was derived from the 1990 U.S. census, using one row per census\nblock group. A block group is the smallest geographical unit for which the U.S.\nCensus Bureau publishes sample data (a block group typically has a population\nof 600 to 3,000 people).\n\nA household is a group of people residing within a home. Since the average\nnumber of rooms and bedrooms in this dataset are provided per household, these\ncolumns may take surprisingly large values for block groups with few households\nand many empty houses, such as vacation resorts.\n\nIt can be downloaded/loaded using the\n:func:`sklearn.datasets.fetch_california_housing` function.\n\n.. topic:: References\n\n    - Pace, R. Kelley and Ronald Barry, Sparse Spatial Autoregressions,\n      Statistics and Probability Letters, 33 (1997) 291-297\n'}




```python
poly_feature_names = poly_transformer.get_feature_names_out(cali().feature_names)
```

여러가지가 곱해져서 2차항들이 생겼다


```python
poly_feature_names
```




    array(['1', 'MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population',
           'AveOccup', 'Latitude', 'Longitude', 'MedInc^2', 'MedInc HouseAge',
           'MedInc AveRooms', 'MedInc AveBedrms', 'MedInc Population',
           'MedInc AveOccup', 'MedInc Latitude', 'MedInc Longitude',
           'HouseAge^2', 'HouseAge AveRooms', 'HouseAge AveBedrms',
           'HouseAge Population', 'HouseAge AveOccup', 'HouseAge Latitude',
           'HouseAge Longitude', 'AveRooms^2', 'AveRooms AveBedrms',
           'AveRooms Population', 'AveRooms AveOccup', 'AveRooms Latitude',
           'AveRooms Longitude', 'AveBedrms^2', 'AveBedrms Population',
           'AveBedrms AveOccup', 'AveBedrms Latitude', 'AveBedrms Longitude',
           'Population^2', 'Population AveOccup', 'Population Latitude',
           'Population Longitude', 'AveOccup^2', 'AveOccup Latitude',
           'AveOccup Longitude', 'Latitude^2', 'Latitude Longitude',
           'Longitude^2'], dtype=object)




```python
poly_df = pd.DataFrame(poly_data, columns=poly_feature_names)
```


```python
poly_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1</th>
      <th>MedInc</th>
      <th>HouseAge</th>
      <th>AveRooms</th>
      <th>AveBedrms</th>
      <th>Population</th>
      <th>AveOccup</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>MedInc^2</th>
      <th>...</th>
      <th>Population^2</th>
      <th>Population AveOccup</th>
      <th>Population Latitude</th>
      <th>Population Longitude</th>
      <th>AveOccup^2</th>
      <th>AveOccup Latitude</th>
      <th>AveOccup Longitude</th>
      <th>Latitude^2</th>
      <th>Latitude Longitude</th>
      <th>Longitude^2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>8.3252</td>
      <td>41.0</td>
      <td>6.984127</td>
      <td>1.023810</td>
      <td>322.0</td>
      <td>2.555556</td>
      <td>37.88</td>
      <td>-122.23</td>
      <td>69.308955</td>
      <td>...</td>
      <td>103684.0</td>
      <td>822.888889</td>
      <td>12197.36</td>
      <td>-39358.06</td>
      <td>6.530864</td>
      <td>96.804444</td>
      <td>-312.365556</td>
      <td>1434.8944</td>
      <td>-4630.0724</td>
      <td>14940.1729</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.0</td>
      <td>8.3014</td>
      <td>21.0</td>
      <td>6.238137</td>
      <td>0.971880</td>
      <td>2401.0</td>
      <td>2.109842</td>
      <td>37.86</td>
      <td>-122.22</td>
      <td>68.913242</td>
      <td>...</td>
      <td>5764801.0</td>
      <td>5065.730228</td>
      <td>90901.86</td>
      <td>-293450.22</td>
      <td>4.451433</td>
      <td>79.878612</td>
      <td>-257.864868</td>
      <td>1433.3796</td>
      <td>-4627.2492</td>
      <td>14937.7284</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.0</td>
      <td>7.2574</td>
      <td>52.0</td>
      <td>8.288136</td>
      <td>1.073446</td>
      <td>496.0</td>
      <td>2.802260</td>
      <td>37.85</td>
      <td>-122.24</td>
      <td>52.669855</td>
      <td>...</td>
      <td>246016.0</td>
      <td>1389.920904</td>
      <td>18773.60</td>
      <td>-60631.04</td>
      <td>7.852660</td>
      <td>106.065537</td>
      <td>-342.548249</td>
      <td>1432.6225</td>
      <td>-4626.7840</td>
      <td>14942.6176</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.0</td>
      <td>5.6431</td>
      <td>52.0</td>
      <td>5.817352</td>
      <td>1.073059</td>
      <td>558.0</td>
      <td>2.547945</td>
      <td>37.85</td>
      <td>-122.25</td>
      <td>31.844578</td>
      <td>...</td>
      <td>311364.0</td>
      <td>1421.753425</td>
      <td>21120.30</td>
      <td>-68215.50</td>
      <td>6.492025</td>
      <td>96.439726</td>
      <td>-311.486301</td>
      <td>1432.6225</td>
      <td>-4627.1625</td>
      <td>14945.0625</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.0</td>
      <td>3.8462</td>
      <td>52.0</td>
      <td>6.281853</td>
      <td>1.081081</td>
      <td>565.0</td>
      <td>2.181467</td>
      <td>37.85</td>
      <td>-122.25</td>
      <td>14.793254</td>
      <td>...</td>
      <td>319225.0</td>
      <td>1232.528958</td>
      <td>21385.25</td>
      <td>-69071.25</td>
      <td>4.758799</td>
      <td>82.568533</td>
      <td>-266.684363</td>
      <td>1432.6225</td>
      <td>-4627.1625</td>
      <td>14945.0625</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>20635</th>
      <td>1.0</td>
      <td>1.5603</td>
      <td>25.0</td>
      <td>5.045455</td>
      <td>1.133333</td>
      <td>845.0</td>
      <td>2.560606</td>
      <td>39.48</td>
      <td>-121.09</td>
      <td>2.434536</td>
      <td>...</td>
      <td>714025.0</td>
      <td>2163.712121</td>
      <td>33360.60</td>
      <td>-102321.05</td>
      <td>6.556703</td>
      <td>101.092727</td>
      <td>-310.063788</td>
      <td>1558.6704</td>
      <td>-4780.6332</td>
      <td>14662.7881</td>
    </tr>
    <tr>
      <th>20636</th>
      <td>1.0</td>
      <td>2.5568</td>
      <td>18.0</td>
      <td>6.114035</td>
      <td>1.315789</td>
      <td>356.0</td>
      <td>3.122807</td>
      <td>39.49</td>
      <td>-121.21</td>
      <td>6.537226</td>
      <td>...</td>
      <td>126736.0</td>
      <td>1111.719298</td>
      <td>14058.44</td>
      <td>-43150.76</td>
      <td>9.751924</td>
      <td>123.319649</td>
      <td>-378.515439</td>
      <td>1559.4601</td>
      <td>-4786.5829</td>
      <td>14691.8641</td>
    </tr>
    <tr>
      <th>20637</th>
      <td>1.0</td>
      <td>1.7000</td>
      <td>17.0</td>
      <td>5.205543</td>
      <td>1.120092</td>
      <td>1007.0</td>
      <td>2.325635</td>
      <td>39.43</td>
      <td>-121.22</td>
      <td>2.890000</td>
      <td>...</td>
      <td>1014049.0</td>
      <td>2341.914550</td>
      <td>39706.01</td>
      <td>-122068.54</td>
      <td>5.408579</td>
      <td>91.699792</td>
      <td>-281.913487</td>
      <td>1554.7249</td>
      <td>-4779.7046</td>
      <td>14694.2884</td>
    </tr>
    <tr>
      <th>20638</th>
      <td>1.0</td>
      <td>1.8672</td>
      <td>18.0</td>
      <td>5.329513</td>
      <td>1.171920</td>
      <td>741.0</td>
      <td>2.123209</td>
      <td>39.43</td>
      <td>-121.32</td>
      <td>3.486436</td>
      <td>...</td>
      <td>549081.0</td>
      <td>1573.297994</td>
      <td>29217.63</td>
      <td>-89898.12</td>
      <td>4.508017</td>
      <td>83.718138</td>
      <td>-257.587736</td>
      <td>1554.7249</td>
      <td>-4783.6476</td>
      <td>14718.5424</td>
    </tr>
    <tr>
      <th>20639</th>
      <td>1.0</td>
      <td>2.3886</td>
      <td>16.0</td>
      <td>5.254717</td>
      <td>1.162264</td>
      <td>1387.0</td>
      <td>2.616981</td>
      <td>39.37</td>
      <td>-121.24</td>
      <td>5.705410</td>
      <td>...</td>
      <td>1923769.0</td>
      <td>3629.752830</td>
      <td>54606.19</td>
      <td>-168159.88</td>
      <td>6.848590</td>
      <td>103.030547</td>
      <td>-317.282792</td>
      <td>1549.9969</td>
      <td>-4773.2188</td>
      <td>14699.1376</td>
    </tr>
  </tbody>
</table>
<p>20640 rows × 45 columns</p>
</div>




```python
target_y
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MedHouseVal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4.526</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3.585</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.521</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3.413</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3.422</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>20635</th>
      <td>0.781</td>
    </tr>
    <tr>
      <th>20636</th>
      <td>0.771</td>
    </tr>
    <tr>
      <th>20637</th>
      <td>0.923</td>
    </tr>
    <tr>
      <th>20638</th>
      <td>0.847</td>
    </tr>
    <tr>
      <th>20639</th>
      <td>0.894</td>
    </tr>
  </tbody>
</table>
<p>20640 rows × 1 columns</p>
</div>




```python
x_train, x_test, y_train, y_test = train_test_split(poly_df, target_y, test_size=0.2, random_state=5)
```


```python
model = LinearRegression()
```


```python
model.fit(x_train, y_train)
```




<style>#sk-container-id-3 {color: black;background-color: white;}#sk-container-id-3 pre{padding: 0;}#sk-container-id-3 div.sk-toggleable {background-color: white;}#sk-container-id-3 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-3 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-3 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-3 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-3 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-3 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-3 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-3 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-container-id-3 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-3 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-3 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-3 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-3 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-3 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-3 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-3 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-3 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-3 div.sk-item {position: relative;z-index: 1;}#sk-container-id-3 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-3 div.sk-item::before, #sk-container-id-3 div.sk-parallel-item::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-3 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-3 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-3 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-3 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-3 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-3 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-3 div.sk-label-container {text-align: center;}#sk-container-id-3 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-3 div.sk-text-repr-fallback {display: none;}</style><div id="sk-container-id-3" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>LinearRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-3" type="checkbox" checked><label for="sk-estimator-id-3" class="sk-toggleable__label sk-toggleable__label-arrow">LinearRegression</label><div class="sk-toggleable__content"><pre>LinearRegression()</pre></div></div></div></div></div>




```python
model.coef_
```




    array([[-2.80248013e-08, -1.11460579e+01, -8.42046678e-01,
             5.87000335e+00, -3.01542591e+01,  7.20176782e-04,
             1.26283255e+00,  9.33913838e+00,  6.53367998e+00,
            -3.19413706e-02,  1.72899488e-03,  4.79729289e-02,
            -1.95588952e-01,  5.70610752e-05,  1.39122241e-02,
            -1.50452986e-01, -1.42318532e-01,  1.95235463e-04,
            -1.48800352e-03,  1.32187964e-02,  2.07859123e-06,
            -1.48270170e-03, -1.01744841e-02, -9.96935878e-03,
             9.17449054e-03, -8.54938496e-02, -7.22232186e-05,
            -3.05461562e-03,  7.95604098e-02,  7.44834510e-02,
             1.94627546e-01,  4.54000811e-04,  3.79241637e-02,
            -4.20723964e-01, -3.84372526e-01,  1.49691637e-09,
             2.32667180e-05,  2.20900756e-05,  1.62102746e-05,
            -4.48299195e-05,  3.11890742e-02,  2.19467176e-02,
             6.50793940e-02,  1.15401126e-01,  4.37692730e-02]])




```python
model.intercept_
```




    array([232.64531149])




```python
y_poly_predict = model.predict(x_test)
```


```python
mean_squared_error(y_poly_predict, y_test) ** 0.5
```




    1.3135630456761564



오히려 RMSE가 커졌다. 1차항으로 할 때 더 잘 맞는다


```python
pdf = pd.DataFrame(y_poly_predict, columns=['poly_predict'])
pdf['real'] = target_y
pdf
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>poly_predict</th>
      <th>real</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.524139</td>
      <td>4.526</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.994496</td>
      <td>3.585</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.220666</td>
      <td>3.521</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.423334</td>
      <td>3.413</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.772791</td>
      <td>3.422</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>4123</th>
      <td>1.081315</td>
      <td>2.581</td>
    </tr>
    <tr>
      <th>4124</th>
      <td>2.791422</td>
      <td>2.724</td>
    </tr>
    <tr>
      <th>4125</th>
      <td>2.324530</td>
      <td>2.042</td>
    </tr>
    <tr>
      <th>4126</th>
      <td>1.962778</td>
      <td>1.865</td>
    </tr>
    <tr>
      <th>4127</th>
      <td>0.679118</td>
      <td>1.898</td>
    </tr>
  </tbody>
</table>
<p>4128 rows × 2 columns</p>
</div>




```python
sns.boxplot(pdf)
```




    <Axes: >




    
![png](output_115_1.png)
    



```python
sns.boxplot(pdf, showfliers = False)
```




    <Axes: >




    
![png](output_116_1.png)
    


## <a id='toc1_7_'></a>[분류 cluster](#toc0_)
---
### <a id='toc1_7_1_'></a>[logistic regression](#toc0_)
---

선형 회귀는 데이터 값에 너무 민감해서 분류에 적합하지 않다  
분류를 위해서는 항상 0과 1 사이 값만 만드는 시그모이드 함수 로지스틱 회귀를 쓴다

사실 logistic regression이니까 regrssion인데 0.5 기준으로 1이냐 0이냐 분류하는 데 쓰이므로 분류의 방법이다

![시그](https://bakey-api.codeit.kr/files/3067/VVdm3V?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-05-14+%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB+11.05.10.png)

![시그](https://editor.analyticsvidhya.com/uploads/23302main-qimg-7fc9e8601c15e33945720800aa237a7f.png)

![로그로스](https://vitalflux.com/wp-content/uploads/2020/10/Screenshot-2020-10-15-at-3.13.11-PM.png)

- logistic 회귀의 가설함수는 시그모이드 함수다
- 손실 함수는 logloss 로그 손실 함수(cross entropy)다
  - 가설 함수의 예측값과 실제 값을 비교한다
    - 실제 값이 1인 경우와 0인 경우의 식이 다르다
    - 가설함수 값을 x축 실제 값을 y축으로 했을 때
      - 실제 값이 1이면 x축이 1일 때 손실이 0
      - 실제 값이 0이면 x축이 0일 때 손실이 0

"손실함수를 편미분 하면 신기하게도 선형회귀와 거의 같은 모양이 된다"고 한다. 알아보자  
다만 가설함수가 선형회귀는 1차함수인데 로지스틱에선 시그모이드 함수다


```python
def sigmoid(x):
    """시그모이드 함수"""
    return 1 / (1 + np.exp(-x))
    

def prediction(X, theta):
    """로지스틱 회귀 가정 함수"""
    # 여기에 코드를 작성하세요
    
    rst = X @ theta    
    
    return sigmoid(rst)
    

# 입력 변수
hours_studied = np.array([0.2, 0.3, 0.7, 1, 1.3, 1.8, 2, 2.1, 2.2, 3, 4, 4.2, 4, 4.7, 5.0, 5.9])  # 공부 시간 (단위: 100시간)
gpa_rank = np.array([0.9, 0.95, 0.8, 0.82, 0.7, 0.6, 0.55, 0.67, 0.4, 0.3, 0.2, 0.2, 0.15, 0.18, 0.15, 0.05]) # 학년 내신 (백분률)
number_of_tries = np.array([1, 2, 2, 2, 4, 2, 2, 2, 3, 3, 3, 3, 2, 4, 1, 2])  # 시험 응시 횟수

# 설계 행렬 X 정의
X = np.array([
    np.ones(16),
    hours_studied,
    gpa_rank,
    number_of_tries
]).T

# 파라미터 theta 정의
theta = [0.5, 0.3, -2, 0.2]  

prediction(X, theta)
```




    array([0.26114999, 0.28699984, 0.37989357, 0.39174097, 0.57199613,
           0.55971365, 0.59868766, 0.54735762, 0.72312181, 0.80218389,
           0.86989153, 0.87653295, 0.85814894, 0.91293423, 0.86989153,
           0.9289057 ])




```python
def gradient_descent(X, theta, y, iterations, alpha):
    """로지스틱 회귀 경사 하강 알고리즘"""
    m = len(X)  # 입력 변수 개수 저장

    for _ in range(iterations):
        # 여기에 코드를 작성하세요
        error = prediction(X, theta) - y
        theta = theta - alpha / m * X.T @ error
            
    return theta
    
    
# 입력 변수
hours_studied = np.array([0.2, 0.3, 0.7, 1, 1.3, 1.8, 2, 2.1, 2.2, 3, 4, 4.2, 4, 4.7, 5.0, 5.9])  # 공부 시간 (단위: 100시간)
gpa_rank = np.array([0.9, 0.95, 0.8, 0.82, 0.7, 0.6, 0.55, 0.67, 0.4, 0.3, 0.2, 0.2, 0.15, 0.18, 0.15, 0.05]) # 학년 내신 (백분률)
number_of_tries = np.array([1, 2, 2, 2, 4, 2, 2, 2, 3, 3, 3, 3, 2, 4, 1, 2])  # 시험 응시 횟수

# 목표 변수
passed = np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1])  # 시험 통과 여부 (0: 탈락, 1:통과)

# 설계 행렬 X 정의
X = np.array([
    np.ones(16),
    hours_studied,
    gpa_rank,
    number_of_tries
]).T

# 입력 변수 y 정의
y = passed

theta = [0, 0, 0, 0]  # 파라미터 초기값 설정
theta = gradient_descent(X, theta, y, 300, 0.1)  # 경사 하강법을 사용해서 최적의 파라미터를 찾는다
theta
```




    array([-1.35280508,  1.61640725, -1.83666046, -0.60286277])



편미분 원소들이 선형식이 아니라서 정규 방정식으로 풀 순 없다고 한다. theta가 e를 포함하는 게 예. 알아보자
>선형 회귀는 손실 함수 $J(MSE)가$ convex (아래로 볼록) 할 뿐만 아니라, 편미분 원소들을 모두 선형식으로 나타낼 수 있기 때문에 정규 방정식처럼 단순 행렬 연산만으로도 최적의 θ 값들을 구할 수 있습니다.
로지스틱 회귀에서는 손실 함수 J(로그 손실)가 아래로 볼록한 (convex) 합니다. 따라서 경사 하강법을 사용하면 항상 최적의 θ값들을 찾을 수 있습니다. 하지만 J에 대한 편미분 원소들이 선형식이 아닙니다. 가장 기본적으로 θ가 e의 지수에 포함됐는데요. 지수로 포함된 식은 일차식으로만 표현하기가 불가능합니다. 그렇기 때문에 단순 행렬 연산만으로는 최소 지점을 찾아낼 수 없죠.


```python
ldf = load_iris()
ldf
```




    {'data': array([[5.1, 3.5, 1.4, 0.2],
            [4.9, 3. , 1.4, 0.2],
            [4.7, 3.2, 1.3, 0.2],
            [4.6, 3.1, 1.5, 0.2],
            [5. , 3.6, 1.4, 0.2],
            [5.4, 3.9, 1.7, 0.4],
            [4.6, 3.4, 1.4, 0.3],
            [5. , 3.4, 1.5, 0.2],
            [4.4, 2.9, 1.4, 0.2],
            [4.9, 3.1, 1.5, 0.1],
            [5.4, 3.7, 1.5, 0.2],
            [4.8, 3.4, 1.6, 0.2],
            [4.8, 3. , 1.4, 0.1],
            [4.3, 3. , 1.1, 0.1],
            [5.8, 4. , 1.2, 0.2],
            [5.7, 4.4, 1.5, 0.4],
            [5.4, 3.9, 1.3, 0.4],
            [5.1, 3.5, 1.4, 0.3],
            [5.7, 3.8, 1.7, 0.3],
            [5.1, 3.8, 1.5, 0.3],
            [5.4, 3.4, 1.7, 0.2],
            [5.1, 3.7, 1.5, 0.4],
            [4.6, 3.6, 1. , 0.2],
            [5.1, 3.3, 1.7, 0.5],
            [4.8, 3.4, 1.9, 0.2],
            [5. , 3. , 1.6, 0.2],
            [5. , 3.4, 1.6, 0.4],
            [5.2, 3.5, 1.5, 0.2],
            [5.2, 3.4, 1.4, 0.2],
            [4.7, 3.2, 1.6, 0.2],
            [4.8, 3.1, 1.6, 0.2],
            [5.4, 3.4, 1.5, 0.4],
            [5.2, 4.1, 1.5, 0.1],
            [5.5, 4.2, 1.4, 0.2],
            [4.9, 3.1, 1.5, 0.2],
            [5. , 3.2, 1.2, 0.2],
            [5.5, 3.5, 1.3, 0.2],
            [4.9, 3.6, 1.4, 0.1],
            [4.4, 3. , 1.3, 0.2],
            [5.1, 3.4, 1.5, 0.2],
            [5. , 3.5, 1.3, 0.3],
            [4.5, 2.3, 1.3, 0.3],
            [4.4, 3.2, 1.3, 0.2],
            [5. , 3.5, 1.6, 0.6],
            [5.1, 3.8, 1.9, 0.4],
            [4.8, 3. , 1.4, 0.3],
            [5.1, 3.8, 1.6, 0.2],
            [4.6, 3.2, 1.4, 0.2],
            [5.3, 3.7, 1.5, 0.2],
            [5. , 3.3, 1.4, 0.2],
            [7. , 3.2, 4.7, 1.4],
            [6.4, 3.2, 4.5, 1.5],
            [6.9, 3.1, 4.9, 1.5],
            [5.5, 2.3, 4. , 1.3],
            [6.5, 2.8, 4.6, 1.5],
            [5.7, 2.8, 4.5, 1.3],
            [6.3, 3.3, 4.7, 1.6],
            [4.9, 2.4, 3.3, 1. ],
            [6.6, 2.9, 4.6, 1.3],
            [5.2, 2.7, 3.9, 1.4],
            [5. , 2. , 3.5, 1. ],
            [5.9, 3. , 4.2, 1.5],
            [6. , 2.2, 4. , 1. ],
            [6.1, 2.9, 4.7, 1.4],
            [5.6, 2.9, 3.6, 1.3],
            [6.7, 3.1, 4.4, 1.4],
            [5.6, 3. , 4.5, 1.5],
            [5.8, 2.7, 4.1, 1. ],
            [6.2, 2.2, 4.5, 1.5],
            [5.6, 2.5, 3.9, 1.1],
            [5.9, 3.2, 4.8, 1.8],
            [6.1, 2.8, 4. , 1.3],
            [6.3, 2.5, 4.9, 1.5],
            [6.1, 2.8, 4.7, 1.2],
            [6.4, 2.9, 4.3, 1.3],
            [6.6, 3. , 4.4, 1.4],
            [6.8, 2.8, 4.8, 1.4],
            [6.7, 3. , 5. , 1.7],
            [6. , 2.9, 4.5, 1.5],
            [5.7, 2.6, 3.5, 1. ],
            [5.5, 2.4, 3.8, 1.1],
            [5.5, 2.4, 3.7, 1. ],
            [5.8, 2.7, 3.9, 1.2],
            [6. , 2.7, 5.1, 1.6],
            [5.4, 3. , 4.5, 1.5],
            [6. , 3.4, 4.5, 1.6],
            [6.7, 3.1, 4.7, 1.5],
            [6.3, 2.3, 4.4, 1.3],
            [5.6, 3. , 4.1, 1.3],
            [5.5, 2.5, 4. , 1.3],
            [5.5, 2.6, 4.4, 1.2],
            [6.1, 3. , 4.6, 1.4],
            [5.8, 2.6, 4. , 1.2],
            [5. , 2.3, 3.3, 1. ],
            [5.6, 2.7, 4.2, 1.3],
            [5.7, 3. , 4.2, 1.2],
            [5.7, 2.9, 4.2, 1.3],
            [6.2, 2.9, 4.3, 1.3],
            [5.1, 2.5, 3. , 1.1],
            [5.7, 2.8, 4.1, 1.3],
            [6.3, 3.3, 6. , 2.5],
            [5.8, 2.7, 5.1, 1.9],
            [7.1, 3. , 5.9, 2.1],
            [6.3, 2.9, 5.6, 1.8],
            [6.5, 3. , 5.8, 2.2],
            [7.6, 3. , 6.6, 2.1],
            [4.9, 2.5, 4.5, 1.7],
            [7.3, 2.9, 6.3, 1.8],
            [6.7, 2.5, 5.8, 1.8],
            [7.2, 3.6, 6.1, 2.5],
            [6.5, 3.2, 5.1, 2. ],
            [6.4, 2.7, 5.3, 1.9],
            [6.8, 3. , 5.5, 2.1],
            [5.7, 2.5, 5. , 2. ],
            [5.8, 2.8, 5.1, 2.4],
            [6.4, 3.2, 5.3, 2.3],
            [6.5, 3. , 5.5, 1.8],
            [7.7, 3.8, 6.7, 2.2],
            [7.7, 2.6, 6.9, 2.3],
            [6. , 2.2, 5. , 1.5],
            [6.9, 3.2, 5.7, 2.3],
            [5.6, 2.8, 4.9, 2. ],
            [7.7, 2.8, 6.7, 2. ],
            [6.3, 2.7, 4.9, 1.8],
            [6.7, 3.3, 5.7, 2.1],
            [7.2, 3.2, 6. , 1.8],
            [6.2, 2.8, 4.8, 1.8],
            [6.1, 3. , 4.9, 1.8],
            [6.4, 2.8, 5.6, 2.1],
            [7.2, 3. , 5.8, 1.6],
            [7.4, 2.8, 6.1, 1.9],
            [7.9, 3.8, 6.4, 2. ],
            [6.4, 2.8, 5.6, 2.2],
            [6.3, 2.8, 5.1, 1.5],
            [6.1, 2.6, 5.6, 1.4],
            [7.7, 3. , 6.1, 2.3],
            [6.3, 3.4, 5.6, 2.4],
            [6.4, 3.1, 5.5, 1.8],
            [6. , 3. , 4.8, 1.8],
            [6.9, 3.1, 5.4, 2.1],
            [6.7, 3.1, 5.6, 2.4],
            [6.9, 3.1, 5.1, 2.3],
            [5.8, 2.7, 5.1, 1.9],
            [6.8, 3.2, 5.9, 2.3],
            [6.7, 3.3, 5.7, 2.5],
            [6.7, 3. , 5.2, 2.3],
            [6.3, 2.5, 5. , 1.9],
            [6.5, 3. , 5.2, 2. ],
            [6.2, 3.4, 5.4, 2.3],
            [5.9, 3. , 5.1, 1.8]]),
     'target': array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
            2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
            2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]),
     'frame': None,
     'target_names': array(['setosa', 'versicolor', 'virginica'], dtype='<U10'),
     'DESCR': '.. _iris_dataset:\n\nIris plants dataset\n--------------------\n\n**Data Set Characteristics:**\n\n    :Number of Instances: 150 (50 in each of three classes)\n    :Number of Attributes: 4 numeric, predictive attributes and the class\n    :Attribute Information:\n        - sepal length in cm\n        - sepal width in cm\n        - petal length in cm\n        - petal width in cm\n        - class:\n                - Iris-Setosa\n                - Iris-Versicolour\n                - Iris-Virginica\n                \n    :Summary Statistics:\n\n    ============== ==== ==== ======= ===== ====================\n                    Min  Max   Mean    SD   Class Correlation\n    ============== ==== ==== ======= ===== ====================\n    sepal length:   4.3  7.9   5.84   0.83    0.7826\n    sepal width:    2.0  4.4   3.05   0.43   -0.4194\n    petal length:   1.0  6.9   3.76   1.76    0.9490  (high!)\n    petal width:    0.1  2.5   1.20   0.76    0.9565  (high!)\n    ============== ==== ==== ======= ===== ====================\n\n    :Missing Attribute Values: None\n    :Class Distribution: 33.3% for each of 3 classes.\n    :Creator: R.A. Fisher\n    :Donor: Michael Marshall (MARSHALL%PLU@io.arc.nasa.gov)\n    :Date: July, 1988\n\nThe famous Iris database, first used by Sir R.A. Fisher. The dataset is taken\nfrom Fisher\'s paper. Note that it\'s the same as in R, but not as in the UCI\nMachine Learning Repository, which has two wrong data points.\n\nThis is perhaps the best known database to be found in the\npattern recognition literature.  Fisher\'s paper is a classic in the field and\nis referenced frequently to this day.  (See Duda & Hart, for example.)  The\ndata set contains 3 classes of 50 instances each, where each class refers to a\ntype of iris plant.  One class is linearly separable from the other 2; the\nlatter are NOT linearly separable from each other.\n\n.. topic:: References\n\n   - Fisher, R.A. "The use of multiple measurements in taxonomic problems"\n     Annual Eugenics, 7, Part II, 179-188 (1936); also in "Contributions to\n     Mathematical Statistics" (John Wiley, NY, 1950).\n   - Duda, R.O., & Hart, P.E. (1973) Pattern Classification and Scene Analysis.\n     (Q327.D83) John Wiley & Sons.  ISBN 0-471-22361-1.  See page 218.\n   - Dasarathy, B.V. (1980) "Nosing Around the Neighborhood: A New System\n     Structure and Classification Rule for Recognition in Partially Exposed\n     Environments".  IEEE Transactions on Pattern Analysis and Machine\n     Intelligence, Vol. PAMI-2, No. 1, 67-71.\n   - Gates, G.W. (1972) "The Reduced Nearest Neighbor Rule".  IEEE Transactions\n     on Information Theory, May 1972, 431-433.\n   - See also: 1988 MLC Proceedings, 54-64.  Cheeseman et al"s AUTOCLASS II\n     conceptual clustering system finds 3 classes in the data.\n   - Many, many more ...',
     'feature_names': ['sepal length (cm)',
      'sepal width (cm)',
      'petal length (cm)',
      'petal width (cm)'],
     'filename': 'iris.csv',
     'data_module': 'sklearn.datasets.data'}




```python
print(ldf.DESCR)
```

    .. _iris_dataset:
    
    Iris plants dataset
    --------------------
    
    **Data Set Characteristics:**
    
        :Number of Instances: 150 (50 in each of three classes)
        :Number of Attributes: 4 numeric, predictive attributes and the class
        :Attribute Information:
            - sepal length in cm
            - sepal width in cm
            - petal length in cm
            - petal width in cm
            - class:
                    - Iris-Setosa
                    - Iris-Versicolour
                    - Iris-Virginica
                    
        :Summary Statistics:
    
        ============== ==== ==== ======= ===== ====================
                        Min  Max   Mean    SD   Class Correlation
        ============== ==== ==== ======= ===== ====================
        sepal length:   4.3  7.9   5.84   0.83    0.7826
        sepal width:    2.0  4.4   3.05   0.43   -0.4194
        petal length:   1.0  6.9   3.76   1.76    0.9490  (high!)
        petal width:    0.1  2.5   1.20   0.76    0.9565  (high!)
        ============== ==== ==== ======= ===== ====================
    
        :Missing Attribute Values: None
        :Class Distribution: 33.3% for each of 3 classes.
        :Creator: R.A. Fisher
        :Donor: Michael Marshall (MARSHALL%PLU@io.arc.nasa.gov)
        :Date: July, 1988
    
    The famous Iris database, first used by Sir R.A. Fisher. The dataset is taken
    from Fisher's paper. Note that it's the same as in R, but not as in the UCI
    Machine Learning Repository, which has two wrong data points.
    
    This is perhaps the best known database to be found in the
    pattern recognition literature.  Fisher's paper is a classic in the field and
    is referenced frequently to this day.  (See Duda & Hart, for example.)  The
    data set contains 3 classes of 50 instances each, where each class refers to a
    type of iris plant.  One class is linearly separable from the other 2; the
    latter are NOT linearly separable from each other.
    
    .. topic:: References
    
       - Fisher, R.A. "The use of multiple measurements in taxonomic problems"
         Annual Eugenics, 7, Part II, 179-188 (1936); also in "Contributions to
         Mathematical Statistics" (John Wiley, NY, 1950).
       - Duda, R.O., & Hart, P.E. (1973) Pattern Classification and Scene Analysis.
         (Q327.D83) John Wiley & Sons.  ISBN 0-471-22361-1.  See page 218.
       - Dasarathy, B.V. (1980) "Nosing Around the Neighborhood: A New System
         Structure and Classification Rule for Recognition in Partially Exposed
         Environments".  IEEE Transactions on Pattern Analysis and Machine
         Intelligence, Vol. PAMI-2, No. 1, 67-71.
       - Gates, G.W. (1972) "The Reduced Nearest Neighbor Rule".  IEEE Transactions
         on Information Theory, May 1972, 431-433.
       - See also: 1988 MLC Proceedings, 54-64.  Cheeseman et al"s AUTOCLASS II
         conceptual clustering system finds 3 classes in the data.
       - Many, many more ...
    


```python
X = pd.DataFrame(ldf.data, columns=ldf.feature_names)
X
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sepal length (cm)</th>
      <th>sepal width (cm)</th>
      <th>petal length (cm)</th>
      <th>petal width (cm)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>145</th>
      <td>6.7</td>
      <td>3.0</td>
      <td>5.2</td>
      <td>2.3</td>
    </tr>
    <tr>
      <th>146</th>
      <td>6.3</td>
      <td>2.5</td>
      <td>5.0</td>
      <td>1.9</td>
    </tr>
    <tr>
      <th>147</th>
      <td>6.5</td>
      <td>3.0</td>
      <td>5.2</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>148</th>
      <td>6.2</td>
      <td>3.4</td>
      <td>5.4</td>
      <td>2.3</td>
    </tr>
    <tr>
      <th>149</th>
      <td>5.9</td>
      <td>3.0</td>
      <td>5.1</td>
      <td>1.8</td>
    </tr>
  </tbody>
</table>
<p>150 rows × 4 columns</p>
</div>




```python
y = pd.DataFrame(ldf.target, columns=['class'])
y
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>class</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>145</th>
      <td>2</td>
    </tr>
    <tr>
      <th>146</th>
      <td>2</td>
    </tr>
    <tr>
      <th>147</th>
      <td>2</td>
    </tr>
    <tr>
      <th>148</th>
      <td>2</td>
    </tr>
    <tr>
      <th>149</th>
      <td>2</td>
    </tr>
  </tbody>
</table>
<p>150 rows × 1 columns</p>
</div>




```python
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)
```


```python
y_train = y_train.values.ravel()
```


```python
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)
```

    (120, 4)
    (30, 4)
    (120,)
    (30, 1)
    


```python
model = LogisticRegression(solver='saga', max_iter=2000)
```


```python
model.fit(x_train, y_train)
```




<style>#sk-container-id-4 {color: black;background-color: white;}#sk-container-id-4 pre{padding: 0;}#sk-container-id-4 div.sk-toggleable {background-color: white;}#sk-container-id-4 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-4 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-4 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-4 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-4 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-4 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-4 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-4 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-container-id-4 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-4 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-4 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-4 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-4 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-4 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-4 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-4 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-4 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-4 div.sk-item {position: relative;z-index: 1;}#sk-container-id-4 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-4 div.sk-item::before, #sk-container-id-4 div.sk-parallel-item::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-4 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-4 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-4 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-4 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-4 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-4 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-4 div.sk-label-container {text-align: center;}#sk-container-id-4 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-4 div.sk-text-repr-fallback {display: none;}</style><div id="sk-container-id-4" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>LogisticRegression(max_iter=2000, solver=&#x27;saga&#x27;)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-4" type="checkbox" checked><label for="sk-estimator-id-4" class="sk-toggleable__label sk-toggleable__label-arrow">LogisticRegression</label><div class="sk-toggleable__content"><pre>LogisticRegression(max_iter=2000, solver=&#x27;saga&#x27;)</pre></div></div></div></div></div>




```python
model.predict(x_test)
```




    array([1, 2, 2, 0, 2, 1, 0, 2, 0, 1, 1, 2, 2, 2, 0, 0, 2, 2, 0, 0, 1, 2,
           0, 1, 1, 2, 1, 1, 1, 2])




```python
model.score(x_test, y_test)
```




    0.9666666666666667




```python
load_wine()
```




    {'data': array([[1.423e+01, 1.710e+00, 2.430e+00, ..., 1.040e+00, 3.920e+00,
             1.065e+03],
            [1.320e+01, 1.780e+00, 2.140e+00, ..., 1.050e+00, 3.400e+00,
             1.050e+03],
            [1.316e+01, 2.360e+00, 2.670e+00, ..., 1.030e+00, 3.170e+00,
             1.185e+03],
            ...,
            [1.327e+01, 4.280e+00, 2.260e+00, ..., 5.900e-01, 1.560e+00,
             8.350e+02],
            [1.317e+01, 2.590e+00, 2.370e+00, ..., 6.000e-01, 1.620e+00,
             8.400e+02],
            [1.413e+01, 4.100e+00, 2.740e+00, ..., 6.100e-01, 1.600e+00,
             5.600e+02]]),
     'target': array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2,
            2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
            2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
            2, 2]),
     'frame': None,
     'target_names': array(['class_0', 'class_1', 'class_2'], dtype='<U7'),
     'DESCR': '.. _wine_dataset:\n\nWine recognition dataset\n------------------------\n\n**Data Set Characteristics:**\n\n    :Number of Instances: 178\n    :Number of Attributes: 13 numeric, predictive attributes and the class\n    :Attribute Information:\n \t\t- Alcohol\n \t\t- Malic acid\n \t\t- Ash\n\t\t- Alcalinity of ash  \n \t\t- Magnesium\n\t\t- Total phenols\n \t\t- Flavanoids\n \t\t- Nonflavanoid phenols\n \t\t- Proanthocyanins\n\t\t- Color intensity\n \t\t- Hue\n \t\t- OD280/OD315 of diluted wines\n \t\t- Proline\n\n    - class:\n            - class_0\n            - class_1\n            - class_2\n\t\t\n    :Summary Statistics:\n    \n    ============================= ==== ===== ======= =====\n                                   Min   Max   Mean     SD\n    ============================= ==== ===== ======= =====\n    Alcohol:                      11.0  14.8    13.0   0.8\n    Malic Acid:                   0.74  5.80    2.34  1.12\n    Ash:                          1.36  3.23    2.36  0.27\n    Alcalinity of Ash:            10.6  30.0    19.5   3.3\n    Magnesium:                    70.0 162.0    99.7  14.3\n    Total Phenols:                0.98  3.88    2.29  0.63\n    Flavanoids:                   0.34  5.08    2.03  1.00\n    Nonflavanoid Phenols:         0.13  0.66    0.36  0.12\n    Proanthocyanins:              0.41  3.58    1.59  0.57\n    Colour Intensity:              1.3  13.0     5.1   2.3\n    Hue:                          0.48  1.71    0.96  0.23\n    OD280/OD315 of diluted wines: 1.27  4.00    2.61  0.71\n    Proline:                       278  1680     746   315\n    ============================= ==== ===== ======= =====\n\n    :Missing Attribute Values: None\n    :Class Distribution: class_0 (59), class_1 (71), class_2 (48)\n    :Creator: R.A. Fisher\n    :Donor: Michael Marshall (MARSHALL%PLU@io.arc.nasa.gov)\n    :Date: July, 1988\n\nThis is a copy of UCI ML Wine recognition datasets.\nhttps://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data\n\nThe data is the results of a chemical analysis of wines grown in the same\nregion in Italy by three different cultivators. There are thirteen different\nmeasurements taken for different constituents found in the three types of\nwine.\n\nOriginal Owners: \n\nForina, M. et al, PARVUS - \nAn Extendible Package for Data Exploration, Classification and Correlation. \nInstitute of Pharmaceutical and Food Analysis and Technologies,\nVia Brigata Salerno, 16147 Genoa, Italy.\n\nCitation:\n\nLichman, M. (2013). UCI Machine Learning Repository\n[https://archive.ics.uci.edu/ml]. Irvine, CA: University of California,\nSchool of Information and Computer Science. \n\n.. topic:: References\n\n  (1) S. Aeberhard, D. Coomans and O. de Vel, \n  Comparison of Classifiers in High Dimensional Settings, \n  Tech. Rep. no. 92-02, (1992), Dept. of Computer Science and Dept. of  \n  Mathematics and Statistics, James Cook University of North Queensland. \n  (Also submitted to Technometrics). \n\n  The data was used with many others for comparing various \n  classifiers. The classes are separable, though only RDA \n  has achieved 100% correct classification. \n  (RDA : 100%, QDA 99.4%, LDA 98.9%, 1NN 96.1% (z-transformed data)) \n  (All results using the leave-one-out technique) \n\n  (2) S. Aeberhard, D. Coomans and O. de Vel, \n  "THE CLASSIFICATION PERFORMANCE OF RDA" \n  Tech. Rep. no. 92-01, (1992), Dept. of Computer Science and Dept. of \n  Mathematics and Statistics, James Cook University of North Queensland. \n  (Also submitted to Journal of Chemometrics).\n',
     'feature_names': ['alcohol',
      'malic_acid',
      'ash',
      'alcalinity_of_ash',
      'magnesium',
      'total_phenols',
      'flavanoids',
      'nonflavanoid_phenols',
      'proanthocyanins',
      'color_intensity',
      'hue',
      'od280/od315_of_diluted_wines',
      'proline']}




```python
print(load_wine().DESCR)
```

    .. _wine_dataset:
    
    Wine recognition dataset
    ------------------------
    
    **Data Set Characteristics:**
    
        :Number of Instances: 178
        :Number of Attributes: 13 numeric, predictive attributes and the class
        :Attribute Information:
     		- Alcohol
     		- Malic acid
     		- Ash
    		- Alcalinity of ash  
     		- Magnesium
    		- Total phenols
     		- Flavanoids
     		- Nonflavanoid phenols
     		- Proanthocyanins
    		- Color intensity
     		- Hue
     		- OD280/OD315 of diluted wines
     		- Proline
    
        - class:
                - class_0
                - class_1
                - class_2
    		
        :Summary Statistics:
        
        ============================= ==== ===== ======= =====
                                       Min   Max   Mean     SD
        ============================= ==== ===== ======= =====
        Alcohol:                      11.0  14.8    13.0   0.8
        Malic Acid:                   0.74  5.80    2.34  1.12
        Ash:                          1.36  3.23    2.36  0.27
        Alcalinity of Ash:            10.6  30.0    19.5   3.3
        Magnesium:                    70.0 162.0    99.7  14.3
        Total Phenols:                0.98  3.88    2.29  0.63
        Flavanoids:                   0.34  5.08    2.03  1.00
        Nonflavanoid Phenols:         0.13  0.66    0.36  0.12
        Proanthocyanins:              0.41  3.58    1.59  0.57
        Colour Intensity:              1.3  13.0     5.1   2.3
        Hue:                          0.48  1.71    0.96  0.23
        OD280/OD315 of diluted wines: 1.27  4.00    2.61  0.71
        Proline:                       278  1680     746   315
        ============================= ==== ===== ======= =====
    
        :Missing Attribute Values: None
        :Class Distribution: class_0 (59), class_1 (71), class_2 (48)
        :Creator: R.A. Fisher
        :Donor: Michael Marshall (MARSHALL%PLU@io.arc.nasa.gov)
        :Date: July, 1988
    
    This is a copy of UCI ML Wine recognition datasets.
    https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data
    
    The data is the results of a chemical analysis of wines grown in the same
    region in Italy by three different cultivators. There are thirteen different
    measurements taken for different constituents found in the three types of
    wine.
    
    Original Owners: 
    
    Forina, M. et al, PARVUS - 
    An Extendible Package for Data Exploration, Classification and Correlation. 
    Institute of Pharmaceutical and Food Analysis and Technologies,
    Via Brigata Salerno, 16147 Genoa, Italy.
    
    Citation:
    
    Lichman, M. (2013). UCI Machine Learning Repository
    [https://archive.ics.uci.edu/ml]. Irvine, CA: University of California,
    School of Information and Computer Science. 
    
    .. topic:: References
    
      (1) S. Aeberhard, D. Coomans and O. de Vel, 
      Comparison of Classifiers in High Dimensional Settings, 
      Tech. Rep. no. 92-02, (1992), Dept. of Computer Science and Dept. of  
      Mathematics and Statistics, James Cook University of North Queensland. 
      (Also submitted to Technometrics). 
    
      The data was used with many others for comparing various 
      classifiers. The classes are separable, though only RDA 
      has achieved 100% correct classification. 
      (RDA : 100%, QDA 99.4%, LDA 98.9%, 1NN 96.1% (z-transformed data)) 
      (All results using the leave-one-out technique) 
    
      (2) S. Aeberhard, D. Coomans and O. de Vel, 
      "THE CLASSIFICATION PERFORMANCE OF RDA" 
      Tech. Rep. no. 92-01, (1992), Dept. of Computer Science and Dept. of 
      Mathematics and Statistics, James Cook University of North Queensland. 
      (Also submitted to Journal of Chemometrics).
    
    


```python
wine_data = load_wine()
""" 데이터 셋을 살펴보는 코드
print(wine_data.DESCR)
"""

# 입력 변수를 사용하기 편하게 pandas dataframe으로 변환
X = pd.DataFrame(wine_data.data, columns=wine_data.feature_names)

# 목표 변수를 사용하기 편하게 pandas dataframe으로 변환
y = pd.DataFrame(wine_data.target, columns=['Y/N'])

# 여기에 코드를 작성하세요
train_x, test_x, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=5)
train_y = train_y.values.ravel()
model = LogisticRegression(solver='saga', max_iter=7500)
model.fit(train_x, train_y)
y_test_predict = model.predict(test_x)


# 테스트 코드
score = model.score(test_x, test_y)
y_test_predict, score
```




    (array([0, 1, 0, 0, 2, 2, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0,
            0, 1, 1, 1, 0, 1, 2, 0, 1, 1, 0, 0, 2, 2]),
     0.75)



## <a id='toc1_8_'></a>[수료증](https://www.codeit.kr/certificates/kKUsi-xDMSV-Erbg5-eDxbu) [&#8593;](#toc0_)
