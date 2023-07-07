---
layout: single
title:  "improving ml "
---

**Table of contents**<a id='toc0_'></a>    
- [improve ML performance](#toc1_)    
  - [feature scaling](#toc1_1_)    
    - [min-max normalization](#toc1_1_1_)    
    - [feature scaling이 경사하강법을 빠르게 해주는 이유는 다음과 같다](#toc1_1_2_)    
    - [standardization](#toc1_1_3_)    
    - [One-hot encoding](#toc1_1_4_)    
    - [정규화](#toc1_1_5_)    
      - [편향 분산 트레이드 오프 bias-variance trade off](#toc1_1_5_1_)    
      - [정규화 방법](#toc1_1_5_2_)    
        - [Lasso Regression L1 model](#toc1_1_5_2_1_)    
        - [Ridge Regression L2 model](#toc1_1_5_2_2_)    
  - [cross validation](#toc1_2_)    
    - [K-fold](#toc1_2_1_)    
  - [hyper parameter](#toc1_3_)    
    - [그중 하나의 방법이 grid search다](#toc1_3_1_)    
  - [수료증](#toc1_4_)    

<!-- vscode-jupyter-toc-config
	numbering=false
	anchor=true
	flat=false
	minLevel=1
	maxLevel=6
	/vscode-jupyter-toc-config -->
<!-- THIS CELL WILL BE REPLACED ON TOC UPDATE. DO NOT WRITE YOUR TEXT IN THIS CELL -->

# <a id='toc1_'></a>[improve ML performance](#toc0_)

## <a id='toc1_1_'></a>[feature scaling](#toc0_)
---

입력 변수 크기를 조정해서 거리를 조절한다 >>> 경사하강에 유리

### <a id='toc1_1_1_'></a>[min-max normalization](#toc0_)
---
데이터의 크기를 0~1사이로 바꿔준다  
모든 데이터에서 min 값을 뺀 후 (max-min)으로 나눠준다

![피쳐 스케일링](https://bakey-api.codeit.kr/files/3322/J9jM7c?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-07-30+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+2.22.40.png)

![민맥스](https://bakey-api.codeit.kr/files/3322/YV0KJZ?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-07-30+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+2.23.33.png)


```python
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression, Lasso, LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.metrics import mean_squared_error
from sklearn.datasets import load_iris
from math import sqrt
```


```python
df = pd.read_csv('NBA_player_of_the_week.csv')
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
      <th>Player</th>
      <th>Team</th>
      <th>Conference</th>
      <th>Date</th>
      <th>Position</th>
      <th>Height</th>
      <th>Weight</th>
      <th>Age</th>
      <th>Draft Year</th>
      <th>Seasons in league</th>
      <th>Season</th>
      <th>Season short</th>
      <th>Pre-draft Team</th>
      <th>Real_value</th>
      <th>Height CM</th>
      <th>Weight KG</th>
      <th>Last Season</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jayson Tatum</td>
      <td>Boston Celtics</td>
      <td>East</td>
      <td>Feb 10, 2020</td>
      <td>SF</td>
      <td>6'8</td>
      <td>208</td>
      <td>21</td>
      <td>2017</td>
      <td>2</td>
      <td>2019-2020</td>
      <td>2020</td>
      <td>Duke</td>
      <td>0.5</td>
      <td>203</td>
      <td>94</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Nikola Jokic</td>
      <td>Denver Nuggets</td>
      <td>West</td>
      <td>Feb 10, 2020</td>
      <td>C</td>
      <td>7'0</td>
      <td>250</td>
      <td>25</td>
      <td>2014</td>
      <td>4</td>
      <td>2019-2020</td>
      <td>2020</td>
      <td>KK Mega Bemax (Serbia)</td>
      <td>0.5</td>
      <td>213</td>
      <td>113</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Jaylen Brown</td>
      <td>Boston Celtics</td>
      <td>East</td>
      <td>Feb 3, 2020</td>
      <td>SF</td>
      <td>6'7</td>
      <td>220</td>
      <td>23</td>
      <td>2016</td>
      <td>3</td>
      <td>2019-2020</td>
      <td>2020</td>
      <td>California</td>
      <td>0.5</td>
      <td>201</td>
      <td>99</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Damian Lillard</td>
      <td>Portland Trail Blazers</td>
      <td>West</td>
      <td>Feb 3, 2020</td>
      <td>G</td>
      <td>6'3</td>
      <td>195</td>
      <td>29</td>
      <td>2012</td>
      <td>7</td>
      <td>2019-2020</td>
      <td>2020</td>
      <td>Weber State</td>
      <td>0.5</td>
      <td>190</td>
      <td>88</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Pascal Siakam</td>
      <td>Toronto Raptors</td>
      <td>East</td>
      <td>Jan 27, 2020</td>
      <td>F</td>
      <td>6'9</td>
      <td>230</td>
      <td>25</td>
      <td>2016</td>
      <td>3</td>
      <td>2019-2020</td>
      <td>2020</td>
      <td>New Mexico State</td>
      <td>0.5</td>
      <td>206</td>
      <td>104</td>
      <td>1</td>
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
    </tr>
    <tr>
      <th>1335</th>
      <td>Phil Ford</td>
      <td>Kansas City Kings</td>
      <td>NaN</td>
      <td>Nov 18, 1979</td>
      <td>G</td>
      <td>6'2</td>
      <td>175</td>
      <td>24</td>
      <td>1978</td>
      <td>1</td>
      <td>1979-1980</td>
      <td>1980</td>
      <td>North Carolina</td>
      <td>1.0</td>
      <td>188</td>
      <td>79</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1336</th>
      <td>Magic Johnson</td>
      <td>Los Angeles Lakers</td>
      <td>NaN</td>
      <td>Nov 11, 1979</td>
      <td>PG</td>
      <td>6'9</td>
      <td>255</td>
      <td>20</td>
      <td>1979</td>
      <td>0</td>
      <td>1979-1980</td>
      <td>1980</td>
      <td>Michigan State</td>
      <td>1.0</td>
      <td>206</td>
      <td>115</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1337</th>
      <td>Marques Johnson</td>
      <td>Milwaukee Bucks</td>
      <td>NaN</td>
      <td>Nov 4, 1979</td>
      <td>GF</td>
      <td>6'7</td>
      <td>218</td>
      <td>24</td>
      <td>1977</td>
      <td>2</td>
      <td>1979-1980</td>
      <td>1980</td>
      <td>UCLA</td>
      <td>1.0</td>
      <td>201</td>
      <td>98</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1338</th>
      <td>Micheal Ray Richardson</td>
      <td>New York Knicks</td>
      <td>NaN</td>
      <td>Oct 28, 1979</td>
      <td>PG</td>
      <td>6'5</td>
      <td>189</td>
      <td>24</td>
      <td>1978</td>
      <td>1</td>
      <td>1979-1980</td>
      <td>1980</td>
      <td>Montana</td>
      <td>1.0</td>
      <td>196</td>
      <td>85</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1339</th>
      <td>Julius Erving</td>
      <td>Philadelphia Sixers</td>
      <td>NaN</td>
      <td>Oct 21, 1979</td>
      <td>SF</td>
      <td>6'6</td>
      <td>200</td>
      <td>30</td>
      <td>1972</td>
      <td>7</td>
      <td>1979-1980</td>
      <td>1980</td>
      <td>Massachusetts</td>
      <td>1.0</td>
      <td>198</td>
      <td>90</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>1340 rows × 17 columns</p>
</div>




```python
df.describe()
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
      <th>Weight</th>
      <th>Age</th>
      <th>Draft Year</th>
      <th>Seasons in league</th>
      <th>Season short</th>
      <th>Real_value</th>
      <th>Height CM</th>
      <th>Weight KG</th>
      <th>Last Season</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>1340.000000</td>
      <td>1340.000000</td>
      <td>1340.000000</td>
      <td>1340.000000</td>
      <td>1340.000000</td>
      <td>1340.000000</td>
      <td>1340.000000</td>
      <td>1340.000000</td>
      <td>1340.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>224.567164</td>
      <td>26.738060</td>
      <td>1996.287313</td>
      <td>5.740299</td>
      <td>2003.156716</td>
      <td>0.686940</td>
      <td>201.071642</td>
      <td>101.384328</td>
      <td>0.023881</td>
    </tr>
    <tr>
      <th>std</th>
      <td>30.798885</td>
      <td>3.400683</td>
      <td>11.253558</td>
      <td>3.293421</td>
      <td>11.470164</td>
      <td>0.242007</td>
      <td>9.367970</td>
      <td>14.011226</td>
      <td>0.152734</td>
    </tr>
    <tr>
      <th>min</th>
      <td>150.000000</td>
      <td>19.000000</td>
      <td>1965.000000</td>
      <td>0.000000</td>
      <td>1980.000000</td>
      <td>0.500000</td>
      <td>175.000000</td>
      <td>68.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>205.000000</td>
      <td>24.000000</td>
      <td>1987.000000</td>
      <td>3.000000</td>
      <td>1994.000000</td>
      <td>0.500000</td>
      <td>193.000000</td>
      <td>93.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>220.000000</td>
      <td>26.000000</td>
      <td>1998.000000</td>
      <td>5.000000</td>
      <td>2005.000000</td>
      <td>0.500000</td>
      <td>201.000000</td>
      <td>99.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>250.000000</td>
      <td>29.000000</td>
      <td>2005.000000</td>
      <td>8.000000</td>
      <td>2013.000000</td>
      <td>1.000000</td>
      <td>208.000000</td>
      <td>113.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>325.000000</td>
      <td>40.000000</td>
      <td>2018.000000</td>
      <td>17.000000</td>
      <td>2020.000000</td>
      <td>1.000000</td>
      <td>229.000000</td>
      <td>147.000000</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
hwa = df[['Age', 'Height CM', 'Weight KG']]
```


```python
hwa.head()
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
      <th>Age</th>
      <th>Height CM</th>
      <th>Weight KG</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>21</td>
      <td>203</td>
      <td>94</td>
    </tr>
    <tr>
      <th>1</th>
      <td>25</td>
      <td>213</td>
      <td>113</td>
    </tr>
    <tr>
      <th>2</th>
      <td>23</td>
      <td>201</td>
      <td>99</td>
    </tr>
    <tr>
      <th>3</th>
      <td>29</td>
      <td>190</td>
      <td>88</td>
    </tr>
    <tr>
      <th>4</th>
      <td>25</td>
      <td>206</td>
      <td>104</td>
    </tr>
  </tbody>
</table>
</div>




```python
scaler = preprocessing.MinMaxScaler()
```


```python
n_hwa=scaler.fit_transform(hwa)
```


```python
n_hwa
```




    array([[0.0952381 , 0.51851852, 0.32911392],
           [0.28571429, 0.7037037 , 0.56962025],
           [0.19047619, 0.48148148, 0.39240506],
           ...,
           [0.23809524, 0.48148148, 0.37974684],
           [0.23809524, 0.38888889, 0.21518987],
           [0.52380952, 0.42592593, 0.27848101]])




```python
nor_hwa = pd.DataFrame(n_hwa, columns=['Height', 'Weight', 'Age'])
```


```python
nor_hwa
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
      <th>Height</th>
      <th>Weight</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.095238</td>
      <td>0.518519</td>
      <td>0.329114</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.285714</td>
      <td>0.703704</td>
      <td>0.569620</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.190476</td>
      <td>0.481481</td>
      <td>0.392405</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.476190</td>
      <td>0.277778</td>
      <td>0.253165</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.285714</td>
      <td>0.574074</td>
      <td>0.455696</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1335</th>
      <td>0.238095</td>
      <td>0.240741</td>
      <td>0.139241</td>
    </tr>
    <tr>
      <th>1336</th>
      <td>0.047619</td>
      <td>0.574074</td>
      <td>0.594937</td>
    </tr>
    <tr>
      <th>1337</th>
      <td>0.238095</td>
      <td>0.481481</td>
      <td>0.379747</td>
    </tr>
    <tr>
      <th>1338</th>
      <td>0.238095</td>
      <td>0.388889</td>
      <td>0.215190</td>
    </tr>
    <tr>
      <th>1339</th>
      <td>0.523810</td>
      <td>0.425926</td>
      <td>0.278481</td>
    </tr>
  </tbody>
</table>
<p>1340 rows × 3 columns</p>
</div>




```python
nor_hwa.describe()
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
      <th>Height</th>
      <th>Weight</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>1340.000000</td>
      <td>1340.000000</td>
      <td>1340.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.368479</td>
      <td>0.482808</td>
      <td>0.422586</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.161937</td>
      <td>0.173481</td>
      <td>0.177357</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>0.238095</td>
      <td>0.333333</td>
      <td>0.316456</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.333333</td>
      <td>0.481481</td>
      <td>0.392405</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.476190</td>
      <td>0.611111</td>
      <td>0.569620</td>
    </tr>
    <tr>
      <th>max</th>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>



### <a id='toc1_1_2_'></a>[feature scaling이 경사하강법을 빠르게 해주는 이유는 다음과 같다](#toc0_)
---

경사하강법은 손실이 최소인 지점을 찾기 위해 기울기(벡터)를 이용한다  
높이가 같은 지점에 등고선을 그리면 다음과 같이 된다

![등고선](https://bakey-api.codeit.kr/files/3332/ZG7hhJ?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-07-30+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+2.50.17.png)


등고선에서 가장 가파르게 내려가는 방향은 등고선과 수직인 방향으로 가는 길이다
![등고선2](https://bakey-api.codeit.kr/files/3332/BJiEpz?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-07-30+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+3.17.50.png)


만약 입력값의 단위가 너무 큰 차이가 난다면 개별 상수의 영향(아웃풋)도 큰 차이가 난다
![등고선3](https://bakey-api.codeit.kr/files/3332/7weEap?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-07-30+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+3.20.42.png)
![등고선4](https://bakey-api.codeit.kr/files/3332/QJliqb?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-07-30+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+3.13.32.png)

이렇게 되면 등고선에 수직인 방향으로 움직일 때 비효율적이다
![등고선5](https://bakey-api.codeit.kr/files/3332/2lmYch?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-07-30+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+3.14.09.png)

입력값의 단위를 통일하면 개별 상수의 영향이 동일해지고 따라서 등고선에 직각인 방향이 최소점을 향한다
![등고선6](https://bakey-api.codeit.kr/files/3332/73joXG?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-07-30+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+3.14.18.png)

### <a id='toc1_1_3_'></a>[standardization](#toc0_)
---

feature scaling 방법 중 표준화를 이용할 수도 있다

평균을 빼고 표준편차로 나눠서 z-score로 만드는 방법  
평균은 0 표준편차는 1인 분포로 만든다


```python
scaler = preprocessing.StandardScaler()
```


```python
standardized = scaler.fit_transform(hwa)
```


```python
standardized
```




    array([[-1.68795564,  0.20592274, -0.52722617],
           [-0.51128218,  1.27378837,  0.82933556],
           [-1.09961891, -0.00765038, -0.17023624],
           ...,
           [-0.80545055, -0.00765038, -0.24163423],
           [-0.80545055, -0.54158319, -1.16980804],
           [ 0.95955965, -0.32801007, -0.81281811]])




```python
stand_df = pd.DataFrame(standardized, columns=['Height', 'Weight', 'Age'])
```


```python
stand_df
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
      <th>Height</th>
      <th>Weight</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-1.687956</td>
      <td>0.205923</td>
      <td>-0.527226</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.511282</td>
      <td>1.273788</td>
      <td>0.829336</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-1.099619</td>
      <td>-0.007650</td>
      <td>-0.170236</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.665391</td>
      <td>-1.182303</td>
      <td>-0.955614</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-0.511282</td>
      <td>0.526282</td>
      <td>0.186754</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1335</th>
      <td>-0.805451</td>
      <td>-1.395876</td>
      <td>-1.598196</td>
    </tr>
    <tr>
      <th>1336</th>
      <td>-1.982124</td>
      <td>0.526282</td>
      <td>0.972132</td>
    </tr>
    <tr>
      <th>1337</th>
      <td>-0.805451</td>
      <td>-0.007650</td>
      <td>-0.241634</td>
    </tr>
    <tr>
      <th>1338</th>
      <td>-0.805451</td>
      <td>-0.541583</td>
      <td>-1.169808</td>
    </tr>
    <tr>
      <th>1339</th>
      <td>0.959560</td>
      <td>-0.328010</td>
      <td>-0.812818</td>
    </tr>
  </tbody>
</table>
<p>1340 rows × 3 columns</p>
</div>




```python
pd.set_option('display.float_format', lambda x: '%.5f' % x)
stand_df.describe()
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
      <th>Height</th>
      <th>Weight</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>1340.00000</td>
      <td>1340.00000</td>
      <td>1340.00000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>-0.00000</td>
      <td>-0.00000</td>
      <td>-0.00000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.00037</td>
      <td>1.00037</td>
      <td>1.00037</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-2.27629</td>
      <td>-2.78410</td>
      <td>-2.38357</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.80545</td>
      <td>-0.86194</td>
      <td>-0.59862</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>-0.21711</td>
      <td>-0.00765</td>
      <td>-0.17024</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.66539</td>
      <td>0.73986</td>
      <td>0.82934</td>
    </tr>
    <tr>
      <th>max</th>
      <td>3.90124</td>
      <td>2.98237</td>
      <td>3.25687</td>
    </tr>
  </tbody>
</table>
</div>




```python
example_1 = [25, 49, 32, 35, 40]
preprocessing.MinMaxScaler().fit_transform(pd.DataFrame(example_1))
```




    array([[0.        ],
           [1.        ],
           [0.29166667],
           [0.41666667],
           [0.625     ]])




```python
example_2 = [25, 35, 30, 50, 35]
preprocessing.MinMaxScaler().fit_transform(pd.DataFrame(example_2))
```




    array([[0. ],
           [0.4],
           [0.2],
           [1. ],
           [0.4]])



### <a id='toc1_1_4_'></a>[One-hot encoding](#toc0_)
---
numerical >>> categorical로 바꾸는 방법

데이터는 크게 둘로 나뉜다
- numerical data
- categorical data

ML은 numerical 인풋이 필요하다

범주형 데이터는 수치로 바꿔주면 된다

그러나 마냥 숫자를 나열해서 부여하면 크고 작음이 생겨서 머신 러닝에 방해가 될 수 있다


![범주형](https://bakey-api.codeit.kr/files/3355/eCXdLK?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-07-30+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+9.31.05.png)

원핫인코딩은 개별 범주를 다 열(feature)로 만들고 여부에 따라 1, 0으로 만든다


![원핫](https://bakey-api.codeit.kr/files/3355/JUFji2?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-07-30+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+9.38.37.png)


```python
df = pd.read_csv('titanic.csv')
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
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.00000</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.25000</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.00000</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.28330</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.00000</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.92500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.00000</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.10000</td>
      <td>C123</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.00000</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.05000</td>
      <td>NaN</td>
      <td>S</td>
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
    </tr>
    <tr>
      <th>886</th>
      <td>887</td>
      <td>0</td>
      <td>2</td>
      <td>Montvila, Rev. Juozas</td>
      <td>male</td>
      <td>27.00000</td>
      <td>0</td>
      <td>0</td>
      <td>211536</td>
      <td>13.00000</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>887</th>
      <td>888</td>
      <td>1</td>
      <td>1</td>
      <td>Graham, Miss. Margaret Edith</td>
      <td>female</td>
      <td>19.00000</td>
      <td>0</td>
      <td>0</td>
      <td>112053</td>
      <td>30.00000</td>
      <td>B42</td>
      <td>S</td>
    </tr>
    <tr>
      <th>888</th>
      <td>889</td>
      <td>0</td>
      <td>3</td>
      <td>Johnston, Miss. Catherine Helen "Carrie"</td>
      <td>female</td>
      <td>NaN</td>
      <td>1</td>
      <td>2</td>
      <td>W./C. 6607</td>
      <td>23.45000</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>889</th>
      <td>890</td>
      <td>1</td>
      <td>1</td>
      <td>Behr, Mr. Karl Howell</td>
      <td>male</td>
      <td>26.00000</td>
      <td>0</td>
      <td>0</td>
      <td>111369</td>
      <td>30.00000</td>
      <td>C148</td>
      <td>C</td>
    </tr>
    <tr>
      <th>890</th>
      <td>891</td>
      <td>0</td>
      <td>3</td>
      <td>Dooley, Mr. Patrick</td>
      <td>male</td>
      <td>32.00000</td>
      <td>0</td>
      <td>0</td>
      <td>370376</td>
      <td>7.75000</td>
      <td>NaN</td>
      <td>Q</td>
    </tr>
  </tbody>
</table>
<p>891 rows × 12 columns</p>
</div>




```python
eb = df[['Sex', 'Embarked']]
eb
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
      <th>Sex</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>male</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>female</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>female</td>
      <td>S</td>
    </tr>
    <tr>
      <th>3</th>
      <td>female</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>male</td>
      <td>S</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>886</th>
      <td>male</td>
      <td>S</td>
    </tr>
    <tr>
      <th>887</th>
      <td>female</td>
      <td>S</td>
    </tr>
    <tr>
      <th>888</th>
      <td>female</td>
      <td>S</td>
    </tr>
    <tr>
      <th>889</th>
      <td>male</td>
      <td>C</td>
    </tr>
    <tr>
      <th>890</th>
      <td>male</td>
      <td>Q</td>
    </tr>
  </tbody>
</table>
<p>891 rows × 2 columns</p>
</div>




```python
hot = pd.get_dummies(eb)
hot
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
      <th>Sex_female</th>
      <th>Sex_male</th>
      <th>Embarked_C</th>
      <th>Embarked_Q</th>
      <th>Embarked_S</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>4</th>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>886</th>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>887</th>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>888</th>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>889</th>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>890</th>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
<p>891 rows × 5 columns</p>
</div>




```python
hotdf = pd.get_dummies(data=df, columns=['Sex', 'Embarked'])
hotdf
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
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Sex_female</th>
      <th>Sex_male</th>
      <th>Embarked_C</th>
      <th>Embarked_Q</th>
      <th>Embarked_S</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>22.00000</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.25000</td>
      <td>NaN</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>38.00000</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.28330</td>
      <td>C85</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>26.00000</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.92500</td>
      <td>NaN</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>35.00000</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.10000</td>
      <td>C123</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>35.00000</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.05000</td>
      <td>NaN</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
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
    </tr>
    <tr>
      <th>886</th>
      <td>887</td>
      <td>0</td>
      <td>2</td>
      <td>Montvila, Rev. Juozas</td>
      <td>27.00000</td>
      <td>0</td>
      <td>0</td>
      <td>211536</td>
      <td>13.00000</td>
      <td>NaN</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>887</th>
      <td>888</td>
      <td>1</td>
      <td>1</td>
      <td>Graham, Miss. Margaret Edith</td>
      <td>19.00000</td>
      <td>0</td>
      <td>0</td>
      <td>112053</td>
      <td>30.00000</td>
      <td>B42</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>888</th>
      <td>889</td>
      <td>0</td>
      <td>3</td>
      <td>Johnston, Miss. Catherine Helen "Carrie"</td>
      <td>NaN</td>
      <td>1</td>
      <td>2</td>
      <td>W./C. 6607</td>
      <td>23.45000</td>
      <td>NaN</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>889</th>
      <td>890</td>
      <td>1</td>
      <td>1</td>
      <td>Behr, Mr. Karl Howell</td>
      <td>26.00000</td>
      <td>0</td>
      <td>0</td>
      <td>111369</td>
      <td>30.00000</td>
      <td>C148</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>890</th>
      <td>891</td>
      <td>0</td>
      <td>3</td>
      <td>Dooley, Mr. Patrick</td>
      <td>32.00000</td>
      <td>0</td>
      <td>0</td>
      <td>370376</td>
      <td>7.75000</td>
      <td>NaN</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
<p>891 rows × 15 columns</p>
</div>



### <a id='toc1_1_5_'></a>[정규화](#toc0_)
---
- 편향 Bias
- 분산 Variance

직선으로 만든 모델은 곡선을 못 잡아낸다 >>> 편향이 크다  


![직선](https://bakey-api.codeit.kr/files/3339/Pw3o1T?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-07-30+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+4.44.36.png)

그러나 편향이 극단적으로 낮은 모델은 분산이 높다 >>> 실전 데이터에서 잘 못 맞춘다


![편향0](https://bakey-api.codeit.kr/files/3339/XseRG7?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-07-30+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+4.33.47.png)

- 편향이 높다 : train set에서 높은 점수를 얻지 못한다 underfit
- 분산이 높다 : data set 마다 나오는 점수 차가 크다 (train에 특화됐다 overfit)
- 편향이 낮으면서도 분산이 낮은 모델이 짱

![적당](https://bakey-api.codeit.kr/files/3343/iOPSBe?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-07-30+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+4.26.03.png)

- 그러나 둘은 트레이드 오프 관계에 있다

#### <a id='toc1_1_5_1_'></a>[편향 분산 트레이드 오프 bias-variance trade off](#toc0_)
---
편향이 낮게 하려면 일단 다항식의 모델로 적용해보면 된다


```python
df = pd.read_csv('admission_data.csv')
df = df.drop('Serial No.', axis=1)
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
      <th>GRE Score</th>
      <th>TOEFL Score</th>
      <th>University Rating</th>
      <th>SOP</th>
      <th>LOR</th>
      <th>CGPA</th>
      <th>Research</th>
      <th>Chance of Admit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>337</td>
      <td>118</td>
      <td>4</td>
      <td>4.5</td>
      <td>4.5</td>
      <td>9.65</td>
      <td>1</td>
      <td>0.92</td>
    </tr>
    <tr>
      <th>1</th>
      <td>324</td>
      <td>107</td>
      <td>4</td>
      <td>4.0</td>
      <td>4.5</td>
      <td>8.87</td>
      <td>1</td>
      <td>0.76</td>
    </tr>
    <tr>
      <th>2</th>
      <td>316</td>
      <td>104</td>
      <td>3</td>
      <td>3.0</td>
      <td>3.5</td>
      <td>8.00</td>
      <td>1</td>
      <td>0.72</td>
    </tr>
    <tr>
      <th>3</th>
      <td>322</td>
      <td>110</td>
      <td>3</td>
      <td>3.5</td>
      <td>2.5</td>
      <td>8.67</td>
      <td>1</td>
      <td>0.80</td>
    </tr>
    <tr>
      <th>4</th>
      <td>314</td>
      <td>103</td>
      <td>2</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>8.21</td>
      <td>0</td>
      <td>0.65</td>
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
      <th>495</th>
      <td>332</td>
      <td>108</td>
      <td>5</td>
      <td>4.5</td>
      <td>4.0</td>
      <td>9.02</td>
      <td>1</td>
      <td>0.87</td>
    </tr>
    <tr>
      <th>496</th>
      <td>337</td>
      <td>117</td>
      <td>5</td>
      <td>5.0</td>
      <td>5.0</td>
      <td>9.87</td>
      <td>1</td>
      <td>0.96</td>
    </tr>
    <tr>
      <th>497</th>
      <td>330</td>
      <td>120</td>
      <td>5</td>
      <td>4.5</td>
      <td>5.0</td>
      <td>9.56</td>
      <td>1</td>
      <td>0.93</td>
    </tr>
    <tr>
      <th>498</th>
      <td>312</td>
      <td>103</td>
      <td>4</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>8.43</td>
      <td>0</td>
      <td>0.73</td>
    </tr>
    <tr>
      <th>499</th>
      <td>327</td>
      <td>113</td>
      <td>4</td>
      <td>4.5</td>
      <td>4.5</td>
      <td>9.04</td>
      <td>0</td>
      <td>0.84</td>
    </tr>
  </tbody>
</table>
<p>500 rows × 8 columns</p>
</div>




```python
X = df.drop(['Chance of Admit '], axis=1)
```


```python
poly_transformer = preprocessing.PolynomialFeatures(6)
poly_features = poly_transformer.fit_transform(X.values)
feature_names = poly_transformer.get_feature_names_out(X.columns)
```


```python
X = pd.DataFrame(poly_features, columns=feature_names)
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
      <th>1</th>
      <th>GRE Score</th>
      <th>TOEFL Score</th>
      <th>University Rating</th>
      <th>SOP</th>
      <th>LOR</th>
      <th>CGPA</th>
      <th>Research</th>
      <th>GRE Score^2</th>
      <th>GRE Score TOEFL Score</th>
      <th>...</th>
      <th>LOR  CGPA^2 Research^3</th>
      <th>LOR  CGPA Research^4</th>
      <th>LOR  Research^5</th>
      <th>CGPA^6</th>
      <th>CGPA^5 Research</th>
      <th>CGPA^4 Research^2</th>
      <th>CGPA^3 Research^3</th>
      <th>CGPA^2 Research^4</th>
      <th>CGPA Research^5</th>
      <th>Research^6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>337.0</td>
      <td>118.0</td>
      <td>4.0</td>
      <td>4.5</td>
      <td>4.5</td>
      <td>9.65</td>
      <td>1.0</td>
      <td>113569.0</td>
      <td>39766.0</td>
      <td>...</td>
      <td>419.05125</td>
      <td>43.425</td>
      <td>4.5</td>
      <td>807539.696082</td>
      <td>83682.870060</td>
      <td>8671.800006</td>
      <td>898.632125</td>
      <td>93.1225</td>
      <td>9.65</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.0</td>
      <td>324.0</td>
      <td>107.0</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>4.5</td>
      <td>8.87</td>
      <td>1.0</td>
      <td>104976.0</td>
      <td>34668.0</td>
      <td>...</td>
      <td>354.04605</td>
      <td>39.915</td>
      <td>4.5</td>
      <td>487014.306256</td>
      <td>54905.784245</td>
      <td>6190.054594</td>
      <td>697.864103</td>
      <td>78.6769</td>
      <td>8.87</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.0</td>
      <td>316.0</td>
      <td>104.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.5</td>
      <td>8.00</td>
      <td>1.0</td>
      <td>99856.0</td>
      <td>32864.0</td>
      <td>...</td>
      <td>224.00000</td>
      <td>28.000</td>
      <td>3.5</td>
      <td>262144.000000</td>
      <td>32768.000000</td>
      <td>4096.000000</td>
      <td>512.000000</td>
      <td>64.0000</td>
      <td>8.00</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.0</td>
      <td>322.0</td>
      <td>110.0</td>
      <td>3.0</td>
      <td>3.5</td>
      <td>2.5</td>
      <td>8.67</td>
      <td>1.0</td>
      <td>103684.0</td>
      <td>35420.0</td>
      <td>...</td>
      <td>187.92225</td>
      <td>21.675</td>
      <td>2.5</td>
      <td>424731.610940</td>
      <td>48988.651781</td>
      <td>5650.363527</td>
      <td>651.714363</td>
      <td>75.1689</td>
      <td>8.67</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.0</td>
      <td>314.0</td>
      <td>103.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>8.21</td>
      <td>0.0</td>
      <td>98596.0</td>
      <td>32342.0</td>
      <td>...</td>
      <td>0.00000</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>306237.903347</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0000</td>
      <td>0.00</td>
      <td>0.0</td>
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
      <th>495</th>
      <td>1.0</td>
      <td>332.0</td>
      <td>108.0</td>
      <td>5.0</td>
      <td>4.5</td>
      <td>4.0</td>
      <td>9.02</td>
      <td>1.0</td>
      <td>110224.0</td>
      <td>35856.0</td>
      <td>...</td>
      <td>325.44160</td>
      <td>36.080</td>
      <td>4.0</td>
      <td>538566.362835</td>
      <td>59708.022487</td>
      <td>6619.514688</td>
      <td>733.870808</td>
      <td>81.3604</td>
      <td>9.02</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>496</th>
      <td>1.0</td>
      <td>337.0</td>
      <td>117.0</td>
      <td>5.0</td>
      <td>5.0</td>
      <td>5.0</td>
      <td>9.87</td>
      <td>1.0</td>
      <td>113569.0</td>
      <td>39429.0</td>
      <td>...</td>
      <td>487.08450</td>
      <td>49.350</td>
      <td>5.0</td>
      <td>924491.486192</td>
      <td>93666.817243</td>
      <td>9490.052406</td>
      <td>961.504803</td>
      <td>97.4169</td>
      <td>9.87</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>497</th>
      <td>1.0</td>
      <td>330.0</td>
      <td>120.0</td>
      <td>5.0</td>
      <td>4.5</td>
      <td>5.0</td>
      <td>9.56</td>
      <td>1.0</td>
      <td>108900.0</td>
      <td>39600.0</td>
      <td>...</td>
      <td>456.96800</td>
      <td>47.800</td>
      <td>5.0</td>
      <td>763391.559199</td>
      <td>79852.673556</td>
      <td>8352.790121</td>
      <td>873.722816</td>
      <td>91.3936</td>
      <td>9.56</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>498</th>
      <td>1.0</td>
      <td>312.0</td>
      <td>103.0</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>8.43</td>
      <td>0.0</td>
      <td>97344.0</td>
      <td>32136.0</td>
      <td>...</td>
      <td>0.00000</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>358893.380131</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0000</td>
      <td>0.00</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>499</th>
      <td>1.0</td>
      <td>327.0</td>
      <td>113.0</td>
      <td>4.0</td>
      <td>4.5</td>
      <td>4.5</td>
      <td>9.04</td>
      <td>0.0</td>
      <td>106929.0</td>
      <td>36951.0</td>
      <td>...</td>
      <td>0.00000</td>
      <td>0.000</td>
      <td>0.0</td>
      <td>545771.160236</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0000</td>
      <td>0.00</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>500 rows × 1716 columns</p>
</div>




```python
y = df[['Chance of Admit ']]
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
      <th>Chance of Admit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.92</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.76</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.72</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.80</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.65</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>495</th>
      <td>0.87</td>
    </tr>
    <tr>
      <th>496</th>
      <td>0.96</td>
    </tr>
    <tr>
      <th>497</th>
      <td>0.93</td>
    </tr>
    <tr>
      <th>498</th>
      <td>0.73</td>
    </tr>
    <tr>
      <th>499</th>
      <td>0.84</td>
    </tr>
  </tbody>
</table>
<p>500 rows × 1 columns</p>
</div>




```python
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3, random_state=5)
```


```python
model = LinearRegression()
model.fit(train_X, train_y)
```




<style>#sk-container-id-1 {color: black;background-color: white;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id="sk-container-id-1" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>LinearRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-1" type="checkbox" checked><label for="sk-estimator-id-1" class="sk-toggleable__label sk-toggleable__label-arrow">LinearRegression</label><div class="sk-toggleable__content"><pre>LinearRegression()</pre></div></div></div></div></div>




```python
y_train_predict = model.predict(train_X)
y_test_predict = model.predict(test_X)
```


```python
print(mean_squared_error(train_y, y_train_predict)**0.5)
print(mean_squared_error(test_y, y_test_predict)**0.5)
```

    0.0015048003392799018
    5.090714856973493
    

과적합이 됐다

#### <a id='toc1_1_5_2_'></a>[정규화 방법](#toc0_)
---
가설 함수의 theta 값이 너무 커지지 않게 함으로써 과적합을 방지


![정규화](https://bakey-api.codeit.kr/files/3347/PFtONJ?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-07-30+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+4.55.08.png)

##### <a id='toc1_1_5_2_1_'></a>[Lasso Regression L1 model](#toc0_)
---

손실 함수에 절대값 theta의 합을 더한 걸 손실 함수로 삼는다. 손실함수를 최소화하려는 노력에서 자연히 theta 값이 커지는 걸 막는다

##### <a id='toc1_1_5_2_2_'></a>[Ridge Regression L2 model](#toc0_)
---

L1과 대체로 동일하되 절대값 theta의 합이 아니라 theta 제곱의 합을 더한다

L1, L2 모두 theta의 합에 임의의 무게값 lambda를 부여한다(sklearn에선 alpha 매개변수) 값이 클수록 theta 크기에 대한 패널티를 크게 주는 거다

**왜 overfit일 때 theta가 큰 게 원인이라는 거지?**


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
      <th>GRE Score</th>
      <th>TOEFL Score</th>
      <th>University Rating</th>
      <th>SOP</th>
      <th>LOR</th>
      <th>CGPA</th>
      <th>Research</th>
      <th>Chance of Admit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>337</td>
      <td>118</td>
      <td>4</td>
      <td>4.5</td>
      <td>4.5</td>
      <td>9.65</td>
      <td>1</td>
      <td>0.92</td>
    </tr>
    <tr>
      <th>1</th>
      <td>324</td>
      <td>107</td>
      <td>4</td>
      <td>4.0</td>
      <td>4.5</td>
      <td>8.87</td>
      <td>1</td>
      <td>0.76</td>
    </tr>
    <tr>
      <th>2</th>
      <td>316</td>
      <td>104</td>
      <td>3</td>
      <td>3.0</td>
      <td>3.5</td>
      <td>8.00</td>
      <td>1</td>
      <td>0.72</td>
    </tr>
    <tr>
      <th>3</th>
      <td>322</td>
      <td>110</td>
      <td>3</td>
      <td>3.5</td>
      <td>2.5</td>
      <td>8.67</td>
      <td>1</td>
      <td>0.80</td>
    </tr>
    <tr>
      <th>4</th>
      <td>314</td>
      <td>103</td>
      <td>2</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>8.21</td>
      <td>0</td>
      <td>0.65</td>
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
      <th>495</th>
      <td>332</td>
      <td>108</td>
      <td>5</td>
      <td>4.5</td>
      <td>4.0</td>
      <td>9.02</td>
      <td>1</td>
      <td>0.87</td>
    </tr>
    <tr>
      <th>496</th>
      <td>337</td>
      <td>117</td>
      <td>5</td>
      <td>5.0</td>
      <td>5.0</td>
      <td>9.87</td>
      <td>1</td>
      <td>0.96</td>
    </tr>
    <tr>
      <th>497</th>
      <td>330</td>
      <td>120</td>
      <td>5</td>
      <td>4.5</td>
      <td>5.0</td>
      <td>9.56</td>
      <td>1</td>
      <td>0.93</td>
    </tr>
    <tr>
      <th>498</th>
      <td>312</td>
      <td>103</td>
      <td>4</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>8.43</td>
      <td>0</td>
      <td>0.73</td>
    </tr>
    <tr>
      <th>499</th>
      <td>327</td>
      <td>113</td>
      <td>4</td>
      <td>4.5</td>
      <td>4.5</td>
      <td>9.04</td>
      <td>0</td>
      <td>0.84</td>
    </tr>
  </tbody>
</table>
<p>500 rows × 8 columns</p>
</div>




```python
model = Lasso(alpha=0.001, max_iter=1000)
```


```python
model.fit(train_X, train_y)
```

    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 5.132e-01, tolerance: 7.568e-04
      model = cd_fast.enet_coordinate_descent(
    




<style>#sk-container-id-2 {color: black;background-color: white;}#sk-container-id-2 pre{padding: 0;}#sk-container-id-2 div.sk-toggleable {background-color: white;}#sk-container-id-2 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-2 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-2 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-2 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-2 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-2 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-2 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-2 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-container-id-2 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-2 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-2 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-2 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-2 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-2 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-2 div.sk-item {position: relative;z-index: 1;}#sk-container-id-2 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-2 div.sk-item::before, #sk-container-id-2 div.sk-parallel-item::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-2 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-2 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-2 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-2 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-2 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-2 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-2 div.sk-label-container {text-align: center;}#sk-container-id-2 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-2 div.sk-text-repr-fallback {display: none;}</style><div id="sk-container-id-2" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>Lasso(alpha=0.001)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-2" type="checkbox" checked><label for="sk-estimator-id-2" class="sk-toggleable__label sk-toggleable__label-arrow">Lasso</label><div class="sk-toggleable__content"><pre>Lasso(alpha=0.001)</pre></div></div></div></div></div>




```python
y_train_predict = model.predict(train_X)
y_test_predict = model.predict(test_X)
```


```python
print(mean_squared_error(train_y, y_train_predict)**0.5)
print(mean_squared_error(test_y, y_test_predict)**0.5)
```

    0.05389371888907576
    0.06689735278061709
    

과적합이 해결됐다

LogisticRegression은 기본적으로 L2 정규화를 적용한다

LogisticRegression(penalty='none')  # 정규화 사용 안함  
LogisticRegression(penalty='l1')  # L1 정규화 사용  
LogisticRegression(penalty='l2')  # L2 정규화 사용  
LogisticRegression()  # 위와 똑같음: L2 정규화 사용

## <a id='toc1_2_'></a>[cross validation](#toc0_)
---

train-test split의 부작용은 test가 하나 뿐이라는 점  
그러므로 교차검증을 사용해 테스트를 여러번 한다

### <a id='toc1_2_1_'></a>[K-fold](#toc0_)
데이터 셋을 k개로 나눈 후 그 중 하나를 테스트 셋으로 삼는다  
돌아가면서 모두 테스트 셋으로 삼는다 >>> k개의 테스트 셋, k 번의 검증 >>> k겹 교차검증이라 부른다

![k](https://bakey-api.codeit.kr/files/3334/6bi8xf?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-07-30+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+4.12.22.png)

![kk](https://bakey-api.codeit.kr/files/3334/OxiaZU?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-07-30+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+4.12.35.png)

![kkk](https://bakey-api.codeit.kr/files/3334/8TZBo1?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-07-30+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+4.12.44.png)

여기서 '성능'이란 아직 설명되지 않았으나 머신러닝 모델을 평가하는 여러 성능지표가 사용 가능한 걸로 보인다

https://scikit-learn.org/stable/modules/cross_validation.html#


```python
iris = load_iris()
iris
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
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.DataFrame(iris.target, columns=['Class'])
```


```python
model = LogisticRegression(max_iter=2000)
```

cv 가 몇겹으로 할지를 정한다 (cross validation의 약자인가)


```python
### test train split 대신 k겹 교차를 한다
cross_val_score(model, X, y.values.ravel(), cv=5)
```




    array([0.96666667, 1.        , 0.93333333, 0.96666667, 1.        ])



모델 성능이 좋다는 건 나왔다  
그럼 이제 모델한테 뭔가 먹여서 결과값을 뽑아야 하는데 그건 어떻게 하지?

## <a id='toc1_3_'></a>[hyper parameter](#toc0_)
---
예를 들어 Lasso 모델을 쓸 때 alpha (lambda를 정하는)라는 파라미터에 값을 지정해주는데 이렇게 사람이 직접 넣어주는 매개변수를 hyper parameter라고 한다  
하이퍼 파라미터에 어떤 값을 넣느냐가 모델의 성능을 좌우한다 따라서 어떤 값을 넣을지 최적화하는 방법을 찾아야 한다

### <a id='toc1_3_1_'></a>[그중 하나의 방법이 grid search다](#toc0_)

후보값을 나열하고 후보를 모두 넣은 다음 grid를 만들어서 개별로 성능을 평가한다  
brute force 같은데?


![그리드](https://bakey-api.codeit.kr/files/3342/ToOUpV?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-07-30+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+4.26.44.png)

비교하는 값은 손실함수의 값으로 작을수록 좋다


```python
df = pd.read_csv('admission_data.csv')
df = df.drop('Serial No.', axis=1)
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
      <th>GRE Score</th>
      <th>TOEFL Score</th>
      <th>University Rating</th>
      <th>SOP</th>
      <th>LOR</th>
      <th>CGPA</th>
      <th>Research</th>
      <th>Chance of Admit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>337</td>
      <td>118</td>
      <td>4</td>
      <td>4.5</td>
      <td>4.5</td>
      <td>9.65</td>
      <td>1</td>
      <td>0.92</td>
    </tr>
    <tr>
      <th>1</th>
      <td>324</td>
      <td>107</td>
      <td>4</td>
      <td>4.0</td>
      <td>4.5</td>
      <td>8.87</td>
      <td>1</td>
      <td>0.76</td>
    </tr>
    <tr>
      <th>2</th>
      <td>316</td>
      <td>104</td>
      <td>3</td>
      <td>3.0</td>
      <td>3.5</td>
      <td>8.00</td>
      <td>1</td>
      <td>0.72</td>
    </tr>
    <tr>
      <th>3</th>
      <td>322</td>
      <td>110</td>
      <td>3</td>
      <td>3.5</td>
      <td>2.5</td>
      <td>8.67</td>
      <td>1</td>
      <td>0.80</td>
    </tr>
    <tr>
      <th>4</th>
      <td>314</td>
      <td>103</td>
      <td>2</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>8.21</td>
      <td>0</td>
      <td>0.65</td>
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
      <th>495</th>
      <td>332</td>
      <td>108</td>
      <td>5</td>
      <td>4.5</td>
      <td>4.0</td>
      <td>9.02</td>
      <td>1</td>
      <td>0.87</td>
    </tr>
    <tr>
      <th>496</th>
      <td>337</td>
      <td>117</td>
      <td>5</td>
      <td>5.0</td>
      <td>5.0</td>
      <td>9.87</td>
      <td>1</td>
      <td>0.96</td>
    </tr>
    <tr>
      <th>497</th>
      <td>330</td>
      <td>120</td>
      <td>5</td>
      <td>4.5</td>
      <td>5.0</td>
      <td>9.56</td>
      <td>1</td>
      <td>0.93</td>
    </tr>
    <tr>
      <th>498</th>
      <td>312</td>
      <td>103</td>
      <td>4</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>8.43</td>
      <td>0</td>
      <td>0.73</td>
    </tr>
    <tr>
      <th>499</th>
      <td>327</td>
      <td>113</td>
      <td>4</td>
      <td>4.5</td>
      <td>4.5</td>
      <td>9.04</td>
      <td>0</td>
      <td>0.84</td>
    </tr>
  </tbody>
</table>
<p>500 rows × 8 columns</p>
</div>




```python
X = df.drop('Chance of Admit ', axis=1)
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
      <th>GRE Score</th>
      <th>TOEFL Score</th>
      <th>University Rating</th>
      <th>SOP</th>
      <th>LOR</th>
      <th>CGPA</th>
      <th>Research</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>337</td>
      <td>118</td>
      <td>4</td>
      <td>4.5</td>
      <td>4.5</td>
      <td>9.65</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>324</td>
      <td>107</td>
      <td>4</td>
      <td>4.0</td>
      <td>4.5</td>
      <td>8.87</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>316</td>
      <td>104</td>
      <td>3</td>
      <td>3.0</td>
      <td>3.5</td>
      <td>8.00</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>322</td>
      <td>110</td>
      <td>3</td>
      <td>3.5</td>
      <td>2.5</td>
      <td>8.67</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>314</td>
      <td>103</td>
      <td>2</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>8.21</td>
      <td>0</td>
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
    </tr>
    <tr>
      <th>495</th>
      <td>332</td>
      <td>108</td>
      <td>5</td>
      <td>4.5</td>
      <td>4.0</td>
      <td>9.02</td>
      <td>1</td>
    </tr>
    <tr>
      <th>496</th>
      <td>337</td>
      <td>117</td>
      <td>5</td>
      <td>5.0</td>
      <td>5.0</td>
      <td>9.87</td>
      <td>1</td>
    </tr>
    <tr>
      <th>497</th>
      <td>330</td>
      <td>120</td>
      <td>5</td>
      <td>4.5</td>
      <td>5.0</td>
      <td>9.56</td>
      <td>1</td>
    </tr>
    <tr>
      <th>498</th>
      <td>312</td>
      <td>103</td>
      <td>4</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>8.43</td>
      <td>0</td>
    </tr>
    <tr>
      <th>499</th>
      <td>327</td>
      <td>113</td>
      <td>4</td>
      <td>4.5</td>
      <td>4.5</td>
      <td>9.04</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>500 rows × 7 columns</p>
</div>




```python
poly_transformer = preprocessing.PolynomialFeatures(2)
```


```python
poly_features = poly_transformer.fit_transform(X.values)
```


```python
feature_names = poly_transformer.get_feature_names_out(X.columns)
```


```python
X = pd.DataFrame(poly_features, columns=feature_names)
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
      <th>1</th>
      <th>GRE Score</th>
      <th>TOEFL Score</th>
      <th>University Rating</th>
      <th>SOP</th>
      <th>LOR</th>
      <th>CGPA</th>
      <th>Research</th>
      <th>GRE Score^2</th>
      <th>GRE Score TOEFL Score</th>
      <th>...</th>
      <th>SOP^2</th>
      <th>SOP LOR</th>
      <th>SOP CGPA</th>
      <th>SOP Research</th>
      <th>LOR ^2</th>
      <th>LOR  CGPA</th>
      <th>LOR  Research</th>
      <th>CGPA^2</th>
      <th>CGPA Research</th>
      <th>Research^2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>337.0</td>
      <td>118.0</td>
      <td>4.0</td>
      <td>4.5</td>
      <td>4.5</td>
      <td>9.65</td>
      <td>1.0</td>
      <td>113569.0</td>
      <td>39766.0</td>
      <td>...</td>
      <td>20.25</td>
      <td>20.25</td>
      <td>43.425</td>
      <td>4.5</td>
      <td>20.25</td>
      <td>43.425</td>
      <td>4.5</td>
      <td>93.1225</td>
      <td>9.65</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.0</td>
      <td>324.0</td>
      <td>107.0</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>4.5</td>
      <td>8.87</td>
      <td>1.0</td>
      <td>104976.0</td>
      <td>34668.0</td>
      <td>...</td>
      <td>16.00</td>
      <td>18.00</td>
      <td>35.480</td>
      <td>4.0</td>
      <td>20.25</td>
      <td>39.915</td>
      <td>4.5</td>
      <td>78.6769</td>
      <td>8.87</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.0</td>
      <td>316.0</td>
      <td>104.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.5</td>
      <td>8.00</td>
      <td>1.0</td>
      <td>99856.0</td>
      <td>32864.0</td>
      <td>...</td>
      <td>9.00</td>
      <td>10.50</td>
      <td>24.000</td>
      <td>3.0</td>
      <td>12.25</td>
      <td>28.000</td>
      <td>3.5</td>
      <td>64.0000</td>
      <td>8.00</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.0</td>
      <td>322.0</td>
      <td>110.0</td>
      <td>3.0</td>
      <td>3.5</td>
      <td>2.5</td>
      <td>8.67</td>
      <td>1.0</td>
      <td>103684.0</td>
      <td>35420.0</td>
      <td>...</td>
      <td>12.25</td>
      <td>8.75</td>
      <td>30.345</td>
      <td>3.5</td>
      <td>6.25</td>
      <td>21.675</td>
      <td>2.5</td>
      <td>75.1689</td>
      <td>8.67</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.0</td>
      <td>314.0</td>
      <td>103.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>8.21</td>
      <td>0.0</td>
      <td>98596.0</td>
      <td>32342.0</td>
      <td>...</td>
      <td>4.00</td>
      <td>6.00</td>
      <td>16.420</td>
      <td>0.0</td>
      <td>9.00</td>
      <td>24.630</td>
      <td>0.0</td>
      <td>67.4041</td>
      <td>0.00</td>
      <td>0.0</td>
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
      <th>495</th>
      <td>1.0</td>
      <td>332.0</td>
      <td>108.0</td>
      <td>5.0</td>
      <td>4.5</td>
      <td>4.0</td>
      <td>9.02</td>
      <td>1.0</td>
      <td>110224.0</td>
      <td>35856.0</td>
      <td>...</td>
      <td>20.25</td>
      <td>18.00</td>
      <td>40.590</td>
      <td>4.5</td>
      <td>16.00</td>
      <td>36.080</td>
      <td>4.0</td>
      <td>81.3604</td>
      <td>9.02</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>496</th>
      <td>1.0</td>
      <td>337.0</td>
      <td>117.0</td>
      <td>5.0</td>
      <td>5.0</td>
      <td>5.0</td>
      <td>9.87</td>
      <td>1.0</td>
      <td>113569.0</td>
      <td>39429.0</td>
      <td>...</td>
      <td>25.00</td>
      <td>25.00</td>
      <td>49.350</td>
      <td>5.0</td>
      <td>25.00</td>
      <td>49.350</td>
      <td>5.0</td>
      <td>97.4169</td>
      <td>9.87</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>497</th>
      <td>1.0</td>
      <td>330.0</td>
      <td>120.0</td>
      <td>5.0</td>
      <td>4.5</td>
      <td>5.0</td>
      <td>9.56</td>
      <td>1.0</td>
      <td>108900.0</td>
      <td>39600.0</td>
      <td>...</td>
      <td>20.25</td>
      <td>22.50</td>
      <td>43.020</td>
      <td>4.5</td>
      <td>25.00</td>
      <td>47.800</td>
      <td>5.0</td>
      <td>91.3936</td>
      <td>9.56</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>498</th>
      <td>1.0</td>
      <td>312.0</td>
      <td>103.0</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>8.43</td>
      <td>0.0</td>
      <td>97344.0</td>
      <td>32136.0</td>
      <td>...</td>
      <td>16.00</td>
      <td>20.00</td>
      <td>33.720</td>
      <td>0.0</td>
      <td>25.00</td>
      <td>42.150</td>
      <td>0.0</td>
      <td>71.0649</td>
      <td>0.00</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>499</th>
      <td>1.0</td>
      <td>327.0</td>
      <td>113.0</td>
      <td>4.0</td>
      <td>4.5</td>
      <td>4.5</td>
      <td>9.04</td>
      <td>0.0</td>
      <td>106929.0</td>
      <td>36951.0</td>
      <td>...</td>
      <td>20.25</td>
      <td>20.25</td>
      <td>40.680</td>
      <td>0.0</td>
      <td>20.25</td>
      <td>40.680</td>
      <td>0.0</td>
      <td>81.7216</td>
      <td>0.00</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>500 rows × 36 columns</p>
</div>




```python
y = df[['Chance of Admit ']]
```


```python
hyper = {
    'alpha' : [0.01, 0.1, 1, 10],
    'max_iter' : [100, 500, 1000, 1500, 2000]
}
```


```python
lmodel = Lasso()
```


```python
grid = GridSearchCV(lmodel, hyper, cv=5)
```


```python
grid.fit(X,y)
```

    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 4.253e-01, tolerance: 6.706e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 7.086e-01, tolerance: 8.246e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 7.684e-01, tolerance: 8.590e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 6.851e-01, tolerance: 7.997e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 7.568e-01, tolerance: 8.115e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 4.205e-01, tolerance: 6.706e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 6.925e-01, tolerance: 8.246e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 7.554e-01, tolerance: 8.590e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 6.607e-01, tolerance: 7.997e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 7.439e-01, tolerance: 8.115e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 4.171e-01, tolerance: 6.706e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.556e-02, tolerance: 8.246e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 7.436e-01, tolerance: 8.590e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 6.566e-01, tolerance: 7.997e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 7.696e-01, tolerance: 8.115e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.752e-01, tolerance: 6.706e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.038e-01, tolerance: 8.590e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 4.612e-01, tolerance: 7.997e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.727e-01, tolerance: 8.115e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.718e-01, tolerance: 6.706e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 2.952e-01, tolerance: 8.590e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 4.070e-01, tolerance: 7.997e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 3.529e-01, tolerance: 8.115e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 4.393e-01, tolerance: 6.706e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 6.902e-01, tolerance: 8.246e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 7.540e-01, tolerance: 8.590e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 6.728e-01, tolerance: 7.997e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 7.481e-01, tolerance: 8.115e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 2.559e-03, tolerance: 6.706e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.618e-01, tolerance: 8.246e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.427e-01, tolerance: 8.590e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 2.017e-01, tolerance: 7.997e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 2.598e-01, tolerance: 8.115e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 2.041e-03, tolerance: 6.706e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.082e-03, tolerance: 8.246e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 8.908e-04, tolerance: 8.590e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.261e-03, tolerance: 7.997e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.431e-03, tolerance: 8.115e-04
      model = cd_fast.enet_coordinate_descent(
    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\linear_model\_coordinate_descent.py:631: ConvergenceWarning: Objective did not converge. You might want to increase the number of iterations, check the scale of the features or consider increasing regularisation. Duality gap: 1.543e-01, tolerance: 9.940e-04
      model = cd_fast.enet_coordinate_descent(
    




<style>#sk-container-id-12 {color: black;background-color: white;}#sk-container-id-12 pre{padding: 0;}#sk-container-id-12 div.sk-toggleable {background-color: white;}#sk-container-id-12 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-12 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-12 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-12 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-12 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-12 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-12 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-12 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-container-id-12 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-12 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-12 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-12 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-12 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-12 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-12 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-12 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-12 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-12 div.sk-item {position: relative;z-index: 1;}#sk-container-id-12 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-12 div.sk-item::before, #sk-container-id-12 div.sk-parallel-item::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-12 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-12 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-12 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-12 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-12 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-12 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-12 div.sk-label-container {text-align: center;}#sk-container-id-12 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-12 div.sk-text-repr-fallback {display: none;}</style><div id="sk-container-id-12" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>GridSearchCV(cv=5, estimator=Lasso(),
             param_grid={&#x27;alpha&#x27;: [0.01, 0.1, 1, 10],
                         &#x27;max_iter&#x27;: [100, 500, 1000, 1500, 2000]})</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item sk-dashed-wrapped"><div class="sk-label-container"><div class="sk-label sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-30" type="checkbox" ><label for="sk-estimator-id-30" class="sk-toggleable__label sk-toggleable__label-arrow">GridSearchCV</label><div class="sk-toggleable__content"><pre>GridSearchCV(cv=5, estimator=Lasso(),
             param_grid={&#x27;alpha&#x27;: [0.01, 0.1, 1, 10],
                         &#x27;max_iter&#x27;: [100, 500, 1000, 1500, 2000]})</pre></div></div></div><div class="sk-parallel"><div class="sk-parallel-item"><div class="sk-item"><div class="sk-label-container"><div class="sk-label sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-31" type="checkbox" ><label for="sk-estimator-id-31" class="sk-toggleable__label sk-toggleable__label-arrow">estimator: Lasso</label><div class="sk-toggleable__content"><pre>Lasso()</pre></div></div></div><div class="sk-serial"><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-32" type="checkbox" ><label for="sk-estimator-id-32" class="sk-toggleable__label sk-toggleable__label-arrow">Lasso</label><div class="sk-toggleable__content"><pre>Lasso()</pre></div></div></div></div></div></div></div></div></div></div>




```python
grid.best_params_
```




    {'alpha': 0.1, 'max_iter': 500}




```python
np.average(cross_val_score(model, X, y, cv=5))
```




    0.799996162455243



## <a id='toc1_4_'></a>[수료증](https://www.codeit.kr/certificates/4LvPn-UGcZK-NaLTn-JCPB2) [&#8593;](#toc0_)
