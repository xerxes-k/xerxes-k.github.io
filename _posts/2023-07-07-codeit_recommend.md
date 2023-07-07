---
layout: single
title:  "recommend system "
---

**Table of contents**<a id='toc0_'></a>    
- [recommend system](#toc1_)    
  - [추천 시스템에서 사용하는 데이터의 종류](#toc1_1_)    
  - [내용 기반 추천](#toc1_2_)    
    - [자료구조 형태](#toc1_2_1_)    
    - [내용기반 추천의 장단점](#toc1_2_2_)    
  - [협업 필터링](#toc1_3_)    
    - [자료구조 형태](#toc1_3_1_)    
    - [유사도 측정방법의 종류](#toc1_3_2_)    
      - [거리 기반 유사도 측정은 유클리드 거리로 측정한다](#toc1_3_2_1_)    
      - [각도 기반 유사도 측정은 코사인을 이용한다](#toc1_3_2_2_)    
      - [유클리드 vs. 코사인](#toc1_3_2_3_)    
    - [유사도 데이터 전처리](#toc1_3_3_)    
      - [결측치를 어떻게 할 것인가](#toc1_3_3_1_)    
    - [유사한 유저 k명 뽑기](#toc1_3_4_)    
    - [협업 필터링의 장단](#toc1_3_5_)    
    - [결론: 내용기반, 협업필터링을 같이 쓰는 게 낫다](#toc1_3_6_)    
  - [행렬 인수분해](#toc1_4_)    
    - [자료구조 형태](#toc1_4_1_)    
    - [손실함수](#toc1_4_2_)    
      - [행렬 인수분해 손실함수 볼록도](#toc1_4_2_1_)    
    - [경사하강법](#toc1_4_3_)    
    - [정규화](#toc1_4_4_)    
  - [수료증](#toc1_5_)    

<!-- vscode-jupyter-toc-config
	numbering=false
	anchor=true
	flat=false
	minLevel=1
	maxLevel=6
	/vscode-jupyter-toc-config -->
<!-- THIS CELL WILL BE REPLACED ON TOC UPDATE. DO NOT WRITE YOUR TEXT IN THIS CELL -->

# <a id='toc1_'></a>[recommend system](#toc0_)
사용자가 좋아할 만한 내용을 추천해주는 시스템

## <a id='toc1_1_'></a>[추천 시스템에서 사용하는 데이터의 종류](#toc0_)
---
- 직접 데이터: 유저가 선호도를 직접 선택한 데이터(좋아요, 구매) 선호도를 직접 알 수 있지만 데이터 양은 적다
- 간접 데이터: 유저가 직접 선택하진 않았지만 다른 행동에 의해 간접적으로 수집되는 데이터(예: 상품 조회, 검색어) 부정확하지만 데이터 양은 많다

## <a id='toc1_2_'></a>[내용 기반 추천](#toc0_)
---
  - 내용(속성)이 무엇인지 분석하고 속성 마다 점수를 부여. 속성을 입력변수, 평점을 목표변수로 학습 후 사용
  - 좋아요/싫어요면 분류 알고리즘, 평점(연속된 값)이면 회귀 알고리즘으로 사용


```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from math import sqrt

import pandas as pd
import numpy as np
```

### <a id='toc1_2_1_'></a>[자료구조 형태](#toc0_)
---
1. 행(case)에는 상품을 넣는다
2. 열(feature)에는 상품의 속성을 넣는다
3. 값(data)은 상품의 속성값이다
4. 마지막 열에 유저의 평점을 넣고 이것을 목표 변수로 삼는다

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3641&directory=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-09-22%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%203.35.42.png&name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-09-22+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+3.35.42.png)

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3641&directory=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-09-22%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%203.43.59.png&name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-09-22+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+3.43.59.png)

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3641&directory=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-09-22%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%203.45.19.png&name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-09-22+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+3.45.19.png)

이를 식으로 표현하면 다음과 같다. 
- x는 영화가 갖고 있는 속성값이다
- theta는 상수다. 유저가 해당 속성을 얼마나 선호하는지를 나타낸다. 즉 가중치의 역할이다

$h_\theta(x) = \theta_0 + \theta_2 x_2 + \theta_3 x_3 + \theta_4 x_4 $


```python
df = pd.read_csv('movie_rating.csv')
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
      <th>romance</th>
      <th>action</th>
      <th>comedy</th>
      <th>heart-warming</th>
      <th>rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.740458</td>
      <td>0.733800</td>
      <td>0.526879</td>
      <td>0.332906</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.658391</td>
      <td>0.825211</td>
      <td>0.608177</td>
      <td>0.906809</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.680250</td>
      <td>0.401992</td>
      <td>0.400964</td>
      <td>0.535223</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.572216</td>
      <td>0.312618</td>
      <td>0.496313</td>
      <td>0.319996</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.543545</td>
      <td>0.623021</td>
      <td>0.713110</td>
      <td>0.696774</td>
      <td>4.0</td>
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
      <th>95</th>
      <td>0.431629</td>
      <td>0.803459</td>
      <td>0.330847</td>
      <td>0.423794</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>96</th>
      <td>0.829724</td>
      <td>0.657431</td>
      <td>0.493758</td>
      <td>0.432268</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>97</th>
      <td>0.685688</td>
      <td>0.760196</td>
      <td>0.661252</td>
      <td>0.534698</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>98</th>
      <td>0.643441</td>
      <td>0.848488</td>
      <td>0.677173</td>
      <td>0.638528</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>99</th>
      <td>0.374184</td>
      <td>0.517988</td>
      <td>0.733646</td>
      <td>0.546950</td>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
<p>100 rows × 5 columns</p>
</div>




```python
X = df.drop('rating', axis=1)
y = df[['rating']]
```


```python
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
      <th>romance</th>
      <th>action</th>
      <th>comedy</th>
      <th>heart-warming</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.740458</td>
      <td>0.733800</td>
      <td>0.526879</td>
      <td>0.332906</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.658391</td>
      <td>0.825211</td>
      <td>0.608177</td>
      <td>0.906809</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.680250</td>
      <td>0.401992</td>
      <td>0.400964</td>
      <td>0.535223</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.572216</td>
      <td>0.312618</td>
      <td>0.496313</td>
      <td>0.319996</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.543545</td>
      <td>0.623021</td>
      <td>0.713110</td>
      <td>0.696774</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>95</th>
      <td>0.431629</td>
      <td>0.803459</td>
      <td>0.330847</td>
      <td>0.423794</td>
    </tr>
    <tr>
      <th>96</th>
      <td>0.829724</td>
      <td>0.657431</td>
      <td>0.493758</td>
      <td>0.432268</td>
    </tr>
    <tr>
      <th>97</th>
      <td>0.685688</td>
      <td>0.760196</td>
      <td>0.661252</td>
      <td>0.534698</td>
    </tr>
    <tr>
      <th>98</th>
      <td>0.643441</td>
      <td>0.848488</td>
      <td>0.677173</td>
      <td>0.638528</td>
    </tr>
    <tr>
      <th>99</th>
      <td>0.374184</td>
      <td>0.517988</td>
      <td>0.733646</td>
      <td>0.546950</td>
    </tr>
  </tbody>
</table>
<p>100 rows × 4 columns</p>
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
      <th>rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>95</th>
      <td>3.0</td>
    </tr>
    <tr>
      <th>96</th>
      <td>3.0</td>
    </tr>
    <tr>
      <th>97</th>
      <td>4.0</td>
    </tr>
    <tr>
      <th>98</th>
      <td>5.0</td>
    </tr>
    <tr>
      <th>99</th>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
<p>100 rows × 1 columns</p>
</div>




```python
tr_X, test_X, tr_y, test_y = train_test_split(X, y, test_size=0.2, random_state=5)
```


```python
model = LinearRegression()
model.fit(tr_X, tr_y)
```




<style>#sk-container-id-1 {color: black;background-color: white;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id="sk-container-id-1" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>LinearRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-1" type="checkbox" checked><label for="sk-estimator-id-1" class="sk-toggleable__label sk-toggleable__label-arrow">LinearRegression</label><div class="sk-toggleable__content"><pre>LinearRegression()</pre></div></div></div></div></div>




```python
y_test_predict = model.predict(test_X)
```


```python
y_test_predict
```




    array([[3.83034441],
           [2.59418977],
           [2.63653566],
           [3.48333221],
           [2.75217812],
           [2.43303141],
           [3.03247628],
           [4.41312853],
           [4.28145539],
           [3.61139607],
           [3.82260281],
           [3.01099122],
           [3.06324646],
           [4.41401949],
           [4.08837667],
           [3.30347874],
           [4.69514621],
           [4.3397661 ],
           [3.42084949],
           [3.94638571]])




```python
(sum(((y_test_predict - test_y)**2).values)/len(test_y))**0.5
```




    array([0.35162271])




```python
mean_squared_error(y_test_predict, test_y)**0.5
```




    0.351622705540817



### <a id='toc1_2_2_'></a>[내용기반 추천의 장단점](#toc0_)

---

- 장점: 
  - 추천 시 다른 사람의 데이터는 필요 없다. 즉, 새롭게 출시하거나 인기가 없는 상품도 추천할 수 있다
    - 사용자들의 선호도가 서로 독립적이라 가정하고 있기 때문이다
- 단점: 
  - 적절한 속성(입력값, feature)을 골라내야 하는데 그 분석과정이 추가로 필요하다
  - 유저가 제공한 데이터 외에는 알 수 없다. 선호도가 유사한 다른 사용자가 좋아하는 상품을 추천할 수 없다

## <a id='toc1_3_'></a>[협업 필터링](#toc0_)
---
많은 유저들의 평점 데이터를 모아서 활용하는 방법  
때로 유저 간의 속성값이 연관성을 가질 수도 있다. "이걸 좋아하는 사람들은 이런 것도 좋아하더라 ~"  
속성은 아예 등장하지 않는다 따라서 해석할 때도 예측값이 왜 그렇게 나왔는지는 알 수 없다

어떤 유저들이 서로 유사한지 알아야 한다
- Euclidean distance 거리기반 유사도
- Cosine similarity 각도기반 유사도

1. 어떤 유저a와 다른 유저 간의 거리를 구한다
2. 가장 유사한 유저 k명을 그룹A로 모은다
3. a가 아직 평가하지 않은 상품에 그룹A의 평균 평점을 부여한다
4. 높은 점수 순으로 a에게 추천한다

### <a id='toc1_3_1_'></a>[자료구조 형태](#toc0_)
---
1. 행(case)에는 사용자를 넣는다
2. 열(feature)에는 상품을 넣는다
3. 값(data)은 사용자의 상품에 대한 평점이다

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3656&directory=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-09-23%20%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB%2011.35.21.png&name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-09-23+%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB+11.35.21.png)

각 행(유저)의 평점은 벡터로 표현된다  
$r(1) = \begin{bmatrix}5\\1\\1\\5\\2 \end{bmatrix}$

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3651&directory=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-09-22%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%204.24.07.png&name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-09-22+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+4.24.07.png)

### <a id='toc1_3_2_'></a>[유사도 측정방법의 종류](#toc0_)
---
- Euclidean distance 거리기반 유사도
- Cosine similarity 각도기반 유사도


![](https://velog.velcdn.com/images%2Foneofakindscene%2Fpost%2Ffe0495cd-c296-40e7-b1d3-d5df2c38bd4f%2Fimage.png)

#### <a id='toc1_3_2_1_'></a>[거리 기반 유사도 측정은 유클리드 거리로 측정한다](#toc0_)
---

각 벡터를 점으로 표현하고 피타고라스 정리를 이용해 거리를 구한다

![](https://t1.daumcdn.net/cfile/tistory/2345B8445754283121)


```python
def distance(user_1, user_2):
    """유클리드 거리를 계산해주는 함수"""
    # 여기에 코드를 작성하세요
    return sqrt(np.sum((user_1 - user_2)**2))    
    

# 테스트 코드
user_1 = np.array([0, 1, 2, 3, 4, 5])
user_2 = np.array([0, 1, 4, 6, 1, 4])

distance(user_1, user_2)

```




    4.795831523312719



#### <a id='toc1_3_2_2_'></a>[각도 기반 유사도 측정은 코사인을 이용한다](#toc0_)
---

각 벡터를 선으로 표현하고 벡터 사이의 거리를 코사인 값으로 만든다  
아주 유용하게도 데이터가 유사해서 벡터 간 각도가 0이 되면 코사인 값은 1이 된다  
데이터가 반대라서 벡터간 각도가 180도가 되면 코사인 값은 -1이 된다.  
같으면 1 반대면 -1 가공해서 쓰기 쉽다

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3655&directory=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-09-22%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%205.36.22.png&name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-09-22+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+5.36.22.png)

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3655&directory=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-09-22%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%205.37.43.png&name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-09-22+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+5.37.43.png)

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3655&directory=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-09-25%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%205.27.00.png&name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-09-25+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+5.27.00.png)

![](https://blog.kakaocdn.net/dn/mv0P1/btqF4yCifLR/kBkYkrIneaQ6ZSpk9S5O31/img.png)

#### <a id='toc1_3_2_3_'></a>[유클리드 vs. 코사인](#toc0_)
---
- 가장 큰 차이는 코사인은 벡터의 크기와 무관하다는 점
  - 값의 스케일 차이가 너무 크면 유클리드는 유사도가 낮다고 나온다
- 유클리드 거리는 작을 수록 유사하고, 코사인은 1에 가까울수록 유사하다

### <a id='toc1_3_3_'></a>[유사도 데이터 전처리](#toc0_)
---
#### <a id='toc1_3_3_1_'></a>[결측치를 어떻게 할 것인가](#toc0_)
- ~~결측치를 0으로 만든다~~: 임의로 낮은 점수를 주는 거여서 좋지 않다
- ~~유저 평점으로 만든다~~: 임의의 점수를 배정하는 거라 좋지 않다

- mean normalization : 결측치는 0으로, 나머지는 평균 대비 높다 낮다로 세팅한다
  - 먼저 결측치에 해당 행의 평균 점수를 배정한다
  - 모든 행에 해당 행의 평균점수를 차감한다
  - 결측치는 0이 되고 다른 모든 값들도 평균보다 높냐 낮냐가 된다


![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3656&directory=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-09-25%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%205.29.32.png&name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-09-25+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+5.29.32.png)

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3656&directory=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-09-25%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%205.29.23.png&name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-09-25+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+5.29.23.png)

### <a id='toc1_3_4_'></a>[유사한 유저 k명 뽑기](#toc0_)
---
- 어떤 유저와 가장 유사한 k명을 모아 그룹 A를 만든다
- 어떤 유저가 평가하지 않은 상품에 대해 그룹 A의 평균 평점을 부여한다
- 높은 예측 평점의 상품을 추천한다

아래 자료는 mean normalization을 하지 않았다 왜지?

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3659&directory=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-09-22%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%206.00.35.png&name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-09-22+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+6.00.35.png)

$r^{(x)}_i = {1 \over k} \displaystyle\sum_{y\in N}{r^{(y)}_i}$

x행 i열 data인 r의 값은 N 집합에 속한 y행들의 i열 값 평균이다

풀어서 표현하면

![예측](https://github.com/xerxes-k/xerxes-k.github.io/blob/master/assets/images/recommend_1.PNG?raw=true)


```python
np.set_printoptions(precision=2)  # 소수점 둘째 자리까지만 출력

def distance(user_1, user_2):
    """유클리드 거리를 계산해주는 함수"""
    return sqrt(np.sum((user_1 - user_2)**2))
    
    
def filter_users_without_movie(rating_data, movie_id):
    """movie_id 번째 영화를 평가하지 않은 유저들은 미리 제외해주는 함수"""
    return rating_data[~np.isnan(rating_data[:,movie_id])]
    
    
def fill_nan_with_user_mean(rating_data):
    """평점 데이터의 빈값들을 각 유저 평균 값으로 체워주는 함수"""
    filled_data = np.copy(rating_data)  # 평점 데이터를 훼손하지 않기 위해 복사
    row_mean = np.nanmean(filled_data, axis=1)  # 유저 평균 평점 계산
    ### axis가 1이면 칼럼 아닌가?
    ### 실험해보니까 axis 0이 칼럼이긴 한데 왜지?
    ## 밑에 정리했다
    
    inds = np.where(np.isnan(filled_data))  # 비어 있는 인덱스들을 구한다
    # print("rowmean", row_mean ,"end of roweman")
    # print("take:", np.take(row_mean, inds[0]), "end of take")    
    filled_data[inds] = np.take(row_mean, inds[0])  # 빈 인덱스를 유저 평점으로 채운다
    # print("filled", filled_data)
    
    return filled_data
    
    
def get_k_neighbors(user_id, rating_data, k):
    """user_id에 해당하는 유저의 이웃들을 찾아주는 함수"""
    distance_data = np.copy(rating_data)  # 평점 데이터를 훼손하지 않기 위해 복사
    # 마지막에 거리 데이터를 담을 열 추가한다
    distance_data = np.append(distance_data, np.zeros((distance_data.shape[0], 1)), axis=1)
    
    # 여기에 코드를 작성하세요
    for i in range(0, len(distance_data)):
        if i == user_id:
            distance_data[i][-1] = np.inf
        else:
            distance_data[i][-1] = distance(distance_data[user_id][:-1], distance_data[i][:-1])
    
    # 데이터를 거리 열을 기준으로 정렬한다
    distance_data = distance_data[np.argsort(distance_data[:, -1])]
    
    # 가장 가까운 k개의 행만 리턴한다 + 마지막(거리) 열은 제외한다
    return distance_data[:k, :-1]
    

# 테스트 코드
# 영화 3을 본 유저들 중, 유저 0와 비슷한 유저 5명을 찾는다
rating_data = pd.read_csv('ratings.csv', index_col='user_id').values  # 평점 데이터를 불러온다
filtered_data = filter_users_without_movie(rating_data, 3)  # 3 번째 영화를 보지 않은 유저를 데이터에서 미리 제외시킨다
filled_data = fill_nan_with_user_mean(filtered_data)  # 빈값들이 채워진 새로운 행렬을 만든다
user_0_neighbors = get_k_neighbors(0, filled_data, 5)  # 유저 0과 비슷한 5개의 유저 데이터를 찾는다
user_0_neighbors
```




    array([[3.18, 3.18, 3.18, 5.  , 3.18, 3.18, 2.  , 2.  , 2.  , 3.18, 3.  ,
            4.  , 2.  , 5.  , 4.  , 3.18, 3.18, 3.18, 4.  , 2.  ],
           [3.36, 5.  , 3.36, 5.  , 3.  , 3.36, 3.36, 3.  , 2.  , 4.  , 2.  ,
            3.36, 4.  , 4.  , 5.  , 4.  , 2.  , 3.36, 1.  , 3.  ],
           [2.71, 2.71, 2.  , 5.  , 2.71, 2.71, 2.71, 2.71, 2.71, 2.71, 2.71,
            2.71, 1.  , 2.71, 2.71, 2.71, 3.  , 1.  , 5.  , 2.  ],
           [2.78, 5.  , 1.  , 4.  , 2.78, 2.78, 2.78, 3.  , 1.  , 2.78, 1.  ,
            2.78, 2.78, 4.  , 2.78, 2.78, 2.  , 2.78, 2.78, 4.  ],
           [3.  , 3.  , 3.  , 5.  , 4.  , 3.  , 3.  , 4.  , 5.  , 3.  , 3.  ,
            1.  , 2.  , 1.  , 1.  , 3.  , 3.  , 3.  , 4.  , 3.  ]])




```python
test = pd.read_csv('ratings.csv', index_col='user_id').values
test[0]
```




    array([ 2.,  3.,  4., nan,  2.,  3., nan, nan, nan,  4.,  4., nan, nan,
            1., nan, nan,  2.,  5.,  2., nan])




```python
np.nanmean(test['0'])
```




    2.375




```python
(2+2+3+1+3+2+4+2)/8
```




    2.375




```python
np.nanmean(test, axis=0) ### axis 0이 칼럼이네?
```




    array([2.38, 3.1 , 2.75, 3.56, 3.  , 4.1 , 2.88, 3.33, 2.45, 2.8 , 2.73,
           3.33, 3.  , 2.83, 2.77, 3.25, 2.5 , 3.62, 3.18, 3.15])




```python
df
```




    array([[ 2.,  3.,  4., nan,  2.,  3., nan, nan, nan,  4.,  4., nan, nan,
             1., nan, nan,  2.,  5.,  2., nan],
           [nan, nan, nan,  4., nan,  5., nan, nan,  2., nan,  4., nan,  1.,
            nan, nan, nan, nan,  5., nan, nan],
           [ 2., nan,  1., nan, nan,  5.,  5., nan, nan, nan, nan,  5.,  3.,
             3., nan,  3.,  3.,  4., nan, nan],
           [nan,  3.,  5., nan, nan, nan,  4.,  3., nan,  5.,  3., nan,  4.,
            nan, nan,  2., nan, nan, nan,  2.],
           [nan, nan, nan,  5., nan, nan,  2.,  2.,  2., nan,  3.,  4.,  2.,
             5.,  4., nan, nan, nan,  4.,  2.],
           [nan,  4.,  3., nan, nan,  5., nan, nan, nan,  3.,  2., nan, nan,
            nan,  1., nan,  4.,  3., nan,  5.],
           [ 3., nan, nan, nan,  4.,  5.,  2.,  2., nan,  3., nan,  4., nan,
            nan,  2.,  4., nan, nan, nan,  1.],
           [nan,  5.,  1.,  4., nan, nan, nan,  3.,  1., nan,  1., nan, nan,
             4., nan, nan,  2., nan, nan,  4.],
           [nan,  3.,  1.,  1., nan,  3., nan,  4., nan,  1.,  1., nan,  4.,
             4.,  2., nan, nan,  5.,  3., nan],
           [ 1.,  1., nan,  1.,  1., nan, nan, nan, nan, nan, nan,  2., nan,
            nan,  1., nan, nan, nan,  4., nan],
           [nan,  2., nan, nan,  2.,  2., nan, nan,  2.,  3.,  2., nan, nan,
             1.,  4.,  5.,  3., nan,  3.,  3.],
           [ 3., nan, nan,  5.,  4., nan, nan,  4.,  5.,  3., nan,  1.,  2.,
             1.,  1., nan, nan, nan,  4., nan],
           [ 2., nan,  5., nan,  5.,  4., nan, nan, nan, nan, nan,  2.,  3.,
            nan,  4., nan, nan, nan, nan,  3.],
           [nan,  2.,  1., nan, nan, nan,  4., nan,  1., nan,  5.,  5.,  4.,
             3.,  5., nan, nan,  5.,  5.,  4.],
           [nan,  3.,  5., nan, nan, nan,  2.,  5.,  3., nan,  3.,  3., nan,
             4., nan,  4., nan,  1., nan, nan],
           [nan, nan,  2.,  5., nan, nan, nan, nan, nan, nan, nan, nan,  1.,
            nan, nan, nan,  3.,  1.,  5.,  2.],
           [nan,  5., nan,  5.,  3., nan, nan,  3.,  2.,  4.,  2., nan,  4.,
             4.,  5.,  4.,  2., nan,  1.,  3.],
           [ 4., nan,  1., nan, nan,  5.,  2., nan,  5., nan, nan,  4., nan,
             2.,  3., nan, nan, nan, nan,  5.],
           [nan, nan,  4., nan,  1.,  4., nan,  4.,  2.,  1., nan, nan, nan,
            nan,  2.,  1.,  1., nan,  3.,  5.],
           [ 2., nan, nan,  2.,  5., nan,  2., nan,  2.,  1., nan, nan,  5.,
             2.,  2.,  3., nan, nan,  1.,  2.]])




```python
np.nanmean(df, axis=1)
```




    array([2.91, 3.5 , 3.4 , 3.44, 3.18, 3.33, 3.  , 2.78, 2.67, 1.57, 2.67,
           3.  , 3.5 , 3.67, 3.3 , 2.71, 3.36, 3.44, 2.55, 2.42])



---
---

여러번 깨닫게 되는데 여러번 궁금하다. 표기법이 헷갈리기 때문이다.

- 행렬은 a x b로 표기하고 a개의 행과 b개의 열로 이루어진다
- x,y는 x가 가로축 y가 세로축이다
- 표기는 a x b, (x,y)니까 a랑 x가 먼저 온다
- 하지만 행렬을 매트릭스로 보면 행이 쌓이는 구조이기 때문에 행이 깊이(높이) = y 다
- 즉 a x b꼴이면 (b, a)꼴인 거다

~~그러므로 열이 가로 값인 x이고 axis 0이다~~  
놀랍게도 이게 스택오버플로우에서 가장 위에 뜨는 질문과 답이었다

---

그러나 의문이 들었다
- 근데 또 데이터프레임에선 칼럼 만질 때 axis 가 1이잖아?  

**그렇다 x축이니 y축이니 따지는 건 다 쌩쑈였다**

- 행렬은 그저 n개 리스트의 중첩일 뿐이다
- axis는 0 ~ n - 1 까지의 단위일 뿐이다
- axis 0부터 바깥쪽 리스트를 의미한다
- https://pybasall.tistory.com/129

---
---


```python
# test = test.values
# test
```


```python
np.where(np.isnan(test))  # 비어 있는 인덱스들을 구한다

### 두번째 어레이는 정체가 뭐지?
## 아하 첫번째 어레이는 0번 인덱스에 nan이 있는 수 만큼 0을 담고 있고
## 두번째 어레이는 0번 인덱스에 nan이 있는 칼럼 이름을 담고 있다
```




    (array([ 0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,  1,  1,  1,  1,
             1,  1,  1,  1,  1,  1,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  3,
             3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  4,  4,  4,  4,  4,  4,  4,
             4,  4,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  6,  6,  6,  6,
             6,  6,  6,  6,  6,  6,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,
             8,  8,  8,  8,  8,  8,  8,  8,  9,  9,  9,  9,  9,  9,  9,  9,  9,
             9,  9,  9,  9, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11,
            11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13,
            13, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14,
            15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16,
            16, 16, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 18, 18, 18, 18,
            18, 18, 18, 18, 18, 19, 19, 19, 19, 19, 19, 19, 19], dtype=int64),
     array([ 3,  6,  7,  8, 11, 12, 14, 15, 19,  0,  1,  2,  4,  6,  7,  9, 11,
            13, 14, 15, 16, 18, 19,  1,  3,  4,  7,  8,  9, 10, 14, 18, 19,  0,
             3,  4,  5,  8, 11, 13, 14, 16, 17, 18,  0,  1,  2,  4,  5,  9, 15,
            16, 17,  0,  3,  4,  6,  7,  8, 11, 12, 13, 15, 18,  1,  2,  3,  8,
            10, 12, 13, 16, 17, 18,  0,  4,  5,  6,  9, 11, 12, 14, 15, 17, 18,
             0,  4,  6,  8, 11, 15, 16, 19,  2,  5,  6,  7,  8,  9, 10, 12, 13,
            15, 16, 17, 19,  0,  2,  3,  6,  7, 11, 12, 17,  1,  2,  5,  6, 10,
            15, 16, 17, 19,  1,  3,  6,  7,  8,  9, 10, 13, 15, 16, 17, 18,  0,
             3,  4,  5,  7,  9, 15, 16,  0,  3,  4,  5,  9, 12, 14, 16, 18, 19,
             0,  1,  4,  5,  6,  7,  8,  9, 10, 11, 13, 14, 15,  0,  2,  5,  6,
            11, 17,  1,  3,  4,  7,  9, 10, 12, 15, 16, 17, 18,  0,  1,  3,  6,
            10, 11, 12, 13, 17,  1,  2,  5,  7, 10, 11, 16, 17], dtype=int64))




```python
np.where(np.isnan(test))[0]
```




    array([ 0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,  1,  1,  1,  1,
            1,  1,  1,  1,  1,  1,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  3,
            3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  4,  4,  4,  4,  4,  4,  4,
            4,  4,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  6,  6,  6,  6,
            6,  6,  6,  6,  6,  6,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,
            8,  8,  8,  8,  8,  8,  8,  8,  9,  9,  9,  9,  9,  9,  9,  9,  9,
            9,  9,  9,  9, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11,
           11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13,
           13, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14,
           15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16,
           16, 16, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 18, 18, 18, 18,
           18, 18, 18, 18, 18, 19, 19, 19, 19, 19, 19, 19, 19], dtype=int64)




```python
test[np.where(np.isnan(test))]
# = np.take(row_mean, inds[0])  # 빈 인덱스를 유저 평점으로 채운다
    # inds = np.where(np.isnan(filled_data))  # 비어 있는 인덱스들을 구한다
    # print("take:", np.take(row_mean, inds[0]))    
    # filled_data[inds] = np.take(row_mean, inds[0])  # 빈 인덱스를 유저 평점으로 채운다
    # print("filled", filled_data)
####### test라는 데이터 프레임으로 조회하려고 하니 안돼서 한참 해멨다. test.values로 어레이로 바꿔주니 바로 됐다.
```




    array([nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
           nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
           nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
           nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
           nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
           nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
           nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
           nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
           nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
           nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
           nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
           nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
           nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
           nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
           nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
           nan, nan, nan, nan, nan])




```python
arr = np.array([[1, 2, np.nan],
                [4, 5, 6],
                [7, 8, 9]])
row_mean = np.nanmean(arr, axis=1)
col_mean = np.nanmean(arr, axis=0)

print(row_mean)
print(col_mean)
```

    [1.5 5.  8. ]
    [4.  5.  7.5]
    


```python
test[1, 1]
```




    nan




```python

# RATING_DATA_PATH = './data/ratings.csv'  # 받아올 평점 데이터 경로 정의

np.set_printoptions(precision=2)  # 소수점 둘째 자리까지만 출력

def distance(user_1, user_2):
    """유클리드 거리를 계산해주는 함수"""
    return sqrt(np.sum((user_1 - user_2)**2))
    
    
def filter_users_without_movie(rating_data, movie_id):
    """movie_id 번째 영화를 평가하지 않은 유저들은 미리 제외해주는 함수"""
    return rating_data[~np.isnan(rating_data[:,movie_id])]
    
    
def fill_nan_with_user_mean(rating_data):
    """평점 데이터의 빈값들을 각 유저 평균 값으로 체워주는 함수"""
    filled_data = np.copy(rating_data)  # 평점 데이터를 훼손하지 않기 위해 복사
    row_mean = np.nanmean(filled_data, axis=1)  # 유저 평균 평점 계산
    
    inds = np.where(np.isnan(filled_data))  # 비어 있는 인덱스들을 구한다
    filled_data[inds] = np.take(row_mean, inds[0])  #빈 인덱스를 유저 평점으로 채운다
    
    return filled_data
    
    
def get_k_neighbors(user_id, rating_data, k):
    """user_id에 해당하는 유저의 이웃들을 찾아주는 함수"""
    distance_data = np.copy(rating_data)  # 평점 데이터를 훼손하지 않기 위해 복사
    # 마지막에 거리 데이터를 담을 열 추가한다
    distance_data = np.append(distance_data, np.zeros((distance_data.shape[0], 1)), axis=1)
    
    # 코드를 쓰세요.
    for i in range(len(distance_data)):
        row = distance_data[i]
        
        if i == user_id:  # 같은 유저면 거리를 무한대로 설정
            row[-1] = np.inf
        else:  # 다른 유저면 마지막 열에 거리 데이터를 저장
            row[-1] = distance(distance_data[user_id][:-1], row[:-1])
    
    # 데이터를 거리 열을 기준으로 정렬한다
    distance_data = distance_data[np.argsort(distance_data[:, -1])]
    
    # 가장 가까운 k개의 행만 리턴한다 + 마지막(거리) 열은 제외한다
    return distance_data[:k, :-1]
    
def predict_user_rating(rating_data, k, user_id, movie_id,):
    """예측 행렬에 따라 유저의 영화 평점 예측 값 구하기"""
    # movie_id 번째 영화를 보지 않은 유저를 데이터에서 미리 제외시킨다
    filtered_data = filter_users_without_movie(rating_data, movie_id)
    # 빈값들이 채워진 새로운 행렬을 만든다
    filled_data = fill_nan_with_user_mean(filtered_data)
    # 유저 user_id와 비슷한 k개의 유저 데이터를 찾는다
    neighbors = get_k_neighbors(user_id, filled_data, k)
    
    # 여기에 코드를 작성하세요
    # negh = []
    
    # for neghibor in neighbors:
    #     negh.append(neghibor[movie_id])    
    # predict = np.mean(negh)
    # return predict
    
    return np.mean(neighbors[:, movie_id])
    
    
    
# 테스트 코드
# 평점 데이터를 불러온다
rating_data = pd.read_csv('ratings.csv', index_col='user_id').values
# 5개의 이웃들을 써서 유저 0의 영화 3에 대한 예측 평점 구하기
predict_user_rating(rating_data, 5, 0, 3)  

```




    4.8



---

지금 복습할 때 보니 예제에서는 mean normalization을 하지 않았다  
fill_nan_with_user_mean(rating_data)를 할 때 row_mean을 빼고 row_mean으로 나눠줘서 정상화한 다음  
마지막에 predict_user_rating(rating_data, k, user_id, movie_id,)할 때 예측값에다가 대상 유저의 원래 평균평점을 더해주면 될 거 같은데?

해보고 결과 쓰자

---

### <a id='toc1_3_5_'></a>[협업 필터링의 장단](#toc0_)

- 장점:
  - 속성을 정의할 필요가 없다
  - 카테고리를 넘나드는 폭 넓은 상품을 추천
  - 내용 기반보다 나은 경우가 많다
  

- 단점:
  - 방대한 데이터 필요
  - 추천 데이터가 쌓이기 전엔 추천이 어렵다
  - 소수의 상품이 주로 추천될 수 있다
  - 추천의 이유를 알기 어렵다
  - 유저의 취향은 복잡해서 유저 협업필터 보다 상품 협업필터링이 나을 수 있다
    - 유저 간 유사도가 아니라 상품 간 유사도를 구한다
    - 유저 a가 평점을 남긴 상품들을 기반으로 하기 때문에 더 나을 수도 있겠군(뇌피셜)

### <a id='toc1_3_6_'></a>[결론: 내용기반, 협업필터링을 같이 쓰는 게 낫다](#toc0_)

## <a id='toc1_4_'></a>[행렬 인수분해](#toc0_)
---
행렬을 행렬의 곱으로 표현할 수 있다  
R = theta @ X

**내용 기반과 협업필터링의 융합버전**

### <a id='toc1_4_1_'></a>[자료구조 형태](#toc0_)
---

1. 두 개의 행렬을 만든다
    - 첫번째 행렬 theta 유저의 선호도
        - 첫번째 행렬 행에는 유저(case) 
        - 첫번째 행렬 열에는 선호도(weight)
    - 두번째 행렬 X 상품의 속성값
        - 두번째 행렬 행에는 속성(feature)
        - 두번째 행렬 열에는 상품(content)
2. theta @ X 연산
    - theta @ X 결과 만들어진 행렬은
        - 행 case에는 유저
        - 열 feature에는 상품이 있다
        - 값은 예측 평점
3. 실제 평점 데이터와 비교한다
    - 실제 평점 데이터는 
        - 행 유저 
        - 열 상품
        - 값 실제 평점

$n^{(i)}_{j}$는 i행 j열 값을 말한다

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3666&directory=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-09-22%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%206.13.35.png&name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-09-22+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+6.13.35.png)

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3666&directory=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-09-22%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%206.23.41.png&name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-09-22+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+6.23.41.png)

영화의 로맨스, 코미디 속성 값과 유저의 로맨스, 코미디 선호도(가중치)를 각각 곱해서 그 영화의 선호도를 예측할 수 있다

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3666&directory=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-09-22%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%206.17.22.png&name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-09-22+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+6.17.22.png)

실제 평점 데이터는 $y^{i, j}$로 표현한다
![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3666&directory=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-09-22%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%206.18.20.png&name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-09-22+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+6.18.20.png)


실제 평점 데이터가 있는지 유무를 나타내는 $r^{i,j}$는 1 또는 0의 값을 갖는다
![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3666&directory=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-09-22%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%206.19.02.png&name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-09-22+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+6.19.02.png)

### <a id='toc1_4_2_'></a>[손실함수](#toc0_)

실제값이 있으니 MSE와 유사하게 쓴다

$J(\Theta, X) = {1 \over 2}{\displaystyle\sum_{i,j:r^{(i,j)=1}}{((\theta^{(i)})^Tx^{(j)}-y^{(i,j)})^2}}$

- 1/2은 경사하강법을 편하게 하기 위함이라고 한다
- ${((\theta^{(i)})^Tx^{(j)}-y^{(i,j)})^2}$은 예측값에서 실제값을 뺀 오차의 제곱이다 즉 SE다
- $\displaystyle\sum_{i,j:r^{(i,j)=1}}$은 실측 값이 있을 경우에 더하라는 뜻이다
- 아직 왜 MSE처럼 평균을 쓰지는 않는 건지 왜 2로 나누는지 잘 모르겠다
    - 평균을 쓰나 오차 제곱을 쓰나 거기서 거기라 그렇다는 의견도 있는데 그럼 2로 왜 나눌까

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3668&directory=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-09-23%20%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB%209.12.14.png&name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-09-23+%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB+9.12.14.png)


```python
def cost(prediction, R):
    """행렬 인수분해 알고리즘의 손실을 계산해주는 함수"""
    # 여기에 코드를 작성하세요
    return np.nansum((prediction-R)**2)
                
    
# 테스트 코드



# 예측 값 행렬
prediction = np.array([
    [4, 4, 1, 1, 2, 2],
    [4, 4, 3, 1, 5, 5],
    [2, 2, 1, 1, 3, 4],
    [1, 3, 1, 4, 2, 2],
    [1, 2, 4, 1, 2, 5],
    ])

# 실제 값 행렬
R = np.array([
    [3, 4, 1, np.nan, 1, 2],
    [4, 4, 3, np.nan, 5, 3],
    [2, 3, np.nan, 1, 3, 4],
    [1, 3, 2, 4, 2, 2],
    [1, 2, np.nan, 2, 2, 4],
    ])

cost(prediction, R)
```




    10.0



#### <a id='toc1_4_2_1_'></a>[행렬 인수분해 손실함수 볼록도](#toc0_)

변수가 여러개라서 아래로 볼록하지 않다. 최소점이 아니라 극소점을 찾게 될 수 있다  
경사하강의 시작점을 여러개 랜덤으로 돌리면서 최소점을 찾아볼 수 있다고도 한다  
그게 가장 나은 해결책은 아닐 거 같은데?


![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3669&directory=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-09-23%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2012.53.49.png&name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-09-23+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+12.53.49.png)

### <a id='toc1_4_3_'></a>[경사하강법](#toc0_)
---
유저선호도  


${\theta^{(i)}_k} {\larr} \ {\theta^{(i)}_k} - \alpha {\partial \over {\partial \theta^{(i)}_k}} {J(\theta, X)} $

이걸 손실함수를 넣고 정리하면

${\theta^{(i)}_k} {\larr} \ {\theta^{(i)}_k} - \alpha {\displaystyle \sum_{j:r^{(i,j)}} ({(\theta^{(i)})^T x^{(j)}}-y^{(i,j)})x^{(j)}_k } $

---

영화 속성

${x^{(j)}_k} {\larr} \ {x^{(j)}_k} - \alpha {\partial \over {\partial x^{(j)}_k}} {J(\theta, X)} $

이걸 손실함수를 넣고 정리하면

${x^{(j)}_k} {\larr} \ {x^{(j)}_k} - \alpha {\displaystyle \sum_{i:r^{(i,j)}} ({(\theta^{(i)})^T x^{(j)}}-y^{(i,j)})\theta^{(i)}_k } $

---

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3671&directory=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-09-23%20%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB%209.22.19.png&name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-09-23+%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB+9.22.19.png)

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3671&directory=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-09-23%20%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB%209.29.57.png&name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-09-23+%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB+9.29.57.png)

### <a id='toc1_4_4_'></a>[정규화](#toc0_)
---
상수값이 커지면 과적합되는 문제가 발생한다  
따라서 손실함수에 상수항의 합을 추가시켜서 상수항의 합도 최소화시키면 과적합을 줄일 수 있다

다항 회귀에서 L1, L2 등으로 했던 내용과 동일하다  
여기선 L2 즉 모든 파라미터를 제곱해서 손실함수에 더하는 방법을 쓴다


${\theta^{(i)}_k} {\larr} \ {\theta^{(i)}_k} - \alpha ({\displaystyle \sum_{j:r^{(i,j)}} ({(\theta^{(i)})^T x^{(j)}}-y^{(i,j)})x^{(j)}_k + \lambda \theta^{(i)}_k}) $

${x^{(j)}_k} {\larr} \ {x^{(j)}_k} - \alpha ({\displaystyle \sum_{i:r^{(i,j)}} ({(\theta^{(i)})^T x^{(j)}}-y^{(i,j)})\theta^{(i)}_k + \lambda x^{(j)}_k}) $

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3673&directory=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-09-23%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%201.06.06.png&name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-09-23+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+1.06.06.png)

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3673&directory=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-09-23%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%201.06.13.png&name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-09-23+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+1.06.13.png)


```python
# 체점을 위해 numpy에서 임의성 도구들의 결과가 일정하게 나오도록 해준다
np.random.seed(5)

def initialize(R, num_features):
    """임의로 유저 취향과 상품 속성 행렬들을 만들어주는 함수"""
    num_users, num_items = R.shape  # 유저 데이터 개수와 영화 개수를 변수에 저장
    ### 행은 앞에 거에 렬은 뒤에 거에 언팩 되는 구나
    
    # 여기에 코드를 작성하세요
    
    Theta = np.random.rand(num_users, num_features)
    X = np.random.rand(num_features, num_items)
    
    return Theta, X
    
    
# 실제 값 행렬
R = np.array([
    [3, 4, 1, np.nan, 1, 2],
    [4, 4, 3, np.nan, 5, 3],
    [2, 3, np.nan, 1, 3, 4],
    [1, 3, 2, 4, 2, 2],
    [1, 2, np.nan, 2, 2, 4],
    ])
    
    
Theta, X = initialize(R, 2)
Theta, X
```




    (array([[0.22199317, 0.87073231],
            [0.20671916, 0.91861091],
            [0.48841119, 0.61174386],
            [0.76590786, 0.51841799],
            [0.2968005 , 0.18772123]]),
     array([[0.08074127, 0.7384403 , 0.44130922, 0.15830987, 0.87993703,
             0.27408646],
            [0.41423502, 0.29607993, 0.62878791, 0.57983781, 0.5999292 ,
             0.26581912]]))




```python
# 체점을 위해 임의성을 사용하는 numpy 도구들의 결과가 일정하게 나오도록 해준다
np.random.seed(5)
# RATING_DATA_PATH = './data/ratings.csv'  # 데이터 파일 경로 정의
# numpy 출력 옵션 설정
np.set_printoptions(precision=2)
np.set_printoptions(suppress=True)

def predict(Theta, X):
    """유저 취향과 상품 속성을 곱해서 예측 값을 계산하는 함수"""
    return Theta @ X


def cost(prediction, R):
    """행렬 인수분해 알고리즘의 손실을 계산해주는 함수"""
    return np.nansum((prediction - R)**2)


def initialize(R, num_features):
    """임의로 유저 취향과 상품 속성 행렬들을 만들어주는 함수"""
    num_users, num_items = R.shape
    
    Theta = np.random.rand(num_users, num_features)
    X = np.random.rand(num_features, num_items)
    
    return Theta, X


def gradient_descent(R, Theta, X, iteration, alpha, lambda_):
    """행렬 인수분해 경사 하강 함수"""
    num_user, num_items = R.shape
    num_features = len(X)
    costs = []
        
    for _ in range(iteration):
        prediction = predict(Theta, X)
        error = prediction - R
        costs.append(cost(prediction, R))                          
        for i in range(num_user):
            for j in range(num_items):
                if not np.isnan(R[i][j]):
                    for k in range(num_features):
                        # 여기에 코드를 작성하세요-------------------------
                        # Theta[i][k] -= alpha * np.nansum(
                        #     ((error[i, :]) * X[k, :]) + (lambda_ * Theta[i][k])
                        # )
                        Theta[i][k] -= alpha * (np.nansum(error[i, :]*X[k, :]) + lambda_*Theta[i][k])
                        X[k][j] -= alpha * (np.nansum((error[:, j])*Theta[:, k]) + lambda_ * X[k][j])
                        
                        ### 정규화 항은 시그마에 포함되는 게 아니었다
                        
                        # X[k][j] -= alpha * np.nansum(((error[:, j])*Theta[:, k]) + lambda_ * X[k][j])
                        
    return Theta, X, costs


#----------------------테스트(채점) 코드----------------------
# 평점 데이터를 가지고 온다
ratings_df = pd.read_csv('ratings.csv', index_col='user_id')

# 평점 데이터에 mean normalization을 적용한다
for row in ratings_df.values:
    row -= np.nanmean(row)
       
R = ratings_df.values
        
Theta, X = initialize(R, 5)  # 행렬들 초기화
Theta, X, costs = gradient_descent(R, Theta, X, 200, 0.001, 0.01)  # 경사 하강
    
# 손실이 줄어드는 걸 시각화 하는 코드 (디버깅에 도움이 됨)
plt.plot(costs)

Theta, X
```




    (array([[-0.35,  1.56,  0.31, -0.21, -0.26],
            [ 0.92,  0.21,  0.36,  0.56,  0.99],
            [ 0.48,  0.55, -0.19,  0.06,  1.71],
            [-0.64,  1.03,  0.35, -0.32,  0.13],
            [-0.39, -0.68,  0.44,  0.05,  1.05],
            [ 0.07, -0.64,  0.92,  1.23, -0.58],
            [ 0.33,  0.93, -1.21,  2.09,  0.27],
            [ 0.79, -0.48,  1.12,  0.05,  0.46],
            [ 1.06, -0.68, -0.28,  0.18, -1.12],
            [ 0.39,  0.63,  0.14,  0.98,  0.1 ],
            [ 1.47,  0.62, -0.91, -0.29, -0.35],
            [-1.56,  0.77,  0.83,  1.1 ,  0.13],
            [-0.89,  0.47,  0.47, -0.25,  0.81],
            [ 0.86, -0.13, -1.01,  0.2 ,  0.76],
            [-0.53, -1.14, -0.47,  0.08, -0.72],
            [-0.27, -0.07,  0.41,  0.49,  1.5 ],
            [ 0.17, -0.01,  0.07, -1.66,  0.27],
            [ 1.32,  0.88,  0.83,  0.72, -1.09],
            [-0.17, -1.68,  1.86, -0.16, -0.26],
            [-0.88, -0.53, -1.33,  0.14,  0.19]]),
     array([[ 0.12,  0.48, -2.18, -0.67, -1.05,  0.41,  0.03, -0.37, -0.86,
              0.44, -0.71,  1.26, -0.55,  0.17,  0.74,  0.94, -0.07,  1.98,
              1.12,  0.68],
            [-0.61, -0.4 , -0.12,  0.11, -0.22,  0.1 ,  0.71, -0.36,  0.97,
              0.95,  0.62, -0.72,  0.26, -1.56,  0.18, -0.28, -0.29,  1.7 ,
              0.02, -0.87],
            [ 0.12,  1.59,  0.25,  1.02, -1.  ,  0.88, -0.27,  0.39,  0.33,
              0.48, -1.17, -0.05, -1.69,  0.65, -0.12, -1.09, -0.89, -0.35,
              0.65,  0.47],
            [ 0.33, -0.84, -0.73, -0.55,  0.11,  1.18, -1.  ,  0.15,  0.29,
             -0.21,  0.76,  0.46, -0.59, -0.5 , -0.92, -0.21,  0.86,  0.45,
              1.77, -0.02],
            [-0.75, -0.25, -0.72,  1.1 ,  0.94,  0.54,  0.55, -1.34, -1.28,
              1.08,  0.79,  0.63, -0.68,  0.21,  1.02, -0.46, -0.06, -0.81,
              0.93, -0.72]]))




    
![png](output_68_1.png)
    


이런 구조를 스스로 짤 수 있을까?  
지금 당장은 불가능에 가깝다  
한단계씩 올려서 스스로 만들 수 있을 때까지 성장하자

## <a id='toc1_5_'></a>[수료증](https://www.codeit.kr/certificates/UQohE-h8b80-s3MDT-2oqo1) [&#8593;](#toc0_)
