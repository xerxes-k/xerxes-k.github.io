---
layout: single
title:  "clustering"
---
**Table of contents**<a id='toc0_'></a>    
- [clustering](#toc1_)    
  - [군집화 방법의 종류](#toc1_1_)    
    - [맛보기 예시](#toc1_1_1_)    
    - [클러스터링의 원리](#toc1_1_2_)    
    - [공통적으로 필요한 전처리](#toc1_1_3_)    
      - [data cleaning](#toc1_1_3_1_)    
      - [데이터 표준화](#toc1_1_3_2_)    
    - [model and learning](#toc1_1_4_)    
    - [k-menas](#toc1_1_5_)    
      - [k-means는 k의 개수에 따라 성능이 달라진다](#toc1_1_5_1_)    
      - [elbow method](#toc1_1_5_2_)    
      - [결과 해석](#toc1_1_5_3_)    
      - [kmeans 장단점](#toc1_1_5_4_)    
      - [차원이 커질수록(변수가 많아질수록) 거리가 넓어지고 계산이 복잡해진다](#toc1_1_5_5_)    
    - [계층 Hierachical  Clustering (bottom up)](#toc1_1_6_)    
      - [Dendrogram 덴드로그램](#toc1_1_6_1_)    
      - [계층 특징](#toc1_1_6_2_)    
    - [밀도 DBSCAN](#toc1_1_7_)    
      - [임의 지정한 반경과 데이터 수에 해당하지 않는 데이터는 탈락된다. 고로 이상치outlier에도 결과가 끌려다니지 않으므로 강건robust하다](#toc1_1_7_1_)    
      - [밀도 특징](#toc1_1_7_2_)    
    - [분포 GMM Gaussian Mixture Model](#toc1_1_8_)    
      - [단점](#toc1_1_8_1_)    
  - [수료증](#toc1_2_)    

<!-- vscode-jupyter-toc-config
	numbering=false
	anchor=true
	flat=false
	minLevel=1
	maxLevel=6
	/vscode-jupyter-toc-config -->
<!-- THIS CELL WILL BE REPLACED ON TOC UPDATE. DO NOT WRITE YOUR TEXT IN THIS CELL -->

# <a id='toc1_'></a>[clustering](#toc0_)
---
주어진 데이터 집합을 유사한 데이터들의 그룹으로 나누는 것을 군집화(clustering)라 하고 이렇게 나누어진 유사한 데이터의 그룹을 군집(cluster)이라 한다.

군집화는 예측 문제와 달리 특정한 독립변수와 종속변수의 구분도 없고 학습을 위한 목푯값도 필요로 하지 않는 비지도학습의 일종이다.

https://datascienceschool.net/03%20machine%20learning/16.01%20%EA%B5%B0%EC%A7%91%ED%99%94.html#:~:text=%EC%A3%BC%EC%96%B4%EC%A7%84%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%A7%91%ED%95%A9%EC%9D%84%20%EC%9C%A0%EC%82%AC%ED%95%9C,%EA%B5%B0%EC%A7%91(cluster)%EC%9D%B4%EB%9D%BC%20%ED%95%9C%EB%8B%A4.

![비지도](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5823&directory=21-1.png&name=21-1.png)

## <a id='toc1_1_'></a>[군집화 방법의 종류](#toc0_)
---
1. K-평균 군집화(K-means Clustering)
2. 디비스캔 군집화(DBSCAN Clustering)
3. 계층적 군집화(Hierarchical Clustering)
4. GMM

- 그 외(tbd)
- 유사도 전파 군집화(Affinity Propagation Clustering)
- 스펙트럴 군집화(Spectral Clustering)


```python
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans, DBSCAN
from sklearn.mixture import GaussianMixture
```


```python
from scipy.cluster.hierarchy import dendrogram, linkage, cut_tree
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons, make_blobs
import numpy as np
```

### <a id='toc1_1_1_'></a>[맛보기 예시](#toc0_)


```python
user = pd.read_csv('app_users.csv', index_col=0)
user
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
      <th>visit_per_month</th>
      <th>use_time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>14</td>
      <td>22.8</td>
    </tr>
    <tr>
      <th>1</th>
      <td>32</td>
      <td>13.6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8</td>
      <td>3.1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>13</td>
      <td>5.7</td>
    </tr>
    <tr>
      <th>4</th>
      <td>19</td>
      <td>20.8</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>495</th>
      <td>26</td>
      <td>3.8</td>
    </tr>
    <tr>
      <th>496</th>
      <td>10</td>
      <td>7.6</td>
    </tr>
    <tr>
      <th>497</th>
      <td>17</td>
      <td>9.7</td>
    </tr>
    <tr>
      <th>498</th>
      <td>14</td>
      <td>7.6</td>
    </tr>
    <tr>
      <th>499</th>
      <td>29</td>
      <td>3.7</td>
    </tr>
  </tbody>
</table>
<p>500 rows × 2 columns</p>
</div>




```python
sns.set(style='darkgrid', rc={'figure.figsize':(16,9)})
sns.scatterplot(data=user, x='visit_per_month', y='use_time', s=100)
```




    <Axes: xlabel='visit_per_month', ylabel='use_time'>




    
![png](output_8_1.png)
    



```python
md = KMeans(n_clusters=3, random_state=123)
md.fit(user)
user['label'] = md.predict(user)
user.groupby('label').count()
```

    c:\Users\path1\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\cluster\_kmeans.py:870: FutureWarning: The default value of `n_init` will change from 10 to 'auto' in 1.4. Set the value of `n_init` explicitly to suppress the warning
      warnings.warn(
    




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
      <th>visit_per_month</th>
      <th>use_time</th>
    </tr>
    <tr>
      <th>label</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>228</td>
      <td>228</td>
    </tr>
    <tr>
      <th>1</th>
      <td>146</td>
      <td>146</td>
    </tr>
    <tr>
      <th>2</th>
      <td>126</td>
      <td>126</td>
    </tr>
  </tbody>
</table>
</div>




```python
sns.scatterplot(data=user, x='visit_per_month', y='use_time', s=100, hue = user['label'], palette='bright')
```




    <Axes: xlabel='visit_per_month', ylabel='use_time'>




    
![png](output_10_1.png)
    


### <a id='toc1_1_2_'></a>[클러스터링의 원리](#toc0_)
---
- 유사한 데이터는 같은 클러스터로 묶는다.
- 유사하지 않은 데이터는 같은 클러스터로 묶지 않는다.

유사하다의 기준은 여러가지가 있는데 그 중 하나는 '거리가 가까울 수록 유사하다'이다

![클러스터](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5804&directory=2-1.png&name=2-1.png)

### <a id='toc1_1_3_'></a>[공통적으로 필요한 전처리](#toc0_)
---
- 데이터 정리
- 표준화

#### <a id='toc1_1_3_1_'></a>[data cleaning](#toc0_)
---


```python
pd.options.display.float_format = '{:,.2f}'.format
```


```python
sales = pd.read_csv('sales_data.csv', index_col=['customer_id'])
sales
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
      <th>total_buy_cnt</th>
      <th>total_price</th>
    </tr>
    <tr>
      <th>customer_id</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>12395</th>
      <td>99</td>
      <td>430250</td>
    </tr>
    <tr>
      <th>12427</th>
      <td>98</td>
      <td>566410</td>
    </tr>
    <tr>
      <th>12431</th>
      <td>122</td>
      <td>849900</td>
    </tr>
    <tr>
      <th>12433</th>
      <td>625</td>
      <td>1180950</td>
    </tr>
    <tr>
      <th>12471</th>
      <td>10</td>
      <td>97750</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>18144</th>
      <td>30</td>
      <td>90750</td>
    </tr>
    <tr>
      <th>18168</th>
      <td>243</td>
      <td>1533530</td>
    </tr>
    <tr>
      <th>18225</th>
      <td>1</td>
      <td>91430</td>
    </tr>
    <tr>
      <th>18229</th>
      <td>48</td>
      <td>559510</td>
    </tr>
    <tr>
      <th>18239</th>
      <td>230</td>
      <td>1114480</td>
    </tr>
  </tbody>
</table>
<p>254 rows × 2 columns</p>
</div>




```python
sns.scatterplot(data=sales, x='total_buy_cnt', y='total_price')
```




    <Axes: xlabel='total_buy_cnt', ylabel='total_price'>




    
![png](output_18_1.png)
    



```python
def outoutlier(df, weight=1.5):
    Q1 = df.quantile(0.15)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    IQR_weight = IQR * weight
    min = Q1 - IQR_weight
    max = Q3 + IQR_weight
    outlier = (df < min) | (df > max)
    isoutlier = outlier.any(axis=1)
    return isoutlier
```


```python
outlier = outoutlier(sales)
```


```python
sales = sales[~outlier]
```


```python
sns.scatterplot(data=sales, x='total_buy_cnt', y='total_price', s=200)
```




    <Axes: xlabel='total_buy_cnt', ylabel='total_price'>




    
![png](output_22_1.png)
    


#### <a id='toc1_1_3_2_'></a>[데이터 표준화](#toc0_)
---


```python
df_mean = sales.mean()
df_std = sales.std()
scaled = (sales - df_mean) / df_std
scaled.index = sales.index
scaled
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
      <th>total_buy_cnt</th>
      <th>total_price</th>
    </tr>
    <tr>
      <th>customer_id</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>12395</th>
      <td>-0.09</td>
      <td>-0.17</td>
    </tr>
    <tr>
      <th>12427</th>
      <td>-0.11</td>
      <td>0.18</td>
    </tr>
    <tr>
      <th>12431</th>
      <td>0.16</td>
      <td>0.91</td>
    </tr>
    <tr>
      <th>12471</th>
      <td>-1.09</td>
      <td>-1.03</td>
    </tr>
    <tr>
      <th>12472</th>
      <td>-0.22</td>
      <td>0.19</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>18144</th>
      <td>-0.87</td>
      <td>-1.05</td>
    </tr>
    <tr>
      <th>18168</th>
      <td>1.52</td>
      <td>2.68</td>
    </tr>
    <tr>
      <th>18225</th>
      <td>-1.19</td>
      <td>-1.05</td>
    </tr>
    <tr>
      <th>18229</th>
      <td>-0.67</td>
      <td>0.16</td>
    </tr>
    <tr>
      <th>18239</th>
      <td>1.38</td>
      <td>1.60</td>
    </tr>
  </tbody>
</table>
<p>228 rows × 2 columns</p>
</div>



### <a id='toc1_1_4_'></a>[model and learning](#toc0_)
---

- 모델
  - 분석 방법론
  - 분석 방법을 통해 얻은 결과를 저장한 프로그램

- 학습
  - 모델에 데이터를 전달하여 결과를 만들게 하는 과정

### <a id='toc1_1_5_'></a>[k-menas](#toc0_)
---
- 가정: 유사한 데이터는 Centroid(중심점)로부터 가까이에 모여있다.

1. Centroid 배치  
먼저, 클러스터의 개수를 의미하는 k를 정해 줘야 합니다. 예시에서는 2로 설정할게요. 그리고, k의 값만큼 Centroid를 생성하여 임의로 배치합니다.

![k](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5807&directory=5-1.png&name=5-1.png)

2. cluster 형성  
생성한 Centroid와 각 데이터 사이의 거리를 계산하여 가까이에 있는 데이터들을 하나의 클러스터로 묶어줍니다.

![k2](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5807&directory=5-2.png&name=5-2.png)

3. centroid 위치 갱신  
클러스터에 속해있는 데이터들의 중심으로 Centroid의 위치를 이동합니다. 이때, 데이터들 사이의 중심을 찾기 위하여 평균값(means)을 사용합니다.

![3](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5807&directory=5-3.png&name=5-3.png)

4. 클러스터 재형성
5. centroid 위치 갱신

![4](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5807&directory=5-4.png&name=5-4.png)
![5](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5807&directory=5-5.png&name=5-5.png)

scikit으로 K-means 모델링 할 때
```python
model = KMeans(n_clusters=2, random_state=123) #모델을 만들고
model.fit(scaled_df) #메소드로 학습을 시킨다 이 때 사용할 데이터를 인자로 준다
scaled_df['label'] = model.predict(scaled_df) # 레이블 칼럼을 추가해서 모델이 학습 결과(예측값)를 저장한다

centers = model.cluster_centers_ ## 모델의 클러스터 센터를 받아온다

sns.scatterplot(x=scaled_df['total_buy_cnt'], y=scaled_df['total_price'], hue=scaled_df['label'], s=200, palette='bright')

sns.scatterplot(x=centers[:,0], y=centers[:,1], color='black', alpha=0.8, s=400) # 중심을 표시해준다?
```


```python
model = KMeans(n_clusters=4, random_state=123)
model.fit(scaled)
scaled['label'] = model.predict(scaled)
```

    c:\Users\path1\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\cluster\_kmeans.py:870: FutureWarning: The default value of `n_init` will change from 10 to 'auto' in 1.4. Set the value of `n_init` explicitly to suppress the warning
      warnings.warn(
    


```python
scaled
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
      <th>total_buy_cnt</th>
      <th>total_price</th>
      <th>label</th>
    </tr>
    <tr>
      <th>customer_id</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>12395</th>
      <td>-0.09</td>
      <td>-0.17</td>
      <td>1</td>
    </tr>
    <tr>
      <th>12427</th>
      <td>-0.11</td>
      <td>0.18</td>
      <td>1</td>
    </tr>
    <tr>
      <th>12431</th>
      <td>0.16</td>
      <td>0.91</td>
      <td>0</td>
    </tr>
    <tr>
      <th>12471</th>
      <td>-1.09</td>
      <td>-1.03</td>
      <td>3</td>
    </tr>
    <tr>
      <th>12472</th>
      <td>-0.22</td>
      <td>0.19</td>
      <td>1</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>18144</th>
      <td>-0.87</td>
      <td>-1.05</td>
      <td>3</td>
    </tr>
    <tr>
      <th>18168</th>
      <td>1.52</td>
      <td>2.68</td>
      <td>2</td>
    </tr>
    <tr>
      <th>18225</th>
      <td>-1.19</td>
      <td>-1.05</td>
      <td>3</td>
    </tr>
    <tr>
      <th>18229</th>
      <td>-0.67</td>
      <td>0.16</td>
      <td>1</td>
    </tr>
    <tr>
      <th>18239</th>
      <td>1.38</td>
      <td>1.60</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
<p>228 rows × 3 columns</p>
</div>




```python
scaled['label'].value_counts()
```




    label
    3    84
    1    77
    0    46
    2    21
    Name: count, dtype: int64




```python
sns.scatterplot(data = scaled, x = 'total_buy_cnt', y = 'total_price', hue=scaled['label'], s=200, palette='bright')
```




    <Axes: xlabel='total_buy_cnt', ylabel='total_price'>




    
![png](output_39_1.png)
    



```python
centers = model.cluster_centers_ 
```


```python
sns.scatterplot(data = scaled, x = 'total_buy_cnt', y = 'total_price', hue=scaled['label'], s=200, palette='bright')
sns.scatterplot(x=centers[:,0], y=centers[:,1], color='black', alpha=0.8, s=400)
```




    <Axes: xlabel='total_buy_cnt', ylabel='total_price'>




    
![png](output_41_1.png)
    


#### <a id='toc1_1_5_1_'></a>[k-means는 k의 개수에 따라 성능이 달라진다](#toc0_)
---
최적의 k를 알기 위해서는 k-means가 잘됐다는 걸 판단할 수 있는 기준이 필요하다
- k개의 centroid에 모인 데이터를 각각 클러스터로 묶어주는 방법이다
- 따라서 각 클러스터 마다 데이터와 centroid 사이의 거리 합이 작을 수록 좋은 클러스터링이다
- 데이터와 centroid 사이 거리의 제곱을 모두 더한 값이 inertia다
- kmeans() 학습시키면 inertia_라는 변수로 생성된다


```python
model.inertia_
```




    78.08220285788859



이 값을 비교하기 위해 여러 k를 사용해봐야 한다


```python
scaled = scaled.drop(['label'], axis=1)
```

#### <a id='toc1_1_5_2_'></a>[elbow method](#toc0_)


```python
inertias = []
for k in range(1, 16):
    model = KMeans(n_clusters=k, random_state=123)
    model.fit(scaled)
    inertias.append(model.inertia_)

sns.lineplot(x=range(1,16), y=inertias, marker='o')    
```

    c:\Users\path1\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\cluster\_kmeans.py:870: FutureWarning: The default value of `n_init` will change from 10 to 'auto' in 1.4. Set the value of `n_init` explicitly to suppress the warning
      warnings.warn(
    c:\Users\path1\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\cluster\_kmeans.py:870: FutureWarning: The default value of `n_init` will change from 10 to 'auto' in 1.4. Set the value of `n_init` explicitly to suppress the warning
      warnings.warn(
    c:\Users\path1\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\cluster\_kmeans.py:870: FutureWarning: The default value of `n_init` will change from 10 to 'auto' in 1.4. Set the value of `n_init` explicitly to suppress the warning
      warnings.warn(
    c:\Users\path1\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\cluster\_kmeans.py:870: FutureWarning: The default value of `n_init` will change from 10 to 'auto' in 1.4. Set the value of `n_init` explicitly to suppress the warning
      warnings.warn(
    c:\Users\path1\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\cluster\_kmeans.py:870: FutureWarning: The default value of `n_init` will change from 10 to 'auto' in 1.4. Set the value of `n_init` explicitly to suppress the warning
      warnings.warn(
    c:\Users\path1\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\cluster\_kmeans.py:870: FutureWarning: The default value of `n_init` will change from 10 to 'auto' in 1.4. Set the value of `n_init` explicitly to suppress the warning
      warnings.warn(
    c:\Users\path1\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\cluster\_kmeans.py:870: FutureWarning: The default value of `n_init` will change from 10 to 'auto' in 1.4. Set the value of `n_init` explicitly to suppress the warning
      warnings.warn(
    c:\Users\path1\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\cluster\_kmeans.py:870: FutureWarning: The default value of `n_init` will change from 10 to 'auto' in 1.4. Set the value of `n_init` explicitly to suppress the warning
      warnings.warn(
    c:\Users\path1\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\cluster\_kmeans.py:870: FutureWarning: The default value of `n_init` will change from 10 to 'auto' in 1.4. Set the value of `n_init` explicitly to suppress the warning
      warnings.warn(
    c:\Users\path1\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\cluster\_kmeans.py:870: FutureWarning: The default value of `n_init` will change from 10 to 'auto' in 1.4. Set the value of `n_init` explicitly to suppress the warning
      warnings.warn(
    c:\Users\path1\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\cluster\_kmeans.py:870: FutureWarning: The default value of `n_init` will change from 10 to 'auto' in 1.4. Set the value of `n_init` explicitly to suppress the warning
      warnings.warn(
    c:\Users\path1\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\cluster\_kmeans.py:870: FutureWarning: The default value of `n_init` will change from 10 to 'auto' in 1.4. Set the value of `n_init` explicitly to suppress the warning
      warnings.warn(
    c:\Users\path1\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\cluster\_kmeans.py:870: FutureWarning: The default value of `n_init` will change from 10 to 'auto' in 1.4. Set the value of `n_init` explicitly to suppress the warning
      warnings.warn(
    c:\Users\path1\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\cluster\_kmeans.py:870: FutureWarning: The default value of `n_init` will change from 10 to 'auto' in 1.4. Set the value of `n_init` explicitly to suppress the warning
      warnings.warn(
    c:\Users\path1\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\cluster\_kmeans.py:870: FutureWarning: The default value of `n_init` will change from 10 to 'auto' in 1.4. Set the value of `n_init` explicitly to suppress the warning
      warnings.warn(
    




    <Axes: >




    
![png](output_47_2.png)
    


클러스터의 수가 많아지면 inertia도 줄어든다  
그러나 극단적인 경우 모든 데이터가 개별로 클러스터가 되면 inertia는 0이 된다  
즉 k의 값이 클수록 inertia가 작아지지만 의미는 없다

최적의 클러스터 개수는 inertia가 충분히 작지만, 분석 목적에 부합하도록 적당해야 합니다. 그리고, 보통 그 지점은 시각화 한 그래프의 기울기가 급격하게 줄어드는 구간으로 정의합니다.

라고 하는데 k 증가 당 inertia의 감소가 작아지는 구간에서 정하는 걸 얘기하는 듯

이렇게 k가 증가함에 따라 inertia가 줄어드는 정도가 급격하게 작아지는 지점을 찾으면 최적 클러스터 개수에 대한 힌트를 얻을 수 있는데요. 이때 시각화한 그래프의 모습이 마치 팔꿈치 모양 같다고 해서 Elbow Method라고 부릅니다.

#### <a id='toc1_1_5_3_'></a>[결과 해석](#toc0_)
---


```python
sales = sales.drop(['label'], axis=1)
sales
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
      <th>total_buy_cnt</th>
      <th>total_price</th>
    </tr>
    <tr>
      <th>customer_id</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>12395</th>
      <td>99</td>
      <td>430250</td>
    </tr>
    <tr>
      <th>12427</th>
      <td>98</td>
      <td>566410</td>
    </tr>
    <tr>
      <th>12431</th>
      <td>122</td>
      <td>849900</td>
    </tr>
    <tr>
      <th>12471</th>
      <td>10</td>
      <td>97750</td>
    </tr>
    <tr>
      <th>12472</th>
      <td>88</td>
      <td>568740</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>18144</th>
      <td>30</td>
      <td>90750</td>
    </tr>
    <tr>
      <th>18168</th>
      <td>243</td>
      <td>1533530</td>
    </tr>
    <tr>
      <th>18225</th>
      <td>1</td>
      <td>91430</td>
    </tr>
    <tr>
      <th>18229</th>
      <td>48</td>
      <td>559510</td>
    </tr>
    <tr>
      <th>18239</th>
      <td>230</td>
      <td>1114480</td>
    </tr>
  </tbody>
</table>
<p>228 rows × 2 columns</p>
</div>




```python
model = KMeans(n_clusters=5, random_state=123)
model.fit(scaled)
inertias.append(model.inertia_)
```

    c:\Users\path1\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\cluster\_kmeans.py:870: FutureWarning: The default value of `n_init` will change from 10 to 'auto' in 1.4. Set the value of `n_init` explicitly to suppress the warning
      warnings.warn(
    


```python
sales.loc[:, 'label'] = model.predict(scaled)
sales
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
      <th>total_buy_cnt</th>
      <th>total_price</th>
      <th>label</th>
    </tr>
    <tr>
      <th>customer_id</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>12395</th>
      <td>99</td>
      <td>430250</td>
      <td>0</td>
    </tr>
    <tr>
      <th>12427</th>
      <td>98</td>
      <td>566410</td>
      <td>0</td>
    </tr>
    <tr>
      <th>12431</th>
      <td>122</td>
      <td>849900</td>
      <td>2</td>
    </tr>
    <tr>
      <th>12471</th>
      <td>10</td>
      <td>97750</td>
      <td>3</td>
    </tr>
    <tr>
      <th>12472</th>
      <td>88</td>
      <td>568740</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>18144</th>
      <td>30</td>
      <td>90750</td>
      <td>3</td>
    </tr>
    <tr>
      <th>18168</th>
      <td>243</td>
      <td>1533530</td>
      <td>1</td>
    </tr>
    <tr>
      <th>18225</th>
      <td>1</td>
      <td>91430</td>
      <td>3</td>
    </tr>
    <tr>
      <th>18229</th>
      <td>48</td>
      <td>559510</td>
      <td>0</td>
    </tr>
    <tr>
      <th>18239</th>
      <td>230</td>
      <td>1114480</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>228 rows × 3 columns</p>
</div>




```python
sales
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
      <th>total_buy_cnt</th>
      <th>total_price</th>
      <th>label</th>
    </tr>
    <tr>
      <th>customer_id</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>12395</th>
      <td>99</td>
      <td>430250</td>
      <td>0</td>
    </tr>
    <tr>
      <th>12427</th>
      <td>98</td>
      <td>566410</td>
      <td>0</td>
    </tr>
    <tr>
      <th>12431</th>
      <td>122</td>
      <td>849900</td>
      <td>2</td>
    </tr>
    <tr>
      <th>12471</th>
      <td>10</td>
      <td>97750</td>
      <td>3</td>
    </tr>
    <tr>
      <th>12472</th>
      <td>88</td>
      <td>568740</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>18144</th>
      <td>30</td>
      <td>90750</td>
      <td>3</td>
    </tr>
    <tr>
      <th>18168</th>
      <td>243</td>
      <td>1533530</td>
      <td>1</td>
    </tr>
    <tr>
      <th>18225</th>
      <td>1</td>
      <td>91430</td>
      <td>3</td>
    </tr>
    <tr>
      <th>18229</th>
      <td>48</td>
      <td>559510</td>
      <td>0</td>
    </tr>
    <tr>
      <th>18239</th>
      <td>230</td>
      <td>1114480</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>228 rows × 3 columns</p>
</div>




```python
sns.scatterplot(data = sales, x = 'total_buy_cnt', y = 'total_price', hue=sales['label'], s=200, palette='bright')
```




    <Axes: xlabel='total_buy_cnt', ylabel='total_price'>




    
![png](output_57_1.png)
    



```python
sales['label'].value_counts()
```




    label
    3    76
    0    66
    2    32
    4    30
    1    24
    Name: count, dtype: int64




```python
rst = sales.groupby('label').mean()
rst['mean'] =  rst['total_price'] / rst['total_buy_cnt']
rst
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
      <th>total_buy_cnt</th>
      <th>total_price</th>
      <th>mean</th>
    </tr>
    <tr>
      <th>label</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>90.36</td>
      <td>430,419.85</td>
      <td>4,763.20</td>
    </tr>
    <tr>
      <th>1</th>
      <td>296.17</td>
      <td>1,189,165.42</td>
      <td>4,015.19</td>
    </tr>
    <tr>
      <th>2</th>
      <td>127.78</td>
      <td>963,223.12</td>
      <td>7,538.06</td>
    </tr>
    <tr>
      <th>3</th>
      <td>25.46</td>
      <td>124,004.74</td>
      <td>4,870.47</td>
    </tr>
    <tr>
      <th>4</th>
      <td>179.53</td>
      <td>536,416.00</td>
      <td>2,987.84</td>
    </tr>
  </tbody>
</table>
</div>



#### <a id='toc1_1_5_4_'></a>[kmeans 장단점](#toc0_)
---
- 장점
  - 데이터 간의 거리만으로 사용할 수 있다
- 단점
  - 최적의 k를 알기 어렵다
  - 이상치에 민감하다
  - 초기 centroid 설정에 민감하다 >>> kmeas++ 모델 등장 (centroid 배치 개선)
    - model = KMeans(init='k-means++') 로 사용
  - 차원이 높은 데이터에 사용 불리

![2](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5814&directory=12-2.1.png&name=12-2.1.png)

#### <a id='toc1_1_5_5_'></a>[차원이 커질수록(변수가 많아질수록) 거리가 넓어지고 계산이 복잡해진다](#toc0_)

![3](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5814&directory=12-3.1.png&name=12-3.1.png)


### <a id='toc1_1_6_'></a>[계층 Hierachical  Clustering (bottom up)](#toc0_)
---

#### <a id='toc1_1_6_1_'></a>[Dendrogram 덴드로그램](#toc0_)
---
계층을 표현한 아래 같은 그림을 덴드로그램이라 부른다

![계층](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5816&directory=14-1.png&name=14-1.png)

ward: 인접한 다른 클러스터를 더했을 때 증가하는 inertia의 크기


```python
model = linkage(scaled, 'ward') #using ward method for distance
```


```python
labellist = scaled.index
plt.figure(figsize=(16,9))
plt.style.use('default')
dendrogram(model, labels=labellist)
plt.show()
```


    
![png](output_67_0.png)
    



```python
cluster = 5
scaled['label'] = cut_tree(model, cluster)
scaled['label'].value_counts()
```




    label
    0    80
    2    77
    3    28
    1    27
    4    16
    Name: count, dtype: int64




```python
sns.set(style="darkgrid",
        rc = {'figure.figsize':(16,9)})
sns.scatterplot(data = scaled, x = 'total_price', y = 'total_buy_cnt', hue = 'label', palette='bright')
```




    <Axes: xlabel='total_price', ylabel='total_buy_cnt'>




    
![png](output_69_1.png)
    


#### <a id='toc1_1_6_2_'></a>[계층 특징](#toc0_)
---
- k를 가정하지 않아도 된다
- 모든 데이터 끼리의 거리를 반복 계산하므로 데이터가 커질수록 연산이 급격히 늘어난다

### <a id='toc1_1_7_'></a>[밀도 DBSCAN](#toc0_)
density based spatial clustering of applications with noise

---

![밀도](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5816&directory=14-2.png&name=14-2.png)

"어떤 데이터가 특정 클러스터에 속할 경우, 클러스터 내의 다른 데이터들과 가까운 위치에 있어야 한다."
- 얼마나 많은 데이터
- 얼마나 가까운 위치

이 두 가지는 모델 학습 시 임의로 지정해 줘야 하는 값입니다. 얼마나 가까운 위치에 데이터가 있어야 하는지 나타내는 반경(Radius), 반경 내에 얼마나 많은 데이터가 있어야 하는지를 나타내는 최소 데이터 개수(Minimum Points)를 어떻게 지정해 주느냐에 따라 결과가 달라집니다.

![dbscan](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5819&directory=17-3.png&name=17-3.png)

#### <a id='toc1_1_7_1_'></a>[임의 지정한 반경과 데이터 수에 해당하지 않는 데이터는 탈락된다. 고로 이상치outlier에도 결과가 끌려다니지 않으므로 강건robust하다](#toc0_)

![db](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5819&directory=17-4.png&name=17-4.png)

#### <a id='toc1_1_7_2_'></a>[밀도 특징](#toc0_)
---
- 이상치에 강건하다
- 고차원으로 갈수록 계산이 어렵다


```python
n = 1000
np.random.seed(3)
X, y = make_moons(n_samples=n, noise=0.05) #noise가 0이면 정확한 반원이 된다?
df = pd.DataFrame(X)
sns.scatterplot(data = df, x=0, y=1, s=150)
# df
```




    <Axes: xlabel='0', ylabel='1'>




    
![png](output_76_1.png)
    



```python
eps = 0.1 # distance
min_n = 5 # min num of data to be included

model = DBSCAN(eps=eps, min_samples=min_n)
model.fit(df)
df['dbscan_label'] = model.labels_ # model.preidct()처럼 매소드가 아니라 속성 값이다

sns.scatterplot(data = df, x=0, y=1, s=150, hue='dbscan_label')
```




    <Axes: xlabel='0', ylabel='1'>




    
![png](output_77_1.png)
    


### <a id='toc1_1_8_'></a>[분포 GMM Gaussian Mixture Model](#toc0_)

정규분포를 가정  
어떤 값이 있으면 평균을 기준으로 어떤 값에 속할 확률이 더 높은지 계산  
평균과 분산이 있는(원형이 아니라 타원형으로 흩어진) 데이터에 최적

---

#### <a id='toc1_1_8_1_'></a>[단점](#toc0_)
- 클러스터 개수 가정 필요
- 충분한 모수가 있어야 추정 가능
- 정규 분포를 가정

![분포](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5816&directory=14-3.png&name=14-3.png)


```python
n = 500
center = 4
std = 0.75
rand = 13

data, cluster = make_blobs(n_samples=n, centers=center, cluster_std=std, random_state=rand)

tf = [[0.6, -0.6], [-0.4, 0.8]]
data_tf = data @ tf  # @ : 행렬의 곱을 나타냄
df = pd.DataFrame(data_tf)

sns.scatterplot(x=df[0], y=df[1], alpha = 0.7, edgecolor="k", s=200)
```




    <Axes: xlabel='0', ylabel='1'>




    
![png](output_81_1.png)
    



```python
n_comp = 4
rand_state = 10
model = GaussianMixture(n_components=n_comp, random_state=rand_state)
```


```python
df.columns = df.columns.astype(str)
model.fit(df)
df['gmm'] = model.predict(df)
# df.columns = df.columns.astype(str)
sns.scatterplot(data = df, x='0', y='1',  hue=df['gmm'], palette='rainbow', alpha=0.7, s=200)
```




    <Axes: xlabel='0', ylabel='1'>




    
![png](output_83_1.png)
    


## <a id='toc1_2_'></a>[수료증](https://www.codeit.kr/certificates/WvT2Z-sIAtM-YysaH-Di2FZ) [&#8593;](#toc0_)
