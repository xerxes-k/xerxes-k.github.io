---
layout: single
title:  "data frame "
---
**Table of contents**<a id='toc0_'></a>    
- [DataFrame indexing, slicing](#toc1_)    
  - [DataFrame 조회하는 방법](#toc1_1_)    
  - [dict로 받아오면 한번에 칼럼명을 지정할 수 있다](#toc1_2_)    
    - [인덱스는 loc으로 조회하는 게 편하고](#toc1_2_1_)    
    - [칼럼은 그냥 []로 조회하는 게 편하다](#toc1_2_2_)    
    - [칼럼 여러개 가져오려면 df.loc[:, ['a', 'b']] 이렇게 콜론까지 찍어줘야 한다](#toc1_2_3_)    
  - [slicing](#toc1_3_)    
    - [칼럼 슬라이싱은 loc으로 해야 한다](#toc1_3_1_)    
    - [인덱스를 조회하고 슬라이싱 한다](#toc1_3_2_)    
    - [칼럼을 조회하고 슬라이싱 한다](#toc1_3_3_)    
  - [boolean을 출력하게 할 수도 있다](#toc1_4_)    
    - [boolean으로 조건을 줄 수 있다](#toc1_4_1_)    
  - [iloc으로는 index로 조회할 수 있다](#toc1_5_)    
  - [값 쓰기](#toc1_6_)    
  - [이름 바꾸기 짓기](#toc1_7_)    
    - [칼럼 이름은 사전식으로 바꾼다](#toc1_7_1_)    
    - [인덱스 이름은 따로 설정한다](#toc1_7_2_)    
    - [인덱스를 지정할 수도 있다](#toc1_7_3_)    
    - [인덱스를 지정하면 기존 인덱스가 날아가니 살리려면 작업해야 한다](#toc1_7_4_)    
  - [큰 데이터 다루기](#toc1_8_)    
  - [수료증](#toc1_9_)    

<!-- vscode-jupyter-toc-config
	numbering=false
	anchor=true
	flat=false
	minLevel=1
	maxLevel=6
	/vscode-jupyter-toc-config -->
<!-- THIS CELL WILL BE REPLACED ON TOC UPDATE. DO NOT WRITE YOUR TEXT IN THIS CELL -->

# <a id='toc1_'></a>[DataFrame indexing, slicing](#toc0_)

A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

## <a id='toc1_1_'></a>[DataFrame 조회하는 방법](#toc0_)
---

1. df['column']
  - 칼럼을 조회하는 데 편하다
2. df.loc[index, 'column']
  - 인덱스를 조회하는 데 편하다


```python
import pandas as pd
df = pd.read_csv('popular_baby_names.csv', index_col=0)
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
      <th>Gender</th>
      <th>Ethnicity</th>
      <th>Child's First Name</th>
      <th>Count</th>
      <th>Rank</th>
    </tr>
    <tr>
      <th>Year of Birth</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2016</th>
      <td>FEMALE</td>
      <td>ASIAN AND PACIFIC ISLANDER</td>
      <td>Olivia</td>
      <td>172</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>FEMALE</td>
      <td>ASIAN AND PACIFIC ISLANDER</td>
      <td>Chloe</td>
      <td>112</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>FEMALE</td>
      <td>ASIAN AND PACIFIC ISLANDER</td>
      <td>Sophia</td>
      <td>104</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>FEMALE</td>
      <td>ASIAN AND PACIFIC ISLANDER</td>
      <td>Emily</td>
      <td>99</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2016</th>
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
    </tr>
    <tr>
      <th>2011</th>
      <td>MALE</td>
      <td>WHITE NON HISPANIC</td>
      <td>LEV</td>
      <td>10</td>
      <td>97</td>
    </tr>
    <tr>
      <th>2011</th>
      <td>MALE</td>
      <td>WHITE NON HISPANIC</td>
      <td>AUGUSTUS</td>
      <td>10</td>
      <td>97</td>
    </tr>
    <tr>
      <th>2011</th>
      <td>MALE</td>
      <td>WHITE NON HISPANIC</td>
      <td>SHAUL</td>
      <td>10</td>
      <td>97</td>
    </tr>
    <tr>
      <th>2011</th>
      <td>MALE</td>
      <td>WHITE NON HISPANIC</td>
      <td>WESLEY</td>
      <td>10</td>
      <td>97</td>
    </tr>
    <tr>
      <th>2011</th>
      <td>MALE</td>
      <td>WHITE NON HISPANIC</td>
      <td>KENNETH</td>
      <td>10</td>
      <td>97</td>
    </tr>
  </tbody>
</table>
<p>11345 rows × 5 columns</p>
</div>




```python
# df.loc[row, column]
df.loc[2016, "Child's First Name"]
```




    Year of Birth
    2016     Olivia
    2016      Chloe
    2016     Sophia
    2016      Emily
    2016       Emma
             ...   
    2016       Umar
    2016      Aviel
    2016    Nikolas
    2016     Walker
    2016     Herman
    Name: Child's First Name, Length: 2063, dtype: object




```python
df.loc[2016] # df.loc[2016, :]
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
      <th>Gender</th>
      <th>Ethnicity</th>
      <th>Child's First Name</th>
      <th>Count</th>
      <th>Rank</th>
    </tr>
    <tr>
      <th>Year of Birth</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2016</th>
      <td>FEMALE</td>
      <td>ASIAN AND PACIFIC ISLANDER</td>
      <td>Olivia</td>
      <td>172</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>FEMALE</td>
      <td>ASIAN AND PACIFIC ISLANDER</td>
      <td>Chloe</td>
      <td>112</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>FEMALE</td>
      <td>ASIAN AND PACIFIC ISLANDER</td>
      <td>Sophia</td>
      <td>104</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>FEMALE</td>
      <td>ASIAN AND PACIFIC ISLANDER</td>
      <td>Emily</td>
      <td>99</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2016</th>
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
    </tr>
    <tr>
      <th>2016</th>
      <td>MALE</td>
      <td>WHITE NON HISPANIC</td>
      <td>Umar</td>
      <td>10</td>
      <td>99</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>MALE</td>
      <td>WHITE NON HISPANIC</td>
      <td>Aviel</td>
      <td>10</td>
      <td>99</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>MALE</td>
      <td>WHITE NON HISPANIC</td>
      <td>Nikolas</td>
      <td>10</td>
      <td>99</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>MALE</td>
      <td>WHITE NON HISPANIC</td>
      <td>Walker</td>
      <td>10</td>
      <td>99</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>MALE</td>
      <td>WHITE NON HISPANIC</td>
      <td>Herman</td>
      <td>10</td>
      <td>99</td>
    </tr>
  </tbody>
</table>
<p>2063 rows × 5 columns</p>
</div>




```python
type(df.loc[2016])
```




    pandas.core.frame.DataFrame




```python
df = pd.read_csv('broadcast.csv', index_col=0)
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
      <th>KBS</th>
      <th>MBC</th>
      <th>SBS</th>
      <th>TV CHOSUN</th>
      <th>JTBC</th>
      <th>Channel A</th>
      <th>MBN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2011</th>
      <td>35.951</td>
      <td>18.374</td>
      <td>11.173</td>
      <td>9.102</td>
      <td>7.380</td>
      <td>3.771</td>
      <td>2.809</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>36.163</td>
      <td>16.022</td>
      <td>11.408</td>
      <td>8.785</td>
      <td>7.878</td>
      <td>5.874</td>
      <td>3.310</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>31.989</td>
      <td>16.778</td>
      <td>9.673</td>
      <td>9.026</td>
      <td>7.810</td>
      <td>5.350</td>
      <td>3.825</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>31.210</td>
      <td>15.663</td>
      <td>9.108</td>
      <td>9.440</td>
      <td>7.490</td>
      <td>5.776</td>
      <td>4.572</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>27.777</td>
      <td>16.573</td>
      <td>9.099</td>
      <td>9.940</td>
      <td>7.267</td>
      <td>6.678</td>
      <td>5.520</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>27.583</td>
      <td>14.982</td>
      <td>8.669</td>
      <td>9.829</td>
      <td>7.727</td>
      <td>6.624</td>
      <td>5.477</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>26.890</td>
      <td>12.465</td>
      <td>8.661</td>
      <td>8.886</td>
      <td>9.453</td>
      <td>6.056</td>
      <td>5.215</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc[2016, 'KBS']
```




    27.583




```python
########### column을 하나만 조회할 때는 row를 : 처리해줘야
df.loc[:,'JTBC']
```




    2011    7.380
    2012    7.878
    2013    7.810
    2014    7.490
    2015    7.267
    2016    7.727
    2017    9.453
    Name: JTBC, dtype: float64




```python
# 인자는 2개만 받는 모양이다
df.loc[:, ['SBS','JTBC']]
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
      <th>SBS</th>
      <th>JTBC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2011</th>
      <td>11.173</td>
      <td>7.380</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>11.408</td>
      <td>7.878</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>9.673</td>
      <td>7.810</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>9.108</td>
      <td>7.490</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>9.099</td>
      <td>7.267</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>8.669</td>
      <td>7.727</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>8.661</td>
      <td>9.453</td>
    </tr>
  </tbody>
</table>
</div>




```python
s = pd.read_csv('s.csv', encoding='utf-8')
h = pd.read_csv('h.csv', encoding='utf-8')
```


```python
s
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
      <th>요일</th>
      <th>식비</th>
      <th>교통비</th>
      <th>문화생활비</th>
      <th>기타</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>MON</td>
      <td>19420</td>
      <td>2560</td>
      <td>4308</td>
      <td>3541</td>
    </tr>
    <tr>
      <th>1</th>
      <td>TUE</td>
      <td>16970</td>
      <td>2499</td>
      <td>7644</td>
      <td>2903</td>
    </tr>
    <tr>
      <th>2</th>
      <td>WED</td>
      <td>15091</td>
      <td>2511</td>
      <td>5674</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>3</th>
      <td>THU</td>
      <td>17880</td>
      <td>2545</td>
      <td>8621</td>
      <td>3012</td>
    </tr>
    <tr>
      <th>4</th>
      <td>FRI</td>
      <td>27104</td>
      <td>2993</td>
      <td>23052</td>
      <td>2508</td>
    </tr>
    <tr>
      <th>5</th>
      <td>SAT</td>
      <td>29055</td>
      <td>2803</td>
      <td>15330</td>
      <td>4901</td>
    </tr>
    <tr>
      <th>6</th>
      <td>SUN</td>
      <td>23509</td>
      <td>1760</td>
      <td>19030</td>
      <td>4230</td>
    </tr>
  </tbody>
</table>
</div>




```python
ss = s.loc[:, ['요일','문화생활비']]
```


```python
hh = h.loc[:, ['요일','문화생활비']]
```


```python
ss + hh
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
      <th>요일</th>
      <th>문화생활비</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>MONMON</td>
      <td>9647</td>
    </tr>
    <tr>
      <th>1</th>
      <td>TUETUE</td>
      <td>11168</td>
    </tr>
    <tr>
      <th>2</th>
      <td>WEDWED</td>
      <td>11038</td>
    </tr>
    <tr>
      <th>3</th>
      <td>THUTHU</td>
      <td>18563</td>
    </tr>
    <tr>
      <th>4</th>
      <td>FRIFRI</td>
      <td>56563</td>
    </tr>
    <tr>
      <th>5</th>
      <td>SATSAT</td>
      <td>34727</td>
    </tr>
    <tr>
      <th>6</th>
      <td>SUNSUN</td>
      <td>38955</td>
    </tr>
  </tbody>
</table>
</div>




```python
sam = s.loc[:, '문화생활비']
hnd = h.loc[:, '문화생활비']
day = s.loc[:, '요일']
```


```python
tab = pd.DataFrame([day, sam, hnd], index=['day', 'samsong','hyundee'])
tab = tab.T
tab
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
      <th>day</th>
      <th>samsong</th>
      <th>hyundee</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>MON</td>
      <td>4308</td>
      <td>5339</td>
    </tr>
    <tr>
      <th>1</th>
      <td>TUE</td>
      <td>7644</td>
      <td>3524</td>
    </tr>
    <tr>
      <th>2</th>
      <td>WED</td>
      <td>5674</td>
      <td>5364</td>
    </tr>
    <tr>
      <th>3</th>
      <td>THU</td>
      <td>8621</td>
      <td>9942</td>
    </tr>
    <tr>
      <th>4</th>
      <td>FRI</td>
      <td>23052</td>
      <td>33511</td>
    </tr>
    <tr>
      <th>5</th>
      <td>SAT</td>
      <td>15330</td>
      <td>19397</td>
    </tr>
    <tr>
      <th>6</th>
      <td>SUN</td>
      <td>19030</td>
      <td>19925</td>
    </tr>
  </tbody>
</table>
</div>




```python
# tab.rename(columns={"요일":"day", "문화생활비":"samsong", "문화생활비":"hyundee"})

```

## <a id='toc1_2_'></a>[dict로 받아오면 한번에 칼럼명을 지정할 수 있다](#toc0_)
---


```python
comb = {'day': s['요일'], 
    'samsong': s['문화생활비'], 
    'hyundee': h['문화생활비']}
combdf = pd.DataFrame(comb)
combdf
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
      <th>day</th>
      <th>samsong</th>
      <th>hyundee</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>MON</td>
      <td>4308</td>
      <td>5339</td>
    </tr>
    <tr>
      <th>1</th>
      <td>TUE</td>
      <td>7644</td>
      <td>3524</td>
    </tr>
    <tr>
      <th>2</th>
      <td>WED</td>
      <td>5674</td>
      <td>5364</td>
    </tr>
    <tr>
      <th>3</th>
      <td>THU</td>
      <td>8621</td>
      <td>9942</td>
    </tr>
    <tr>
      <th>4</th>
      <td>FRI</td>
      <td>23052</td>
      <td>33511</td>
    </tr>
    <tr>
      <th>5</th>
      <td>SAT</td>
      <td>15330</td>
      <td>19397</td>
    </tr>
    <tr>
      <th>6</th>
      <td>SUN</td>
      <td>19030</td>
      <td>19925</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.read_csv('broadcast.csv', index_col=0)
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
      <th>KBS</th>
      <th>MBC</th>
      <th>SBS</th>
      <th>TV CHOSUN</th>
      <th>JTBC</th>
      <th>Channel A</th>
      <th>MBN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2011</th>
      <td>35.951</td>
      <td>18.374</td>
      <td>11.173</td>
      <td>9.102</td>
      <td>7.380</td>
      <td>3.771</td>
      <td>2.809</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>36.163</td>
      <td>16.022</td>
      <td>11.408</td>
      <td>8.785</td>
      <td>7.878</td>
      <td>5.874</td>
      <td>3.310</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>31.989</td>
      <td>16.778</td>
      <td>9.673</td>
      <td>9.026</td>
      <td>7.810</td>
      <td>5.350</td>
      <td>3.825</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>31.210</td>
      <td>15.663</td>
      <td>9.108</td>
      <td>9.440</td>
      <td>7.490</td>
      <td>5.776</td>
      <td>4.572</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>27.777</td>
      <td>16.573</td>
      <td>9.099</td>
      <td>9.940</td>
      <td>7.267</td>
      <td>6.678</td>
      <td>5.520</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>27.583</td>
      <td>14.982</td>
      <td>8.669</td>
      <td>9.829</td>
      <td>7.727</td>
      <td>6.624</td>
      <td>5.477</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>26.890</td>
      <td>12.465</td>
      <td>8.661</td>
      <td>8.886</td>
      <td>9.453</td>
      <td>6.056</td>
      <td>5.215</td>
    </tr>
  </tbody>
</table>
</div>



### <a id='toc1_2_1_'></a>[인덱스는 loc으로 조회하는 게 편하고](#toc0_)


```python
df.loc[[2016, 2017]]
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
      <th>KBS</th>
      <th>MBC</th>
      <th>SBS</th>
      <th>TV CHOSUN</th>
      <th>JTBC</th>
      <th>Channel A</th>
      <th>MBN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2016</th>
      <td>27.583</td>
      <td>14.982</td>
      <td>8.669</td>
      <td>9.829</td>
      <td>7.727</td>
      <td>6.624</td>
      <td>5.477</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>26.890</td>
      <td>12.465</td>
      <td>8.661</td>
      <td>8.886</td>
      <td>9.453</td>
      <td>6.056</td>
      <td>5.215</td>
    </tr>
  </tbody>
</table>
</div>



### <a id='toc1_2_2_'></a>[칼럼은 그냥 []로 조회하는 게 편하다](#toc0_)


```python
df[['JTBC', 'SBS']]
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
      <th>JTBC</th>
      <th>SBS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2011</th>
      <td>7.380</td>
      <td>11.173</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>7.878</td>
      <td>11.408</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>7.810</td>
      <td>9.673</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>7.490</td>
      <td>9.108</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>7.267</td>
      <td>9.099</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>7.727</td>
      <td>8.669</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>9.453</td>
      <td>8.661</td>
    </tr>
  </tbody>
</table>
</div>



### <a id='toc1_2_3_'></a>[칼럼 여러개 가져오려면 df.loc[:, ['a', 'b']] 이렇게 콜론까지 찍어줘야 한다](#toc0_)


```python
df.loc[:, ['JTBC', 'SBS']]
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
      <th>JTBC</th>
      <th>SBS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2011</th>
      <td>7.380</td>
      <td>11.173</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>7.878</td>
      <td>11.408</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>7.810</td>
      <td>9.673</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>7.490</td>
      <td>9.108</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>7.267</td>
      <td>9.099</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>7.727</td>
      <td>8.669</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>9.453</td>
      <td>8.661</td>
    </tr>
  </tbody>
</table>
</div>



## <a id='toc1_3_'></a>[slicing](#toc0_)
---


```python
# 인덱스 슬라이싱은 쉽다
df.loc[2013 : 2016]
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
      <th>KBS</th>
      <th>MBC</th>
      <th>SBS</th>
      <th>TV CHOSUN</th>
      <th>JTBC</th>
      <th>Channel A</th>
      <th>MBN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013</th>
      <td>31.989</td>
      <td>16.778</td>
      <td>9.673</td>
      <td>9.026</td>
      <td>7.810</td>
      <td>5.350</td>
      <td>3.825</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>31.210</td>
      <td>15.663</td>
      <td>9.108</td>
      <td>9.440</td>
      <td>7.490</td>
      <td>5.776</td>
      <td>4.572</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>27.777</td>
      <td>16.573</td>
      <td>9.099</td>
      <td>9.940</td>
      <td>7.267</td>
      <td>6.678</td>
      <td>5.520</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>27.583</td>
      <td>14.982</td>
      <td>8.669</td>
      <td>9.829</td>
      <td>7.727</td>
      <td>6.624</td>
      <td>5.477</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 칼럼을 직접 슬라이싱 하려면 안 된다
# df['MBC':'JTBC']
```

### <a id='toc1_3_1_'></a>[칼럼 슬라이싱은 loc으로 해야 한다](#toc0_)


```python
df.loc[:, 'JTBC']
```




    2011    7.380
    2012    7.878
    2013    7.810
    2014    7.490
    2015    7.267
    2016    7.727
    2017    9.453
    Name: JTBC, dtype: float64




```python
# df.loc[:, ['MBC' : 'JTBC']] 이것도 아니다
df.loc[:, 'MBC':'JTBC']
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
      <th>MBC</th>
      <th>SBS</th>
      <th>TV CHOSUN</th>
      <th>JTBC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2011</th>
      <td>18.374</td>
      <td>11.173</td>
      <td>9.102</td>
      <td>7.380</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>16.022</td>
      <td>11.408</td>
      <td>8.785</td>
      <td>7.878</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>16.778</td>
      <td>9.673</td>
      <td>9.026</td>
      <td>7.810</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>15.663</td>
      <td>9.108</td>
      <td>9.440</td>
      <td>7.490</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>16.573</td>
      <td>9.099</td>
      <td>9.940</td>
      <td>7.267</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>14.982</td>
      <td>8.669</td>
      <td>9.829</td>
      <td>7.727</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>12.465</td>
      <td>8.661</td>
      <td>8.886</td>
      <td>9.453</td>
    </tr>
  </tbody>
</table>
</div>



### <a id='toc1_3_2_'></a>[인덱스를 조회하고 슬라이싱 한다](#toc0_)


```python
df.loc[2016]
```




    KBS          27.583
    MBC          14.982
    SBS           8.669
    TV CHOSUN     9.829
    JTBC          7.727
    Channel A     6.624
    MBN           5.477
    Name: 2016, dtype: float64




```python
# 복수 개의 인덱스를 조회하려면 리스트로 한번 더 감싸기
df.loc[[2013, 2016]]
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
      <th>KBS</th>
      <th>MBC</th>
      <th>SBS</th>
      <th>TV CHOSUN</th>
      <th>JTBC</th>
      <th>Channel A</th>
      <th>MBN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013</th>
      <td>31.989</td>
      <td>16.778</td>
      <td>9.673</td>
      <td>9.026</td>
      <td>7.810</td>
      <td>5.350</td>
      <td>3.825</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>27.583</td>
      <td>14.982</td>
      <td>8.669</td>
      <td>9.829</td>
      <td>7.727</td>
      <td>6.624</td>
      <td>5.477</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 슬라이싱은 바로 loc에서 진행
df.loc[2013:2016]
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
      <th>KBS</th>
      <th>MBC</th>
      <th>SBS</th>
      <th>TV CHOSUN</th>
      <th>JTBC</th>
      <th>Channel A</th>
      <th>MBN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013</th>
      <td>31.989</td>
      <td>16.778</td>
      <td>9.673</td>
      <td>9.026</td>
      <td>7.810</td>
      <td>5.350</td>
      <td>3.825</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>31.210</td>
      <td>15.663</td>
      <td>9.108</td>
      <td>9.440</td>
      <td>7.490</td>
      <td>5.776</td>
      <td>4.572</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>27.777</td>
      <td>16.573</td>
      <td>9.099</td>
      <td>9.940</td>
      <td>7.267</td>
      <td>6.678</td>
      <td>5.520</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>27.583</td>
      <td>14.982</td>
      <td>8.669</td>
      <td>9.829</td>
      <td>7.727</td>
      <td>6.624</td>
      <td>5.477</td>
    </tr>
  </tbody>
</table>
</div>



### <a id='toc1_3_3_'></a>[칼럼을 조회하고 슬라이싱 한다](#toc0_)
---


```python
df['JTBC']
```




    2011    7.380
    2012    7.878
    2013    7.810
    2014    7.490
    2015    7.267
    2016    7.727
    2017    9.453
    Name: JTBC, dtype: float64




```python
# 복수 개의 칼럼 조회할 땐 리스트로 한번 더 감싸기
df[['JTBC', 'MBC']]
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
      <th>JTBC</th>
      <th>MBC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2011</th>
      <td>7.380</td>
      <td>18.374</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>7.878</td>
      <td>16.022</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>7.810</td>
      <td>16.778</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>7.490</td>
      <td>15.663</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>7.267</td>
      <td>16.573</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>7.727</td>
      <td>14.982</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>9.453</td>
      <td>12.465</td>
    </tr>
  </tbody>
</table>
</div>



직접 조회에서는 슬라이싱이 안 된다

loc으로 조회할 땐 row를 지정해주기


```python
df.loc[2016, 'JTBC']
```




    7.727




```python
df.loc[:, 'JTBC']
```




    2011    7.380
    2012    7.878
    2013    7.810
    2014    7.490
    2015    7.267
    2016    7.727
    2017    9.453
    Name: JTBC, dtype: float64




```python
type(df.loc[:, 'JTBC'])
```




    pandas.core.series.Series




```python
# 복수로 가져오려면 리스트로 감싸기
df.loc[:, ['JTBC', 'MBC']]
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
      <th>JTBC</th>
      <th>MBC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2011</th>
      <td>7.380</td>
      <td>18.374</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>7.878</td>
      <td>16.022</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>7.810</td>
      <td>16.778</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>7.490</td>
      <td>15.663</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>7.267</td>
      <td>16.573</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>7.727</td>
      <td>14.982</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>9.453</td>
      <td>12.465</td>
    </tr>
  </tbody>
</table>
</div>



슬라이싱 할 때도 loc이니까 이름으로 불러야 한다


```python
# 슬라이싱 할 땐 리스트로 감싸지 않기
df.loc[:, 'MBC':'JTBC']
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
      <th>MBC</th>
      <th>SBS</th>
      <th>TV CHOSUN</th>
      <th>JTBC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2011</th>
      <td>18.374</td>
      <td>11.173</td>
      <td>9.102</td>
      <td>7.380</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>16.022</td>
      <td>11.408</td>
      <td>8.785</td>
      <td>7.878</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>16.778</td>
      <td>9.673</td>
      <td>9.026</td>
      <td>7.810</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>15.663</td>
      <td>9.108</td>
      <td>9.440</td>
      <td>7.490</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>16.573</td>
      <td>9.099</td>
      <td>9.940</td>
      <td>7.267</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>14.982</td>
      <td>8.669</td>
      <td>9.829</td>
      <td>7.727</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>12.465</td>
      <td>8.661</td>
      <td>8.886</td>
      <td>9.453</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc[2012:2017, 'KBS':'SBS']
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
      <th>KBS</th>
      <th>MBC</th>
      <th>SBS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2012</th>
      <td>36.163</td>
      <td>16.022</td>
      <td>11.408</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>31.989</td>
      <td>16.778</td>
      <td>9.673</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>31.210</td>
      <td>15.663</td>
      <td>9.108</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>27.777</td>
      <td>16.573</td>
      <td>9.099</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>27.583</td>
      <td>14.982</td>
      <td>8.669</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>26.890</td>
      <td>12.465</td>
      <td>8.661</td>
    </tr>
  </tbody>
</table>
</div>



## <a id='toc1_4_'></a>[boolean을 출력하게 할 수도 있다](#toc0_)
---


```python
df['JTBC'] > 8
```




    2011    False
    2012    False
    2013    False
    2014    False
    2015    False
    2016    False
    2017     True
    Name: JTBC, dtype: bool



### <a id='toc1_4_1_'></a>[boolean으로 조건을 줄 수 있다](#toc0_)


```python
df.loc[df['JTBC'] > 8]
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
      <th>KBS</th>
      <th>MBC</th>
      <th>SBS</th>
      <th>TV CHOSUN</th>
      <th>JTBC</th>
      <th>Channel A</th>
      <th>MBN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017</th>
      <td>26.89</td>
      <td>12.465</td>
      <td>8.661</td>
      <td>8.886</td>
      <td>9.453</td>
      <td>6.056</td>
      <td>5.215</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['JTBC'][df['JTBC'] > 8]
```




    2017    9.453
    Name: JTBC, dtype: float64




```python
df.loc[df['JTBC'] > 8, 'JTBC']
```




    2017    9.453
    Name: JTBC, dtype: float64




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
      <th>KBS</th>
      <th>MBC</th>
      <th>SBS</th>
      <th>TV CHOSUN</th>
      <th>JTBC</th>
      <th>Channel A</th>
      <th>MBN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2011</th>
      <td>35.951</td>
      <td>18.374</td>
      <td>11.173</td>
      <td>9.102</td>
      <td>7.380</td>
      <td>3.771</td>
      <td>2.809</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>36.163</td>
      <td>16.022</td>
      <td>11.408</td>
      <td>8.785</td>
      <td>7.878</td>
      <td>5.874</td>
      <td>3.310</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>31.989</td>
      <td>16.778</td>
      <td>9.673</td>
      <td>9.026</td>
      <td>7.810</td>
      <td>5.350</td>
      <td>3.825</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>31.210</td>
      <td>15.663</td>
      <td>9.108</td>
      <td>9.440</td>
      <td>7.490</td>
      <td>5.776</td>
      <td>4.572</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>27.777</td>
      <td>16.573</td>
      <td>9.099</td>
      <td>9.940</td>
      <td>7.267</td>
      <td>6.678</td>
      <td>5.520</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>27.583</td>
      <td>14.982</td>
      <td>8.669</td>
      <td>9.829</td>
      <td>7.727</td>
      <td>6.624</td>
      <td>5.477</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>26.890</td>
      <td>12.465</td>
      <td>8.661</td>
      <td>8.886</td>
      <td>9.453</td>
      <td>6.056</td>
      <td>5.215</td>
    </tr>
  </tbody>
</table>
</div>




```python
cond = df['SBS'] < df['TV CHOSUN']
df.loc[cond, ['SBS', 'TV CHOSUN']]
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
      <th>SBS</th>
      <th>TV CHOSUN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014</th>
      <td>9.108</td>
      <td>9.440</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>9.099</td>
      <td>9.940</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>8.669</td>
      <td>9.829</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>8.661</td>
      <td>8.886</td>
    </tr>
  </tbody>
</table>
</div>



## <a id='toc1_5_'></a>[iloc으로는 index로 조회할 수 있다](#toc0_)
---


```python
df.iloc[2, 4]
```




    7.81




```python
df.iloc[[2,4], [3,5]]
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
      <th>TV CHOSUN</th>
      <th>Channel A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013</th>
      <td>9.026</td>
      <td>5.350</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>9.940</td>
      <td>6.678</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.iloc[3:, 1:4]
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
      <th>MBC</th>
      <th>SBS</th>
      <th>TV CHOSUN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014</th>
      <td>15.663</td>
      <td>9.108</td>
      <td>9.440</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>16.573</td>
      <td>9.099</td>
      <td>9.940</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>14.982</td>
      <td>8.669</td>
      <td>9.829</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>12.465</td>
      <td>8.661</td>
      <td>8.886</td>
    </tr>
  </tbody>
</table>
</div>



인덱싱 하는 방법이 다양한 만큼 유연하게 사용할 수 있으나 그만큼 헷갈리는 것도 사실이다

## <a id='toc1_6_'></a>[값 쓰기](#toc0_)
---


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
      <th>KBS</th>
      <th>MBC</th>
      <th>SBS</th>
      <th>TV CHOSUN</th>
      <th>JTBC</th>
      <th>Channel A</th>
      <th>MBN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2011</th>
      <td>35.951</td>
      <td>18.374</td>
      <td>11.173</td>
      <td>9.102</td>
      <td>7.380</td>
      <td>3.771</td>
      <td>2.809</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>36.163</td>
      <td>16.022</td>
      <td>11.408</td>
      <td>8.785</td>
      <td>7.878</td>
      <td>5.874</td>
      <td>3.310</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>31.989</td>
      <td>16.778</td>
      <td>9.673</td>
      <td>9.026</td>
      <td>7.810</td>
      <td>5.350</td>
      <td>3.825</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>31.210</td>
      <td>15.663</td>
      <td>9.108</td>
      <td>9.440</td>
      <td>7.490</td>
      <td>5.776</td>
      <td>4.572</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>27.777</td>
      <td>16.573</td>
      <td>9.099</td>
      <td>9.940</td>
      <td>7.267</td>
      <td>6.678</td>
      <td>5.520</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>27.583</td>
      <td>14.982</td>
      <td>8.669</td>
      <td>9.829</td>
      <td>7.727</td>
      <td>6.624</td>
      <td>5.477</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>26.890</td>
      <td>12.465</td>
      <td>8.661</td>
      <td>8.886</td>
      <td>9.453</td>
      <td>6.056</td>
      <td>5.215</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc[2011, 'MBN']
```




    2.809




```python
df.loc[2011, 'MBN'] = 999
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
      <th>KBS</th>
      <th>MBC</th>
      <th>SBS</th>
      <th>TV CHOSUN</th>
      <th>JTBC</th>
      <th>Channel A</th>
      <th>MBN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2011</th>
      <td>35.951</td>
      <td>18.374</td>
      <td>11.173</td>
      <td>9.102</td>
      <td>7.380</td>
      <td>3.771</td>
      <td>999.000</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>36.163</td>
      <td>16.022</td>
      <td>11.408</td>
      <td>8.785</td>
      <td>7.878</td>
      <td>5.874</td>
      <td>3.310</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>31.989</td>
      <td>16.778</td>
      <td>9.673</td>
      <td>9.026</td>
      <td>7.810</td>
      <td>5.350</td>
      <td>3.825</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>31.210</td>
      <td>15.663</td>
      <td>9.108</td>
      <td>9.440</td>
      <td>7.490</td>
      <td>5.776</td>
      <td>4.572</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>27.777</td>
      <td>16.573</td>
      <td>9.099</td>
      <td>9.940</td>
      <td>7.267</td>
      <td>6.678</td>
      <td>5.520</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>27.583</td>
      <td>14.982</td>
      <td>8.669</td>
      <td>9.829</td>
      <td>7.727</td>
      <td>6.624</td>
      <td>5.477</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>26.890</td>
      <td>12.465</td>
      <td>8.661</td>
      <td>8.886</td>
      <td>9.453</td>
      <td>6.056</td>
      <td>5.215</td>
    </tr>
  </tbody>
</table>
</div>




```python
######## 행을 지정해주지 않아서 'mbn'이라는 이름으로 행이 생겨버렸다
df.loc['MBN'] = 999
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
      <th>KBS</th>
      <th>MBC</th>
      <th>SBS</th>
      <th>TV CHOSUN</th>
      <th>JTBC</th>
      <th>Channel A</th>
      <th>MBN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2011</th>
      <td>35.951</td>
      <td>18.374</td>
      <td>11.173</td>
      <td>9.102</td>
      <td>7.380</td>
      <td>3.771</td>
      <td>999.000</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>36.163</td>
      <td>16.022</td>
      <td>11.408</td>
      <td>8.785</td>
      <td>7.878</td>
      <td>5.874</td>
      <td>3.310</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>31.989</td>
      <td>16.778</td>
      <td>9.673</td>
      <td>9.026</td>
      <td>7.810</td>
      <td>5.350</td>
      <td>3.825</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>31.210</td>
      <td>15.663</td>
      <td>9.108</td>
      <td>9.440</td>
      <td>7.490</td>
      <td>5.776</td>
      <td>4.572</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>27.777</td>
      <td>16.573</td>
      <td>9.099</td>
      <td>9.940</td>
      <td>7.267</td>
      <td>6.678</td>
      <td>5.520</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>27.583</td>
      <td>14.982</td>
      <td>8.669</td>
      <td>9.829</td>
      <td>7.727</td>
      <td>6.624</td>
      <td>5.477</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>26.890</td>
      <td>12.465</td>
      <td>8.661</td>
      <td>8.886</td>
      <td>9.453</td>
      <td>6.056</td>
      <td>5.215</td>
    </tr>
    <tr>
      <th>MBN</th>
      <td>999.000</td>
      <td>999.000</td>
      <td>999.000</td>
      <td>999.000</td>
      <td>999.000</td>
      <td>999.000</td>
      <td>999.000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc[:, 'MBN'] = 999
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
      <th>KBS</th>
      <th>MBC</th>
      <th>SBS</th>
      <th>TV CHOSUN</th>
      <th>JTBC</th>
      <th>Channel A</th>
      <th>MBN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2011</th>
      <td>35.951</td>
      <td>18.374</td>
      <td>11.173</td>
      <td>9.102</td>
      <td>7.380</td>
      <td>3.771</td>
      <td>999.0</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>36.163</td>
      <td>16.022</td>
      <td>11.408</td>
      <td>8.785</td>
      <td>7.878</td>
      <td>5.874</td>
      <td>999.0</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>31.989</td>
      <td>16.778</td>
      <td>9.673</td>
      <td>9.026</td>
      <td>7.810</td>
      <td>5.350</td>
      <td>999.0</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>31.210</td>
      <td>15.663</td>
      <td>9.108</td>
      <td>9.440</td>
      <td>7.490</td>
      <td>5.776</td>
      <td>999.0</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>27.777</td>
      <td>16.573</td>
      <td>9.099</td>
      <td>9.940</td>
      <td>7.267</td>
      <td>6.678</td>
      <td>999.0</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>27.583</td>
      <td>14.982</td>
      <td>8.669</td>
      <td>9.829</td>
      <td>7.727</td>
      <td>6.624</td>
      <td>999.0</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>26.890</td>
      <td>12.465</td>
      <td>8.661</td>
      <td>8.886</td>
      <td>9.453</td>
      <td>6.056</td>
      <td>999.0</td>
    </tr>
    <tr>
      <th>MBN</th>
      <td>999.000</td>
      <td>999.000</td>
      <td>999.000</td>
      <td>999.000</td>
      <td>999.000</td>
      <td>999.000</td>
      <td>999.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[['JTBC', 'SBS']] = 9999
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
      <th>KBS</th>
      <th>MBC</th>
      <th>SBS</th>
      <th>TV CHOSUN</th>
      <th>JTBC</th>
      <th>Channel A</th>
      <th>MBN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2011</th>
      <td>35.951</td>
      <td>18.374</td>
      <td>9999</td>
      <td>9.102</td>
      <td>9999</td>
      <td>3.771</td>
      <td>999.0</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>36.163</td>
      <td>16.022</td>
      <td>9999</td>
      <td>8.785</td>
      <td>9999</td>
      <td>5.874</td>
      <td>999.0</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>31.989</td>
      <td>16.778</td>
      <td>9999</td>
      <td>9.026</td>
      <td>9999</td>
      <td>5.350</td>
      <td>999.0</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>31.210</td>
      <td>15.663</td>
      <td>9999</td>
      <td>9.440</td>
      <td>9999</td>
      <td>5.776</td>
      <td>999.0</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>27.777</td>
      <td>16.573</td>
      <td>9999</td>
      <td>9.940</td>
      <td>9999</td>
      <td>6.678</td>
      <td>999.0</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>27.583</td>
      <td>14.982</td>
      <td>9999</td>
      <td>9.829</td>
      <td>9999</td>
      <td>6.624</td>
      <td>999.0</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>26.890</td>
      <td>12.465</td>
      <td>9999</td>
      <td>8.886</td>
      <td>9999</td>
      <td>6.056</td>
      <td>999.0</td>
    </tr>
    <tr>
      <th>MBN</th>
      <td>999.000</td>
      <td>999.000</td>
      <td>9999</td>
      <td>999.000</td>
      <td>9999</td>
      <td>999.000</td>
      <td>999.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.read_csv('broadcast.csv', index_col=0)
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
      <th>KBS</th>
      <th>MBC</th>
      <th>SBS</th>
      <th>TV CHOSUN</th>
      <th>JTBC</th>
      <th>Channel A</th>
      <th>MBN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2011</th>
      <td>35.951</td>
      <td>18.374</td>
      <td>11.173</td>
      <td>9.102</td>
      <td>7.380</td>
      <td>3.771</td>
      <td>2.809</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>36.163</td>
      <td>16.022</td>
      <td>11.408</td>
      <td>8.785</td>
      <td>7.878</td>
      <td>5.874</td>
      <td>3.310</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>31.989</td>
      <td>16.778</td>
      <td>9.673</td>
      <td>9.026</td>
      <td>7.810</td>
      <td>5.350</td>
      <td>3.825</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>31.210</td>
      <td>15.663</td>
      <td>9.108</td>
      <td>9.440</td>
      <td>7.490</td>
      <td>5.776</td>
      <td>4.572</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>27.777</td>
      <td>16.573</td>
      <td>9.099</td>
      <td>9.940</td>
      <td>7.267</td>
      <td>6.678</td>
      <td>5.520</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>27.583</td>
      <td>14.982</td>
      <td>8.669</td>
      <td>9.829</td>
      <td>7.727</td>
      <td>6.624</td>
      <td>5.477</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>26.890</td>
      <td>12.465</td>
      <td>8.661</td>
      <td>8.886</td>
      <td>9.453</td>
      <td>6.056</td>
      <td>5.215</td>
    </tr>
  </tbody>
</table>
</div>




```python
cond = df['SBS'] > df['TV CHOSUN']
cond
```




    2011     True
    2012     True
    2013     True
    2014    False
    2015    False
    2016    False
    2017    False
    dtype: bool




```python
df.loc[cond]
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
      <th>KBS</th>
      <th>MBC</th>
      <th>SBS</th>
      <th>TV CHOSUN</th>
      <th>JTBC</th>
      <th>Channel A</th>
      <th>MBN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2011</th>
      <td>35.951</td>
      <td>18.374</td>
      <td>11.173</td>
      <td>9.102</td>
      <td>7.380</td>
      <td>3.771</td>
      <td>2.809</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>36.163</td>
      <td>16.022</td>
      <td>11.408</td>
      <td>8.785</td>
      <td>7.878</td>
      <td>5.874</td>
      <td>3.310</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>31.989</td>
      <td>16.778</td>
      <td>9.673</td>
      <td>9.026</td>
      <td>7.810</td>
      <td>5.350</td>
      <td>3.825</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc[cond] = 'what'
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
      <th>KBS</th>
      <th>MBC</th>
      <th>SBS</th>
      <th>TV CHOSUN</th>
      <th>JTBC</th>
      <th>Channel A</th>
      <th>MBN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2011</th>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>31.21</td>
      <td>15.663</td>
      <td>9.108</td>
      <td>9.44</td>
      <td>7.49</td>
      <td>5.776</td>
      <td>4.572</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>27.777</td>
      <td>16.573</td>
      <td>9.099</td>
      <td>9.94</td>
      <td>7.267</td>
      <td>6.678</td>
      <td>5.52</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>27.583</td>
      <td>14.982</td>
      <td>8.669</td>
      <td>9.829</td>
      <td>7.727</td>
      <td>6.624</td>
      <td>5.477</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>26.89</td>
      <td>12.465</td>
      <td>8.661</td>
      <td>8.886</td>
      <td>9.453</td>
      <td>6.056</td>
      <td>5.215</td>
    </tr>
  </tbody>
</table>
</div>




```python
#################### 열을 셀 때 인덱스 칼럼은 빼고다
df.iloc[1,2] = 'q'
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
      <th>KBS</th>
      <th>MBC</th>
      <th>SBS</th>
      <th>TV CHOSUN</th>
      <th>JTBC</th>
      <th>Channel A</th>
      <th>MBN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2011</th>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>what</td>
      <td>what</td>
      <td>q</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>31.21</td>
      <td>15.663</td>
      <td>9.108</td>
      <td>9.44</td>
      <td>7.49</td>
      <td>5.776</td>
      <td>4.572</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>27.777</td>
      <td>16.573</td>
      <td>9.099</td>
      <td>9.94</td>
      <td>7.267</td>
      <td>6.678</td>
      <td>5.52</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>27.583</td>
      <td>14.982</td>
      <td>8.669</td>
      <td>9.829</td>
      <td>7.727</td>
      <td>6.624</td>
      <td>5.477</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>26.89</td>
      <td>12.465</td>
      <td>8.661</td>
      <td>8.886</td>
      <td>9.453</td>
      <td>6.056</td>
      <td>5.215</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.iloc[[1,3], [2,4]] = 'lol'
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
      <th>KBS</th>
      <th>MBC</th>
      <th>SBS</th>
      <th>TV CHOSUN</th>
      <th>JTBC</th>
      <th>Channel A</th>
      <th>MBN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2011</th>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>what</td>
      <td>what</td>
      <td>lol</td>
      <td>what</td>
      <td>lol</td>
      <td>what</td>
      <td>what</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>31.21</td>
      <td>15.663</td>
      <td>lol</td>
      <td>9.44</td>
      <td>lol</td>
      <td>5.776</td>
      <td>4.572</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>27.777</td>
      <td>16.573</td>
      <td>9.099</td>
      <td>9.94</td>
      <td>7.267</td>
      <td>6.678</td>
      <td>5.52</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>27.583</td>
      <td>14.982</td>
      <td>8.669</td>
      <td>9.829</td>
      <td>7.727</td>
      <td>6.624</td>
      <td>5.477</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>26.89</td>
      <td>12.465</td>
      <td>8.661</td>
      <td>8.886</td>
      <td>9.453</td>
      <td>6.056</td>
      <td>5.215</td>
    </tr>
  </tbody>
</table>
</div>




```python
############# 이번엔 df.loc이 아니라 df[]에서 바꿨더니 행이 아니라 열이 생겼다 환장
df[2018] = 75
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
      <th>KBS</th>
      <th>MBC</th>
      <th>SBS</th>
      <th>TV CHOSUN</th>
      <th>JTBC</th>
      <th>Channel A</th>
      <th>MBN</th>
      <th>2018</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2011</th>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>what</td>
      <td>what</td>
      <td>lol</td>
      <td>what</td>
      <td>lol</td>
      <td>what</td>
      <td>what</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>31.21</td>
      <td>15.663</td>
      <td>lol</td>
      <td>9.44</td>
      <td>lol</td>
      <td>5.776</td>
      <td>4.572</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>27.777</td>
      <td>16.573</td>
      <td>9.099</td>
      <td>9.94</td>
      <td>7.267</td>
      <td>6.678</td>
      <td>5.52</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>27.583</td>
      <td>14.982</td>
      <td>8.669</td>
      <td>9.829</td>
      <td>7.727</td>
      <td>6.624</td>
      <td>5.477</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>26.89</td>
      <td>12.465</td>
      <td>8.661</td>
      <td>8.886</td>
      <td>9.453</td>
      <td>6.056</td>
      <td>5.215</td>
      <td>75</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc[2018] = 24
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
      <th>KBS</th>
      <th>MBC</th>
      <th>SBS</th>
      <th>TV CHOSUN</th>
      <th>JTBC</th>
      <th>Channel A</th>
      <th>MBN</th>
      <th>2018</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2011</th>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>what</td>
      <td>what</td>
      <td>lol</td>
      <td>what</td>
      <td>lol</td>
      <td>what</td>
      <td>what</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>31.21</td>
      <td>15.663</td>
      <td>lol</td>
      <td>9.44</td>
      <td>lol</td>
      <td>5.776</td>
      <td>4.572</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>27.777</td>
      <td>16.573</td>
      <td>9.099</td>
      <td>9.94</td>
      <td>7.267</td>
      <td>6.678</td>
      <td>5.52</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>27.583</td>
      <td>14.982</td>
      <td>8.669</td>
      <td>9.829</td>
      <td>7.727</td>
      <td>6.624</td>
      <td>5.477</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>26.89</td>
      <td>12.465</td>
      <td>8.661</td>
      <td>8.886</td>
      <td>9.453</td>
      <td>6.056</td>
      <td>5.215</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>24</td>
      <td>24</td>
      <td>24</td>
      <td>24</td>
      <td>24</td>
      <td>24</td>
      <td>24</td>
      <td>24</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.drop(2018, axis='index', inplace=False)
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
      <th>KBS</th>
      <th>MBC</th>
      <th>SBS</th>
      <th>TV CHOSUN</th>
      <th>JTBC</th>
      <th>Channel A</th>
      <th>MBN</th>
      <th>2018</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2011</th>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>what</td>
      <td>what</td>
      <td>lol</td>
      <td>what</td>
      <td>lol</td>
      <td>what</td>
      <td>what</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>31.21</td>
      <td>15.663</td>
      <td>lol</td>
      <td>9.44</td>
      <td>lol</td>
      <td>5.776</td>
      <td>4.572</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>27.777</td>
      <td>16.573</td>
      <td>9.099</td>
      <td>9.94</td>
      <td>7.267</td>
      <td>6.678</td>
      <td>5.52</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>27.583</td>
      <td>14.982</td>
      <td>8.669</td>
      <td>9.829</td>
      <td>7.727</td>
      <td>6.624</td>
      <td>5.477</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>26.89</td>
      <td>12.465</td>
      <td>8.661</td>
      <td>8.886</td>
      <td>9.453</td>
      <td>6.056</td>
      <td>5.215</td>
      <td>75</td>
    </tr>
  </tbody>
</table>
</div>



inplace=False로 하면 기존 데이터프레임을 inplace 하지 않는다 즉 원본은 보전된다


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
      <th>KBS</th>
      <th>MBC</th>
      <th>SBS</th>
      <th>TV CHOSUN</th>
      <th>JTBC</th>
      <th>Channel A</th>
      <th>MBN</th>
      <th>2018</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2011</th>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>what</td>
      <td>what</td>
      <td>lol</td>
      <td>what</td>
      <td>lol</td>
      <td>what</td>
      <td>what</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>31.21</td>
      <td>15.663</td>
      <td>lol</td>
      <td>9.44</td>
      <td>lol</td>
      <td>5.776</td>
      <td>4.572</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>27.777</td>
      <td>16.573</td>
      <td>9.099</td>
      <td>9.94</td>
      <td>7.267</td>
      <td>6.678</td>
      <td>5.52</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>27.583</td>
      <td>14.982</td>
      <td>8.669</td>
      <td>9.829</td>
      <td>7.727</td>
      <td>6.624</td>
      <td>5.477</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>26.89</td>
      <td>12.465</td>
      <td>8.661</td>
      <td>8.886</td>
      <td>9.453</td>
      <td>6.056</td>
      <td>5.215</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>24</td>
      <td>24</td>
      <td>24</td>
      <td>24</td>
      <td>24</td>
      <td>24</td>
      <td>24</td>
      <td>24</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.drop(2018, axis='columns')
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
      <th>KBS</th>
      <th>MBC</th>
      <th>SBS</th>
      <th>TV CHOSUN</th>
      <th>JTBC</th>
      <th>Channel A</th>
      <th>MBN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2011</th>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>what</td>
      <td>what</td>
      <td>lol</td>
      <td>what</td>
      <td>lol</td>
      <td>what</td>
      <td>what</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>31.21</td>
      <td>15.663</td>
      <td>lol</td>
      <td>9.44</td>
      <td>lol</td>
      <td>5.776</td>
      <td>4.572</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>27.777</td>
      <td>16.573</td>
      <td>9.099</td>
      <td>9.94</td>
      <td>7.267</td>
      <td>6.678</td>
      <td>5.52</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>27.583</td>
      <td>14.982</td>
      <td>8.669</td>
      <td>9.829</td>
      <td>7.727</td>
      <td>6.624</td>
      <td>5.477</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>26.89</td>
      <td>12.465</td>
      <td>8.661</td>
      <td>8.886</td>
      <td>9.453</td>
      <td>6.056</td>
      <td>5.215</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>24</td>
      <td>24</td>
      <td>24</td>
      <td>24</td>
      <td>24</td>
      <td>24</td>
      <td>24</td>
    </tr>
  </tbody>
</table>
</div>




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
      <th>KBS</th>
      <th>MBC</th>
      <th>SBS</th>
      <th>TV CHOSUN</th>
      <th>JTBC</th>
      <th>Channel A</th>
      <th>MBN</th>
      <th>2018</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2011</th>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>what</td>
      <td>what</td>
      <td>lol</td>
      <td>what</td>
      <td>lol</td>
      <td>what</td>
      <td>what</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>31.21</td>
      <td>15.663</td>
      <td>lol</td>
      <td>9.44</td>
      <td>lol</td>
      <td>5.776</td>
      <td>4.572</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>27.777</td>
      <td>16.573</td>
      <td>9.099</td>
      <td>9.94</td>
      <td>7.267</td>
      <td>6.678</td>
      <td>5.52</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>27.583</td>
      <td>14.982</td>
      <td>8.669</td>
      <td>9.829</td>
      <td>7.727</td>
      <td>6.624</td>
      <td>5.477</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>26.89</td>
      <td>12.465</td>
      <td>8.661</td>
      <td>8.886</td>
      <td>9.453</td>
      <td>6.056</td>
      <td>5.215</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>24</td>
      <td>24</td>
      <td>24</td>
      <td>24</td>
      <td>24</td>
      <td>24</td>
      <td>24</td>
      <td>24</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.drop([2016, 2018], axis='index')
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
      <th>KBS</th>
      <th>MBC</th>
      <th>SBS</th>
      <th>TV CHOSUN</th>
      <th>JTBC</th>
      <th>Channel A</th>
      <th>MBN</th>
      <th>2018</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2011</th>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>what</td>
      <td>what</td>
      <td>lol</td>
      <td>what</td>
      <td>lol</td>
      <td>what</td>
      <td>what</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>31.21</td>
      <td>15.663</td>
      <td>lol</td>
      <td>9.44</td>
      <td>lol</td>
      <td>5.776</td>
      <td>4.572</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>27.777</td>
      <td>16.573</td>
      <td>9.099</td>
      <td>9.94</td>
      <td>7.267</td>
      <td>6.678</td>
      <td>5.52</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>26.89</td>
      <td>12.465</td>
      <td>8.661</td>
      <td>8.886</td>
      <td>9.453</td>
      <td>6.056</td>
      <td>5.215</td>
      <td>75</td>
    </tr>
  </tbody>
</table>
</div>




```python
# df.drop(2016:2018, axis='index')
# 이건 오류가 난다 이렇게 슬라이싱은 안된다
```


```python
df.loc[2011:2013]
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
      <th>KBS</th>
      <th>MBC</th>
      <th>SBS</th>
      <th>TV CHOSUN</th>
      <th>JTBC</th>
      <th>Channel A</th>
      <th>MBN</th>
      <th>2018</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2011</th>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>what</td>
      <td>what</td>
      <td>lol</td>
      <td>what</td>
      <td>lol</td>
      <td>what</td>
      <td>what</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>what</td>
      <td>75</td>
    </tr>
  </tbody>
</table>
</div>



## <a id='toc1_7_'></a>[이름 바꾸기 짓기](#toc0_)
---


```python
df = pd.read_csv('broadcast.csv', index_col=0)
df2 = df
```


```python
df2
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
      <th>KBS</th>
      <th>MBC</th>
      <th>SBS</th>
      <th>TV CHOSUN</th>
      <th>JTBC</th>
      <th>Channel A</th>
      <th>MBN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2011</th>
      <td>35.951</td>
      <td>18.374</td>
      <td>11.173</td>
      <td>9.102</td>
      <td>7.380</td>
      <td>3.771</td>
      <td>2.809</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>36.163</td>
      <td>16.022</td>
      <td>11.408</td>
      <td>8.785</td>
      <td>7.878</td>
      <td>5.874</td>
      <td>3.310</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>31.989</td>
      <td>16.778</td>
      <td>9.673</td>
      <td>9.026</td>
      <td>7.810</td>
      <td>5.350</td>
      <td>3.825</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>31.210</td>
      <td>15.663</td>
      <td>9.108</td>
      <td>9.440</td>
      <td>7.490</td>
      <td>5.776</td>
      <td>4.572</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>27.777</td>
      <td>16.573</td>
      <td>9.099</td>
      <td>9.940</td>
      <td>7.267</td>
      <td>6.678</td>
      <td>5.520</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>27.583</td>
      <td>14.982</td>
      <td>8.669</td>
      <td>9.829</td>
      <td>7.727</td>
      <td>6.624</td>
      <td>5.477</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>26.890</td>
      <td>12.465</td>
      <td>8.661</td>
      <td>8.886</td>
      <td>9.453</td>
      <td>6.056</td>
      <td>5.215</td>
    </tr>
  </tbody>
</table>
</div>



### <a id='toc1_7_1_'></a>[칼럼 이름은 사전식으로 바꾼다](#toc0_)


```python
df2.rename(columns={'KBS':'kbs'})
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
      <th>kbs</th>
      <th>MBC</th>
      <th>SBS</th>
      <th>TV CHOSUN</th>
      <th>JTBC</th>
      <th>Channel A</th>
      <th>MBN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2011</th>
      <td>35.951</td>
      <td>18.374</td>
      <td>11.173</td>
      <td>9.102</td>
      <td>7.380</td>
      <td>3.771</td>
      <td>2.809</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>36.163</td>
      <td>16.022</td>
      <td>11.408</td>
      <td>8.785</td>
      <td>7.878</td>
      <td>5.874</td>
      <td>3.310</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>31.989</td>
      <td>16.778</td>
      <td>9.673</td>
      <td>9.026</td>
      <td>7.810</td>
      <td>5.350</td>
      <td>3.825</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>31.210</td>
      <td>15.663</td>
      <td>9.108</td>
      <td>9.440</td>
      <td>7.490</td>
      <td>5.776</td>
      <td>4.572</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>27.777</td>
      <td>16.573</td>
      <td>9.099</td>
      <td>9.940</td>
      <td>7.267</td>
      <td>6.678</td>
      <td>5.520</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>27.583</td>
      <td>14.982</td>
      <td>8.669</td>
      <td>9.829</td>
      <td>7.727</td>
      <td>6.624</td>
      <td>5.477</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>26.890</td>
      <td>12.465</td>
      <td>8.661</td>
      <td>8.886</td>
      <td>9.453</td>
      <td>6.056</td>
      <td>5.215</td>
    </tr>
  </tbody>
</table>
</div>



### <a id='toc1_7_2_'></a>[인덱스 이름은 따로 설정한다](#toc0_)


```python
df2.index.name = 'year'
df2
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
      <th>KBS</th>
      <th>MBC</th>
      <th>SBS</th>
      <th>TV CHOSUN</th>
      <th>JTBC</th>
      <th>Channel A</th>
      <th>MBN</th>
    </tr>
    <tr>
      <th>year</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2011</th>
      <td>35.951</td>
      <td>18.374</td>
      <td>11.173</td>
      <td>9.102</td>
      <td>7.380</td>
      <td>3.771</td>
      <td>2.809</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>36.163</td>
      <td>16.022</td>
      <td>11.408</td>
      <td>8.785</td>
      <td>7.878</td>
      <td>5.874</td>
      <td>3.310</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>31.989</td>
      <td>16.778</td>
      <td>9.673</td>
      <td>9.026</td>
      <td>7.810</td>
      <td>5.350</td>
      <td>3.825</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>31.210</td>
      <td>15.663</td>
      <td>9.108</td>
      <td>9.440</td>
      <td>7.490</td>
      <td>5.776</td>
      <td>4.572</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>27.777</td>
      <td>16.573</td>
      <td>9.099</td>
      <td>9.940</td>
      <td>7.267</td>
      <td>6.678</td>
      <td>5.520</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>27.583</td>
      <td>14.982</td>
      <td>8.669</td>
      <td>9.829</td>
      <td>7.727</td>
      <td>6.624</td>
      <td>5.477</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>26.890</td>
      <td>12.465</td>
      <td>8.661</td>
      <td>8.886</td>
      <td>9.453</td>
      <td>6.056</td>
      <td>5.215</td>
    </tr>
  </tbody>
</table>
</div>



### <a id='toc1_7_3_'></a>[인덱스를 지정할 수도 있다](#toc0_)


```python
df2.set_index('SBS')
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
      <th>KBS</th>
      <th>MBC</th>
      <th>TV CHOSUN</th>
      <th>JTBC</th>
      <th>Channel A</th>
      <th>MBN</th>
    </tr>
    <tr>
      <th>SBS</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>11.173</th>
      <td>35.951</td>
      <td>18.374</td>
      <td>9.102</td>
      <td>7.380</td>
      <td>3.771</td>
      <td>2.809</td>
    </tr>
    <tr>
      <th>11.408</th>
      <td>36.163</td>
      <td>16.022</td>
      <td>8.785</td>
      <td>7.878</td>
      <td>5.874</td>
      <td>3.310</td>
    </tr>
    <tr>
      <th>9.673</th>
      <td>31.989</td>
      <td>16.778</td>
      <td>9.026</td>
      <td>7.810</td>
      <td>5.350</td>
      <td>3.825</td>
    </tr>
    <tr>
      <th>9.108</th>
      <td>31.210</td>
      <td>15.663</td>
      <td>9.440</td>
      <td>7.490</td>
      <td>5.776</td>
      <td>4.572</td>
    </tr>
    <tr>
      <th>9.099</th>
      <td>27.777</td>
      <td>16.573</td>
      <td>9.940</td>
      <td>7.267</td>
      <td>6.678</td>
      <td>5.520</td>
    </tr>
    <tr>
      <th>8.669</th>
      <td>27.583</td>
      <td>14.982</td>
      <td>9.829</td>
      <td>7.727</td>
      <td>6.624</td>
      <td>5.477</td>
    </tr>
    <tr>
      <th>8.661</th>
      <td>26.890</td>
      <td>12.465</td>
      <td>8.886</td>
      <td>9.453</td>
      <td>6.056</td>
      <td>5.215</td>
    </tr>
  </tbody>
</table>
</div>



### <a id='toc1_7_4_'></a>[인덱스를 지정하면 기존 인덱스가 날아가니 살리려면 작업해야 한다](#toc0_)


```python
df2['year'] = df2.index
df2.set_index('SBS')
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
      <th>KBS</th>
      <th>MBC</th>
      <th>TV CHOSUN</th>
      <th>JTBC</th>
      <th>Channel A</th>
      <th>MBN</th>
      <th>year</th>
    </tr>
    <tr>
      <th>SBS</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>11.173</th>
      <td>35.951</td>
      <td>18.374</td>
      <td>9.102</td>
      <td>7.380</td>
      <td>3.771</td>
      <td>2.809</td>
      <td>2011</td>
    </tr>
    <tr>
      <th>11.408</th>
      <td>36.163</td>
      <td>16.022</td>
      <td>8.785</td>
      <td>7.878</td>
      <td>5.874</td>
      <td>3.310</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>9.673</th>
      <td>31.989</td>
      <td>16.778</td>
      <td>9.026</td>
      <td>7.810</td>
      <td>5.350</td>
      <td>3.825</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>9.108</th>
      <td>31.210</td>
      <td>15.663</td>
      <td>9.440</td>
      <td>7.490</td>
      <td>5.776</td>
      <td>4.572</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>9.099</th>
      <td>27.777</td>
      <td>16.573</td>
      <td>9.940</td>
      <td>7.267</td>
      <td>6.678</td>
      <td>5.520</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>8.669</th>
      <td>27.583</td>
      <td>14.982</td>
      <td>9.829</td>
      <td>7.727</td>
      <td>6.624</td>
      <td>5.477</td>
      <td>2016</td>
    </tr>
    <tr>
      <th>8.661</th>
      <td>26.890</td>
      <td>12.465</td>
      <td>8.886</td>
      <td>9.453</td>
      <td>6.056</td>
      <td>5.215</td>
      <td>2017</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.read_csv('toeic.csv')

# 여기에 코드를 작성하세요

# 테스트 코드
df['합격 여부'] = False
cond = (df['LC'] >= 250) & (df['RC'] >= 250) & ((df['LC'] + df['RC']) >= 600)
df.loc[cond, '합격 여부'] = True



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
      <th>Gender</th>
      <th>LC</th>
      <th>RC</th>
      <th>합격 여부</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>female</td>
      <td>315</td>
      <td>320</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>female</td>
      <td>430</td>
      <td>245</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>female</td>
      <td>430</td>
      <td>475</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>male</td>
      <td>180</td>
      <td>220</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>male</td>
      <td>325</td>
      <td>350</td>
      <td>True</td>
    </tr>
    <tr>
      <th>5</th>
      <td>female</td>
      <td>295</td>
      <td>400</td>
      <td>True</td>
    </tr>
    <tr>
      <th>6</th>
      <td>female</td>
      <td>405</td>
      <td>475</td>
      <td>True</td>
    </tr>
    <tr>
      <th>7</th>
      <td>male</td>
      <td>155</td>
      <td>150</td>
      <td>False</td>
    </tr>
    <tr>
      <th>8</th>
      <td>male</td>
      <td>280</td>
      <td>315</td>
      <td>False</td>
    </tr>
    <tr>
      <th>9</th>
      <td>female</td>
      <td>215</td>
      <td>475</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



칼럼에 결과값을 넣을 땐 그냥 연산만 지정해줘도 연산 결과로 넣어준다


```python
df = pd.read_csv('toeic.csv')

pass_total = df['LC'] + df['RC'] > 600
pass_both = (df['LC'] >= 250) & (df['RC'] >= 250)
df['합격 여부'] = pass_total & pass_both

# 테스트 코드
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
      <th>Gender</th>
      <th>LC</th>
      <th>RC</th>
      <th>합격 여부</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>female</td>
      <td>315</td>
      <td>320</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>female</td>
      <td>430</td>
      <td>245</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>female</td>
      <td>430</td>
      <td>475</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>male</td>
      <td>180</td>
      <td>220</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>male</td>
      <td>325</td>
      <td>350</td>
      <td>True</td>
    </tr>
    <tr>
      <th>5</th>
      <td>female</td>
      <td>295</td>
      <td>400</td>
      <td>True</td>
    </tr>
    <tr>
      <th>6</th>
      <td>female</td>
      <td>405</td>
      <td>475</td>
      <td>True</td>
    </tr>
    <tr>
      <th>7</th>
      <td>male</td>
      <td>155</td>
      <td>150</td>
      <td>False</td>
    </tr>
    <tr>
      <th>8</th>
      <td>male</td>
      <td>280</td>
      <td>315</td>
      <td>False</td>
    </tr>
    <tr>
      <th>9</th>
      <td>female</td>
      <td>215</td>
      <td>475</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



아래 그림에서 아래 아래 그림으로 코드 4줄로 바꾸기

![puzzle](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=1024&directory=2-8-1.png&name=2-8-1.png)

![puzzle2](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=1024&directory=2-8-2.png&name=2-8-2.png)


```python
df = pd.read_csv('Puzzle_before.csv')
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
      <th>F</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>55</td>
      <td>70</td>
      <td>87</td>
      <td>56</td>
      <td>13</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>45</td>
      <td>60</td>
      <td>99</td>
      <td>53</td>
      <td>24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>88</td>
      <td>70</td>
      <td>94</td>
      <td>39</td>
      <td>29</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>97</td>
      <td>80</td>
      <td>24</td>
      <td>83</td>
      <td>78</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>13</td>
      <td>90</td>
      <td>26</td>
      <td>80</td>
      <td>61</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['A'] = df['A'] * 2
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
      <th>F</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>55</td>
      <td>70</td>
      <td>87</td>
      <td>56</td>
      <td>13</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>45</td>
      <td>60</td>
      <td>99</td>
      <td>53</td>
      <td>24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>88</td>
      <td>70</td>
      <td>94</td>
      <td>39</td>
      <td>29</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8</td>
      <td>97</td>
      <td>80</td>
      <td>24</td>
      <td>83</td>
      <td>78</td>
    </tr>
    <tr>
      <th>4</th>
      <td>10</td>
      <td>13</td>
      <td>90</td>
      <td>26</td>
      <td>80</td>
      <td>61</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['F'][2] = 99
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
      <th>F</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>55</td>
      <td>70</td>
      <td>87</td>
      <td>56</td>
      <td>13</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>45</td>
      <td>60</td>
      <td>99</td>
      <td>53</td>
      <td>24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>88</td>
      <td>70</td>
      <td>94</td>
      <td>39</td>
      <td>99</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8</td>
      <td>97</td>
      <td>80</td>
      <td>24</td>
      <td>83</td>
      <td>78</td>
    </tr>
    <tr>
      <th>4</th>
      <td>10</td>
      <td>13</td>
      <td>90</td>
      <td>26</td>
      <td>80</td>
      <td>61</td>
    </tr>
  </tbody>
</table>
</div>




```python
# df.loc[df['B'] < 80, 'B'] = 0
# df.loc[df['C'] < 80, 'C'] = 0
# df.loc[df['D'] < 80, 'D'] = 0
# df.loc[df['E'] < 80, 'E'] = 0
# df
```


```python
# df.loc[df['B'] >= 80, 'B'] = 1
# df.loc[df['C'] >= 80, 'C'] = 1
# df.loc[df['D'] >= 80, 'D'] = 1
# df.loc[df['E'] >= 80, 'E'] = 1
# df
```

답에 거의 다 왔었네 일단 조건값을 만드는 것까진 왔었다


```python
cond = df.loc[:, 'B':'E'] < 80
```


```python
df[cond]
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
      <th>F</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>55.0</td>
      <td>70.0</td>
      <td>NaN</td>
      <td>56.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>45.0</td>
      <td>60.0</td>
      <td>NaN</td>
      <td>53.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>70.0</td>
      <td>NaN</td>
      <td>39.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>24.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>13.0</td>
      <td>NaN</td>
      <td>26.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



그런데 이 조건값으로 df를 조회하면 NaN을 포함한 거여서 어떻게 쓰지 했었다  


- 그러나 이 조건값으로 보는 df[cond]가 사실은 필터링 된 결과값이다 value를 반환하는 거다  
- 그러므로 아래처럼 df[cond] = 0을 하면 필터링 된 결과들만 0으로 처리가 된다
- NaN들 한텐 아무 영향이 없다

- df[칼럼명], df[불리언] 형태로 쓰는 걸 유념하자


```python
df[cond] = 0
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
      <th>F</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>87</td>
      <td>0</td>
      <td>13</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>99</td>
      <td>0</td>
      <td>24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>88</td>
      <td>0</td>
      <td>94</td>
      <td>0</td>
      <td>99</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8</td>
      <td>97</td>
      <td>80</td>
      <td>0</td>
      <td>83</td>
      <td>78</td>
    </tr>
    <tr>
      <th>4</th>
      <td>10</td>
      <td>0</td>
      <td>90</td>
      <td>0</td>
      <td>80</td>
      <td>61</td>
    </tr>
  </tbody>
</table>
</div>




```python
cond2 = df.loc[:, 'B':'E'] >= 80
```


```python
df[cond2] = 1
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
      <th>F</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>13</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>99</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>78</td>
    </tr>
    <tr>
      <th>4</th>
      <td>10</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>61</td>
    </tr>
  </tbody>
</table>
</div>



인터넷을 뒤져도 이런 대답은 찾을 수 없었다. 필터링을 하면 결과값이 반환되는 거고 그 결과값만 조작할 수 있구나. 배워서 다행이고 고맙다 이 간단한 문제에 30분 넘게 썼지만 전혀 아깝지 않다

## <a id='toc1_8_'></a>[큰 데이터 다루기](#toc0_)
---


```python
df.shape
```




    (5, 6)




```python
df.head(3)
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
      <th>F</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>13</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>99</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.tail(3)
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
      <th>F</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>99</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>78</td>
    </tr>
    <tr>
      <th>4</th>
      <td>10</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>61</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.columns
```




    Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')




```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 5 entries, 0 to 4
    Data columns (total 6 columns):
     #   Column  Non-Null Count  Dtype
    ---  ------  --------------  -----
     0   A       5 non-null      int64
     1   B       5 non-null      int64
     2   C       5 non-null      int64
     3   D       5 non-null      int64
     4   E       5 non-null      int64
     5   F       5 non-null      int64
    dtypes: int64(6)
    memory usage: 368.0 bytes
    


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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
      <th>F</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>6.000000</td>
      <td>0.400000</td>
      <td>0.400000</td>
      <td>0.600000</td>
      <td>0.400000</td>
      <td>55.000000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>3.162278</td>
      <td>0.547723</td>
      <td>0.547723</td>
      <td>0.547723</td>
      <td>0.547723</td>
      <td>36.145539</td>
    </tr>
    <tr>
      <th>min</th>
      <td>2.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>13.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>4.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>24.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>6.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>61.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>8.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>78.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>10.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>99.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.sort_values(by='A')
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
      <th>F</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>13</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>99</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>78</td>
    </tr>
    <tr>
      <th>4</th>
      <td>10</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>61</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.sort_values(by='A', ascending=False)
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
      <th>F</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>10</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>61</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>78</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>99</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>24</td>
    </tr>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>13</td>
    </tr>
  </tbody>
</table>
</div>




```python
sr = df['A']
```


```python
sr.unique()
```




    array([ 2,  4,  6,  8, 10], dtype=int64)




```python
sr.value_counts()
```




    A
    2     1
    4     1
    6     1
    8     1
    10    1
    Name: count, dtype: int64




```python
sr.describe()
```




    count     5.000000
    mean      6.000000
    std       3.162278
    min       2.000000
    25%       4.000000
    50%       6.000000
    75%       8.000000
    max      10.000000
    Name: A, dtype: float64




```python
d = pd.read_csv('world_cities.csv')
d
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
      <th>Unnamed: 0</th>
      <th>City / Urban area</th>
      <th>Country</th>
      <th>Population</th>
      <th>Land area (in sqKm)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Buenos Aires</td>
      <td>Argentina</td>
      <td>11200000</td>
      <td>2266</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Melbourne</td>
      <td>Australia</td>
      <td>3162000</td>
      <td>2080</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Sydney</td>
      <td>Australia</td>
      <td>3502000</td>
      <td>1687</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Brisbane</td>
      <td>Australia</td>
      <td>1508000</td>
      <td>1603</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Perth</td>
      <td>Australia</td>
      <td>1177000</td>
      <td>964</td>
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
      <th>244</th>
      <td>245</td>
      <td>Canton</td>
      <td>USA</td>
      <td>267000</td>
      <td>372</td>
    </tr>
    <tr>
      <th>245</th>
      <td>246</td>
      <td>Spokane</td>
      <td>USA</td>
      <td>335000</td>
      <td>371</td>
    </tr>
    <tr>
      <th>246</th>
      <td>247</td>
      <td>Tashkent</td>
      <td>Uzbekistan</td>
      <td>2200000</td>
      <td>531</td>
    </tr>
    <tr>
      <th>247</th>
      <td>248</td>
      <td>Ho Chi Minh City</td>
      <td>Vietnam</td>
      <td>4900000</td>
      <td>518</td>
    </tr>
    <tr>
      <th>248</th>
      <td>249</td>
      <td>Harare</td>
      <td>Zimbabwe</td>
      <td>1750000</td>
      <td>712</td>
    </tr>
  </tbody>
</table>
<p>249 rows × 5 columns</p>
</div>




```python
d['City / Urban area'].describe()
```




    count              249
    unique             249
    top       Buenos Aires
    freq                 1
    Name: City / Urban area, dtype: object




```python
d['Country'].describe()
```




    count     249
    unique     61
    top       USA
    freq      105
    Name: Country, dtype: object




```python
b = d['Population']/d['Land area (in sqKm)'] > 10000
b.value_counts()
```




    False    230
    True      19
    Name: count, dtype: int64




```python
n = d['Population']/d['Land area (in sqKm)']
```


```python
d['density'] = n
d.sort_values(by='density', ascending=False)
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
      <th>Unnamed: 0</th>
      <th>City / Urban area</th>
      <th>Country</th>
      <th>Population</th>
      <th>Land area (in sqKm)</th>
      <th>density</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>75</th>
      <td>75</td>
      <td>Mumbai</td>
      <td>India</td>
      <td>14350000</td>
      <td>484</td>
      <td>29648.760331</td>
    </tr>
    <tr>
      <th>74</th>
      <td>74</td>
      <td>Kolkata</td>
      <td>India</td>
      <td>12700000</td>
      <td>531</td>
      <td>23917.137476</td>
    </tr>
    <tr>
      <th>101</th>
      <td>101</td>
      <td>Karachi</td>
      <td>Pakistan</td>
      <td>9800000</td>
      <td>518</td>
      <td>18918.918919</td>
    </tr>
    <tr>
      <th>99</th>
      <td>99</td>
      <td>Lagos</td>
      <td>Nigeria</td>
      <td>13400000</td>
      <td>738</td>
      <td>18157.181572</td>
    </tr>
    <tr>
      <th>34</th>
      <td>34</td>
      <td>Shenzhen</td>
      <td>China</td>
      <td>8000000</td>
      <td>466</td>
      <td>17167.381974</td>
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
      <th>194</th>
      <td>195</td>
      <td>Chattanooga</td>
      <td>USA</td>
      <td>344000</td>
      <td>751</td>
      <td>458.055925</td>
    </tr>
    <tr>
      <th>223</th>
      <td>224</td>
      <td>Asheville</td>
      <td>USA</td>
      <td>222000</td>
      <td>536</td>
      <td>414.179104</td>
    </tr>
    <tr>
      <th>57</th>
      <td>57</td>
      <td>Pau</td>
      <td>France</td>
      <td>181000</td>
      <td>450</td>
      <td>402.222222</td>
    </tr>
    <tr>
      <th>220</th>
      <td>221</td>
      <td>Hickory</td>
      <td>USA</td>
      <td>188000</td>
      <td>546</td>
      <td>344.322344</td>
    </tr>
    <tr>
      <th>196</th>
      <td>197</td>
      <td>Barnstable Town</td>
      <td>USA</td>
      <td>244000</td>
      <td>741</td>
      <td>329.284750</td>
    </tr>
  </tbody>
</table>
<p>249 rows × 6 columns</p>
</div>




```python
cond = d.value_counts(subset='Country')
cond
```




    Country
    USA            105
    France          15
    Brazil          10
    Canada           9
    Germany          8
                  ... 
    Israel           1
    Kuwait           1
    Malaysia         1
    Netherlands      1
    Zimbabwe         1
    Name: count, Length: 61, dtype: int64




```python
cond[cond == 4]
```




    Country
    Italy    4
    Name: count, dtype: int64



위와 다르게 세는 법도 있었다  
**그냥 그 칼럼만 뗀 다음에 값을 세면 된다**


```python
d['Country'].value_counts()
```




    Country
    USA            105
    France          15
    Brazil          10
    Canada           9
    Germany          8
                  ... 
    Israel           1
    Kuwait           1
    Malaysia         1
    Netherlands      1
    Zimbabwe         1
    Name: count, Length: 61, dtype: int64



여기서 조회하는 건 값이 4인 곳이다. 무엇의 값이 4인가? 이건 시리즈다 그래서 칼럼 이름이 뭐지 고민했었는데 칼럼이 아예 없는 거다  
**대신 시리즈 이름이 값의 이름이다**


```python
cnt = d['Country'].value_counts()
cnt[cnt == 4]
```




    Country
    Italy    4
    Name: count, dtype: int64



이 문제도 혼자 풀긴 했는데 시간이 꽤 걸렸다 머리 써보는 재미


```python
df = pd.read_csv('enrolment_1.csv')
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
      <th>id</th>
      <th>year</th>
      <th>course name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2777729</td>
      <td>1</td>
      <td>information technology</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2777730</td>
      <td>2</td>
      <td>science</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2777765</td>
      <td>1</td>
      <td>arts</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2777766</td>
      <td>2</td>
      <td>arts</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2777785</td>
      <td>1</td>
      <td>mba</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1995</th>
      <td>2796805</td>
      <td>3</td>
      <td>computer application</td>
    </tr>
    <tr>
      <th>1996</th>
      <td>2796812</td>
      <td>1</td>
      <td>nursing</td>
    </tr>
    <tr>
      <th>1997</th>
      <td>2796813</td>
      <td>2</td>
      <td>nursing</td>
    </tr>
    <tr>
      <th>1998</th>
      <td>2796814</td>
      <td>3</td>
      <td>nursing</td>
    </tr>
    <tr>
      <th>1999</th>
      <td>2796815</td>
      <td>4</td>
      <td>nursing</td>
    </tr>
  </tbody>
</table>
<p>2000 rows × 3 columns</p>
</div>




```python
df['status'] = 'allowed'
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
      <th>id</th>
      <th>year</th>
      <th>course name</th>
      <th>status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2777729</td>
      <td>1</td>
      <td>information technology</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2777730</td>
      <td>2</td>
      <td>science</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2777765</td>
      <td>1</td>
      <td>arts</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2777766</td>
      <td>2</td>
      <td>arts</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2777785</td>
      <td>1</td>
      <td>mba</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1995</th>
      <td>2796805</td>
      <td>3</td>
      <td>computer application</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>1996</th>
      <td>2796812</td>
      <td>1</td>
      <td>nursing</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>1997</th>
      <td>2796813</td>
      <td>2</td>
      <td>nursing</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>1998</th>
      <td>2796814</td>
      <td>3</td>
      <td>nursing</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>1999</th>
      <td>2796815</td>
      <td>4</td>
      <td>nursing</td>
      <td>allowed</td>
    </tr>
  </tbody>
</table>
<p>2000 rows × 4 columns</p>
</div>



ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ


하 ... 틀린 이유는 “information technology” 과목은 심화과목이라 1학년은 수강할 수 없습니다.

이게 조건인데 
```
cond1 = (df['course name'] == 'information technology') & (df['year'] != 1)
```
1학년이 아니면 못 듣는다고 해놔서 그렇다

원하는 대로 코드를 치는 건 문제가 없었다 잘못 이해했었다  
앞으로는 뭘 하려고 하는지 잘 이해하자


```python
cond1 = (df['course name'] == 'information technology') & (df['year'] == 1)
cond2 = (df['course name'] == 'commerce') & (df['year'] == 4)
```


```python
df.loc[cond1, 'status'] = 'not allowed'
df.loc[cond2, 'status'] = 'not allowed'
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
      <th>id</th>
      <th>year</th>
      <th>course name</th>
      <th>status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2777729</td>
      <td>1</td>
      <td>information technology</td>
      <td>not allowed</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2777730</td>
      <td>2</td>
      <td>science</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2777765</td>
      <td>1</td>
      <td>arts</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2777766</td>
      <td>2</td>
      <td>arts</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2777785</td>
      <td>1</td>
      <td>mba</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1995</th>
      <td>2796805</td>
      <td>3</td>
      <td>computer application</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>1996</th>
      <td>2796812</td>
      <td>1</td>
      <td>nursing</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>1997</th>
      <td>2796813</td>
      <td>2</td>
      <td>nursing</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>1998</th>
      <td>2796814</td>
      <td>3</td>
      <td>nursing</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>1999</th>
      <td>2796815</td>
      <td>4</td>
      <td>nursing</td>
      <td>allowed</td>
    </tr>
  </tbody>
</table>
<p>2000 rows × 4 columns</p>
</div>




```python
df[cond1]
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
      <th>id</th>
      <th>year</th>
      <th>course name</th>
      <th>status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2777729</td>
      <td>1</td>
      <td>information technology</td>
      <td>not allowed</td>
    </tr>
    <tr>
      <th>612</th>
      <td>2783664</td>
      <td>1</td>
      <td>information technology</td>
      <td>not allowed</td>
    </tr>
    <tr>
      <th>1017</th>
      <td>2787200</td>
      <td>1</td>
      <td>information technology</td>
      <td>not allowed</td>
    </tr>
    <tr>
      <th>1218</th>
      <td>2789267</td>
      <td>1</td>
      <td>information technology</td>
      <td>not allowed</td>
    </tr>
    <tr>
      <th>1284</th>
      <td>2789753</td>
      <td>1</td>
      <td>information technology</td>
      <td>not allowed</td>
    </tr>
    <tr>
      <th>1836</th>
      <td>2795583</td>
      <td>1</td>
      <td>information technology</td>
      <td>not allowed</td>
    </tr>
    <tr>
      <th>1931</th>
      <td>2796418</td>
      <td>1</td>
      <td>information technology</td>
      <td>not allowed</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[(df['course name'] == 'information technology') & (df['year'] == 1)]
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
      <th>id</th>
      <th>year</th>
      <th>course name</th>
      <th>status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2777729</td>
      <td>1</td>
      <td>information technology</td>
      <td>not allowed</td>
    </tr>
    <tr>
      <th>612</th>
      <td>2783664</td>
      <td>1</td>
      <td>information technology</td>
      <td>not allowed</td>
    </tr>
    <tr>
      <th>1017</th>
      <td>2787200</td>
      <td>1</td>
      <td>information technology</td>
      <td>not allowed</td>
    </tr>
    <tr>
      <th>1218</th>
      <td>2789267</td>
      <td>1</td>
      <td>information technology</td>
      <td>not allowed</td>
    </tr>
    <tr>
      <th>1284</th>
      <td>2789753</td>
      <td>1</td>
      <td>information technology</td>
      <td>not allowed</td>
    </tr>
    <tr>
      <th>1836</th>
      <td>2795583</td>
      <td>1</td>
      <td>information technology</td>
      <td>not allowed</td>
    </tr>
    <tr>
      <th>1931</th>
      <td>2796418</td>
      <td>1</td>
      <td>information technology</td>
      <td>not allowed</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[cond2]
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
      <th>id</th>
      <th>year</th>
      <th>course name</th>
      <th>status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>29</th>
      <td>2777900</td>
      <td>4</td>
      <td>commerce</td>
      <td>not allowed</td>
    </tr>
    <tr>
      <th>161</th>
      <td>2779222</td>
      <td>4</td>
      <td>commerce</td>
      <td>not allowed</td>
    </tr>
    <tr>
      <th>546</th>
      <td>2783130</td>
      <td>4</td>
      <td>commerce</td>
      <td>not allowed</td>
    </tr>
    <tr>
      <th>1074</th>
      <td>2787740</td>
      <td>4</td>
      <td>commerce</td>
      <td>not allowed</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[(df['course name'] == 'commerce') & (df['year'] != 4)]['status'].describe()
```




    count         101
    unique          1
    top       allowed
    freq          101
    Name: status, dtype: object




```python
df['status'][df['status'] == 'not allowed']
```




    0       not allowed
    29      not allowed
    161     not allowed
    546     not allowed
    612     not allowed
    1017    not allowed
    1074    not allowed
    1218    not allowed
    1284    not allowed
    1836    not allowed
    1931    not allowed
    Name: status, dtype: object




```python
# import pandas as pd

# df = pd.read_csv('./data/enrolment_1.csv')
# df['status'] = 'allowed'

# cond1 = (df['course name'] == 'information technology') & (df['year'] != 1)
# cond2 = (df['course name'] == 'commerce') & (df['year'] == 4)

# df.loc[cond1, 'status'] = 'not allowed'
# df.loc[cond2, 'status'] = 'not allowed'

# cnt = df['course name'].value_counts()
# course = cnt[cnt < 5].index
# course = list(course)

# for x in df['course name']:
#     if x in course:
#         cond = df['course name'] == x
#         df.loc[cond, 'status'] = 'not allowed'

# df
########## 처음에 썼던 답
```


```python
cnt = df['course name'].value_counts()
# df['course name'][df['course name'] == cnt]
cnt
# cnt[cnt < 5]
```




    course name
    arts                         158
    science                      123
    commerce                     105
    english                       56
    education                     41
                                ... 
    arthroscopy                    1
    aih                            1
    sciences                       1
    library and information        1
    home sc. food & nutrition      1
    Name: count, Length: 296, dtype: int64



ㅡ,.ㅡ 흠냐  
이렇게 과목명으로만 카운트 하면 방금 전에 2가지 조건으로 수강불가 처리한 허수 신청자를 걸러내지 못한다 ...  
그렇게 중요한 내용은 힌트로라도 알려줘야지 이게 코딩 수업이야 논리 수업이야  

거의 1시간 매달렸다. 코딩 구현하는 데 대부분의 시간을 쓰긴 했는데 구현해놓고도 답이 안 맞으니 승질이 나 안 나?

바꿨는데 달라지는 게 없는데?

그렇다 이것 때문에 틀린 게 아니었다. 컨디션 1을 잘못 이해했던 거다 ㅠㅠ  
이건 그나마 답안이 있으니까 비교해서 알면 다행인데 야생에서 이러면 곤란하다  


**안 풀리는 게 있으면 우선 이미 짰던 내용은 주석을 달아가면서 내 의도랑 코딩이랑 같은 내용인지 비교해보자**


```python
cnt = df.loc[df['status'] == 'allowed', 'course name']
cnt
```




    1                    science
    2                       arts
    3                       arts
    4                        mba
    5                        mba
                    ...         
    1995    computer application
    1996                 nursing
    1997                 nursing
    1998                 nursing
    1999                 nursing
    Name: course name, Length: 1989, dtype: object




```python
cnt = cnt.value_counts()
cnt
```




    course name
    arts                     158
    science                  123
    commerce                 101
    english                   56
    education                 41
                            ... 
    environmental science      1
    jmc                        1
    biological sciences        1
    aqua culture               1
    dcl                        1
    Name: count, Length: 296, dtype: int64




```python
cnt[cnt < 5]
```




    course name
    applied sc.                               4
    electrical engg                           4
    chemical                                  4
    electrical and electronics engineering    4
    electronics and communication             4
                                             ..
    environmental science                     1
    jmc                                       1
    biological sciences                       1
    aqua culture                              1
    dcl                                       1
    Name: count, Length: 214, dtype: int64




```python
course = cnt[cnt < 5].index
course
```




    Index(['applied sc.', 'electrical engg', 'chemical',
           'electrical and electronics engineering',
           'electronics and communication', 'instrumentation engineering',
           'computer engg with specialization in cloud computing.',
           'electronics & communication engineering', 'civil engg',
           'mechanical engg.',
           ...
           'school of management', 'library and information', 'sciences', 'aih',
           'arthroscopy', 'environmental science', 'jmc', 'biological sciences',
           'aqua culture', 'dcl'],
          dtype='object', name='course name', length=214)




```python
course = list(course)
course
```




    ['applied sc.',
     'electrical engg',
     'chemical',
     'electrical and electronics engineering',
     'electronics and communication',
     'instrumentation engineering',
     'computer engg with specialization in cloud computing.',
     'electronics & communication engineering',
     'civil engg',
     'mechanical engg.',
     'physical education',
     'engg. & tech.',
     'bpt',
     'electros & communicationnic',
     'mechanical related subjects',
     'mech',
     'information subjects',
     'data structure',
     'pathology',
     'database',
     'agriculture',
     'korean',
     'fashion communication',
     'electronics and instrumentation',
     'refactoring',
     'leather design',
     'computer architecture',
     'environment',
     'tool & die making',
     'ai & as',
     'master of computer application',
     'buisiness administration',
     'digital electronics',
     'compulsory',
     'electronics & comm engg',
     'b.com.',
     'i.t',
     'jain darshan',
     'bbi',
     'co-operation',
     'c bc bt',
     'vocational',
     'corporate secaratoryship',
     'comp science',
     'b.com (p)',
     'm.i.l',
     'b.com.(gen.e/m)',
     'industrial microbiology',
     'computer engg',
     'software computer science',
     'politics',
     'diploma',
     'all subjects',
     'sahitya',
     'mca 2nd shift',
     'music vocal',
     'tm',
     'em',
     'res',
     'pol-science',
     'saskrit',
     'travel tourism & hospitality management',
     'computers',
     'gandhian thought',
     'cmmerce',
     'hons.',
     'medicine',
     'tb & chest',
     'eep',
     'bca',
     'btzc',
     'bjmc',
     'comp(em)',
     'bcom (general)',
     'applied science & humanities',
     'bcom marketing',
     'bcom computer',
     '3 year ll.b course',
     'science(bzc)',
     'b.sc-m.p.c',
     'anaesthesiology',
     'mobile communication',
     'community medicine',
     'bcom finance and taxation',
     'computers (ug)',
     'mangement',
     'electronics & comm. engg.',
     'dcp',
     'deee',
     'diploma in computer engineering',
     'yes',
     'electronics & communication engineeering',
     'mat',
     'bsc bzc',
     'tax procedure and practice',
     'rasshastra evum bhaisgya kalpana',
     'english literature',
     'kayachikitsa',
     'administration services',
     'if',
     'professional  accounting',
     'bsc mpe',
     'civit',
     'discipline',
     'electronic',
     'electronics engineering',
     'bsc btmc',
     'b.b.m',
     'microbiology-botany-chemistry',
     'co',
     'admistrator',
     'bio technology',
     'veterinary epidemiology & preventive medicine',
     'aero dynamics',
     'electronics & communication engg.  with specialization in  vlsi design & embedded systems',
     'dmrd',
     'nano science & technology',
     'information security',
     'git',
     'physical science',
     'nutrition & dietetics',
     'd.ed',
     '(biotechnology))',
     'social science',
     'scientific computing',
     'd.el.ed',
     'cad/cam',
     'btc-2012',
     'hcl',
     'quality assurance',
     'mass relation',
     'civil and environmental engineering',
     'material science and engineering',
     'architecture',
     'nuclear science & engineering',
     'data science',
     'it cs',
     'medical surgical nursing',
     'vlsi design and signal processing',
     'environmental engg.',
     'mpharmacy',
     'mpharmacypa',
     'pharmaceutics',
     'fibre optics and communication',
     'spl. education',
     'vlsi',
     'communication and signal processing',
     'mba 2nd shift',
     'special education (h.i.)',
     'electro nics and commun ications enginee ring',
     'b.ed.',
     'construction technology and management',
     'structural engineering',
     'taalvadya-parichay',
     'power & energy systems',
     'co-education',
     'pharmacognosy',
     'computational mathematics',
     'dharmashastra',
     'infra structural engineering',
     'm.com',
     'science arts',
     'molecular virology',
     'political sc',
     'construction technology',
     'social studies',
     'english geography',
     'social work',
     'international business',
     'history & archeology',
     'transportation engineering',
     'math chemistry',
     'lab technology',
     'power systems engineering',
     'btc 2013',
     'biochemistry',
     'computer integrated manufacturing',
     'drugs and pharmaceuticals',
     'polotical',
     'computer appplication',
     'arts/commerce/science/maths',
     'automobile engineering',
     'm.sc chemistry(analytical chemistry)',
     'chmistry',
     'thermal power engineering',
     'digital communicati ons',
     'msc cs',
     'dance-parangat',
     'humanities and social science (h',
     'b.ed',
     'technician',
     'chemstry',
     'arts/science',
     'home sc. food & nutrition',
     'library & information & science',
     'statistics',
     'computer science (lateral entry)',
     'physical edu.',
     'full time',
     'punjabi',
     'lib. & info sci',
     'pg.diploma',
     'pgdca',
     'library',
     'school of management',
     'library and information',
     'sciences',
     'aih',
     'arthroscopy',
     'environmental science',
     'jmc',
     'biological sciences',
     'aqua culture',
     'dcl']



소름. 지금 힌트 보는데 힌트3번까지 이미 왔었다


```python
# df['course name'][df['course name'] is in course]
```


```python
# df2 = df
```


```python
# smp = ['aih']
```


```python
# if 'aih' in smp:
#     print('y')
```


```python
# for x in df2['course name']:
#     if x in smp:
#         print(x)
        

```


```python
# see = []
```


```python
# con = df2['course name'] == 'aih'
# df2.loc[con, 'status'] = 'joking'
# df2.loc[con, 'status']
```


```python
# df2[df2['course name'] == 'aih']['status'] = 'joking'
# df2[df2['course name'] == 'aih']['status']
```


```python
# for x in df2['course name']:
#     if x in course:
#         cond = df2['course name'] == x
#         df2.loc[cond, 'status'] = 'not allowed'
# df2
```


```python
# df2[df2['course name'] == 'aih']
```


```python
df[df['course name'] == 'aih']
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
      <th>id</th>
      <th>year</th>
      <th>course name</th>
      <th>status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>541</th>
      <td>2783091</td>
      <td>4</td>
      <td>aih</td>
      <td>allowed</td>
    </tr>
  </tbody>
</table>
</div>



우선 이렇게 값을 수정할 떈
```python
df.loc[cond, 'status'] = 'not allowed'
```
이런 식으로 .loc을 써서 조건과 칼럼을 넣어야 한다는 걸 잘 배웠다


```python
for x in df['course name']:
    if x in course:
        cond = df['course name'] == x
        df.loc[cond, 'status'] = 'not allowed'
```


```python
df[df['course name'] == 'aih']
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
      <th>id</th>
      <th>year</th>
      <th>course name</th>
      <th>status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>541</th>
      <td>2783091</td>
      <td>4</td>
      <td>aih</td>
      <td>not allowed</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[df['course name'] == 'music']
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
      <th>id</th>
      <th>year</th>
      <th>course name</th>
      <th>status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>162</th>
      <td>2779286</td>
      <td>1</td>
      <td>music</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>163</th>
      <td>2779287</td>
      <td>2</td>
      <td>music</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>164</th>
      <td>2779288</td>
      <td>3</td>
      <td>music</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>165</th>
      <td>2779289</td>
      <td>4</td>
      <td>music</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>1757</th>
      <td>2794801</td>
      <td>4</td>
      <td>music</td>
      <td>allowed</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['status'].describe()
```




    count        2000
    unique          2
    top       allowed
    freq         1447
    Name: status, dtype: object




```python
search = df['status'] == 'not allowed'
df.loc[search, 'course name'].value_counts()
```




    course name
    information technology              7
    chemical                            4
    applied sc.                         4
    environment                         4
    electronics and communication       4
                                       ..
    library                             1
    school of management                1
    computer science (lateral entry)    1
    arthroscopy                         1
    lib. & info sci                     1
    Name: count, Length: 216, dtype: int64




```python
'commerce' in df.loc[search, 'course name'].value_counts()
```




    True




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
      <th>id</th>
      <th>year</th>
      <th>course name</th>
      <th>status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2777729</td>
      <td>1</td>
      <td>information technology</td>
      <td>not allowed</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2777730</td>
      <td>2</td>
      <td>science</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2777765</td>
      <td>1</td>
      <td>arts</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2777766</td>
      <td>2</td>
      <td>arts</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2777785</td>
      <td>1</td>
      <td>mba</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1995</th>
      <td>2796805</td>
      <td>3</td>
      <td>computer application</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>1996</th>
      <td>2796812</td>
      <td>1</td>
      <td>nursing</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>1997</th>
      <td>2796813</td>
      <td>2</td>
      <td>nursing</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>1998</th>
      <td>2796814</td>
      <td>3</td>
      <td>nursing</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>1999</th>
      <td>2796815</td>
      <td>4</td>
      <td>nursing</td>
      <td>allowed</td>
    </tr>
  </tbody>
</table>
<p>2000 rows × 4 columns</p>
</div>




```python
tf = pd.read_csv('enrolment_1.csv')
tf["status"] = "allowed"

# 조건 1
boolean1 = tf["course name"] == "information technology"
boolean2 = tf["year"] == 1
tf.loc[boolean1 & boolean2, "status"] = "not allowed"

# 조건 2
boolean3= tf["course name"] == "commerce"
boolean4= tf["year"] == 4
tf.loc[boolean3 & boolean4, "status"] = "not allowed"

# 조건 3
allowed = tf["status"] == "allowed"
course_counts = tf.loc[allowed, "course name"].value_counts()
closed_courses = list(course_counts[course_counts < 5].index)
for course in closed_courses:
    tf.loc[tf["course name"] == course, "status"] = "not allowed"

# 테스트 코드
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
      <th>id</th>
      <th>year</th>
      <th>course name</th>
      <th>status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2777729</td>
      <td>1</td>
      <td>information technology</td>
      <td>not allowed</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2777730</td>
      <td>2</td>
      <td>science</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2777765</td>
      <td>1</td>
      <td>arts</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2777766</td>
      <td>2</td>
      <td>arts</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2777785</td>
      <td>1</td>
      <td>mba</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1995</th>
      <td>2796805</td>
      <td>3</td>
      <td>computer application</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>1996</th>
      <td>2796812</td>
      <td>1</td>
      <td>nursing</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>1997</th>
      <td>2796813</td>
      <td>2</td>
      <td>nursing</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>1998</th>
      <td>2796814</td>
      <td>3</td>
      <td>nursing</td>
      <td>allowed</td>
    </tr>
    <tr>
      <th>1999</th>
      <td>2796815</td>
      <td>4</td>
      <td>nursing</td>
      <td>allowed</td>
    </tr>
  </tbody>
</table>
<p>2000 rows × 4 columns</p>
</div>




```python
tf['room assignment'] = 'not assigned'
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
      <th>id</th>
      <th>year</th>
      <th>course name</th>
      <th>status</th>
      <th>room assignment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2777729</td>
      <td>1</td>
      <td>information technology</td>
      <td>not allowed</td>
      <td>not assigned</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2777730</td>
      <td>2</td>
      <td>science</td>
      <td>allowed</td>
      <td>not assigned</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2777765</td>
      <td>1</td>
      <td>arts</td>
      <td>allowed</td>
      <td>not assigned</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2777766</td>
      <td>2</td>
      <td>arts</td>
      <td>allowed</td>
      <td>not assigned</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2777785</td>
      <td>1</td>
      <td>mba</td>
      <td>allowed</td>
      <td>not assigned</td>
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
      <th>1995</th>
      <td>2796805</td>
      <td>3</td>
      <td>computer application</td>
      <td>allowed</td>
      <td>not assigned</td>
    </tr>
    <tr>
      <th>1996</th>
      <td>2796812</td>
      <td>1</td>
      <td>nursing</td>
      <td>allowed</td>
      <td>not assigned</td>
    </tr>
    <tr>
      <th>1997</th>
      <td>2796813</td>
      <td>2</td>
      <td>nursing</td>
      <td>allowed</td>
      <td>not assigned</td>
    </tr>
    <tr>
      <th>1998</th>
      <td>2796814</td>
      <td>3</td>
      <td>nursing</td>
      <td>allowed</td>
      <td>not assigned</td>
    </tr>
    <tr>
      <th>1999</th>
      <td>2796815</td>
      <td>4</td>
      <td>nursing</td>
      <td>allowed</td>
      <td>not assigned</td>
    </tr>
  </tbody>
</table>
<p>2000 rows × 5 columns</p>
</div>




```python
allowed = tf["status"] == "allowed"
course_counts = tf.loc[allowed, "course name"].value_counts()

# 폐강 등의 이유로 status가 “not allowed”인 수강생은 room assignment 또한 “not assigned”가 되어야 합니다.    
tf.loc[tf["status"] == 'not allowed', "room assignment"] = "not assigned"

# 5명 이상, 15명 미만의 학생이 수강하는 과목은 “Small room”에서 진행됩니다.
small = list(course_counts[(5 <= course_counts) & (course_counts < 15)].index)
for course in small:
    tf.loc[(tf["course name"] == course) & allowed, "room assignment"] = "Small room"

# 15명 이상, 40명 미만의 학생이 수강하는 과목은 “Medium room”에서 진행됩니다.
medium = list(course_counts[(15 <= course_counts) & (course_counts < 40)].index)
for course in medium:
    tf.loc[(tf["course name"] == course) & allowed, "room assignment"] = "Medium room"

# 40명 이상, 80명 미만의 학생이 수강하는 과목은 “Large room”에서 진행됩니다.
large = list(course_counts[(40 <= course_counts) & (course_counts < 80)].index)
for course in large:
    tf.loc[(tf["course name"] == course) & allowed, "room assignment"] = "Large room"

# 80명 이상의 학생이 수강하는 과목은 “Auditorium”에서 진행됩니다.
audi = list(course_counts[course_counts >= 80].index)
for course in audi:
    tf.loc[(tf["course name"] == course) & allowed, "room assignment"] = "Auditorium"

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
      <th>id</th>
      <th>year</th>
      <th>course name</th>
      <th>status</th>
      <th>room assignment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2777729</td>
      <td>1</td>
      <td>information technology</td>
      <td>not allowed</td>
      <td>not assigned</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2777730</td>
      <td>2</td>
      <td>science</td>
      <td>allowed</td>
      <td>Auditorium</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2777765</td>
      <td>1</td>
      <td>arts</td>
      <td>allowed</td>
      <td>Auditorium</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2777766</td>
      <td>2</td>
      <td>arts</td>
      <td>allowed</td>
      <td>Auditorium</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2777785</td>
      <td>1</td>
      <td>mba</td>
      <td>allowed</td>
      <td>Small room</td>
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
      <th>1995</th>
      <td>2796805</td>
      <td>3</td>
      <td>computer application</td>
      <td>allowed</td>
      <td>Medium room</td>
    </tr>
    <tr>
      <th>1996</th>
      <td>2796812</td>
      <td>1</td>
      <td>nursing</td>
      <td>allowed</td>
      <td>Medium room</td>
    </tr>
    <tr>
      <th>1997</th>
      <td>2796813</td>
      <td>2</td>
      <td>nursing</td>
      <td>allowed</td>
      <td>Medium room</td>
    </tr>
    <tr>
      <th>1998</th>
      <td>2796814</td>
      <td>3</td>
      <td>nursing</td>
      <td>allowed</td>
      <td>Medium room</td>
    </tr>
    <tr>
      <th>1999</th>
      <td>2796815</td>
      <td>4</td>
      <td>nursing</td>
      <td>allowed</td>
      <td>Medium room</td>
    </tr>
  </tbody>
</table>
<p>2000 rows × 5 columns</p>
</div>




```python
tf.loc[tf['status'] == 'not allowed', 'room assignment'].describe()
```




    count              553
    unique               1
    top       not assigned
    freq               553
    Name: room assignment, dtype: object




```python
# 과목별 인원 가져오기
allowed = df["status"] == "allowed"
course_counts = df.loc[allowed, "course name"].value_counts()

# 각 강의실 규모에 해당되는 과목 리스트 만들기
auditorium_list = list(course_counts[course_counts >= 80].index)
large_room_list = list(course_counts[(80 > course_counts) & (course_counts >= 40)].index)
medium_room_list = list(course_counts[(40 > course_counts) & (course_counts >= 15)].index)
small_room_list = list(course_counts[(15 > course_counts) & (course_counts > 4)].index)

# not allowed 과목에 대해 값 지정해주기
not_allowed = df["status"] == "not allowed"
df.loc[not_allowed, "room assignment"] = "not assigned"

# allowed 과목에 대해 값 지정해주기
for course in auditorium_list:
    df.loc[(df["course name"] == course) & allowed, "room assignment"] = "Auditorium"

for course in large_room_list:
    df.loc[(df["course name"] == course) & allowed, "room assignment"] = "Large room"
    
for course in medium_room_list:
    df.loc[(df["course name"] == course) & allowed, "room assignment"] = "Medium room"
    
for course in small_room_list:
    df.loc[(df["course name"] == course) & allowed, "room assignment"] = "Small room"
    
# 정답 출력
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
      <th>id</th>
      <th>year</th>
      <th>course name</th>
      <th>status</th>
      <th>room assignment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2777729</td>
      <td>1</td>
      <td>information technology</td>
      <td>not allowed</td>
      <td>not assigned</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2777730</td>
      <td>2</td>
      <td>science</td>
      <td>allowed</td>
      <td>Auditorium</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2777765</td>
      <td>1</td>
      <td>arts</td>
      <td>allowed</td>
      <td>Auditorium</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2777766</td>
      <td>2</td>
      <td>arts</td>
      <td>allowed</td>
      <td>Auditorium</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2777785</td>
      <td>1</td>
      <td>mba</td>
      <td>allowed</td>
      <td>Small room</td>
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
      <th>1995</th>
      <td>2796805</td>
      <td>3</td>
      <td>computer application</td>
      <td>allowed</td>
      <td>Medium room</td>
    </tr>
    <tr>
      <th>1996</th>
      <td>2796812</td>
      <td>1</td>
      <td>nursing</td>
      <td>allowed</td>
      <td>Medium room</td>
    </tr>
    <tr>
      <th>1997</th>
      <td>2796813</td>
      <td>2</td>
      <td>nursing</td>
      <td>allowed</td>
      <td>Medium room</td>
    </tr>
    <tr>
      <th>1998</th>
      <td>2796814</td>
      <td>3</td>
      <td>nursing</td>
      <td>allowed</td>
      <td>Medium room</td>
    </tr>
    <tr>
      <th>1999</th>
      <td>2796815</td>
      <td>4</td>
      <td>nursing</td>
      <td>allowed</td>
      <td>Medium room</td>
    </tr>
  </tbody>
</table>
<p>2000 rows × 5 columns</p>
</div>




```python
small
```




    ['sociology',
     'sanskrit',
     'computer applications',
     'hindi',
     'information technology',
     'computer engineering',
     'electronics & communication engg',
     'ee',
     'urdu',
     'business administration',
     'bzc',
     'philosophy',
     'yoga',
     'bengali',
     'marathi',
     'political science',
     'electrical engineering',
     'maths',
     'computer science & engineering',
     'finance',
     'technical',
     'ece',
     'me',
     'electrical & electronics engineering',
     'biotechnology',
     'computer science and engineering',
     'ug',
     'physiotherapy',
     'electronics',
     'bio-chemistry',
     'general medicine',
     'electronics and communication engineering',
     'anatomy',
     'bio chemistry',
     'mpcs',
     'mecs',
     'mpc',
     'mba',
     'ca',
     'mechanical engg',
     'pali',
     'home science',
     'cbz',
     'engineering & technology',
     'geography',
     'maithili',
     'psychology',
     'music',
     'mca',
     'nanotechnology',
     'building construction and mangement',
     'interior design',
     'dental']




```python
list(tf[tf['course name'] == 'ee']['room assignment'])
```




    ['Small room',
     'Small room',
     'Small room',
     'Small room',
     'Small room',
     'Small room',
     'Small room',
     'Small room',
     'Small room',
     'Small room',
     'Small room',
     'Small room']




```python
tf[tf['course name'] == 'ee']
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
      <th>id</th>
      <th>year</th>
      <th>course name</th>
      <th>status</th>
      <th>room assignment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>854</th>
      <td>2786016</td>
      <td>4</td>
      <td>ee</td>
      <td>allowed</td>
      <td>Small room</td>
    </tr>
    <tr>
      <th>855</th>
      <td>2786017</td>
      <td>4</td>
      <td>ee</td>
      <td>allowed</td>
      <td>Small room</td>
    </tr>
    <tr>
      <th>962</th>
      <td>2786698</td>
      <td>1</td>
      <td>ee</td>
      <td>allowed</td>
      <td>Small room</td>
    </tr>
    <tr>
      <th>963</th>
      <td>2786699</td>
      <td>2</td>
      <td>ee</td>
      <td>allowed</td>
      <td>Small room</td>
    </tr>
    <tr>
      <th>964</th>
      <td>2786700</td>
      <td>3</td>
      <td>ee</td>
      <td>allowed</td>
      <td>Small room</td>
    </tr>
    <tr>
      <th>965</th>
      <td>2786701</td>
      <td>4</td>
      <td>ee</td>
      <td>allowed</td>
      <td>Small room</td>
    </tr>
    <tr>
      <th>966</th>
      <td>2786708</td>
      <td>1</td>
      <td>ee</td>
      <td>allowed</td>
      <td>Small room</td>
    </tr>
    <tr>
      <th>967</th>
      <td>2786709</td>
      <td>2</td>
      <td>ee</td>
      <td>allowed</td>
      <td>Small room</td>
    </tr>
    <tr>
      <th>968</th>
      <td>2786710</td>
      <td>3</td>
      <td>ee</td>
      <td>allowed</td>
      <td>Small room</td>
    </tr>
    <tr>
      <th>1175</th>
      <td>2788637</td>
      <td>1</td>
      <td>ee</td>
      <td>allowed</td>
      <td>Small room</td>
    </tr>
    <tr>
      <th>1176</th>
      <td>2788638</td>
      <td>2</td>
      <td>ee</td>
      <td>allowed</td>
      <td>Small room</td>
    </tr>
    <tr>
      <th>1177</th>
      <td>2788639</td>
      <td>3</td>
      <td>ee</td>
      <td>allowed</td>
      <td>Small room</td>
    </tr>
  </tbody>
</table>
</div>




```python
# sm = tf["room assignment"] == "Small room"
# sms = tf.loc[sm, "course name"].value_counts()
# list(sms.index)
```


```python
# i = 1
# issmall = tf["room assignment"] == "Small room"
# for course in small:
#     tf.loc[(tf["room assignment"] == "Small room"), "room assignment"] = f'{tf[issmall]["room assignment"]}-{i}'
#     i += 1
```


```python
for n in range(0, len(sorted(small))):
    iscourse = tf['course name'] == sorted(small)[n]
    tf.loc[iscourse, 'room assignment'] = f'Small room-{n+1}'
tf[tf['course name'] == 'ee']
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
      <th>id</th>
      <th>year</th>
      <th>course name</th>
      <th>status</th>
      <th>room assignment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>854</th>
      <td>2786016</td>
      <td>4</td>
      <td>ee</td>
      <td>allowed</td>
      <td>Small room-17</td>
    </tr>
    <tr>
      <th>855</th>
      <td>2786017</td>
      <td>4</td>
      <td>ee</td>
      <td>allowed</td>
      <td>Small room-17</td>
    </tr>
    <tr>
      <th>962</th>
      <td>2786698</td>
      <td>1</td>
      <td>ee</td>
      <td>allowed</td>
      <td>Small room-17</td>
    </tr>
    <tr>
      <th>963</th>
      <td>2786699</td>
      <td>2</td>
      <td>ee</td>
      <td>allowed</td>
      <td>Small room-17</td>
    </tr>
    <tr>
      <th>964</th>
      <td>2786700</td>
      <td>3</td>
      <td>ee</td>
      <td>allowed</td>
      <td>Small room-17</td>
    </tr>
    <tr>
      <th>965</th>
      <td>2786701</td>
      <td>4</td>
      <td>ee</td>
      <td>allowed</td>
      <td>Small room-17</td>
    </tr>
    <tr>
      <th>966</th>
      <td>2786708</td>
      <td>1</td>
      <td>ee</td>
      <td>allowed</td>
      <td>Small room-17</td>
    </tr>
    <tr>
      <th>967</th>
      <td>2786709</td>
      <td>2</td>
      <td>ee</td>
      <td>allowed</td>
      <td>Small room-17</td>
    </tr>
    <tr>
      <th>968</th>
      <td>2786710</td>
      <td>3</td>
      <td>ee</td>
      <td>allowed</td>
      <td>Small room-17</td>
    </tr>
    <tr>
      <th>1175</th>
      <td>2788637</td>
      <td>1</td>
      <td>ee</td>
      <td>allowed</td>
      <td>Small room-17</td>
    </tr>
    <tr>
      <th>1176</th>
      <td>2788638</td>
      <td>2</td>
      <td>ee</td>
      <td>allowed</td>
      <td>Small room-17</td>
    </tr>
    <tr>
      <th>1177</th>
      <td>2788639</td>
      <td>3</td>
      <td>ee</td>
      <td>allowed</td>
      <td>Small room-17</td>
    </tr>
  </tbody>
</table>
</div>




```python
# small room에 배정되는 강의들 마다 작업한다
i = 1
for course in sorted(small):
    # small room을 쓰는 강의목록
    # num = range(1, len(small)+1)
    # small room인 강의들을 따로 뺀다
    iscourse = tf['course name'] == course
    tf.loc[iscourse, 'room assignment'] = f'Small room-{i}'
    i += 1
    # 1번부터 끝번까지 
    # for n in num:
    #     tf.loc[iscourse, 'room assignment'] = f'{tf[iscourse]["room assignment"]} + {n}'
tf[tf['course name'] == 'ee']
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
      <th>id</th>
      <th>year</th>
      <th>course name</th>
      <th>status</th>
      <th>room assignment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>854</th>
      <td>2786016</td>
      <td>4</td>
      <td>ee</td>
      <td>allowed</td>
      <td>Small room-17</td>
    </tr>
    <tr>
      <th>855</th>
      <td>2786017</td>
      <td>4</td>
      <td>ee</td>
      <td>allowed</td>
      <td>Small room-17</td>
    </tr>
    <tr>
      <th>962</th>
      <td>2786698</td>
      <td>1</td>
      <td>ee</td>
      <td>allowed</td>
      <td>Small room-17</td>
    </tr>
    <tr>
      <th>963</th>
      <td>2786699</td>
      <td>2</td>
      <td>ee</td>
      <td>allowed</td>
      <td>Small room-17</td>
    </tr>
    <tr>
      <th>964</th>
      <td>2786700</td>
      <td>3</td>
      <td>ee</td>
      <td>allowed</td>
      <td>Small room-17</td>
    </tr>
    <tr>
      <th>965</th>
      <td>2786701</td>
      <td>4</td>
      <td>ee</td>
      <td>allowed</td>
      <td>Small room-17</td>
    </tr>
    <tr>
      <th>966</th>
      <td>2786708</td>
      <td>1</td>
      <td>ee</td>
      <td>allowed</td>
      <td>Small room-17</td>
    </tr>
    <tr>
      <th>967</th>
      <td>2786709</td>
      <td>2</td>
      <td>ee</td>
      <td>allowed</td>
      <td>Small room-17</td>
    </tr>
    <tr>
      <th>968</th>
      <td>2786710</td>
      <td>3</td>
      <td>ee</td>
      <td>allowed</td>
      <td>Small room-17</td>
    </tr>
    <tr>
      <th>1175</th>
      <td>2788637</td>
      <td>1</td>
      <td>ee</td>
      <td>allowed</td>
      <td>Small room-17</td>
    </tr>
    <tr>
      <th>1176</th>
      <td>2788638</td>
      <td>2</td>
      <td>ee</td>
      <td>allowed</td>
      <td>Small room-17</td>
    </tr>
    <tr>
      <th>1177</th>
      <td>2788639</td>
      <td>3</td>
      <td>ee</td>
      <td>allowed</td>
      <td>Small room-17</td>
    </tr>
  </tbody>
</table>
</div>




```python
tf[tf['course name'] == 'me']
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
      <th>id</th>
      <th>year</th>
      <th>course name</th>
      <th>status</th>
      <th>room assignment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>826</th>
      <td>2785894</td>
      <td>1</td>
      <td>me</td>
      <td>allowed</td>
      <td>Small room-36</td>
    </tr>
    <tr>
      <th>827</th>
      <td>2785895</td>
      <td>1</td>
      <td>me</td>
      <td>allowed</td>
      <td>Small room-36</td>
    </tr>
    <tr>
      <th>828</th>
      <td>2785896</td>
      <td>2</td>
      <td>me</td>
      <td>allowed</td>
      <td>Small room-36</td>
    </tr>
    <tr>
      <th>829</th>
      <td>2785897</td>
      <td>2</td>
      <td>me</td>
      <td>allowed</td>
      <td>Small room-36</td>
    </tr>
    <tr>
      <th>830</th>
      <td>2785898</td>
      <td>3</td>
      <td>me</td>
      <td>allowed</td>
      <td>Small room-36</td>
    </tr>
    <tr>
      <th>831</th>
      <td>2785899</td>
      <td>3</td>
      <td>me</td>
      <td>allowed</td>
      <td>Small room-36</td>
    </tr>
    <tr>
      <th>832</th>
      <td>2785900</td>
      <td>4</td>
      <td>me</td>
      <td>allowed</td>
      <td>Small room-36</td>
    </tr>
    <tr>
      <th>833</th>
      <td>2785901</td>
      <td>4</td>
      <td>me</td>
      <td>allowed</td>
      <td>Small room-36</td>
    </tr>
  </tbody>
</table>
</div>




```python
for n in range(0, len(sorted(small))):
    iscourse = tf['course name'] == sorted(small)[n]
    tf.loc[iscourse & allowed, 'room assignment'] = f'Small-{n+1}'


for n in range(0, len(sorted(medium))):
    iscourse = tf['course name'] == sorted(medium)[n]
    tf.loc[iscourse & allowed, 'room assignment'] = f'Medium-{n+1}'


for n in range(0, len(sorted(large))):
    iscourse = tf['course name'] == sorted(large)[n]
    tf.loc[iscourse & allowed, 'room assignment'] = f'Large-{n+1}'


for n in range(0, len(sorted(audi))):
    iscourse = tf['course name'] == sorted(audi)[n]
    tf.loc[iscourse & allowed, 'room assignment'] = f'Auditorium-{n+1}'

# tf.loc[tf["status"] == 'not allowed', "room assignment"] = "not assigned"

# tf[tf['course name'] == 'hindi']
tf.rename(columns={'room assignment': 'room number'}, inplace=True)
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
      <th>id</th>
      <th>year</th>
      <th>course name</th>
      <th>status</th>
      <th>room number</th>
      <th>room number</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2777729</td>
      <td>1</td>
      <td>information technology</td>
      <td>not allowed</td>
      <td>not assigned</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2777730</td>
      <td>2</td>
      <td>science</td>
      <td>allowed</td>
      <td>Auditorium-3</td>
      <td>Auditorium-3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2777765</td>
      <td>1</td>
      <td>arts</td>
      <td>allowed</td>
      <td>Auditorium-1</td>
      <td>Auditorium-1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2777766</td>
      <td>2</td>
      <td>arts</td>
      <td>allowed</td>
      <td>Auditorium-1</td>
      <td>Auditorium-1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2777785</td>
      <td>1</td>
      <td>mba</td>
      <td>allowed</td>
      <td>Small room-34</td>
      <td>Small-34</td>
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
      <th>1995</th>
      <td>2796805</td>
      <td>3</td>
      <td>computer application</td>
      <td>allowed</td>
      <td>Medium room-7</td>
      <td>Medium-7</td>
    </tr>
    <tr>
      <th>1996</th>
      <td>2796812</td>
      <td>1</td>
      <td>nursing</td>
      <td>allowed</td>
      <td>Medium room-22</td>
      <td>Medium-22</td>
    </tr>
    <tr>
      <th>1997</th>
      <td>2796813</td>
      <td>2</td>
      <td>nursing</td>
      <td>allowed</td>
      <td>Medium room-22</td>
      <td>Medium-22</td>
    </tr>
    <tr>
      <th>1998</th>
      <td>2796814</td>
      <td>3</td>
      <td>nursing</td>
      <td>allowed</td>
      <td>Medium room-22</td>
      <td>Medium-22</td>
    </tr>
    <tr>
      <th>1999</th>
      <td>2796815</td>
      <td>4</td>
      <td>nursing</td>
      <td>allowed</td>
      <td>Medium room-22</td>
      <td>Medium-22</td>
    </tr>
  </tbody>
</table>
<p>2000 rows × 6 columns</p>
</div>



완성

꽤 오래 걸렸다. 그러나 스스로 잘 해냈다. 문제의 조건을 잘 보자. 칼럼 이름 바꾸는 걸 깜빡 했었다 ㅋㅋㅋ 그리고 강의실 이름도 이전 버전이랑 달라졌었다 강의실 이름 바뀐 건 내가 스스로 캐치했다. 하하하 문제의 조건을 잘 안 본다는 약점을 스스로 캐치하고 극복해서 짜릿하다


```python
tf = pd.read_csv('enrolment_1.csv')
tf["status"] = "allowed"

# 조건 1
boolean1 = tf["course name"] == "information technology"
boolean2 = tf["year"] == 1
tf.loc[boolean1 & boolean2, "status"] = "not allowed"

# 조건 2
boolean3= tf["course name"] == "commerce"
boolean4= tf["year"] == 4
tf.loc[boolean3 & boolean4, "status"] = "not allowed"

# 조건 3
allowed = tf["status"] == "allowed"
course_counts = tf.loc[allowed, "course name"].value_counts()
closed_courses = list(course_counts[course_counts < 5].index)
for course in closed_courses:
    tf.loc[tf["course name"] == course, "status"] = "not allowed"

# 5명 이상, 15명 미만의 학생이 수강하는 과목은 “Small room”에서 진행됩니다.
small = list(course_counts[(5 <= course_counts) & (course_counts < 15)].index)

# 15명 이상, 40명 미만의 학생이 수강하는 과목은 “Medium room”에서 진행됩니다.
medium = list(course_counts[(15 <= course_counts) & (course_counts < 40)].index)

# 40명 이상, 80명 미만의 학생이 수강하는 과목은 “Large room”에서 진행됩니다.
large = list(course_counts[(40 <= course_counts) & (course_counts < 80)].index)

# 80명 이상의 학생이 수강하는 과목은 “Auditorium”에서 진행됩니다.
audi = list(course_counts[course_counts >= 80].index)

tf.loc[tf["status"] == 'not allowed', "room assignment"] = "not assigned"

for n in range(0, len(sorted(small))):
    iscourse = tf['course name'] == sorted(small)[n]
    tf.loc[iscourse & allowed, 'room assignment'] = f'Small-{n+1}'


for n in range(0, len(sorted(medium))):
    iscourse = tf['course name'] == sorted(medium)[n]
    tf.loc[iscourse & allowed, 'room assignment'] = f'Medium-{n+1}'


for n in range(0, len(sorted(large))):
    iscourse = tf['course name'] == sorted(large)[n]
    tf.loc[iscourse & allowed, 'room assignment'] = f'Large-{n+1}'


for n in range(0, len(sorted(audi))):
    iscourse = tf['course name'] == sorted(audi)[n]
    tf.loc[iscourse & allowed, 'room assignment'] = f'Auditorium-{n+1}'



# tf[tf['course name'] == 'hindi']
tf.rename(columns={'room assignment': 'room number'}, inplace=True)
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
      <th>id</th>
      <th>year</th>
      <th>course name</th>
      <th>status</th>
      <th>room number</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2777729</td>
      <td>1</td>
      <td>information technology</td>
      <td>not allowed</td>
      <td>not assigned</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2777730</td>
      <td>2</td>
      <td>science</td>
      <td>allowed</td>
      <td>Auditorium-3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2777765</td>
      <td>1</td>
      <td>arts</td>
      <td>allowed</td>
      <td>Auditorium-1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2777766</td>
      <td>2</td>
      <td>arts</td>
      <td>allowed</td>
      <td>Auditorium-1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2777785</td>
      <td>1</td>
      <td>mba</td>
      <td>allowed</td>
      <td>Small-34</td>
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
      <th>1995</th>
      <td>2796805</td>
      <td>3</td>
      <td>computer application</td>
      <td>allowed</td>
      <td>Medium-7</td>
    </tr>
    <tr>
      <th>1996</th>
      <td>2796812</td>
      <td>1</td>
      <td>nursing</td>
      <td>allowed</td>
      <td>Medium-22</td>
    </tr>
    <tr>
      <th>1997</th>
      <td>2796813</td>
      <td>2</td>
      <td>nursing</td>
      <td>allowed</td>
      <td>Medium-22</td>
    </tr>
    <tr>
      <th>1998</th>
      <td>2796814</td>
      <td>3</td>
      <td>nursing</td>
      <td>allowed</td>
      <td>Medium-22</td>
    </tr>
    <tr>
      <th>1999</th>
      <td>2796815</td>
      <td>4</td>
      <td>nursing</td>
      <td>allowed</td>
      <td>Medium-22</td>
    </tr>
  </tbody>
</table>
<p>2000 rows × 5 columns</p>
</div>



## <a id='toc1_9_'></a>[수료증](https://www.codeit.kr/certificates/ShDif-jEnza-IiwXC-BgDHN) [&#8593;](#toc0_)
