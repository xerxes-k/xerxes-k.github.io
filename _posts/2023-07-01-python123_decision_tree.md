---
layout: single
title:  "decision tree"
---
# decision tree

ML > classification 중의 하나

예/아니오 질문으로 이어진 분류

![트리](https://bakey-api.codeit.kr/files/3112/Y0kw9y?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-05-19+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+8.35.57.png)


```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
import matplotlib.pyplot as plt
import numpy as np

import pandas as pd
```


```python
def survival_classifier(seat_belt, highway, speed, age):
    # 여기에 코드를 작성하세요
    if not seat_belt:
        if highway:
            if speed > 100:
                if age > 50:
                    return 1                    
    return 0
        
    
        
    

print(survival_classifier(False, True, 110, 55))
print(survival_classifier(True, False, 40, 70))
print(survival_classifier(False, True, 80, 25))
print(survival_classifier(False, True, 120, 60))
print(survival_classifier(True, False, 30, 20))
```

    1
    0
    0
    1
    0
    

## 지니 불순도 gini impurity
데이터 셋 안에 서로 다른 분류가 얼마나 섞여있는지 나타내는 값

1 - p(x)^2 - p(1-x)^2

지니 불순도가 클수록 데이터 셋이 불순하다
![지니](https://bakey-api.codeit.kr/files/3113/f4HXAP?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-05-19+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+8.40.39.png)

![지니2](https://bakey-api.codeit.kr/files/3113/j1gcQj?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-05-19+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+8.39.59.png)


```python
def ginie(total, x):
    g = 1 - (x / total)**2 - ((total - x) / total)**2
    return round(g, 3)
```


```python
ginie(210, 150)
```




    0.408




```python
ginie(1300, 600)
```




    0.497




```python
ginie(400, 350)
```




    0.219



### 분류 노드 평가하기

먼저, 분류 노드와 질문 노드가 있다
- 분류: a다 b다 판단을 내린다
- 질문: 속성에 대해 질문한다

속성들에 대해 예/아니오 답을 하면서 목표변수를 예측한다  
분류 노드가 좋은지 안 좋은지는 지니 불순도를 사용한다  
- 좋은 분류 노드는 최대한 많은 학습 데이터 예측을 맞춘다  
  - 불순도가 낮으려면 하나의 종류로만 있어야 한다


### 질문 노드 평가하기

질문 노드에서 나뉜 데이터 셋의 가중평균 지니 불순도가 낮을 수록 성능이 좋다

![](https://bakey-api.codeit.kr/files/3115/XmAJSv?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-05-19+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+6.58.19.png)
![](https://bakey-api.codeit.kr/files/3115/W1SlN9?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-05-19+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+6.58.25.png)
![](https://bakey-api.codeit.kr/files/3115/YmTDaF?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-05-19+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+7.03.48.png)

현재 시점에서 분류 노드를 만들었을 때의 지니 불순도와 질문 후보들의 지니 불순도를 비교해서 분류를 할지 질문을 할지 결정한다

![](https://bakey-api.codeit.kr/files/3116/gljlje?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-05-19+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+7.09.13.png)


```python
ginie(50, 10)
```




    0.32




```python
ginie(75, 60)
```




    0.32




```python
(50*0.32 + 75*0.32)/125
```




    0.32




```python
def question_node(l, lt, r, rt, total):
    lg = ginie(lt, l)
    rg = ginie(rt, r)
    return round((lt*lg + rt*rg)/total, 3)
```


```python
question_node(10, 50, 60, 75, 125)
```




    0.32




```python
question_node(40, 45, 10, 45, 90)
```




    0.272




```python
question_node(15, 95, 90, 90, 185)
```




    0.137



트리의 깊이 depth

필요 시 트리 깊이를 제한할 수 있다


![](https://velog.velcdn.com/images%2Fuvictoli%2Fpost%2Fd102da13-3eac-42ca-b0cb-5bd170f49824%2Fimage.png)

## Node importance = information gain

ni = n/m*GI - n(left)/m*GI(left) - n(right)/m*GI(right)

![](https://bakey-api.codeit.kr/files/3118/FN4X0W?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-05-19+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+7.25.11.png)


```python
90/90 * 0.333 - 60/90 * 0.270 - 30/90 * 0.222
```




    0.07900000000000003



- 해당 노드의 아래 노드들이 지니 불순도가 낮을수록 해당 노드의 중요도가 올라간다
- 해당 노드의 불순도가 높을수록 중요도가 올라간다
  - 불순도가 높았는데 이 노드를 지남으로써 불순도가 확 낮아진다면 중요한 노드다
- 전체 데이터 중 해당 노드를 지나는 데이터가 많으면 중요도가 올라간다

## feature importance = mean gini decrease

어떤 입력값이 중요한지 확인 할 때 해당 입력값과 관련 있는 노드들의 중요도가 얼마나 높은지로 확인할 수 있다

전체 노드들의 중요도를 더하고 그 중에서 해당 입력값과 관련 있는 노드들의 중요도가 얼만큼인지 보면 된다

![](https://bakey-api.codeit.kr/files/3118/bWeJVC?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-06-22+%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB+10.27.38.png)

![](https://bakey-api.codeit.kr/files/3118/jKdln6?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-05-19+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+7.27.05.png)

---


```python
iris = load_iris()
print(iris.DESCR)
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
X = pd.DataFrame(iris.data, columns=iris.feature_names)
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
y = pd.DataFrame(iris.target, columns=['Class'])
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
      <th>Class</th>
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
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=5)
```


```python
model = DecisionTreeClassifier(max_depth=4)
```


```python
model.fit(train_X, train_y)
```




<style>#sk-container-id-1 {color: black;background-color: white;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id="sk-container-id-1" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>DecisionTreeClassifier(max_depth=4)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-1" type="checkbox" checked><label for="sk-estimator-id-1" class="sk-toggleable__label sk-toggleable__label-arrow">DecisionTreeClassifier</label><div class="sk-toggleable__content"><pre>DecisionTreeClassifier(max_depth=4)</pre></div></div></div></div></div>




```python
model.predict(test_X)
```




    array([1, 2, 2, 0, 2, 2, 0, 2, 0, 1, 1, 1, 2, 2, 0, 0, 2, 2, 0, 0, 1, 2,
           0, 1, 1, 2, 1, 1, 1, 2])




```python
model.score(test_X, test_y)
```




    0.9




```python
importance = (model.feature_importances_)
```


```python
indices = np.argsort(importance)
plt.bar(range(len(importance)), importance[indices])
plt.xticks(range(len(importance)), X.columns[indices], rotation=90)
```




    ([<matplotlib.axis.XTick at 0x1c57fa4ce50>,
      <matplotlib.axis.XTick at 0x1c57fa4ce20>,
      <matplotlib.axis.XTick at 0x1c57fa4ca00>,
      <matplotlib.axis.XTick at 0x1c57fa5da80>],
     [Text(0, 0, 'sepal width (cm)'),
      Text(1, 0, 'petal length (cm)'),
      Text(2, 0, 'sepal length (cm)'),
      Text(3, 0, 'petal width (cm)')])




    
![png](output_42_1.png)
    


Trees have one aspect that prevents them from being the ideal tool for
predictive learning, namely inaccuracy

p.352 [the elements of statistical learning]

결정 트리 자체는 정확성이 떨어진다. 그러나 결정트리를 응용해 다른 모델을 만들 수 있다

책을 잠깐 봤는데 배운 내용도 있고 처음 보는 내용도 있다. 구체적인 페이지로 들어갔더니 수식들이 너무 많아 보기 어려웠다 ㅠㅠ

---

## 앙상블 ensemble

수 많은 모델을 종합해 사용

## 랜덤 포레스트 random forest (bagging을 사용한다)

트리 모델을 임의로 많이 만들어서 결과를 다수결 투표로 종합하는 알고리즘  
bootstrapping으로 임의의 데이터셋을 쓰고  
속성을 임의로 선택해서 수 많은 트리를 만든다

### bootstrapping

이미 있는 정보를 가지고 다른 정보를 만들어내는 방법  

머신러닝에서는 갖고 있는 데이터 셋을 shuffle 해서 새로운 데이터 셋을 만든다(중복, 탈락 가능)  
이렇게 bootstrapping 한 데이터 셋을 만들고 각 데이터 셋을 기반한 모델의 결정을 합친다(aggregating)  
= **bagging**

살짝 k-fold랑 겹치는데?


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
      <th>Class</th>
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
train_X
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
      <th>39</th>
      <td>5.1</td>
      <td>3.4</td>
      <td>1.5</td>
      <td>0.2</td>
    </tr>
    <tr>
      <th>53</th>
      <td>5.5</td>
      <td>2.3</td>
      <td>4.0</td>
      <td>1.3</td>
    </tr>
    <tr>
      <th>79</th>
      <td>5.7</td>
      <td>2.6</td>
      <td>3.5</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>5.4</td>
      <td>3.7</td>
      <td>1.5</td>
      <td>0.2</td>
    </tr>
    <tr>
      <th>50</th>
      <td>7.0</td>
      <td>3.2</td>
      <td>4.7</td>
      <td>1.4</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>4.4</td>
      <td>2.9</td>
      <td>1.4</td>
      <td>0.2</td>
    </tr>
    <tr>
      <th>73</th>
      <td>6.1</td>
      <td>2.8</td>
      <td>4.7</td>
      <td>1.2</td>
    </tr>
    <tr>
      <th>144</th>
      <td>6.7</td>
      <td>3.3</td>
      <td>5.7</td>
      <td>2.5</td>
    </tr>
    <tr>
      <th>118</th>
      <td>7.7</td>
      <td>2.6</td>
      <td>6.9</td>
      <td>2.3</td>
    </tr>
    <tr>
      <th>99</th>
      <td>5.7</td>
      <td>2.8</td>
      <td>4.1</td>
      <td>1.3</td>
    </tr>
  </tbody>
</table>
<p>120 rows × 4 columns</p>
</div>




```python
model = RandomForestClassifier(n_estimators=100, max_depth=4)
```


```python
model.fit(train_X, train_y)
```

    C:\Users\moonlight\AppData\Local\Temp\ipykernel_16312\1723167297.py:1: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples,), for example using ravel().
      model.fit(train_X, train_y)
    




<style>#sk-container-id-2 {color: black;background-color: white;}#sk-container-id-2 pre{padding: 0;}#sk-container-id-2 div.sk-toggleable {background-color: white;}#sk-container-id-2 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-2 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-2 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-2 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-2 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-2 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-2 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-2 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-container-id-2 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-2 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-2 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-2 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-2 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-2 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-2 div.sk-item {position: relative;z-index: 1;}#sk-container-id-2 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-2 div.sk-item::before, #sk-container-id-2 div.sk-parallel-item::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-2 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-2 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-2 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-2 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-2 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-2 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-2 div.sk-label-container {text-align: center;}#sk-container-id-2 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-2 div.sk-text-repr-fallback {display: none;}</style><div id="sk-container-id-2" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>RandomForestClassifier(max_depth=4)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-2" type="checkbox" checked><label for="sk-estimator-id-2" class="sk-toggleable__label sk-toggleable__label-arrow">RandomForestClassifier</label><div class="sk-toggleable__content"><pre>RandomForestClassifier(max_depth=4)</pre></div></div></div></div></div>




```python
model.predict(test_X)
```




    array([1, 2, 2, 0, 2, 1, 0, 2, 0, 1, 1, 1, 2, 2, 0, 0, 2, 2, 0, 0, 1, 2,
           0, 1, 1, 2, 1, 1, 1, 2])




```python
model.score(test_X, test_y)
```




    0.9333333333333333




```python
importance = (model.feature_importances_)
```


```python
indices = np.argsort(importance)
plt.bar(range(len(importance)), importance[indices])
plt.xticks(range(len(importance)), X.columns[indices], rotation=90)
```




    ([<matplotlib.axis.XTick at 0x1c57fab48b0>,
      <matplotlib.axis.XTick at 0x1c57fab61a0>,
      <matplotlib.axis.XTick at 0x1c57fc21cc0>,
      <matplotlib.axis.XTick at 0x1c57fabb5e0>],
     [Text(0, 0, 'sepal width (cm)'),
      Text(1, 0, 'sepal length (cm)'),
      Text(2, 0, 'petal length (cm)'),
      Text(3, 0, 'petal width (cm)')])




    
![png](output_58_1.png)
    


## adaboost (boosting을 사용한다)

- 일부러 성능이 안 좋은 모델을 사용
- 먼저 사용한 모델의 성능이 뒤에 사용하는 모델의 데이터 셋을 바꾼다
- 성능이 좋은 모델 결과에 가중치를 두고 반영한다

1. adaboost는 root node와 그에 대한 답변 2개만 달린 stump 들만을 쓴다  
2. 각 stump는 성능이 50% 정도 된다 즉 boosting은 weak learner를 쓴다  
3. 앞선 모델이 틀리게 분류한 데이터에 중요도를 부여해서 다음 모델은 앞 모델이 틀렸던 데이터를 맞추는 데 집중하게 한다  
4. 성능이 좋은 스텀프의 결과를 더 많이 반영한다

![](https://bakey-api.codeit.kr/files/3122/ZwmFUa?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-05-19+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+7.40.35.png)
![](https://bakey-api.codeit.kr/files/3122/oybAXS?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-05-19+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+7.40.50.png)

스텀프의 성능을 계산하는 데 중요도를 사용한다(중요도는 합이 1이 되도록 부여한다)
![](https://bakey-api.codeit.kr/files/3123/K0VSfr?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-05-19+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+7.49.23.png)

어떤 스텀프의 성능은 다음과 같은 함수로 정한다

1/2 * log(1-total_error/total_error)  
total_error = 잘못 분류한 데이터의 중요도 합

그림으로 표현하면  
![](https://bakey-api.codeit.kr/files/3123/0xnnjt?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-05-19+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+7.51.11.png)

따라서 에러가 0이면 무한히 높은 중요도를, 에러가 1이면 음수의 중요도를, 반만 맞추면 중요도 0을 부여한다

한 스텀프가 분류하고 나면 그 스텀프의 성능을 평가한 다음 데이터의 중요도를 갱신해준다

잘못 분류한 데이터 weight = weight * e^성능  
잘 분류한 데이터 weight = weight * e^-성능  

갱신 후에도 모든 중요도의 합은 1이 돼야 하므로 각 중요도 마다 (중요도 / 중요도의 합)으로 다시 갱신해준다

예를 들어

![](https://bakey-api.codeit.kr/files/3124/6RrgJp?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-05-19+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+7.56.16.png)

중요도는 다음과 같이 갱신되므로

![](https://bakey-api.codeit.kr/files/3124/YFDhRy?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-05-19+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+7.58.33.png)

중요도는 이렇게 계산된다

![](https://bakey-api.codeit.kr/files/3124/sO7Oal?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-05-19+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+7.57.15.png)

중요도 합이 1이 되도록 각 중요도를 총 중요도의 비율로 조정하면


![](https://bakey-api.codeit.kr/files/3124/5Q7NRu?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-05-19+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+7.57.36.png)

스텀프가 추가 될 때는 이전 분류 결과를 반영하여 데이터 셋을 만든다  
중요도를 누계로 표현해서 각 행에 범위를 부여한다  
난수를 생성해 해당 값이 속한 범위의 데이터를 새 데이터 셋에 포함한다  
- 이렇게 하면 중요도가 높은 데이터일수록 범위가 넓어 새 데이터에 포함될 확률이 높다
    - 중요도가 높은 데이터가 새 데이터 셋에 여러번 포함될 가능성이 있다

![](https://bakey-api.codeit.kr/files/3125/zRiTtZ?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-05-19+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+8.04.34.png)
![](https://bakey-api.codeit.kr/files/3125/we09xX?name=%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA+2020-05-19+%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE+8.05.05.png)

새 데이터 셋을 새 스텀프로 분류하고, 그 결과에 따라 원래 데이터셋의 데이터 중요도를 업데이트 한다  
즉 원래 데이터 셋은 존속하고 중요도를 여기서 계속 업데이트 한다

스텀프들의 분류 결과를 모아놓고 각 스텀프의 중요도에 따라 가중치를 부여해서 중요도가 높은 분류 결과를 채택한다


```python
model = AdaBoostClassifier(n_estimators=100)
```


```python
model.fit(train_X, train_y)
```

    c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\sklearn\utils\validation.py:1143: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().
      y = column_or_1d(y, warn=True)
    




<style>#sk-container-id-3 {color: black;background-color: white;}#sk-container-id-3 pre{padding: 0;}#sk-container-id-3 div.sk-toggleable {background-color: white;}#sk-container-id-3 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-3 label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-3 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-3 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-3 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-3 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-3 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-3 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-container-id-3 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-3 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-3 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-3 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-3 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-3 div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-3 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-3 div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-3 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-3 div.sk-item {position: relative;z-index: 1;}#sk-container-id-3 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-3 div.sk-item::before, #sk-container-id-3 div.sk-parallel-item::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-3 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-3 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-3 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-3 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-3 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-3 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-3 div.sk-label-container {text-align: center;}#sk-container-id-3 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-3 div.sk-text-repr-fallback {display: none;}</style><div id="sk-container-id-3" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>AdaBoostClassifier(n_estimators=100)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-3" type="checkbox" checked><label for="sk-estimator-id-3" class="sk-toggleable__label sk-toggleable__label-arrow">AdaBoostClassifier</label><div class="sk-toggleable__content"><pre>AdaBoostClassifier(n_estimators=100)</pre></div></div></div></div></div>




```python
model.predict(test_X)
```




    array([1, 1, 2, 0, 2, 2, 0, 2, 0, 1, 1, 1, 2, 2, 0, 0, 2, 2, 0, 0, 1, 2,
           0, 1, 1, 2, 1, 1, 1, 2])




```python
model.score(test_X, test_y)
```




    0.8666666666666667




```python
importance = model.feature_importances_
```


```python
indices = np.argsort(importance)
plt.bar(range(len(importance)), importance[indices])
plt.xticks(range(len(importance)), X.columns[indices], rotation=90)
```




    ([<matplotlib.axis.XTick at 0x1c57fb4e290>,
      <matplotlib.axis.XTick at 0x1c57fb4e260>,
      <matplotlib.axis.XTick at 0x1c57fb4de70>,
      <matplotlib.axis.XTick at 0x1c50303fdf0>],
     [Text(0, 0, 'sepal width (cm)'),
      Text(1, 0, 'sepal length (cm)'),
      Text(2, 0, 'petal width (cm)'),
      Text(3, 0, 'petal length (cm)')])




    
![png](output_80_1.png)
    

