**Table of contents**<a id='toc0_'></a>    
- [data science](#toc1_)    
  - [정의](#toc1_1_)    
  - [data engineering](#toc1_2_)    
  - [data science](#toc1_3_)    
    - [steps](#toc1_3_1_)    
  - [numpy](#toc1_4_)    
  - [pandas dataframe](#toc1_5_)    
  - [수료증](#toc1_6_)    

<!-- vscode-jupyter-toc-config
	numbering=false
	anchor=true
	flat=false
	minLevel=1
	maxLevel=6
	/vscode-jupyter-toc-config -->
<!-- THIS CELL WILL BE REPLACED ON TOC UPDATE. DO NOT WRITE YOUR TEXT IN THIS CELL -->

# <a id='toc1_'></a>[data science](#toc0_)

## <a id='toc1_1_'></a>[정의](#toc0_)
---
위키피디아  
Data science is an interdisciplinary academic field [1] that uses statistics, scientific computing, scientific methods, processes, algorithms and systems to extract or extrapolate knowledge and insights from noisy, structured, and unstructured data.[2]

drew conway: 프로그래밍, 수학 통계, 전문분야 필요

![drew](https://international.binus.ac.id/computer-science/files/2020/10/Screen-Shot-2020-10-28-at-9.19.43-AM-1200x649.png)

"실리콘 벨리에 사는 통계학자가 데이터 사이언티스트다"  
"맥북으로 하는 통계가 데이터 사이언스다"

데이터를 저장하고 분석하는 능력이 발전함에 따라 데이터 분석 능력이 필수가 됐다

## <a id='toc1_2_'></a>[data engineering](#toc0_)
---
1. collect
2. store
3. process  

## <a id='toc1_3_'></a>[data science](#toc0_)
---
4. analysis
5. ab test
6. artificial intelligence
    - machine learning
      - deep learning

### <a id='toc1_3_1_'></a>[steps](#toc0_)
---
- goal setting
  - what to know, what to ask
  - period
  - how to evaluate the result
  - data property
- collect
- process
- analyze
- communicate

## <a id='toc1_4_'></a>[numpy](#toc0_)


```python
import numpy as np
a1 = np.array([1,2,3])
# np.array에 파이썬 리스트를 인수로 넘긴다
print(a1)
print(type(a1))
# nd array menas n-dimension array
print(a1.shape)
print(a1.size)
```

    [1 2 3]
    <class 'numpy.ndarray'>
    (3,)
    3
    


```python
a2 = np.array([[1,2,3], [4,5,6]])
# np.array에 파이썬 리스트를 인수로 넘긴다
print(a2)
print(type(a2))
print(a2.shape)
# row, column 형태 (row 행, column 렬)
print(a2.size)
```

    [[1 2 3]
     [4 5 6]]
    <class 'numpy.ndarray'>
    (2, 3)
    6
    


```python
# np.full(개수, 채울 숫자)
a3 = np.full(10, 5)
a3
```




    array([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])




```python
# 특별히 0이나 1로 채울 땐 한글자를 아낄 수 있다
a4 = np.zeros(10, dtype=int)
print(a4)
a5 = np.ones(10, dtype=int)
print(a5)
```

    [0 0 0 0 0 0 0 0 0 0]
    [1 1 1 1 1 1 1 1 1 1]
    


```python
np.random.random(10)
```




    array([0.21485246, 0.06833002, 0.80106829, 0.65509831, 0.82948982,
           0.83841915, 0.13883369, 0.0268359 , 0.30373294, 0.66020314])




```python
np.arange(10)
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])




```python
np.arange(5, 10)
```




    array([5, 6, 7, 8, 9])




```python
np.arange(5, 10, 2)
```




    array([5, 7, 9])




```python
np.arange(3,101,3)
```




    array([ 3,  6,  9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51,
           54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99])




```python
revenue_in_yen = [
    300000, 340000, 320000, 360000, 
    440000, 140000, 180000, 340000, 
    330000, 290000, 280000, 380000, 
    170000, 140000, 230000, 390000, 
    400000, 350000, 380000, 150000, 
    110000, 240000, 380000, 380000, 
    340000, 420000, 150000, 130000, 
    360000, 320000, 250000
]

# 여기에 코드를 작성하세요
rev = np.array(revenue_in_yen) * 10.08
rev
```




    array([3024000., 3427200., 3225600., 3628800., 4435200., 1411200.,
           1814400., 3427200., 3326400., 2923200., 2822400., 3830400.,
           1713600., 1411200., 2318400., 3931200., 4032000., 3528000.,
           3830400., 1512000., 1108800., 2419200., 3830400., 3830400.,
           3427200., 4233600., 1512000., 1310400., 3628800., 3225600.,
           2520000.])




```python
booleans = np.array([True, False, True, False])
np.where(booleans)
# True가 있는 인덱스를 반환한다
```




    (array([0, 2], dtype=int64),)




```python
filter = np.where(rev > 3000000)
# 조건값에 따른 인덱스를 찾아준다
filter
#### 인덱스가 나오는 거니까 응용할 수 있다
rev[filter]
```




    array([3024000., 3427200., 3225600., 3628800., 4435200., 3427200.,
           3326400., 3830400., 3931200., 4032000., 3528000., 3830400.,
           3830400., 3830400., 3427200., 4233600., 3628800., 3225600.])




```python
revenue_in_yen = [
    300000, 340000, 320000, 360000, 
    440000, 140000, 180000, 340000, 
    330000, 290000, 280000, 380000, 
    170000, 140000, 230000, 390000, 
    400000, 350000, 380000, 150000, 
    110000, 240000, 380000, 380000, 
    340000, 420000, 150000, 130000, 
    360000, 320000, 250000
]

# 여기에 코드를 작성하세요
rev = np.array(revenue_in_yen)
filter = np.where(rev <= 200000)
# bad_days_revenue = revenue_in_yen[filter]
# # 테스트 코드
# bad_days_revenue
filter
rev[filter]
```




    array([140000, 180000, 170000, 140000, 150000, 110000, 150000, 130000])




```python
# 여기에 코드를 작성하세요

rev[np.where(np.array(revenue_in_yen) <= 200000)]
```




    array([140000, 180000, 170000, 140000, 150000, 110000, 150000, 130000])



numpy array는 사칙연산을 각 요소에 해주는데 파이썬 리스트에 하면 리스트 자체에 적용하려고 하거나 오류가 난다


```python
print(rev.max())
print(rev.min())
print(rev.mean())
print(np.median(rev))
print(rev.std())
print(rev.var())
```

    440000
    110000
    290000.0
    320000.0
    97517.57492552222
    9509677419.35484
    

## <a id='toc1_5_'></a>[pandas dataframe](#toc0_)
---
pandas는 numpy를 이용해서 만들었다. 따라서 물려 받는 기능이 많고 데이터 읽고 쓰기, 새로운 파일로 저장, 시각화, 표 형식 편집 등에 특화됐다


```python
import pandas as pd
```


```python
tdlt = [['a', 1, 2], ['b', 3, 4], ['c', 5, 6], ['d', 7, 8]]
```


```python
# pd.DataFrame에 인자로 리스트를 준다
df = pd.DataFrame(tdlt, columns=['name', 'eng', 'math'], index=['a', 'b', 'c', 'd'])
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
      <th>name</th>
      <th>eng</th>
      <th>math</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>a</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>b</th>
      <td>b</td>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>c</th>
      <td>c</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>d</th>
      <td>d</td>
      <td>7</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
type(df)
```




    pandas.core.frame.DataFrame




```python
df.columns
```




    Index(['name', 'eng', 'math'], dtype='object')




```python
df.index
```




    Index(['a', 'b', 'c', 'd'], dtype='object')




```python
df.dtypes
```




    name    object
    eng      int64
    math     int64
    dtype: object




```python
pd.Series(tdlt)
```




    0    [a, 1, 2]
    1    [b, 3, 4]
    2    [c, 5, 6]
    3    [d, 7, 8]
    dtype: object




```python
two_dimensional_list = [['dongwook', 50, 86], ['sineui', 89, 31], ['ikjoong', 68, 91], ['yoonsoo', 88, 75]]
two_dimensional_array = np.array(two_dimensional_list)
list_of_series = [
    pd.Series(['dongwook', 50, 86]), 
    pd.Series(['sineui', 89, 31]), 
    pd.Series(['ikjoong', 68, 91]), 
    pd.Series(['yoonsoo', 88, 75])
]

# 아래 셋은 모두 동일합니다
df1 = pd.DataFrame(two_dimensional_list)
df2 = pd.DataFrame(two_dimensional_array)
df3 = pd.DataFrame(list_of_series)

print(df1)
```

              0   1   2
    0  dongwook  50  86
    1    sineui  89  31
    2   ikjoong  68  91
    3   yoonsoo  88  75
    


```python
names = ['dongwook', 'sineui', 'ikjoong', 'yoonsoo']
english_scores = [50, 89, 68, 88]
math_scores = [86, 31, 91, 75]

dict1 = {
    'name': names, 
    'english_score': english_scores, 
    'math_score': math_scores
}

dict2 = {
    'name': np.array(names), 
    'english_score': np.array(english_scores), 
    'math_score': np.array(math_scores)
}

dict3 = {
    'name': pd.Series(names), 
    'english_score': pd.Series(english_scores), 
    'math_score': pd.Series(math_scores)
}


# 아래 셋은 모두 동일합니다
df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)
df3 = pd.DataFrame(dict3)

print(df1)
```

           name  english_score  math_score
    0  dongwook             50          86
    1    sineui             89          31
    2   ikjoong             68          91
    3   yoonsoo             88          75
    


```python
my_list = [
    {'name': 'dongwook', 'english_score': 50, 'math_score': 86},
    {'name': 'sineui', 'english_score': 89, 'math_score': 31},
    {'name': 'ikjoong', 'english_score': 68, 'math_score': 91},
    {'name': 'yoonsoo', 'english_score': 88, 'math_score': 75}
]

df = pd.DataFrame(my_list)
print(df)
```

           name  english_score  math_score
    0  dongwook             50          86
    1    sineui             89          31
    2   ikjoong             68          91
    3   yoonsoo             88          75
    


```python
names = ['Taylor Swift', 'Aaron Sorkin', 'Harry Potter', 'Ji-Sung Park']
english_scores = ['December 13, 1989', 'June 9, 1961', 'July 31, 1980', 'February 25, 1981']
math_scores = ['Singer-songwriter', 'Screenwriter', 'Wizard', 'Footballer']

dict1 = {
    'name': names, 
    'birthday': english_scores, 
    'occupation': math_scores
}

pd.DataFrame(dict1)
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
      <th>name</th>
      <th>birthday</th>
      <th>occupation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Taylor Swift</td>
      <td>December 13, 1989</td>
      <td>Singer-songwriter</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Aaron Sorkin</td>
      <td>June 9, 1961</td>
      <td>Screenwriter</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Harry Potter</td>
      <td>July 31, 1980</td>
      <td>Wizard</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ji-Sung Park</td>
      <td>February 25, 1981</td>
      <td>Footballer</td>
    </tr>
  </tbody>
</table>
</div>



한 칼럼 내에는 동일한 dtype을 가져야 한다


```python
pd.read_csv('popular_baby_names.csv')
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
      <th>Year of Birth</th>
      <th>Gender</th>
      <th>Ethnicity</th>
      <th>Child's First Name</th>
      <th>Count</th>
      <th>Rank</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2016</td>
      <td>FEMALE</td>
      <td>ASIAN AND PACIFIC ISLANDER</td>
      <td>Olivia</td>
      <td>172</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2016</td>
      <td>FEMALE</td>
      <td>ASIAN AND PACIFIC ISLANDER</td>
      <td>Chloe</td>
      <td>112</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016</td>
      <td>FEMALE</td>
      <td>ASIAN AND PACIFIC ISLANDER</td>
      <td>Sophia</td>
      <td>104</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016</td>
      <td>FEMALE</td>
      <td>ASIAN AND PACIFIC ISLANDER</td>
      <td>Emily</td>
      <td>99</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016</td>
      <td>FEMALE</td>
      <td>ASIAN AND PACIFIC ISLANDER</td>
      <td>Emma</td>
      <td>99</td>
      <td>4</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>11340</th>
      <td>2011</td>
      <td>MALE</td>
      <td>WHITE NON HISPANIC</td>
      <td>LEV</td>
      <td>10</td>
      <td>97</td>
    </tr>
    <tr>
      <th>11341</th>
      <td>2011</td>
      <td>MALE</td>
      <td>WHITE NON HISPANIC</td>
      <td>AUGUSTUS</td>
      <td>10</td>
      <td>97</td>
    </tr>
    <tr>
      <th>11342</th>
      <td>2011</td>
      <td>MALE</td>
      <td>WHITE NON HISPANIC</td>
      <td>SHAUL</td>
      <td>10</td>
      <td>97</td>
    </tr>
    <tr>
      <th>11343</th>
      <td>2011</td>
      <td>MALE</td>
      <td>WHITE NON HISPANIC</td>
      <td>WESLEY</td>
      <td>10</td>
      <td>97</td>
    </tr>
    <tr>
      <th>11344</th>
      <td>2011</td>
      <td>MALE</td>
      <td>WHITE NON HISPANIC</td>
      <td>KENNETH</td>
      <td>10</td>
      <td>97</td>
    </tr>
  </tbody>
</table>
<p>11345 rows × 6 columns</p>
</div>




```python
pd.read_csv('mega_millions.csv', index_col=0)
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
      <th>Winning Numbers</th>
      <th>Mega Ball</th>
      <th>Multiplier</th>
    </tr>
    <tr>
      <th>Draw Date</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>02/15/2019</th>
      <td>10 38 40 43 65</td>
      <td>12</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>02/12/2019</th>
      <td>15 32 39 50 65</td>
      <td>7</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>02/08/2019</th>
      <td>14 24 31 42 48</td>
      <td>13</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>02/05/2019</th>
      <td>03 34 36 59 66</td>
      <td>7</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>02/01/2019</th>
      <td>02 37 48 66 68</td>
      <td>11</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>05/31/2002</th>
      <td>12 28 45 46 52</td>
      <td>47</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>05/28/2002</th>
      <td>06 21 22 29 32</td>
      <td>24</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>05/24/2002</th>
      <td>02 04 32 44 52</td>
      <td>36</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>05/21/2002</th>
      <td>04 28 39 41 44</td>
      <td>9</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>05/17/2002</th>
      <td>15 18 25 33 47</td>
      <td>30</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>1746 rows × 3 columns</p>
</div>



## <a id='toc1_6_'></a>[수료증](https://www.codeit.kr/certificates/tkHGu-u6dxG-AyIaM-rC9tJ) [&#8593;](#toc0_)
