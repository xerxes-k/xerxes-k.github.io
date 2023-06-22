---
layout: single
title:  "data visualization"
---
# Data Visualization

각 그래프의 특성을 알고 상황에 맞게 쓸 줄 알아야 한다


```python
%matplotlib inline
import pandas as pd
```


```python
df = pd.read_csv('broadcast.csv', index_col=0)
```


```python
df.plot()
#df.plot(kind='line') line이 기본값이다
```




    <Axes: >




    
![png](output_4_1.png)
    



```python
df.plot(y=['KBS', 'JTBC'])
```




    <Axes: >




    
![png](output_5_1.png)
    



```python
df['KBS']
```




    2011    35.951
    2012    36.163
    2013    31.989
    2014    31.210
    2015    27.777
    2016    27.583
    2017    26.890
    Name: KBS, dtype: float64




```python
df['KBS'].plot()
```




    <Axes: >




    
![png](output_7_1.png)
    



```python
df[['KBS', 'JTBC']]
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
      <th>JTBC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2011</th>
      <td>35.951</td>
      <td>7.380</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>36.163</td>
      <td>7.878</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>31.989</td>
      <td>7.810</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>31.210</td>
      <td>7.490</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>27.777</td>
      <td>7.267</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>27.583</td>
      <td>7.727</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>26.890</td>
      <td>9.453</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[['KBS', 'JTBC']].plot()
```




    <Axes: >




    
![png](output_9_1.png)
    



```python
gdp = pd.read_csv('gdp.csv', index_col=0)
gdp
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
      <th>Aruba</th>
      <th>Angola</th>
      <th>Albania</th>
      <th>Andorra</th>
      <th>Arab World</th>
      <th>United Arab Emirates</th>
      <th>Argentina</th>
      <th>Armenia</th>
      <th>Antigua and Barbuda</th>
      <th>Australia</th>
      <th>...</th>
      <th>St. Vincent and the Grenadines</th>
      <th>Vietnam</th>
      <th>Vanuatu</th>
      <th>World</th>
      <th>Samoa</th>
      <th>Kosovo</th>
      <th>Yemen, Rep.</th>
      <th>South Africa</th>
      <th>Zambia</th>
      <th>Zimbabwe</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000</th>
      <td>1.873453e+09</td>
      <td>9.129595e+09</td>
      <td>3.480355e+09</td>
      <td>1.434430e+09</td>
      <td>7.351881e+11</td>
      <td>1.043374e+11</td>
      <td>2.842038e+11</td>
      <td>1.911564e+09</td>
      <td>8.301588e+08</td>
      <td>4.150342e+11</td>
      <td>...</td>
      <td>3.962614e+08</td>
      <td>3.117252e+10</td>
      <td>2.720147e+08</td>
      <td>3.359786e+13</td>
      <td>2.690197e+08</td>
      <td>1.849196e+09</td>
      <td>9.652436e+09</td>
      <td>1.363619e+11</td>
      <td>3.600683e+09</td>
      <td>6.689958e+09</td>
    </tr>
    <tr>
      <th>2001</th>
      <td>1.920112e+09</td>
      <td>8.936064e+09</td>
      <td>3.922101e+09</td>
      <td>1.496913e+09</td>
      <td>7.234491e+11</td>
      <td>1.033116e+11</td>
      <td>2.686968e+11</td>
      <td>2.118468e+09</td>
      <td>8.007403e+08</td>
      <td>3.782151e+11</td>
      <td>...</td>
      <td>4.300393e+08</td>
      <td>3.268520e+10</td>
      <td>2.579269e+08</td>
      <td>3.340101e+13</td>
      <td>2.730884e+08</td>
      <td>2.535334e+09</td>
      <td>9.861560e+09</td>
      <td>1.216008e+11</td>
      <td>4.094481e+09</td>
      <td>6.777385e+09</td>
    </tr>
    <tr>
      <th>2002</th>
      <td>1.941341e+09</td>
      <td>1.528559e+10</td>
      <td>4.348068e+09</td>
      <td>1.733117e+09</td>
      <td>7.292314e+11</td>
      <td>1.098162e+11</td>
      <td>9.772400e+10</td>
      <td>2.376335e+09</td>
      <td>8.146153e+08</td>
      <td>3.944867e+11</td>
      <td>...</td>
      <td>4.618834e+08</td>
      <td>3.506411e+10</td>
      <td>2.626038e+08</td>
      <td>3.468623e+13</td>
      <td>2.880789e+08</td>
      <td>2.406271e+09</td>
      <td>1.069463e+10</td>
      <td>1.157481e+11</td>
      <td>4.193846e+09</td>
      <td>6.342116e+09</td>
    </tr>
    <tr>
      <th>2003</th>
      <td>2.021229e+09</td>
      <td>1.781271e+10</td>
      <td>5.611496e+09</td>
      <td>2.398646e+09</td>
      <td>8.233413e+11</td>
      <td>1.243464e+11</td>
      <td>1.275870e+11</td>
      <td>2.807061e+09</td>
      <td>8.556431e+08</td>
      <td>4.662947e+11</td>
      <td>...</td>
      <td>4.818063e+08</td>
      <td>3.955251e+10</td>
      <td>3.144631e+08</td>
      <td>3.892649e+13</td>
      <td>3.388386e+08</td>
      <td>2.790456e+09</td>
      <td>1.177797e+10</td>
      <td>1.752569e+11</td>
      <td>4.901840e+09</td>
      <td>5.727592e+09</td>
    </tr>
    <tr>
      <th>2004</th>
      <td>2.228492e+09</td>
      <td>2.355205e+10</td>
      <td>7.184686e+09</td>
      <td>2.935659e+09</td>
      <td>9.643273e+11</td>
      <td>1.478244e+11</td>
      <td>1.646579e+11</td>
      <td>3.576615e+09</td>
      <td>9.195771e+08</td>
      <td>6.119043e+11</td>
      <td>...</td>
      <td>5.219751e+08</td>
      <td>4.542785e+10</td>
      <td>3.649969e+08</td>
      <td>4.384476e+13</td>
      <td>4.203202e+08</td>
      <td>3.556757e+09</td>
      <td>1.387279e+10</td>
      <td>2.289373e+11</td>
      <td>6.221078e+09</td>
      <td>5.805598e+09</td>
    </tr>
    <tr>
      <th>2005</th>
      <td>2.330726e+09</td>
      <td>3.697092e+10</td>
      <td>8.052074e+09</td>
      <td>3.255789e+09</td>
      <td>1.185143e+12</td>
      <td>1.806170e+11</td>
      <td>1.987371e+11</td>
      <td>4.900470e+09</td>
      <td>1.022191e+09</td>
      <td>6.926417e+11</td>
      <td>...</td>
      <td>5.507287e+08</td>
      <td>5.763326e+10</td>
      <td>3.949626e+08</td>
      <td>4.748718e+13</td>
      <td>4.626490e+08</td>
      <td>3.663102e+09</td>
      <td>1.674634e+10</td>
      <td>2.576714e+11</td>
      <td>8.331870e+09</td>
      <td>5.755215e+09</td>
    </tr>
    <tr>
      <th>2006</th>
      <td>2.424581e+09</td>
      <td>5.238101e+10</td>
      <td>8.896073e+09</td>
      <td>3.543257e+09</td>
      <td>1.404653e+12</td>
      <td>2.221165e+11</td>
      <td>2.325573e+11</td>
      <td>6.384452e+09</td>
      <td>1.157005e+09</td>
      <td>7.455219e+11</td>
      <td>...</td>
      <td>6.109300e+08</td>
      <td>6.637166e+10</td>
      <td>4.393768e+08</td>
      <td>5.144603e+13</td>
      <td>5.085037e+08</td>
      <td>3.846820e+09</td>
      <td>1.906198e+10</td>
      <td>2.716385e+11</td>
      <td>1.275686e+10</td>
      <td>5.443896e+09</td>
    </tr>
    <tr>
      <th>2007</th>
      <td>2.615084e+09</td>
      <td>6.526645e+10</td>
      <td>1.067732e+10</td>
      <td>4.016972e+09</td>
      <td>1.638214e+12</td>
      <td>2.579161e+11</td>
      <td>2.875305e+11</td>
      <td>9.206302e+09</td>
      <td>1.311401e+09</td>
      <td>8.519628e+11</td>
      <td>...</td>
      <td>6.844463e+08</td>
      <td>7.741443e+10</td>
      <td>5.264283e+08</td>
      <td>5.795330e+13</td>
      <td>5.509707e+08</td>
      <td>4.655899e+09</td>
      <td>2.165053e+10</td>
      <td>2.994155e+11</td>
      <td>1.405696e+10</td>
      <td>5.291950e+09</td>
    </tr>
    <tr>
      <th>2008</th>
      <td>2.745251e+09</td>
      <td>8.853861e+10</td>
      <td>1.288135e+10</td>
      <td>4.007353e+09</td>
      <td>2.078570e+12</td>
      <td>3.154746e+11</td>
      <td>3.615580e+11</td>
      <td>1.166204e+10</td>
      <td>1.368431e+09</td>
      <td>1.052585e+12</td>
      <td>...</td>
      <td>6.954289e+08</td>
      <td>9.913030e+10</td>
      <td>6.079586e+08</td>
      <td>6.357489e+13</td>
      <td>6.441325e+08</td>
      <td>5.687418e+09</td>
      <td>2.691085e+10</td>
      <td>2.867698e+11</td>
      <td>1.791086e+10</td>
      <td>4.415703e+09</td>
    </tr>
    <tr>
      <th>2009</th>
      <td>2.498883e+09</td>
      <td>7.030716e+10</td>
      <td>1.204421e+10</td>
      <td>3.660531e+09</td>
      <td>1.796200e+12</td>
      <td>2.535474e+11</td>
      <td>3.329765e+11</td>
      <td>8.647937e+09</td>
      <td>1.224253e+09</td>
      <td>9.264482e+11</td>
      <td>...</td>
      <td>6.749225e+08</td>
      <td>1.060147e+11</td>
      <td>6.100666e+08</td>
      <td>6.026707e+13</td>
      <td>5.609595e+08</td>
      <td>5.653793e+09</td>
      <td>2.513027e+10</td>
      <td>2.959365e+11</td>
      <td>1.532834e+10</td>
      <td>9.665793e+09</td>
    </tr>
    <tr>
      <th>2010</th>
      <td>2.390503e+09</td>
      <td>8.379950e+10</td>
      <td>1.192696e+10</td>
      <td>3.355695e+09</td>
      <td>2.109932e+12</td>
      <td>2.897873e+11</td>
      <td>4.236274e+11</td>
      <td>9.260285e+09</td>
      <td>1.152469e+09</td>
      <td>1.144261e+12</td>
      <td>...</td>
      <td>6.812260e+08</td>
      <td>1.159317e+11</td>
      <td>7.008043e+08</td>
      <td>6.596588e+13</td>
      <td>6.430467e+08</td>
      <td>5.830464e+09</td>
      <td>3.090675e+10</td>
      <td>3.753494e+11</td>
      <td>2.026556e+10</td>
      <td>1.204166e+10</td>
    </tr>
    <tr>
      <th>2011</th>
      <td>2.549721e+09</td>
      <td>1.117897e+11</td>
      <td>1.289087e+10</td>
      <td>3.442063e+09</td>
      <td>2.501739e+12</td>
      <td>3.506660e+11</td>
      <td>5.301633e+11</td>
      <td>1.014211e+10</td>
      <td>1.142043e+09</td>
      <td>1.394281e+12</td>
      <td>...</td>
      <td>6.761294e+08</td>
      <td>1.355394e+11</td>
      <td>7.921497e+08</td>
      <td>7.331678e+13</td>
      <td>7.397851e+08</td>
      <td>6.691827e+09</td>
      <td>3.272642e+10</td>
      <td>4.164189e+11</td>
      <td>2.346010e+10</td>
      <td>1.410192e+10</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>2.534637e+09</td>
      <td>1.280529e+11</td>
      <td>1.231978e+10</td>
      <td>3.164615e+09</td>
      <td>2.786787e+12</td>
      <td>3.745906e+11</td>
      <td>5.459824e+11</td>
      <td>1.061932e+10</td>
      <td>1.211412e+09</td>
      <td>1.543411e+12</td>
      <td>...</td>
      <td>6.929337e+08</td>
      <td>1.558200e+11</td>
      <td>7.817029e+08</td>
      <td>7.499371e+13</td>
      <td>8.011686e+08</td>
      <td>6.499936e+09</td>
      <td>3.540134e+10</td>
      <td>3.963279e+11</td>
      <td>2.550337e+10</td>
      <td>1.711485e+10</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>2.581564e+09</td>
      <td>1.367099e+11</td>
      <td>1.277628e+10</td>
      <td>3.281585e+09</td>
      <td>2.866861e+12</td>
      <td>3.901076e+11</td>
      <td>5.520251e+11</td>
      <td>1.112147e+10</td>
      <td>1.192920e+09</td>
      <td>1.573697e+12</td>
      <td>...</td>
      <td>7.212090e+08</td>
      <td>1.712220e+11</td>
      <td>8.017876e+08</td>
      <td>7.709879e+13</td>
      <td>8.048085e+08</td>
      <td>7.071960e+09</td>
      <td>4.041523e+10</td>
      <td>3.666432e+11</td>
      <td>2.804546e+10</td>
      <td>1.909102e+10</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>2.649721e+09</td>
      <td>1.457122e+11</td>
      <td>1.322825e+10</td>
      <td>3.350736e+09</td>
      <td>2.908394e+12</td>
      <td>4.031371e+11</td>
      <td>5.263197e+11</td>
      <td>1.160951e+10</td>
      <td>1.275577e+09</td>
      <td>1.464955e+12</td>
      <td>...</td>
      <td>7.277144e+08</td>
      <td>1.862047e+11</td>
      <td>8.149543e+08</td>
      <td>7.918846e+13</td>
      <td>8.051626e+08</td>
      <td>7.386891e+09</td>
      <td>4.322858e+10</td>
      <td>3.506362e+11</td>
      <td>2.715063e+10</td>
      <td>1.949552e+10</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>2.691620e+09</td>
      <td>1.161936e+11</td>
      <td>1.138693e+10</td>
      <td>2.811489e+09</td>
      <td>2.560754e+12</td>
      <td>3.581351e+11</td>
      <td>5.947493e+11</td>
      <td>1.055334e+10</td>
      <td>1.359195e+09</td>
      <td>1.349034e+12</td>
      <td>...</td>
      <td>7.554580e+08</td>
      <td>1.932411e+11</td>
      <td>7.379172e+08</td>
      <td>7.491609e+13</td>
      <td>8.041006e+08</td>
      <td>6.440612e+09</td>
      <td>4.559357e+10</td>
      <td>3.175368e+11</td>
      <td>2.115439e+10</td>
      <td>1.996312e+10</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>2.646927e+09</td>
      <td>1.011239e+11</td>
      <td>1.188368e+10</td>
      <td>2.877312e+09</td>
      <td>2.513936e+12</td>
      <td>3.570451e+11</td>
      <td>5.548609e+11</td>
      <td>1.054614e+10</td>
      <td>1.464630e+09</td>
      <td>1.208039e+12</td>
      <td>...</td>
      <td>7.707622e+08</td>
      <td>2.052762e+11</td>
      <td>7.879426e+08</td>
      <td>7.599738e+13</td>
      <td>7.866400e+08</td>
      <td>6.714712e+09</td>
      <td>3.643665e+10</td>
      <td>2.957466e+11</td>
      <td>2.095475e+10</td>
      <td>2.054868e+10</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>2.700559e+09</td>
      <td>1.221238e+11</td>
      <td>1.303854e+10</td>
      <td>3.012914e+09</td>
      <td>2.586311e+12</td>
      <td>3.825751e+11</td>
      <td>6.374303e+11</td>
      <td>1.153659e+10</td>
      <td>1.510085e+09</td>
      <td>1.323421e+12</td>
      <td>...</td>
      <td>7.852225e+08</td>
      <td>2.237799e+11</td>
      <td>8.628798e+08</td>
      <td>8.073758e+13</td>
      <td>8.409280e+08</td>
      <td>7.244889e+09</td>
      <td>3.126768e+10</td>
      <td>3.488716e+11</td>
      <td>2.586814e+10</td>
      <td>2.204090e+10</td>
    </tr>
  </tbody>
</table>
<p>18 rows × 232 columns</p>
</div>




```python
gdp.plot(y = ['Korea_Rep', 'United_States', 'United_Kingdom', 'Germany', 'China', 'Japan'])
```




    <Axes: >




    
![png](output_11_1.png)
    



```python
sv = pd.read_csv('silicon_valley_summary.csv')
sv
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
      <th>job_category</th>
      <th>race_ethnicity</th>
      <th>gender</th>
      <th>count</th>
      <th>percentage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>All workers</td>
      <td>White</td>
      <td>Male</td>
      <td>268883</td>
      <td>41.257252</td>
    </tr>
    <tr>
      <th>1</th>
      <td>All workers</td>
      <td>White</td>
      <td>Female</td>
      <td>105560</td>
      <td>16.197065</td>
    </tr>
    <tr>
      <th>2</th>
      <td>All workers</td>
      <td>Black_or_African American</td>
      <td>Male</td>
      <td>17508</td>
      <td>2.686417</td>
    </tr>
    <tr>
      <th>3</th>
      <td>All workers</td>
      <td>Black_or_African American</td>
      <td>Female</td>
      <td>11479</td>
      <td>1.761331</td>
    </tr>
    <tr>
      <th>4</th>
      <td>All workers</td>
      <td>Asian</td>
      <td>Male</td>
      <td>125347</td>
      <td>19.233171</td>
    </tr>
    <tr>
      <th>5</th>
      <td>All workers</td>
      <td>Asian</td>
      <td>Female</td>
      <td>58049</td>
      <td>8.907005</td>
    </tr>
    <tr>
      <th>6</th>
      <td>All workers</td>
      <td>Hispanic_or_Latino</td>
      <td>Male</td>
      <td>32201</td>
      <td>4.940903</td>
    </tr>
    <tr>
      <th>7</th>
      <td>All workers</td>
      <td>Hispanic_or_Latino</td>
      <td>Female</td>
      <td>15512</td>
      <td>2.380152</td>
    </tr>
    <tr>
      <th>8</th>
      <td>All workers</td>
      <td>All</td>
      <td>Male</td>
      <td>454813</td>
      <td>69.786244</td>
    </tr>
    <tr>
      <th>9</th>
      <td>All workers</td>
      <td>All</td>
      <td>Female</td>
      <td>196910</td>
      <td>30.213756</td>
    </tr>
    <tr>
      <th>10</th>
      <td>All workers</td>
      <td>Totals</td>
      <td>Both</td>
      <td>651723</td>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Executives</td>
      <td>White</td>
      <td>Male</td>
      <td>7282</td>
      <td>58.678485</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Executives</td>
      <td>White</td>
      <td>Female</td>
      <td>1818</td>
      <td>14.649476</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Executives</td>
      <td>Black_or_African American</td>
      <td>Male</td>
      <td>120</td>
      <td>0.966962</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Executives</td>
      <td>Black_or_African American</td>
      <td>Female</td>
      <td>53</td>
      <td>0.427075</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Executives</td>
      <td>Asian</td>
      <td>Male</td>
      <td>2023</td>
      <td>16.301370</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Executives</td>
      <td>Asian</td>
      <td>Female</td>
      <td>556</td>
      <td>4.500000</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Executives</td>
      <td>Hispanic_or_Latino</td>
      <td>Male</td>
      <td>266</td>
      <td>2.143433</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Executives</td>
      <td>Hispanic_or_Latino</td>
      <td>Female</td>
      <td>103</td>
      <td>0.829976</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Executives</td>
      <td>All</td>
      <td>Male</td>
      <td>9824</td>
      <td>79.161966</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Executives</td>
      <td>All</td>
      <td>Female</td>
      <td>2586</td>
      <td>20.838034</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Executives</td>
      <td>Totals</td>
      <td>Both</td>
      <td>12410</td>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Managers</td>
      <td>White</td>
      <td>Male</td>
      <td>48311</td>
      <td>46.479253</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Managers</td>
      <td>White</td>
      <td>Female</td>
      <td>18935</td>
      <td>18.217065</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Managers</td>
      <td>Black_or_African American</td>
      <td>Male</td>
      <td>1575</td>
      <td>1.515283</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Managers</td>
      <td>Black_or_African American</td>
      <td>Female</td>
      <td>978</td>
      <td>0.940918</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Managers</td>
      <td>Asian</td>
      <td>Male</td>
      <td>18563</td>
      <td>17.859170</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Managers</td>
      <td>Asian</td>
      <td>Female</td>
      <td>8084</td>
      <td>7.777489</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Managers</td>
      <td>Hispanic_or_Latino</td>
      <td>Male</td>
      <td>3741</td>
      <td>3.599157</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Managers</td>
      <td>Hispanic_or_Latino</td>
      <td>Female</td>
      <td>1642</td>
      <td>1.579742</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Managers</td>
      <td>All</td>
      <td>Male</td>
      <td>73526</td>
      <td>70.738207</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Managers</td>
      <td>All</td>
      <td>Female</td>
      <td>30415</td>
      <td>29.261793</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Managers</td>
      <td>Totals</td>
      <td>Both</td>
      <td>103941</td>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Professionals</td>
      <td>White</td>
      <td>Male</td>
      <td>133311</td>
      <td>38.660592</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Professionals</td>
      <td>White</td>
      <td>Female</td>
      <td>47505</td>
      <td>13.776593</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Professionals</td>
      <td>Black_or_African American</td>
      <td>Male</td>
      <td>6301</td>
      <td>1.827309</td>
    </tr>
    <tr>
      <th>36</th>
      <td>Professionals</td>
      <td>Black_or_African American</td>
      <td>Female</td>
      <td>3756</td>
      <td>1.089251</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Professionals</td>
      <td>Asian</td>
      <td>Male</td>
      <td>89365</td>
      <td>25.916120</td>
    </tr>
    <tr>
      <th>38</th>
      <td>Professionals</td>
      <td>Asian</td>
      <td>Female</td>
      <td>39902</td>
      <td>11.571700</td>
    </tr>
    <tr>
      <th>39</th>
      <td>Professionals</td>
      <td>Hispanic_or_Latino</td>
      <td>Male</td>
      <td>11820</td>
      <td>3.427836</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Professionals</td>
      <td>Hispanic_or_Latino</td>
      <td>Female</td>
      <td>5533</td>
      <td>1.604587</td>
    </tr>
    <tr>
      <th>41</th>
      <td>Professionals</td>
      <td>All</td>
      <td>Male</td>
      <td>245461</td>
      <td>71.184430</td>
    </tr>
    <tr>
      <th>42</th>
      <td>Professionals</td>
      <td>All</td>
      <td>Female</td>
      <td>99363</td>
      <td>28.815570</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Professionals</td>
      <td>Totals</td>
      <td>Both</td>
      <td>344824</td>
      <td>100.000000</td>
    </tr>
  </tbody>
</table>
</div>



아니 ... 답이 all이 없어서 뭔가 멋진 방법이 있나 했더니 나랑 똑같이 손으로 뺀 거잖아 ... ?


```python
man = sv['job_category'] == 'Managers'
male = sv['gender'] == 'Male'
nall = sv['race_ethnicity'] != 'All'
sv.loc[man & male & nall].plot(kind='bar', x = 'race_ethnicity', y = 'count')
```




    <Axes: xlabel='race_ethnicity'>




    
![png](output_14_1.png)
    



```python
df.loc[2017].plot(kind='pie')
```




    <Axes: ylabel='2017'>




    
![png](output_15_1.png)
    



```python
svd = pd.read_csv('silicon_valley_details.csv')
svd
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
      <th>company</th>
      <th>year</th>
      <th>race</th>
      <th>gender</th>
      <th>job_category</th>
      <th>count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>23andMe</td>
      <td>2016</td>
      <td>Hispanic_or_Latino</td>
      <td>male</td>
      <td>Executives</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>23andMe</td>
      <td>2016</td>
      <td>Hispanic_or_Latino</td>
      <td>male</td>
      <td>Managers</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>23andMe</td>
      <td>2016</td>
      <td>Hispanic_or_Latino</td>
      <td>male</td>
      <td>Professionals</td>
      <td>7</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23andMe</td>
      <td>2016</td>
      <td>Hispanic_or_Latino</td>
      <td>male</td>
      <td>Technicians</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23andMe</td>
      <td>2016</td>
      <td>Hispanic_or_Latino</td>
      <td>male</td>
      <td>Sales workers</td>
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
    </tr>
    <tr>
      <th>4435</th>
      <td>Sanmina</td>
      <td>2016</td>
      <td>Overall_totals</td>
      <td>NaN</td>
      <td>laborers and helpers</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4436</th>
      <td>Sanmina</td>
      <td>2016</td>
      <td>Overall_totals</td>
      <td>NaN</td>
      <td>Service workers</td>
      <td>57</td>
    </tr>
    <tr>
      <th>4437</th>
      <td>Sanmina</td>
      <td>2016</td>
      <td>Overall_totals</td>
      <td>NaN</td>
      <td>Totals</td>
      <td>5205</td>
    </tr>
    <tr>
      <th>4438</th>
      <td>Sanmina</td>
      <td>2016</td>
      <td>Overall_totals</td>
      <td>NaN</td>
      <td>Previous_totals</td>
      <td>5615</td>
    </tr>
    <tr>
      <th>4439</th>
      <td>Sanmina</td>
      <td>2016</td>
      <td>Overall_totals</td>
      <td>NaN</td>
      <td>Managers</td>
      <td>591</td>
    </tr>
  </tbody>
</table>
<p>4440 rows × 6 columns</p>
</div>




```python
adb = svd['company'] == 'Adobe'
ntotals = svd['job_category'] != 'Totals'
nsub = svd['job_category'] != 'Previous_totals'
nzero = svd['count'] > 0
cnt = svd.loc[adb & ntotals & nsub & nzero]['job_category'].value_counts()
cnt.plot(kind = 'pie')
```




    <Axes: ylabel='count'>




    
![png](output_17_1.png)
    


하 진짜 파라미터로 어떤 걸 넣는지 같은 건 알려주고 문제를 풀라고 하든가  
이게 짱 답답한 부분인긴 한데 구글링하면서 스스로 답을 찾는 게 개발자 마인드고 다 떠먹여 주는 게 아니라 개발자 마인드를 길러야 한다는 사람도 있다  
죽빵이라도 갈겨야 한다  

왜 빡쳤냐면 파이 그래프가 인덱스를 이름표로 붙인다는 걸 설명도 안 해놓고 그걸 안 맞추면 틀리게 해놨다


```python
nrace = svd['race'] == 'Overall_totals'
base = svd.loc[adb & nrace & nzero & ntotals & nsub]
base.set_index('job_category', inplace = True)
base.plot(kind = 'pie', y = 'count')
```




    <Axes: ylabel='count'>




    
![png](output_20_1.png)
    



```python
stb = pd.read_csv('starbucks_drinks.csv')
stb
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
      <th>Beverage_category</th>
      <th>Beverage</th>
      <th>Beverage_prep</th>
      <th>Calories</th>
      <th>Total Fat (g)</th>
      <th>Trans Fat (g)</th>
      <th>Saturated Fat (g)</th>
      <th>Sodium (mg)</th>
      <th>Total Carbohydrates (g)</th>
      <th>Cholesterol (mg)</th>
      <th>Dietary Fibre (g)</th>
      <th>Sugars (g)</th>
      <th>Protein (g)</th>
      <th>Vitamin A (% DV)</th>
      <th>Vitamin C (% DV)</th>
      <th>Calcium (% DV)</th>
      <th>Iron (% DV)</th>
      <th>Caffeine (mg)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Coffee</td>
      <td>Brewed Coffee</td>
      <td>Short</td>
      <td>3</td>
      <td>0.1</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.3</td>
      <td>0%</td>
      <td>0%</td>
      <td>0%</td>
      <td>0%</td>
      <td>175</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Coffee</td>
      <td>Brewed Coffee</td>
      <td>Tall</td>
      <td>4</td>
      <td>0.1</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>10</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.5</td>
      <td>0%</td>
      <td>0%</td>
      <td>0%</td>
      <td>0%</td>
      <td>260</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Coffee</td>
      <td>Brewed Coffee</td>
      <td>Grande</td>
      <td>5</td>
      <td>0.1</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>10</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1.0</td>
      <td>0%</td>
      <td>0%</td>
      <td>0%</td>
      <td>0%</td>
      <td>330</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Coffee</td>
      <td>Brewed Coffee</td>
      <td>Venti</td>
      <td>5</td>
      <td>0.1</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>10</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1.0</td>
      <td>0%</td>
      <td>0%</td>
      <td>2%</td>
      <td>0%</td>
      <td>410</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Classic Espresso Drinks</td>
      <td>Caffè Latte</td>
      <td>Short Nonfat Milk</td>
      <td>70</td>
      <td>0.1</td>
      <td>0.1</td>
      <td>0.0</td>
      <td>5</td>
      <td>75</td>
      <td>10</td>
      <td>0</td>
      <td>9</td>
      <td>6.0</td>
      <td>10%</td>
      <td>0%</td>
      <td>20%</td>
      <td>0%</td>
      <td>75</td>
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
    </tr>
    <tr>
      <th>214</th>
      <td>Frappuccino® Blended Crème</td>
      <td>Strawberries &amp; Crème (Without Whipped Cream)</td>
      <td>Soymilk</td>
      <td>320</td>
      <td>3 2</td>
      <td>0.4</td>
      <td>0.0</td>
      <td>0</td>
      <td>250</td>
      <td>67</td>
      <td>1</td>
      <td>64</td>
      <td>5.0</td>
      <td>6%</td>
      <td>8%</td>
      <td>20%</td>
      <td>10%</td>
      <td>0</td>
    </tr>
    <tr>
      <th>215</th>
      <td>Frappuccino® Blended Crème</td>
      <td>Vanilla Bean (Without Whipped Cream)</td>
      <td>Tall Nonfat Milk</td>
      <td>170</td>
      <td>0.1</td>
      <td>0.1</td>
      <td>0.0</td>
      <td>0</td>
      <td>160</td>
      <td>39</td>
      <td>0</td>
      <td>38</td>
      <td>4.0</td>
      <td>6%</td>
      <td>0%</td>
      <td>10%</td>
      <td>0%</td>
      <td>0</td>
    </tr>
    <tr>
      <th>216</th>
      <td>Frappuccino® Blended Crème</td>
      <td>Vanilla Bean (Without Whipped Cream)</td>
      <td>Whole Milk</td>
      <td>200</td>
      <td>3.5</td>
      <td>2.0</td>
      <td>0.1</td>
      <td>10</td>
      <td>160</td>
      <td>39</td>
      <td>0</td>
      <td>38</td>
      <td>3.0</td>
      <td>6%</td>
      <td>0%</td>
      <td>10%</td>
      <td>0%</td>
      <td>0</td>
    </tr>
    <tr>
      <th>217</th>
      <td>Frappuccino® Blended Crème</td>
      <td>Vanilla Bean (Without Whipped Cream)</td>
      <td>Soymilk</td>
      <td>180</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>0.0</td>
      <td>0</td>
      <td>160</td>
      <td>37</td>
      <td>1</td>
      <td>35</td>
      <td>3.0</td>
      <td>4%</td>
      <td>0%</td>
      <td>10%</td>
      <td>6%</td>
      <td>0</td>
    </tr>
    <tr>
      <th>218</th>
      <td>Frappuccino® Blended Crème</td>
      <td>Vanilla Bean (Without Whipped Cream)</td>
      <td>Grande Nonfat Milk</td>
      <td>240</td>
      <td>0.1</td>
      <td>0.1</td>
      <td>0.0</td>
      <td>5</td>
      <td>230</td>
      <td>56</td>
      <td>0</td>
      <td>55</td>
      <td>5.0</td>
      <td>8%</td>
      <td>0%</td>
      <td>15%</td>
      <td>0%</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>219 rows × 18 columns</p>
</div>




```python
stb.plot(kind='hist', y='Calories', bins = 20)
```




    <Axes: ylabel='Frequency'>




    
![png](output_22_1.png)
    



```python
stb.plot(kind='box', y='Calories')
```




    <Axes: >




    
![png](output_23_1.png)
    



```python
wd = pd.read_csv('world_indexes.csv')
wd
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
      <th>Id</th>
      <th>Human Development Index HDI-2014</th>
      <th>Gini coefficient 2005-2013</th>
      <th>Adolescent birth rate 15-19 per 100k 20102015</th>
      <th>Birth registration funder age 5 2005-2013</th>
      <th>Carbon dioxide emissionsAverage annual growth</th>
      <th>Carbon dioxide emissions per capita 2011 Tones</th>
      <th>Change forest percentable 1900 to 2012</th>
      <th>Change mobile usage 2009 2014</th>
      <th>Consumer price index 2013</th>
      <th>...</th>
      <th>Renewable sources percentage of total 2012</th>
      <th>Research and development expenditure  2005-2012</th>
      <th>Secondary 2008-2014</th>
      <th>Share of seats in parliament percentage held by womand 2014</th>
      <th>Stock of immigrants percentage of population 2013</th>
      <th>Taxes on income profit and capital gain 205 2013</th>
      <th>Tertiary -2008-2014</th>
      <th>Total tax revenue of GDP 2005-2013</th>
      <th>Tuberculosis rate per thousands 2012</th>
      <th>Under-five Mortality 2013 thousands</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Norway</td>
      <td>0.943877</td>
      <td>26.83</td>
      <td>7.834</td>
      <td>100.000000</td>
      <td>0.778925</td>
      <td>9.192879</td>
      <td>11.914567</td>
      <td>5.22</td>
      <td>104.194175</td>
      <td>...</td>
      <td>47.752676</td>
      <td>1.654740</td>
      <td>111.061300</td>
      <td>39.644970</td>
      <td>13.772622</td>
      <td>31.798391</td>
      <td>74.10112</td>
      <td>27.288097</td>
      <td>0.14</td>
      <td>2.8</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Australia</td>
      <td>0.934958</td>
      <td>34.01</td>
      <td>12.059</td>
      <td>100.000000</td>
      <td>1.090351</td>
      <td>16.519210</td>
      <td>-4.561812</td>
      <td>30.27</td>
      <td>107.789440</td>
      <td>...</td>
      <td>4.632202</td>
      <td>2.385620</td>
      <td>135.535430</td>
      <td>30.530974</td>
      <td>27.711793</td>
      <td>65.333748</td>
      <td>86.33409</td>
      <td>21.361426</td>
      <td>0.19</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Switzerland</td>
      <td>0.929613</td>
      <td>32.35</td>
      <td>1.900</td>
      <td>100.000000</td>
      <td>-1.101254</td>
      <td>4.625230</td>
      <td>8.567416</td>
      <td>16.72</td>
      <td>99.317229</td>
      <td>...</td>
      <td>49.659398</td>
      <td>2.870460</td>
      <td>96.306380</td>
      <td>28.455285</td>
      <td>28.906998</td>
      <td>22.673299</td>
      <td>55.56190</td>
      <td>9.759124</td>
      <td>0.22</td>
      <td>4.2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Denmark</td>
      <td>0.923328</td>
      <td>26.88</td>
      <td>5.101</td>
      <td>100.000000</td>
      <td>-1.767733</td>
      <td>7.248329</td>
      <td>23.029974</td>
      <td>1.83</td>
      <td>106.057718</td>
      <td>...</td>
      <td>26.767245</td>
      <td>2.984160</td>
      <td>124.659270</td>
      <td>37.988827</td>
      <td>9.909512</td>
      <td>39.677938</td>
      <td>79.59763</td>
      <td>33.395651</td>
      <td>0.40</td>
      <td>3.5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Netherlands</td>
      <td>0.921794</td>
      <td>28.87</td>
      <td>6.165</td>
      <td>100.000000</td>
      <td>-0.252734</td>
      <td>10.064490</td>
      <td>5.922602</td>
      <td>-4.31</td>
      <td>107.474154</td>
      <td>...</td>
      <td>6.671366</td>
      <td>2.156760</td>
      <td>129.912770</td>
      <td>36.888889</td>
      <td>11.724418</td>
      <td>23.533104</td>
      <td>77.34356</td>
      <td>19.724059</td>
      <td>0.17</td>
      <td>4.0</td>
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
      <th>183</th>
      <td>Burundi</td>
      <td>0.399928</td>
      <td>33.27</td>
      <td>30.256</td>
      <td>75.000000</td>
      <td>0.630172</td>
      <td>0.021909</td>
      <td>-41.730104</td>
      <td>195.33</td>
      <td>140.018625</td>
      <td>...</td>
      <td>53.544693</td>
      <td>0.121260</td>
      <td>33.102310</td>
      <td>34.931507</td>
      <td>2.504071</td>
      <td>19.855360</td>
      <td>3.16599</td>
      <td>11.006974</td>
      <td>18.00</td>
      <td>82.9</td>
    </tr>
    <tr>
      <th>184</th>
      <td>Chad</td>
      <td>0.391906</td>
      <td>43.30</td>
      <td>152.015</td>
      <td>16.000000</td>
      <td>0.861268</td>
      <td>0.044623</td>
      <td>-13.298246</td>
      <td>98.14</td>
      <td>109.954331</td>
      <td>...</td>
      <td>88.289148</td>
      <td>0.612717</td>
      <td>22.794100</td>
      <td>14.893617</td>
      <td>3.423823</td>
      <td>27.618325</td>
      <td>2.25039</td>
      <td>15.978897</td>
      <td>18.00</td>
      <td>147.5</td>
    </tr>
    <tr>
      <th>185</th>
      <td>Eritrea</td>
      <td>0.390899</td>
      <td>36.75</td>
      <td>65.280</td>
      <td>99.333333</td>
      <td>2.709607</td>
      <td>0.087768</td>
      <td>-6.033313</td>
      <td>151.49</td>
      <td>113.652667</td>
      <td>...</td>
      <td>78.271531</td>
      <td>0.226783</td>
      <td>42.522027</td>
      <td>22.000000</td>
      <td>0.249450</td>
      <td>17.402965</td>
      <td>2.04323</td>
      <td>13.265781</td>
      <td>4.60</td>
      <td>49.9</td>
    </tr>
    <tr>
      <th>186</th>
      <td>Central African Republic</td>
      <td>0.350131</td>
      <td>56.30</td>
      <td>98.334</td>
      <td>61.000000</td>
      <td>-1.829932</td>
      <td>0.064475</td>
      <td>-2.835840</td>
      <td>54.91</td>
      <td>108.757088</td>
      <td>...</td>
      <td>80.467360</td>
      <td>0.253410</td>
      <td>17.791890</td>
      <td>12.500000</td>
      <td>2.907818</td>
      <td>6.902223</td>
      <td>2.84086</td>
      <td>9.455153</td>
      <td>50.00</td>
      <td>139.2</td>
    </tr>
    <tr>
      <th>187</th>
      <td>Niger</td>
      <td>0.348254</td>
      <td>31.16</td>
      <td>204.789</td>
      <td>64.000000</td>
      <td>1.835631</td>
      <td>0.086170</td>
      <td>-39.372751</td>
      <td>161.65</td>
      <td>105.786143</td>
      <td>...</td>
      <td>26.755224</td>
      <td>0.088957</td>
      <td>15.924760</td>
      <td>13.274336</td>
      <td>0.741921</td>
      <td>11.558007</td>
      <td>1.75417</td>
      <td>11.337822</td>
      <td>16.00</td>
      <td>104.2</td>
    </tr>
  </tbody>
</table>
<p>188 rows × 66 columns</p>
</div>




```python
wd.plot(kind='scatter', x='Life expectancy at birth- years', y='Internet users percentage of population 2014')
```




    <Axes: xlabel='Life expectancy at birth- years', ylabel='Internet users percentage of population 2014'>




    
![png](output_25_1.png)
    



```python
wd.plot(kind='scatter', x='Life expectancy at birth- years', y= 'Forest area percentage of total land area 2012')
```




    <Axes: xlabel='Life expectancy at birth- years', ylabel='Forest area percentage of total land area 2012'>




    
![png](output_26_1.png)
    



```python
wd.plot(kind='scatter', x='Life expectancy at birth- years', y= 'Carbon dioxide emissionsAverage annual growth')
```




    <Axes: xlabel='Life expectancy at birth- years', ylabel='Carbon dioxide emissionsAverage annual growth'>




    
![png](output_27_1.png)
    


---

## Seaborn library
statistical data visualization

pdf : probability density function 확률 밀도 함수
- 확률분포의 합은 1
- 어떤 조건에 해당할 확률은 넓이
- 어느 한 사건이 발생할 가능성은 0

kde : kernel density estimation 커널 밀도 추정


```python
import seaborn as sns
```


```python
bd = pd.read_csv('body.csv')
bd
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
      <th>Number</th>
      <th>Height</th>
      <th>Weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>176.0</td>
      <td>85.2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>175.3</td>
      <td>67.7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>168.6</td>
      <td>75.2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>168.1</td>
      <td>67.1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>175.3</td>
      <td>63.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>995</th>
      <td>996</td>
      <td>171.8</td>
      <td>68.2</td>
    </tr>
    <tr>
      <th>996</th>
      <td>997</td>
      <td>171.5</td>
      <td>75.6</td>
    </tr>
    <tr>
      <th>997</th>
      <td>998</td>
      <td>177.9</td>
      <td>66.5</td>
    </tr>
    <tr>
      <th>998</th>
      <td>999</td>
      <td>174.4</td>
      <td>72.0</td>
    </tr>
    <tr>
      <th>999</th>
      <td>1000</td>
      <td>173.5</td>
      <td>77.4</td>
    </tr>
  </tbody>
</table>
<p>1000 rows × 3 columns</p>
</div>




```python
bd['Height'].value_counts().sort_index().plot()
```




    <Axes: xlabel='Height'>




    
![png](output_34_1.png)
    


이런 실측치를 kde 해서 확률분포로 만들어낸다


```python
sns.kdeplot(bd['Height'])
```




    <Axes: xlabel='Height', ylabel='Density'>




    
![png](output_36_1.png)
    



```python
sns.kdeplot(bd['Height'], bw = 0.5)
```

    C:\Users\moonlight\AppData\Local\Temp\ipykernel_8316\987186475.py:1: UserWarning: 
    
    The `bw` parameter is deprecated in favor of `bw_method` and `bw_adjust`.
    Setting `bw_method=0.5`, but please see the docs for the new parameters
    and update your code. This will become an error in seaborn v0.13.0.
    
      sns.kdeplot(bd['Height'], bw = 0.5)
    




    <Axes: xlabel='Height', ylabel='Density'>




    
![png](output_37_2.png)
    



```python
sub = pd.read_csv('subway.csv')
sub
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
      <th>line</th>
      <th>station</th>
      <th>in</th>
      <th>out</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>중앙선</td>
      <td>지평</td>
      <td>37</td>
      <td>28</td>
    </tr>
    <tr>
      <th>1</th>
      <td>중앙선</td>
      <td>용문</td>
      <td>2064</td>
      <td>2103</td>
    </tr>
    <tr>
      <th>2</th>
      <td>중앙선</td>
      <td>원덕</td>
      <td>375</td>
      <td>357</td>
    </tr>
    <tr>
      <th>3</th>
      <td>중앙선</td>
      <td>양평</td>
      <td>4338</td>
      <td>4378</td>
    </tr>
    <tr>
      <th>4</th>
      <td>중앙선</td>
      <td>오빈</td>
      <td>321</td>
      <td>321</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>586</th>
      <td>1호선</td>
      <td>종로5가</td>
      <td>31245</td>
      <td>30678</td>
    </tr>
    <tr>
      <th>587</th>
      <td>1호선</td>
      <td>종로3가</td>
      <td>38099</td>
      <td>36928</td>
    </tr>
    <tr>
      <th>588</th>
      <td>1호선</td>
      <td>종각</td>
      <td>52310</td>
      <td>50088</td>
    </tr>
    <tr>
      <th>589</th>
      <td>1호선</td>
      <td>시청</td>
      <td>29150</td>
      <td>29043</td>
    </tr>
    <tr>
      <th>590</th>
      <td>1호선</td>
      <td>서울역</td>
      <td>58391</td>
      <td>54356</td>
    </tr>
  </tbody>
</table>
<p>591 rows × 4 columns</p>
</div>




```python
sns.kdeplot(sub['in'])
```




    <Axes: xlabel='in', ylabel='Density'>




    
![png](output_39_1.png)
    



```python
bd.plot(kind='hist', y='Height')
```




    <Axes: ylabel='Frequency'>




    
![png](output_40_1.png)
    



```python
sns.displot(bd['Height'], bins = 30)
```




    <seaborn.axisgrid.FacetGrid at 0x219ba946f20>




    
![png](output_41_1.png)
    



```python
sns.violinplot(y=bd['Height'])
```




    <Axes: ylabel='Height'>




    
![png](output_42_1.png)
    



```python
sns.kdeplot(x = bd['Height'], y = bd['Weight'])
```




    <Axes: xlabel='Height', ylabel='Weight'>




    
![png](output_43_1.png)
    



```python
sal = pd.read_csv('salaries.csv')
sal
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
      <th>rank</th>
      <th>discipline</th>
      <th>yrs.since.phd</th>
      <th>yrs.service</th>
      <th>sex</th>
      <th>salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Prof</td>
      <td>B</td>
      <td>56</td>
      <td>49</td>
      <td>Male</td>
      <td>186960</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Prof</td>
      <td>A</td>
      <td>12</td>
      <td>6</td>
      <td>Male</td>
      <td>93000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Prof</td>
      <td>A</td>
      <td>23</td>
      <td>20</td>
      <td>Male</td>
      <td>110515</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Prof</td>
      <td>A</td>
      <td>40</td>
      <td>31</td>
      <td>Male</td>
      <td>131205</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Prof</td>
      <td>B</td>
      <td>20</td>
      <td>18</td>
      <td>Male</td>
      <td>104800</td>
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
      <th>73</th>
      <td>Prof</td>
      <td>B</td>
      <td>18</td>
      <td>10</td>
      <td>Female</td>
      <td>105450</td>
    </tr>
    <tr>
      <th>74</th>
      <td>AssocProf</td>
      <td>B</td>
      <td>19</td>
      <td>6</td>
      <td>Female</td>
      <td>104542</td>
    </tr>
    <tr>
      <th>75</th>
      <td>Prof</td>
      <td>B</td>
      <td>17</td>
      <td>17</td>
      <td>Female</td>
      <td>124312</td>
    </tr>
    <tr>
      <th>76</th>
      <td>Prof</td>
      <td>A</td>
      <td>28</td>
      <td>14</td>
      <td>Female</td>
      <td>109954</td>
    </tr>
    <tr>
      <th>77</th>
      <td>Prof</td>
      <td>A</td>
      <td>23</td>
      <td>15</td>
      <td>Female</td>
      <td>109646</td>
    </tr>
  </tbody>
</table>
<p>78 rows × 6 columns</p>
</div>




```python
sns.violinplot(sal['salary'])
```




    <Axes: >




    
![png](output_45_1.png)
    



```python
sns.lmplot(data=bd, x='Height', y='Weight')
```




    <seaborn.axisgrid.FacetGrid at 0x219bd013790>




    
![png](output_46_1.png)
    



```python
sns.catplot(data = sal, x = 'rank', y = 'salary', kind = 'box')
```




    <seaborn.axisgrid.FacetGrid at 0x219bd0523b0>




    
![png](output_47_1.png)
    



```python
sns.catplot(data = sal, x = 'rank', y = 'salary', kind = 'strip')
```




    <seaborn.axisgrid.FacetGrid at 0x219bcf95570>




    
![png](output_48_1.png)
    



```python
sns.catplot(data = sal, x = 'rank', y = 'salary', kind = 'strip', hue= 'sex')
```




    <seaborn.axisgrid.FacetGrid at 0x219bd323f40>




    
![png](output_49_1.png)
    



```python
sns.catplot(data = sal, x = 'rank', y = 'salary', kind = 'swarm', hue= 'sex')
```




    <seaborn.axisgrid.FacetGrid at 0x219bd3926e0>




    
![png](output_50_1.png)
    



```python
ins = pd.read_csv('insurance.csv')
ins
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
      <th>age</th>
      <th>sex</th>
      <th>bmi</th>
      <th>children</th>
      <th>smoker</th>
      <th>region</th>
      <th>charges</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>19</td>
      <td>female</td>
      <td>27.900</td>
      <td>0</td>
      <td>yes</td>
      <td>southwest</td>
      <td>16884.92400</td>
    </tr>
    <tr>
      <th>1</th>
      <td>18</td>
      <td>male</td>
      <td>33.770</td>
      <td>1</td>
      <td>no</td>
      <td>southeast</td>
      <td>1725.55230</td>
    </tr>
    <tr>
      <th>2</th>
      <td>28</td>
      <td>male</td>
      <td>33.000</td>
      <td>3</td>
      <td>no</td>
      <td>southeast</td>
      <td>4449.46200</td>
    </tr>
    <tr>
      <th>3</th>
      <td>33</td>
      <td>male</td>
      <td>22.705</td>
      <td>0</td>
      <td>no</td>
      <td>northwest</td>
      <td>21984.47061</td>
    </tr>
    <tr>
      <th>4</th>
      <td>32</td>
      <td>male</td>
      <td>28.880</td>
      <td>0</td>
      <td>no</td>
      <td>northwest</td>
      <td>3866.85520</td>
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
      <th>1333</th>
      <td>50</td>
      <td>male</td>
      <td>30.970</td>
      <td>3</td>
      <td>no</td>
      <td>northwest</td>
      <td>10600.54830</td>
    </tr>
    <tr>
      <th>1334</th>
      <td>18</td>
      <td>female</td>
      <td>31.920</td>
      <td>0</td>
      <td>no</td>
      <td>northeast</td>
      <td>2205.98080</td>
    </tr>
    <tr>
      <th>1335</th>
      <td>18</td>
      <td>female</td>
      <td>36.850</td>
      <td>0</td>
      <td>no</td>
      <td>southeast</td>
      <td>1629.83350</td>
    </tr>
    <tr>
      <th>1336</th>
      <td>21</td>
      <td>female</td>
      <td>25.800</td>
      <td>0</td>
      <td>no</td>
      <td>southwest</td>
      <td>2007.94500</td>
    </tr>
    <tr>
      <th>1337</th>
      <td>61</td>
      <td>female</td>
      <td>29.070</td>
      <td>0</td>
      <td>yes</td>
      <td>northwest</td>
      <td>29141.36030</td>
    </tr>
  </tbody>
</table>
<p>1338 rows × 7 columns</p>
</div>




```python
sns.catplot(data = ins, x = 'smoker', y = 'charges', kind = 'violin')
```




    <seaborn.axisgrid.FacetGrid at 0x219bd467c70>




    
![png](output_52_1.png)
    



```python
lt = [44, 42, 43, 28, 46, 33, 42, 37, 29]
lt.sort()
lt[int((len(lt)+1)/2)]
```




    42




```python
lt = [33, 45, 98, 38, 21, 49, 51, 58, 82, 75]
lt.sort()
lt
```




    [21, 33, 38, 45, 49, 51, 58, 75, 82, 98]



pearson correlation coefficient

---

## EDA exploratory data analysis

- 각 행, 렬은 무엇을 뜻하는가?
- 각 행, 렬의 값은 어떤 분포를 가지는가?
- 행, 렬들의 조합은 어떤 연관성을 갖는가?


```python
oc = pd.read_csv('occupations.csv')
oc
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
      <th>user_id</th>
      <th>age</th>
      <th>gender</th>
      <th>occupation</th>
      <th>zip_code</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>24</td>
      <td>M</td>
      <td>technician</td>
      <td>85711</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>53</td>
      <td>F</td>
      <td>other</td>
      <td>94043</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>23</td>
      <td>M</td>
      <td>writer</td>
      <td>32067</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>24</td>
      <td>M</td>
      <td>technician</td>
      <td>43537</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>33</td>
      <td>F</td>
      <td>other</td>
      <td>15213</td>
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
      <th>938</th>
      <td>939</td>
      <td>26</td>
      <td>F</td>
      <td>student</td>
      <td>33319</td>
    </tr>
    <tr>
      <th>939</th>
      <td>940</td>
      <td>32</td>
      <td>M</td>
      <td>administrator</td>
      <td>02215</td>
    </tr>
    <tr>
      <th>940</th>
      <td>941</td>
      <td>20</td>
      <td>M</td>
      <td>student</td>
      <td>97229</td>
    </tr>
    <tr>
      <th>941</th>
      <td>942</td>
      <td>48</td>
      <td>F</td>
      <td>librarian</td>
      <td>78209</td>
    </tr>
    <tr>
      <th>942</th>
      <td>943</td>
      <td>22</td>
      <td>M</td>
      <td>student</td>
      <td>77841</td>
    </tr>
  </tbody>
</table>
<p>943 rows × 5 columns</p>
</div>




```python
oc.loc[oc['gender'] == 'F', 'occupation'].value_counts()
```




    occupation
    student          60
    other            36
    administrator    36
    librarian        29
    educator         26
    writer           19
    artist           13
    healthcare       11
    marketing        10
    homemaker         6
    programmer        6
    none              4
    executive         3
    scientist         3
    salesman          3
    engineer          2
    lawyer            2
    entertainment     2
    retired           1
    technician        1
    Name: count, dtype: int64




```python
oc.loc[oc['gender'] == 'M', 'occupation'].value_counts()
```




    occupation
    student          136
    other             69
    educator          69
    engineer          65
    programmer        60
    administrator     43
    executive         29
    scientist         28
    technician        26
    writer            26
    librarian         22
    entertainment     16
    marketing         16
    artist            15
    retired           13
    lawyer            10
    salesman           9
    doctor             7
    none               5
    healthcare         5
    homemaker          1
    Name: count, dtype: int64




```python
sns.heatmap(bd.corr(), annot= True)
```




    <Axes: >




    
![png](output_62_1.png)
    



```python
ys = pd.read_csv('young_survey.csv')
ys
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
      <th>Music</th>
      <th>Slow songs or fast songs</th>
      <th>Dance</th>
      <th>Folk</th>
      <th>Country</th>
      <th>Classical music</th>
      <th>Musical</th>
      <th>Pop</th>
      <th>Rock</th>
      <th>Metal or Hardrock</th>
      <th>...</th>
      <th>Spending on looks</th>
      <th>Spending on gadgets</th>
      <th>Spending on healthy eating</th>
      <th>Age</th>
      <th>Height</th>
      <th>Weight</th>
      <th>Number of siblings</th>
      <th>Gender</th>
      <th>Handedness</th>
      <th>Education</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.0</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>5.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>3.0</td>
      <td>1</td>
      <td>3.0</td>
      <td>20.0</td>
      <td>163.0</td>
      <td>48.0</td>
      <td>1.0</td>
      <td>female</td>
      <td>right</td>
      <td>bachelor's degree</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.0</td>
      <td>4.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>4.0</td>
      <td>...</td>
      <td>2.0</td>
      <td>5</td>
      <td>2.0</td>
      <td>19.0</td>
      <td>163.0</td>
      <td>58.0</td>
      <td>2.0</td>
      <td>female</td>
      <td>right</td>
      <td>bachelor's degree</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>3.0</td>
      <td>...</td>
      <td>3.0</td>
      <td>4</td>
      <td>2.0</td>
      <td>20.0</td>
      <td>176.0</td>
      <td>67.0</td>
      <td>2.0</td>
      <td>female</td>
      <td>right</td>
      <td>high school</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5.0</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>4.0</td>
      <td>4</td>
      <td>1.0</td>
      <td>22.0</td>
      <td>172.0</td>
      <td>59.0</td>
      <td>1.0</td>
      <td>female</td>
      <td>right</td>
      <td>bachelor's degree</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>3.0</td>
      <td>2</td>
      <td>4.0</td>
      <td>20.0</td>
      <td>170.0</td>
      <td>59.0</td>
      <td>1.0</td>
      <td>female</td>
      <td>right</td>
      <td>high school</td>
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
      <th>992</th>
      <td>5.0</td>
      <td>2.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>5.0</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>3.0</td>
      <td>...</td>
      <td>4.0</td>
      <td>3</td>
      <td>4.0</td>
      <td>20.0</td>
      <td>164.0</td>
      <td>57.0</td>
      <td>1.0</td>
      <td>female</td>
      <td>right</td>
      <td>high school</td>
    </tr>
    <tr>
      <th>993</th>
      <td>4.0</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>1.0</td>
      <td>5</td>
      <td>3.0</td>
      <td>27.0</td>
      <td>183.0</td>
      <td>80.0</td>
      <td>5.0</td>
      <td>male</td>
      <td>left</td>
      <td>master's degree</td>
    </tr>
    <tr>
      <th>994</th>
      <td>4.0</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>2.0</td>
      <td>2</td>
      <td>5.0</td>
      <td>18.0</td>
      <td>173.0</td>
      <td>75.0</td>
      <td>0.0</td>
      <td>female</td>
      <td>right</td>
      <td>high school</td>
    </tr>
    <tr>
      <th>995</th>
      <td>5.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>3.0</td>
      <td>3</td>
      <td>3.0</td>
      <td>25.0</td>
      <td>173.0</td>
      <td>58.0</td>
      <td>1.0</td>
      <td>female</td>
      <td>right</td>
      <td>bachelor's degree</td>
    </tr>
    <tr>
      <th>996</th>
      <td>5.0</td>
      <td>5.0</td>
      <td>4.0</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>1.0</td>
      <td>1</td>
      <td>5.0</td>
      <td>21.0</td>
      <td>185.0</td>
      <td>72.0</td>
      <td>1.0</td>
      <td>male</td>
      <td>right</td>
      <td>high school</td>
    </tr>
  </tbody>
</table>
<p>997 rows × 147 columns</p>
</div>




```python
ys.corr()
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[56], line 1
    ----> 1 ys.corr()
    

    File c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\frame.py:10059, in DataFrame.corr(self, method, min_periods, numeric_only)
      10057 cols = data.columns
      10058 idx = cols.copy()
    > 10059 mat = data.to_numpy(dtype=float, na_value=np.nan, copy=False)
      10061 if method == "pearson":
      10062     correl = libalgos.nancorr(mat, minp=min_periods)
    

    File c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\frame.py:1838, in DataFrame.to_numpy(self, dtype, copy, na_value)
       1836 if dtype is not None:
       1837     dtype = np.dtype(dtype)
    -> 1838 result = self._mgr.as_array(dtype=dtype, copy=copy, na_value=na_value)
       1839 if result.dtype is not dtype:
       1840     result = np.array(result, dtype=dtype, copy=False)
    

    File c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\internals\managers.py:1732, in BlockManager.as_array(self, dtype, copy, na_value)
       1730         arr.flags.writeable = False
       1731 else:
    -> 1732     arr = self._interleave(dtype=dtype, na_value=na_value)
       1733     # The underlying data was copied within _interleave, so no need
       1734     # to further copy if copy=True or setting na_value
       1736 if na_value is not lib.no_default:
    

    File c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\internals\managers.py:1794, in BlockManager._interleave(self, dtype, na_value)
       1792     else:
       1793         arr = blk.get_values(dtype)
    -> 1794     result[rl.indexer] = arr
       1795     itemmask[rl.indexer] = 1
       1797 if not itemmask.all():
    

    ValueError: could not convert string to float: 'never smoked'



```python
yv = pd.read_csv('young_surv.csv')
yv
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
      <th>Music</th>
      <th>Slow songs or fast songs</th>
      <th>Dance</th>
      <th>Folk</th>
      <th>Country</th>
      <th>Classical music</th>
      <th>Musical</th>
      <th>Pop</th>
      <th>Rock</th>
      <th>Metal or Hardrock</th>
      <th>...</th>
      <th>Spending on looks</th>
      <th>Spending on gadgets</th>
      <th>Spending on healthy eating</th>
      <th>Age</th>
      <th>Height</th>
      <th>Weight</th>
      <th>Number of siblings</th>
      <th>Gender</th>
      <th>Handedness</th>
      <th>Education</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.0</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>5.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>3.0</td>
      <td>1</td>
      <td>3.0</td>
      <td>20.0</td>
      <td>163.0</td>
      <td>48.0</td>
      <td>1.0</td>
      <td>female</td>
      <td>right</td>
      <td>bachelor's degree</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.0</td>
      <td>4.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>4.0</td>
      <td>...</td>
      <td>2.0</td>
      <td>5</td>
      <td>2.0</td>
      <td>19.0</td>
      <td>163.0</td>
      <td>58.0</td>
      <td>2.0</td>
      <td>female</td>
      <td>right</td>
      <td>bachelor's degree</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>3.0</td>
      <td>...</td>
      <td>3.0</td>
      <td>4</td>
      <td>2.0</td>
      <td>20.0</td>
      <td>176.0</td>
      <td>67.0</td>
      <td>2.0</td>
      <td>female</td>
      <td>right</td>
      <td>high school</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5.0</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>4.0</td>
      <td>4</td>
      <td>1.0</td>
      <td>22.0</td>
      <td>172.0</td>
      <td>59.0</td>
      <td>1.0</td>
      <td>female</td>
      <td>right</td>
      <td>bachelor's degree</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>3.0</td>
      <td>2</td>
      <td>4.0</td>
      <td>20.0</td>
      <td>170.0</td>
      <td>59.0</td>
      <td>1.0</td>
      <td>female</td>
      <td>right</td>
      <td>high school</td>
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
      <th>992</th>
      <td>5.0</td>
      <td>2.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>5.0</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>3.0</td>
      <td>...</td>
      <td>4.0</td>
      <td>3</td>
      <td>4.0</td>
      <td>20.0</td>
      <td>164.0</td>
      <td>57.0</td>
      <td>1.0</td>
      <td>female</td>
      <td>right</td>
      <td>high school</td>
    </tr>
    <tr>
      <th>993</th>
      <td>4.0</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>1.0</td>
      <td>5</td>
      <td>3.0</td>
      <td>27.0</td>
      <td>183.0</td>
      <td>80.0</td>
      <td>5.0</td>
      <td>male</td>
      <td>left</td>
      <td>master's degree</td>
    </tr>
    <tr>
      <th>994</th>
      <td>4.0</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>2.0</td>
      <td>2</td>
      <td>5.0</td>
      <td>18.0</td>
      <td>173.0</td>
      <td>75.0</td>
      <td>0.0</td>
      <td>female</td>
      <td>right</td>
      <td>high school</td>
    </tr>
    <tr>
      <th>995</th>
      <td>5.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>3.0</td>
      <td>3</td>
      <td>3.0</td>
      <td>25.0</td>
      <td>173.0</td>
      <td>58.0</td>
      <td>1.0</td>
      <td>female</td>
      <td>right</td>
      <td>bachelor's degree</td>
    </tr>
    <tr>
      <th>996</th>
      <td>5.0</td>
      <td>5.0</td>
      <td>4.0</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>1.0</td>
      <td>1</td>
      <td>5.0</td>
      <td>21.0</td>
      <td>185.0</td>
      <td>72.0</td>
      <td>1.0</td>
      <td>male</td>
      <td>right</td>
      <td>high school</td>
    </tr>
  </tbody>
</table>
<p>997 rows × 147 columns</p>
</div>




```python
yv[['Branded clothing', 'Spending on looks']].corr()
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
      <th>Branded clothing</th>
      <th>Spending on looks</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Branded clothing</th>
      <td>1.000000</td>
      <td>0.418399</td>
    </tr>
    <tr>
      <th>Spending on looks</th>
      <td>0.418399</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
yv[['Musical instruments','Writing']].corr()
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
      <th>Musical instruments</th>
      <th>Writing</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Musical instruments</th>
      <td>1.000000</td>
      <td>0.343816</td>
    </tr>
    <tr>
      <th>Writing</th>
      <td>0.343816</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
yv[['New environment','Writing notes']].corr()
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
      <th>New environment</th>
      <th>Writing notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>New environment</th>
      <td>1.000000</td>
      <td>-0.079397</td>
    </tr>
    <tr>
      <th>Writing notes</th>
      <td>-0.079397</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
yvs = yv.loc[:, 'Music':'Metal or Hardrock']
```


```python
corr = yvs.corr()
corr
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
      <th>Music</th>
      <th>Slow songs or fast songs</th>
      <th>Dance</th>
      <th>Folk</th>
      <th>Country</th>
      <th>Classical music</th>
      <th>Musical</th>
      <th>Pop</th>
      <th>Rock</th>
      <th>Metal or Hardrock</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Music</th>
      <td>1.000000</td>
      <td>0.075426</td>
      <td>0.066719</td>
      <td>0.027648</td>
      <td>-0.014272</td>
      <td>0.055648</td>
      <td>0.056730</td>
      <td>0.059967</td>
      <td>0.149958</td>
      <td>0.016043</td>
    </tr>
    <tr>
      <th>Slow songs or fast songs</th>
      <td>0.075426</td>
      <td>1.000000</td>
      <td>0.188217</td>
      <td>-0.062023</td>
      <td>-0.072138</td>
      <td>-0.159021</td>
      <td>-0.078479</td>
      <td>0.054375</td>
      <td>-0.018347</td>
      <td>0.050913</td>
    </tr>
    <tr>
      <th>Dance</th>
      <td>0.066719</td>
      <td>0.188217</td>
      <td>1.000000</td>
      <td>0.065863</td>
      <td>0.055106</td>
      <td>-0.093125</td>
      <td>0.067430</td>
      <td>0.424794</td>
      <td>-0.147867</td>
      <td>-0.241477</td>
    </tr>
    <tr>
      <th>Folk</th>
      <td>0.027648</td>
      <td>-0.062023</td>
      <td>0.065863</td>
      <td>1.000000</td>
      <td>0.391850</td>
      <td>0.366988</td>
      <td>0.263987</td>
      <td>0.023641</td>
      <td>0.056471</td>
      <td>0.062454</td>
    </tr>
    <tr>
      <th>Country</th>
      <td>-0.014272</td>
      <td>-0.072138</td>
      <td>0.055106</td>
      <td>0.391850</td>
      <td>1.000000</td>
      <td>0.257474</td>
      <td>0.202831</td>
      <td>0.000716</td>
      <td>0.129917</td>
      <td>0.115289</td>
    </tr>
    <tr>
      <th>Classical music</th>
      <td>0.055648</td>
      <td>-0.159021</td>
      <td>-0.093125</td>
      <td>0.366988</td>
      <td>0.257474</td>
      <td>1.000000</td>
      <td>0.351101</td>
      <td>-0.048159</td>
      <td>0.217929</td>
      <td>0.176309</td>
    </tr>
    <tr>
      <th>Musical</th>
      <td>0.056730</td>
      <td>-0.078479</td>
      <td>0.067430</td>
      <td>0.263987</td>
      <td>0.202831</td>
      <td>0.351101</td>
      <td>1.000000</td>
      <td>0.223045</td>
      <td>0.094484</td>
      <td>-0.029776</td>
    </tr>
    <tr>
      <th>Pop</th>
      <td>0.059967</td>
      <td>0.054375</td>
      <td>0.424794</td>
      <td>0.023641</td>
      <td>0.000716</td>
      <td>-0.048159</td>
      <td>0.223045</td>
      <td>1.000000</td>
      <td>-0.029376</td>
      <td>-0.289975</td>
    </tr>
    <tr>
      <th>Rock</th>
      <td>0.149958</td>
      <td>-0.018347</td>
      <td>-0.147867</td>
      <td>0.056471</td>
      <td>0.129917</td>
      <td>0.217929</td>
      <td>0.094484</td>
      <td>-0.029376</td>
      <td>1.000000</td>
      <td>0.527272</td>
    </tr>
    <tr>
      <th>Metal or Hardrock</th>
      <td>0.016043</td>
      <td>0.050913</td>
      <td>-0.241477</td>
      <td>0.062454</td>
      <td>0.115289</td>
      <td>0.176309</td>
      <td>-0.029776</td>
      <td>-0.289975</td>
      <td>0.527272</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
corr['Pop'].sort_values(ascending=False)
```




    Pop                         1.000000
    Dance                       0.424794
    Musical                     0.223045
    Music                       0.059967
    Slow songs or fast songs    0.054375
    Folk                        0.023641
    Country                     0.000716
    Rock                       -0.029376
    Classical music            -0.048159
    Metal or Hardrock          -0.289975
    Name: Pop, dtype: float64




```python
sns.clustermap(corr)
```




    <seaborn.matrix.ClusterGrid at 0x219bec87eb0>




    
![png](output_72_1.png)
    



```python
mov = pd.read_csv('survey.csv')
mov = mov.loc[:,'Horror':'Action']
```


```python
mcorr = mov.corr()
mcorr
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
      <th>Horror</th>
      <th>Thriller</th>
      <th>Comedy</th>
      <th>Romantic</th>
      <th>Sci-fi</th>
      <th>War</th>
      <th>Fantasy/Fairy tales</th>
      <th>Animated</th>
      <th>Documentary</th>
      <th>Western</th>
      <th>Action</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Horror</th>
      <td>1.000000</td>
      <td>0.503069</td>
      <td>0.098243</td>
      <td>-0.128117</td>
      <td>0.165834</td>
      <td>0.136508</td>
      <td>-0.087150</td>
      <td>0.004865</td>
      <td>-0.063749</td>
      <td>0.078845</td>
      <td>0.129958</td>
    </tr>
    <tr>
      <th>Thriller</th>
      <td>0.503069</td>
      <td>1.000000</td>
      <td>-0.008975</td>
      <td>-0.164751</td>
      <td>0.230838</td>
      <td>0.220754</td>
      <td>-0.090075</td>
      <td>-0.025239</td>
      <td>0.046558</td>
      <td>0.124719</td>
      <td>0.278214</td>
    </tr>
    <tr>
      <th>Comedy</th>
      <td>0.098243</td>
      <td>-0.008975</td>
      <td>1.000000</td>
      <td>0.286236</td>
      <td>0.040425</td>
      <td>-0.077274</td>
      <td>0.211025</td>
      <td>0.180246</td>
      <td>-0.007444</td>
      <td>-0.033091</td>
      <td>0.121256</td>
    </tr>
    <tr>
      <th>Romantic</th>
      <td>-0.128117</td>
      <td>-0.164751</td>
      <td>0.286236</td>
      <td>1.000000</td>
      <td>-0.097219</td>
      <td>-0.193751</td>
      <td>0.349432</td>
      <td>0.239951</td>
      <td>-0.083895</td>
      <td>-0.126574</td>
      <td>-0.181823</td>
    </tr>
    <tr>
      <th>Sci-fi</th>
      <td>0.165834</td>
      <td>0.230838</td>
      <td>0.040425</td>
      <td>-0.097219</td>
      <td>1.000000</td>
      <td>0.274634</td>
      <td>-0.009158</td>
      <td>0.068642</td>
      <td>0.141714</td>
      <td>0.276898</td>
      <td>0.363429</td>
    </tr>
    <tr>
      <th>War</th>
      <td>0.136508</td>
      <td>0.220754</td>
      <td>-0.077274</td>
      <td>-0.193751</td>
      <td>0.274634</td>
      <td>1.000000</td>
      <td>-0.072474</td>
      <td>-0.026996</td>
      <td>0.235355</td>
      <td>0.396669</td>
      <td>0.299257</td>
    </tr>
    <tr>
      <th>Fantasy/Fairy tales</th>
      <td>-0.087150</td>
      <td>-0.090075</td>
      <td>0.211025</td>
      <td>0.349432</td>
      <td>-0.009158</td>
      <td>-0.072474</td>
      <td>1.000000</td>
      <td>0.679270</td>
      <td>0.140227</td>
      <td>-0.023267</td>
      <td>-0.051591</td>
    </tr>
    <tr>
      <th>Animated</th>
      <td>0.004865</td>
      <td>-0.025239</td>
      <td>0.180246</td>
      <td>0.239951</td>
      <td>0.068642</td>
      <td>-0.026996</td>
      <td>0.679270</td>
      <td>1.000000</td>
      <td>0.148375</td>
      <td>-0.003069</td>
      <td>0.019379</td>
    </tr>
    <tr>
      <th>Documentary</th>
      <td>-0.063749</td>
      <td>0.046558</td>
      <td>-0.007444</td>
      <td>-0.083895</td>
      <td>0.141714</td>
      <td>0.235355</td>
      <td>0.140227</td>
      <td>0.148375</td>
      <td>1.000000</td>
      <td>0.263859</td>
      <td>0.131062</td>
    </tr>
    <tr>
      <th>Western</th>
      <td>0.078845</td>
      <td>0.124719</td>
      <td>-0.033091</td>
      <td>-0.126574</td>
      <td>0.276898</td>
      <td>0.396669</td>
      <td>-0.023267</td>
      <td>-0.003069</td>
      <td>0.263859</td>
      <td>1.000000</td>
      <td>0.320005</td>
    </tr>
    <tr>
      <th>Action</th>
      <td>0.129958</td>
      <td>0.278214</td>
      <td>0.121256</td>
      <td>-0.181823</td>
      <td>0.363429</td>
      <td>0.299257</td>
      <td>-0.051591</td>
      <td>0.019379</td>
      <td>0.131062</td>
      <td>0.320005</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
sns.clustermap(mcorr)
```




    <seaborn.matrix.ClusterGrid at 0x219c42d9150>




    
![png](output_75_1.png)
    



```python
ti = pd.read_csv('titanic.csv', index_col=0)
ti
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
    <tr>
      <th>PassengerId</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
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
      <th>1</th>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
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
    </tr>
    <tr>
      <th>887</th>
      <td>0</td>
      <td>2</td>
      <td>Montvila, Rev. Juozas</td>
      <td>male</td>
      <td>27.0</td>
      <td>0</td>
      <td>0</td>
      <td>211536</td>
      <td>13.0000</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>888</th>
      <td>1</td>
      <td>1</td>
      <td>Graham, Miss. Margaret Edith</td>
      <td>female</td>
      <td>19.0</td>
      <td>0</td>
      <td>0</td>
      <td>112053</td>
      <td>30.0000</td>
      <td>B42</td>
      <td>S</td>
    </tr>
    <tr>
      <th>889</th>
      <td>0</td>
      <td>3</td>
      <td>Johnston, Miss. Catherine Helen "Carrie"</td>
      <td>female</td>
      <td>NaN</td>
      <td>1</td>
      <td>2</td>
      <td>W./C. 6607</td>
      <td>23.4500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>890</th>
      <td>1</td>
      <td>1</td>
      <td>Behr, Mr. Karl Howell</td>
      <td>male</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>111369</td>
      <td>30.0000</td>
      <td>C148</td>
      <td>C</td>
    </tr>
    <tr>
      <th>891</th>
      <td>0</td>
      <td>3</td>
      <td>Dooley, Mr. Patrick</td>
      <td>male</td>
      <td>32.0</td>
      <td>0</td>
      <td>0</td>
      <td>370376</td>
      <td>7.7500</td>
      <td>NaN</td>
      <td>Q</td>
    </tr>
  </tbody>
</table>
<p>891 rows × 11 columns</p>
</div>




```python
ti = ti.drop(['Name', 'Ticket', 'Cabin', "Embarked", 'Sex'], axis='columns')
```


```python
ti['Survived'].value_counts()
```




    Survived
    0    549
    1    342
    Name: count, dtype: int64




```python
ti.corr()
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
      <th>Survived</th>
      <th>Pclass</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Fare</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Survived</th>
      <td>1.000000</td>
      <td>-0.338481</td>
      <td>-0.077221</td>
      <td>-0.035322</td>
      <td>0.081629</td>
      <td>0.257307</td>
    </tr>
    <tr>
      <th>Pclass</th>
      <td>-0.338481</td>
      <td>1.000000</td>
      <td>-0.369226</td>
      <td>0.083081</td>
      <td>0.018443</td>
      <td>-0.549500</td>
    </tr>
    <tr>
      <th>Age</th>
      <td>-0.077221</td>
      <td>-0.369226</td>
      <td>1.000000</td>
      <td>-0.308247</td>
      <td>-0.189119</td>
      <td>0.096067</td>
    </tr>
    <tr>
      <th>SibSp</th>
      <td>-0.035322</td>
      <td>0.083081</td>
      <td>-0.308247</td>
      <td>1.000000</td>
      <td>0.414838</td>
      <td>0.159651</td>
    </tr>
    <tr>
      <th>Parch</th>
      <td>0.081629</td>
      <td>0.018443</td>
      <td>-0.189119</td>
      <td>0.414838</td>
      <td>1.000000</td>
      <td>0.216225</td>
    </tr>
    <tr>
      <th>Fare</th>
      <td>0.257307</td>
      <td>-0.549500</td>
      <td>0.096067</td>
      <td>0.159651</td>
      <td>0.216225</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
ti['Pclass'].value_counts()
```




    Pclass
    3    491
    1    216
    2    184
    Name: count, dtype: int64




```python
ti.loc[ti['Survived'] == 1, 'Pclass'].value_counts()
```




    Pclass
    1    136
    3    119
    2     87
    Name: count, dtype: int64




```python
ti[['Survived', 'Age']].corr()
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
      <th>Survived</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Survived</th>
      <td>1.000000</td>
      <td>-0.077221</td>
    </tr>
    <tr>
      <th>Age</th>
      <td>-0.077221</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
ti.loc[ti['Sex']== 'male', 'Sex'] = 1
ti.loc[ti['Sex']== 'female', 'Sex'] = 0
```


```python
ti[['Survived', 'Sex']].corr()
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
      <th>Survived</th>
      <th>Sex</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Survived</th>
      <td>1.000000</td>
      <td>-0.543351</td>
    </tr>
    <tr>
      <th>Sex</th>
      <td>-0.543351</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
ti['Age'].plot(kind='hist')
```




    <Axes: ylabel='Frequency'>




    
![png](output_85_1.png)
    



```python
ti[['Age','Fare']].sort_values(by = 'Fare')
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
      <th>Fare</th>
    </tr>
    <tr>
      <th>PassengerId</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>272</th>
      <td>25.0</td>
      <td>0.0000</td>
    </tr>
    <tr>
      <th>598</th>
      <td>49.0</td>
      <td>0.0000</td>
    </tr>
    <tr>
      <th>303</th>
      <td>19.0</td>
      <td>0.0000</td>
    </tr>
    <tr>
      <th>634</th>
      <td>NaN</td>
      <td>0.0000</td>
    </tr>
    <tr>
      <th>278</th>
      <td>NaN</td>
      <td>0.0000</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>439</th>
      <td>64.0</td>
      <td>263.0000</td>
    </tr>
    <tr>
      <th>342</th>
      <td>24.0</td>
      <td>263.0000</td>
    </tr>
    <tr>
      <th>738</th>
      <td>35.0</td>
      <td>512.3292</td>
    </tr>
    <tr>
      <th>259</th>
      <td>35.0</td>
      <td>512.3292</td>
    </tr>
    <tr>
      <th>680</th>
      <td>36.0</td>
      <td>512.3292</td>
    </tr>
  </tbody>
</table>
<p>891 rows × 2 columns</p>
</div>




```python
sns.violinplot(data=ti, x="Survived", y="Age")
```




    <Axes: xlabel='Survived', ylabel='Age'>




    
![png](output_87_1.png)
    



```python
df = pd.read_csv('broadcast.csv', index_col=0)
```


```python
df['total'] = df.loc[:,:].sum(axis='columns')
df['major'] = df.loc[:, 'KBS':'SBS'].sum(axis='columns')
df['jp'] = df.loc[:, 'TV CHOSUN':'MBN'].sum(axis='columns')

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
      <th>total</th>
      <th>major</th>
      <th>jp</th>
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
      <td>88.560</td>
      <td>65.498</td>
      <td>23.062</td>
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
      <td>89.440</td>
      <td>63.593</td>
      <td>25.847</td>
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
      <td>84.451</td>
      <td>58.440</td>
      <td>26.011</td>
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
      <td>83.259</td>
      <td>55.981</td>
      <td>27.278</td>
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
      <td>82.854</td>
      <td>53.449</td>
      <td>29.405</td>
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
      <td>80.891</td>
      <td>51.234</td>
      <td>29.657</td>
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
      <td>77.626</td>
      <td>48.016</td>
      <td>29.610</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.plot(y=['major', 'jp', 'total'])
```




    <Axes: >




    
![png](output_90_1.png)
    


---

## 문자열
1. 칼럼 안에 값이 특정 문자열을 갖고 있을 때
- df['col'].str.contains()  
- df['col'].str.startswith()


```python
ms = pd.read_csv('museum_1.csv')
ms
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
      <th>시설명</th>
      <th>어른관람료</th>
      <th>운영기관전화번호</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>필암서원 유물전시관</td>
      <td>500</td>
      <td>061-390-7224</td>
    </tr>
    <tr>
      <th>1</th>
      <td>원주역사박물관</td>
      <td>0</td>
      <td>033-737-4371</td>
    </tr>
    <tr>
      <th>2</th>
      <td>뮤지엄산미술관</td>
      <td>15000</td>
      <td>033-730-9000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>오랜미래신화미술관</td>
      <td>0</td>
      <td>033-746-5256</td>
    </tr>
    <tr>
      <th>4</th>
      <td>연세대학교 원주박물관</td>
      <td>0</td>
      <td>033-760-2731</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>895</th>
      <td>함양박물관</td>
      <td>0</td>
      <td>055-960-5532</td>
    </tr>
    <tr>
      <th>896</th>
      <td>박물관수</td>
      <td>5000</td>
      <td>053-744-5500</td>
    </tr>
    <tr>
      <th>897</th>
      <td>대구은행금융박물관</td>
      <td>0</td>
      <td>053-740-2061</td>
    </tr>
    <tr>
      <th>898</th>
      <td>국립대구박물관</td>
      <td>0</td>
      <td>053-768-6051</td>
    </tr>
    <tr>
      <th>899</th>
      <td>증평민속체험박물관</td>
      <td>0</td>
      <td>043-835-4161</td>
    </tr>
  </tbody>
</table>
<p>900 rows × 3 columns</p>
</div>




```python
univ = ms['시설명'].str.contains('대학')
ms['분류'] = '일반'
ms.loc[univ, '분류'] = '대학'
ms
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
      <th>시설명</th>
      <th>어른관람료</th>
      <th>운영기관전화번호</th>
      <th>분류</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>필암서원 유물전시관</td>
      <td>500</td>
      <td>061-390-7224</td>
      <td>일반</td>
    </tr>
    <tr>
      <th>1</th>
      <td>원주역사박물관</td>
      <td>0</td>
      <td>033-737-4371</td>
      <td>일반</td>
    </tr>
    <tr>
      <th>2</th>
      <td>뮤지엄산미술관</td>
      <td>15000</td>
      <td>033-730-9000</td>
      <td>일반</td>
    </tr>
    <tr>
      <th>3</th>
      <td>오랜미래신화미술관</td>
      <td>0</td>
      <td>033-746-5256</td>
      <td>일반</td>
    </tr>
    <tr>
      <th>4</th>
      <td>연세대학교 원주박물관</td>
      <td>0</td>
      <td>033-760-2731</td>
      <td>대학</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>895</th>
      <td>함양박물관</td>
      <td>0</td>
      <td>055-960-5532</td>
      <td>일반</td>
    </tr>
    <tr>
      <th>896</th>
      <td>박물관수</td>
      <td>5000</td>
      <td>053-744-5500</td>
      <td>일반</td>
    </tr>
    <tr>
      <th>897</th>
      <td>대구은행금융박물관</td>
      <td>0</td>
      <td>053-740-2061</td>
      <td>일반</td>
    </tr>
    <tr>
      <th>898</th>
      <td>국립대구박물관</td>
      <td>0</td>
      <td>053-768-6051</td>
      <td>일반</td>
    </tr>
    <tr>
      <th>899</th>
      <td>증평민속체험박물관</td>
      <td>0</td>
      <td>043-835-4161</td>
      <td>일반</td>
    </tr>
  </tbody>
</table>
<p>900 rows × 4 columns</p>
</div>



2. 칼럼 안의 문자열을 쪼개고 싶을 때
- df['col'].str.split(n=x, expand=True)
- 학습자료는 pat을 설명하지 않았으나 공식 문서 참조해서 확인. 이렇게 하는 게 공부긴 하다
- expand를 true로 해서 데이터프레임으로 만들어야 0번 칼럼을 통째로 떠올 수 있구나
- 만약 시리즈로 뗐으면 리스트라서 0번 인덱스가 가져와진다


```python
n = ms['운영기관전화번호'].str.split(n=1, pat='-', expand=True)
ms['지역번호'] = n[0]
ms

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
      <th>시설명</th>
      <th>어른관람료</th>
      <th>운영기관전화번호</th>
      <th>분류</th>
      <th>지역번호</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>필암서원 유물전시관</td>
      <td>500</td>
      <td>061-390-7224</td>
      <td>일반</td>
      <td>061</td>
    </tr>
    <tr>
      <th>1</th>
      <td>원주역사박물관</td>
      <td>0</td>
      <td>033-737-4371</td>
      <td>일반</td>
      <td>033</td>
    </tr>
    <tr>
      <th>2</th>
      <td>뮤지엄산미술관</td>
      <td>15000</td>
      <td>033-730-9000</td>
      <td>일반</td>
      <td>033</td>
    </tr>
    <tr>
      <th>3</th>
      <td>오랜미래신화미술관</td>
      <td>0</td>
      <td>033-746-5256</td>
      <td>일반</td>
      <td>033</td>
    </tr>
    <tr>
      <th>4</th>
      <td>연세대학교 원주박물관</td>
      <td>0</td>
      <td>033-760-2731</td>
      <td>대학</td>
      <td>033</td>
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
      <th>895</th>
      <td>함양박물관</td>
      <td>0</td>
      <td>055-960-5532</td>
      <td>일반</td>
      <td>055</td>
    </tr>
    <tr>
      <th>896</th>
      <td>박물관수</td>
      <td>5000</td>
      <td>053-744-5500</td>
      <td>일반</td>
      <td>053</td>
    </tr>
    <tr>
      <th>897</th>
      <td>대구은행금융박물관</td>
      <td>0</td>
      <td>053-740-2061</td>
      <td>일반</td>
      <td>053</td>
    </tr>
    <tr>
      <th>898</th>
      <td>국립대구박물관</td>
      <td>0</td>
      <td>053-768-6051</td>
      <td>일반</td>
      <td>053</td>
    </tr>
    <tr>
      <th>899</th>
      <td>증평민속체험박물관</td>
      <td>0</td>
      <td>043-835-4161</td>
      <td>일반</td>
      <td>043</td>
    </tr>
  </tbody>
</table>
<p>900 rows × 5 columns</p>
</div>



3. 칼럼 안의 문자열을 치환 할 때
- df['col'].map(dict)
- dict는 dict = {'a' : 'b'} 바꾸려는 문자와 치환값이 있어야 한다


```python
loc = {'02':'서울시',
       '031': '경기도',
       '032': '경기도',
       '033': '강원도',
       '041': '충청도',
       '042': '충청도',
       '043': '충청도',
       '044': '충청도',
       '051': '부산시',
       '052': '경상도',
       '053': '경상도',
       '054': '경상도',
       '055': '경상도',
       '061': '전라도',
       '062': '전라도',
       '063': '전라도',
       '064': '제주도',
       '1577': '기타',
       '070':'기타'
       }
```


```python
ms = ms.astype({'지역번호':'str'})
ms.dtypes
```




    시설명         object
    어른관람료        int64
    운영기관전화번호    object
    분류          object
    지역번호        object
    dtype: object




```python
# 칼럼을 추가하고
ms['지역명'] = ms['지역번호'].map(loc)
# 기존 칼럼을 없앤다
ms.drop('지역번호', axis='columns', inplace=True)
ms
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
      <th>시설명</th>
      <th>어른관람료</th>
      <th>운영기관전화번호</th>
      <th>분류</th>
      <th>지역명</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>필암서원 유물전시관</td>
      <td>500</td>
      <td>061-390-7224</td>
      <td>일반</td>
      <td>전라도</td>
    </tr>
    <tr>
      <th>1</th>
      <td>원주역사박물관</td>
      <td>0</td>
      <td>033-737-4371</td>
      <td>일반</td>
      <td>강원도</td>
    </tr>
    <tr>
      <th>2</th>
      <td>뮤지엄산미술관</td>
      <td>15000</td>
      <td>033-730-9000</td>
      <td>일반</td>
      <td>강원도</td>
    </tr>
    <tr>
      <th>3</th>
      <td>오랜미래신화미술관</td>
      <td>0</td>
      <td>033-746-5256</td>
      <td>일반</td>
      <td>강원도</td>
    </tr>
    <tr>
      <th>4</th>
      <td>연세대학교 원주박물관</td>
      <td>0</td>
      <td>033-760-2731</td>
      <td>대학</td>
      <td>강원도</td>
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
      <th>895</th>
      <td>함양박물관</td>
      <td>0</td>
      <td>055-960-5532</td>
      <td>일반</td>
      <td>경상도</td>
    </tr>
    <tr>
      <th>896</th>
      <td>박물관수</td>
      <td>5000</td>
      <td>053-744-5500</td>
      <td>일반</td>
      <td>경상도</td>
    </tr>
    <tr>
      <th>897</th>
      <td>대구은행금융박물관</td>
      <td>0</td>
      <td>053-740-2061</td>
      <td>일반</td>
      <td>경상도</td>
    </tr>
    <tr>
      <th>898</th>
      <td>국립대구박물관</td>
      <td>0</td>
      <td>053-768-6051</td>
      <td>일반</td>
      <td>경상도</td>
    </tr>
    <tr>
      <th>899</th>
      <td>증평민속체험박물관</td>
      <td>0</td>
      <td>043-835-4161</td>
      <td>일반</td>
      <td>충청도</td>
    </tr>
  </tbody>
</table>
<p>900 rows × 5 columns</p>
</div>




```python
# 해설 답안은 칼럼 내용을 바꾸고 칼럼 이름을 바꿨다
# ms["지역번호"] = ms["지역번호"].map(loc)
# ms.rename(columns={"지역번호": "지역명"}, inplace=True)
# ms
```

4. 칼럼을 묶어줄 때
- df.groupby('col')


```python
occ = pd.read_csv('occupations_2.csv')
og = occ[['occupation', 'age']].groupby('occupation')
og
```




    <pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000022295A828C0>




```python
og.count()
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
      <th>age</th>
    </tr>
    <tr>
      <th>occupation</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>administrator</th>
      <td>79</td>
    </tr>
    <tr>
      <th>artist</th>
      <td>28</td>
    </tr>
    <tr>
      <th>doctor</th>
      <td>7</td>
    </tr>
    <tr>
      <th>educator</th>
      <td>95</td>
    </tr>
    <tr>
      <th>engineer</th>
      <td>67</td>
    </tr>
    <tr>
      <th>entertainment</th>
      <td>18</td>
    </tr>
    <tr>
      <th>executive</th>
      <td>32</td>
    </tr>
    <tr>
      <th>healthcare</th>
      <td>16</td>
    </tr>
    <tr>
      <th>homemaker</th>
      <td>7</td>
    </tr>
    <tr>
      <th>lawyer</th>
      <td>12</td>
    </tr>
    <tr>
      <th>librarian</th>
      <td>51</td>
    </tr>
    <tr>
      <th>marketing</th>
      <td>26</td>
    </tr>
    <tr>
      <th>none</th>
      <td>9</td>
    </tr>
    <tr>
      <th>other</th>
      <td>105</td>
    </tr>
    <tr>
      <th>programmer</th>
      <td>66</td>
    </tr>
    <tr>
      <th>retired</th>
      <td>14</td>
    </tr>
    <tr>
      <th>salesman</th>
      <td>12</td>
    </tr>
    <tr>
      <th>scientist</th>
      <td>31</td>
    </tr>
    <tr>
      <th>student</th>
      <td>196</td>
    </tr>
    <tr>
      <th>technician</th>
      <td>27</td>
    </tr>
    <tr>
      <th>writer</th>
      <td>45</td>
    </tr>
  </tbody>
</table>
</div>




```python
og.mean().sort_values(by='age')
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
      <th>age</th>
    </tr>
    <tr>
      <th>occupation</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>student</th>
      <td>22.081633</td>
    </tr>
    <tr>
      <th>none</th>
      <td>26.555556</td>
    </tr>
    <tr>
      <th>entertainment</th>
      <td>29.222222</td>
    </tr>
    <tr>
      <th>artist</th>
      <td>31.392857</td>
    </tr>
    <tr>
      <th>homemaker</th>
      <td>32.571429</td>
    </tr>
    <tr>
      <th>programmer</th>
      <td>33.121212</td>
    </tr>
    <tr>
      <th>technician</th>
      <td>33.148148</td>
    </tr>
    <tr>
      <th>other</th>
      <td>34.523810</td>
    </tr>
    <tr>
      <th>scientist</th>
      <td>35.548387</td>
    </tr>
    <tr>
      <th>salesman</th>
      <td>35.666667</td>
    </tr>
    <tr>
      <th>writer</th>
      <td>36.311111</td>
    </tr>
    <tr>
      <th>engineer</th>
      <td>36.388060</td>
    </tr>
    <tr>
      <th>lawyer</th>
      <td>36.750000</td>
    </tr>
    <tr>
      <th>marketing</th>
      <td>37.615385</td>
    </tr>
    <tr>
      <th>executive</th>
      <td>38.718750</td>
    </tr>
    <tr>
      <th>administrator</th>
      <td>38.746835</td>
    </tr>
    <tr>
      <th>librarian</th>
      <td>40.000000</td>
    </tr>
    <tr>
      <th>healthcare</th>
      <td>41.562500</td>
    </tr>
    <tr>
      <th>educator</th>
      <td>42.010526</td>
    </tr>
    <tr>
      <th>doctor</th>
      <td>43.571429</td>
    </tr>
    <tr>
      <th>retired</th>
      <td>63.071429</td>
    </tr>
  </tbody>
</table>
</div>




```python
og2 = occ[['occupation', 'gender']].groupby('occupation')
og2.count()
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
      <th>gender</th>
    </tr>
    <tr>
      <th>occupation</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>administrator</th>
      <td>79</td>
    </tr>
    <tr>
      <th>artist</th>
      <td>28</td>
    </tr>
    <tr>
      <th>doctor</th>
      <td>7</td>
    </tr>
    <tr>
      <th>educator</th>
      <td>95</td>
    </tr>
    <tr>
      <th>engineer</th>
      <td>67</td>
    </tr>
    <tr>
      <th>entertainment</th>
      <td>18</td>
    </tr>
    <tr>
      <th>executive</th>
      <td>32</td>
    </tr>
    <tr>
      <th>healthcare</th>
      <td>16</td>
    </tr>
    <tr>
      <th>homemaker</th>
      <td>7</td>
    </tr>
    <tr>
      <th>lawyer</th>
      <td>12</td>
    </tr>
    <tr>
      <th>librarian</th>
      <td>51</td>
    </tr>
    <tr>
      <th>marketing</th>
      <td>26</td>
    </tr>
    <tr>
      <th>none</th>
      <td>9</td>
    </tr>
    <tr>
      <th>other</th>
      <td>105</td>
    </tr>
    <tr>
      <th>programmer</th>
      <td>66</td>
    </tr>
    <tr>
      <th>retired</th>
      <td>14</td>
    </tr>
    <tr>
      <th>salesman</th>
      <td>12</td>
    </tr>
    <tr>
      <th>scientist</th>
      <td>31</td>
    </tr>
    <tr>
      <th>student</th>
      <td>196</td>
    </tr>
    <tr>
      <th>technician</th>
      <td>27</td>
    </tr>
    <tr>
      <th>writer</th>
      <td>45</td>
    </tr>
  </tbody>
</table>
</div>




```python
og2.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="4" halign="left">gender</th>
    </tr>
    <tr>
      <th></th>
      <th>count</th>
      <th>unique</th>
      <th>top</th>
      <th>freq</th>
    </tr>
    <tr>
      <th>occupation</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>administrator</th>
      <td>79</td>
      <td>2</td>
      <td>M</td>
      <td>43</td>
    </tr>
    <tr>
      <th>artist</th>
      <td>28</td>
      <td>2</td>
      <td>M</td>
      <td>15</td>
    </tr>
    <tr>
      <th>doctor</th>
      <td>7</td>
      <td>1</td>
      <td>M</td>
      <td>7</td>
    </tr>
    <tr>
      <th>educator</th>
      <td>95</td>
      <td>2</td>
      <td>M</td>
      <td>69</td>
    </tr>
    <tr>
      <th>engineer</th>
      <td>67</td>
      <td>2</td>
      <td>M</td>
      <td>65</td>
    </tr>
    <tr>
      <th>entertainment</th>
      <td>18</td>
      <td>2</td>
      <td>M</td>
      <td>16</td>
    </tr>
    <tr>
      <th>executive</th>
      <td>32</td>
      <td>2</td>
      <td>M</td>
      <td>29</td>
    </tr>
    <tr>
      <th>healthcare</th>
      <td>16</td>
      <td>2</td>
      <td>F</td>
      <td>11</td>
    </tr>
    <tr>
      <th>homemaker</th>
      <td>7</td>
      <td>2</td>
      <td>F</td>
      <td>6</td>
    </tr>
    <tr>
      <th>lawyer</th>
      <td>12</td>
      <td>2</td>
      <td>M</td>
      <td>10</td>
    </tr>
    <tr>
      <th>librarian</th>
      <td>51</td>
      <td>2</td>
      <td>F</td>
      <td>29</td>
    </tr>
    <tr>
      <th>marketing</th>
      <td>26</td>
      <td>2</td>
      <td>M</td>
      <td>16</td>
    </tr>
    <tr>
      <th>none</th>
      <td>9</td>
      <td>2</td>
      <td>M</td>
      <td>5</td>
    </tr>
    <tr>
      <th>other</th>
      <td>105</td>
      <td>2</td>
      <td>M</td>
      <td>69</td>
    </tr>
    <tr>
      <th>programmer</th>
      <td>66</td>
      <td>2</td>
      <td>M</td>
      <td>60</td>
    </tr>
    <tr>
      <th>retired</th>
      <td>14</td>
      <td>2</td>
      <td>M</td>
      <td>13</td>
    </tr>
    <tr>
      <th>salesman</th>
      <td>12</td>
      <td>2</td>
      <td>M</td>
      <td>9</td>
    </tr>
    <tr>
      <th>scientist</th>
      <td>31</td>
      <td>2</td>
      <td>M</td>
      <td>28</td>
    </tr>
    <tr>
      <th>student</th>
      <td>196</td>
      <td>2</td>
      <td>M</td>
      <td>136</td>
    </tr>
    <tr>
      <th>technician</th>
      <td>27</td>
      <td>2</td>
      <td>M</td>
      <td>26</td>
    </tr>
    <tr>
      <th>writer</th>
      <td>45</td>
      <td>2</td>
      <td>M</td>
      <td>26</td>
    </tr>
  </tbody>
</table>
</div>




```python
og2[og2['gender'] == 'M']
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    Cell In[82], line 1
    ----> 1 og2[og2['gender'] == 'M']
    

    File c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\groupby\generic.py:1771, in DataFrameGroupBy.__getitem__(self, key)
       1764 if isinstance(key, tuple) and len(key) > 1:
       1765     # if len == 1, then it becomes a SeriesGroupBy and this is actually
       1766     # valid syntax, so don't raise
       1767     raise ValueError(
       1768         "Cannot subset columns with a tuple with more than one element. "
       1769         "Use a list instead."
       1770     )
    -> 1771 return super().__getitem__(key)
    

    File c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\base.py:244, in SelectionMixin.__getitem__(self, key)
        242 else:
        243     if key not in self.obj:
    --> 244         raise KeyError(f"Column not found: {key}")
        245     ndim = self.obj[key].ndim
        246     return self._gotitem(key, ndim=ndim)
    

    KeyError: 'Column not found: False'



```python
occ['male'] = 0
occ.loc[occ['gender'] == 'M', 'male'] = 1
occ['female'] = 0
occ.loc[occ['gender'] == 'F', 'female'] = 1
occ['gender'] = occ['female']
occ
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
      <th>age</th>
      <th>gender</th>
      <th>occupation</th>
      <th>male</th>
      <th>female</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>24</td>
      <td>0</td>
      <td>technician</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>53</td>
      <td>1</td>
      <td>other</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>23</td>
      <td>0</td>
      <td>writer</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>24</td>
      <td>0</td>
      <td>technician</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>33</td>
      <td>1</td>
      <td>other</td>
      <td>0</td>
      <td>1</td>
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
      <th>938</th>
      <td>26</td>
      <td>1</td>
      <td>student</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>939</th>
      <td>32</td>
      <td>0</td>
      <td>administrator</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>940</th>
      <td>20</td>
      <td>0</td>
      <td>student</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>941</th>
      <td>48</td>
      <td>1</td>
      <td>librarian</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>942</th>
      <td>22</td>
      <td>0</td>
      <td>student</td>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>943 rows × 5 columns</p>
</div>




```python
og3 = occ[['occupation', 'gender']].groupby('occupation')
og3.mean().sort_values(by='gender', ascending=False)
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
      <th>gender</th>
    </tr>
    <tr>
      <th>occupation</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>homemaker</th>
      <td>0.857143</td>
    </tr>
    <tr>
      <th>healthcare</th>
      <td>0.687500</td>
    </tr>
    <tr>
      <th>librarian</th>
      <td>0.568627</td>
    </tr>
    <tr>
      <th>artist</th>
      <td>0.464286</td>
    </tr>
    <tr>
      <th>administrator</th>
      <td>0.455696</td>
    </tr>
    <tr>
      <th>none</th>
      <td>0.444444</td>
    </tr>
    <tr>
      <th>writer</th>
      <td>0.422222</td>
    </tr>
    <tr>
      <th>marketing</th>
      <td>0.384615</td>
    </tr>
    <tr>
      <th>other</th>
      <td>0.342857</td>
    </tr>
    <tr>
      <th>student</th>
      <td>0.306122</td>
    </tr>
    <tr>
      <th>educator</th>
      <td>0.273684</td>
    </tr>
    <tr>
      <th>salesman</th>
      <td>0.250000</td>
    </tr>
    <tr>
      <th>lawyer</th>
      <td>0.166667</td>
    </tr>
    <tr>
      <th>entertainment</th>
      <td>0.111111</td>
    </tr>
    <tr>
      <th>scientist</th>
      <td>0.096774</td>
    </tr>
    <tr>
      <th>executive</th>
      <td>0.093750</td>
    </tr>
    <tr>
      <th>programmer</th>
      <td>0.090909</td>
    </tr>
    <tr>
      <th>retired</th>
      <td>0.071429</td>
    </tr>
    <tr>
      <th>technician</th>
      <td>0.037037</td>
    </tr>
    <tr>
      <th>engineer</th>
      <td>0.029851</td>
    </tr>
    <tr>
      <th>doctor</th>
      <td>0.000000</td>
    </tr>
  </tbody>
</table>
</div>



5. 데이터 합치기
- 기준으로 하는 칼럼의 값에 대해서
- inner join
  - 교집합 A & B
  - 기준 칼럼 안에 같은 이름을 갖는 값을 기준으로 데이터를 합친다
- left outer join
  - 집합 A
  - 기준 칼럼 안에 같은 이름을 갖는 값과 왼쪽(집합A) 칼럼의 데이터를 합친다
- right outer join
  - 집합 B
  - 기준 칼럼 안에 같은 이름을 갖는 값과 오른쪽(집합B) 칼럼의 데이터를 합친다
- full outer join
  - 합집합 A + B
  - 기준 칼럼 안에 모든 이름의 데이터를 합친다

![merge](https://miro.medium.com/v2/resize:fit:1200/1*9eH1_7VbTZPZd9jBiGIyNA.png)


```python
ms3 = pd.read_csv('museum_3.csv')
reg = pd.read_csv('region_number.csv')
msreg = pd.merge(ms3, reg, on='지역번호', how='left')
msreg
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
      <th>시설명</th>
      <th>어른관람료</th>
      <th>운영기관전화번호</th>
      <th>분류</th>
      <th>지역번호</th>
      <th>지역명</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>필암서원 유물전시관</td>
      <td>500</td>
      <td>061-390-7224</td>
      <td>일반</td>
      <td>61</td>
      <td>전라남도</td>
    </tr>
    <tr>
      <th>1</th>
      <td>원주역사박물관</td>
      <td>0</td>
      <td>033-737-4371</td>
      <td>일반</td>
      <td>33</td>
      <td>강원도</td>
    </tr>
    <tr>
      <th>2</th>
      <td>뮤지엄산미술관</td>
      <td>15000</td>
      <td>033-730-9000</td>
      <td>일반</td>
      <td>33</td>
      <td>강원도</td>
    </tr>
    <tr>
      <th>3</th>
      <td>오랜미래신화미술관</td>
      <td>0</td>
      <td>033-746-5256</td>
      <td>일반</td>
      <td>33</td>
      <td>강원도</td>
    </tr>
    <tr>
      <th>4</th>
      <td>연세대학교 원주박물관</td>
      <td>0</td>
      <td>033-760-2731</td>
      <td>대학</td>
      <td>33</td>
      <td>강원도</td>
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
      <th>895</th>
      <td>함양박물관</td>
      <td>0</td>
      <td>055-960-5532</td>
      <td>일반</td>
      <td>55</td>
      <td>경상남도</td>
    </tr>
    <tr>
      <th>896</th>
      <td>박물관수</td>
      <td>5000</td>
      <td>053-744-5500</td>
      <td>일반</td>
      <td>53</td>
      <td>대구광역시</td>
    </tr>
    <tr>
      <th>897</th>
      <td>대구은행금융박물관</td>
      <td>0</td>
      <td>053-740-2061</td>
      <td>일반</td>
      <td>53</td>
      <td>대구광역시</td>
    </tr>
    <tr>
      <th>898</th>
      <td>국립대구박물관</td>
      <td>0</td>
      <td>053-768-6051</td>
      <td>일반</td>
      <td>53</td>
      <td>대구광역시</td>
    </tr>
    <tr>
      <th>899</th>
      <td>증평민속체험박물관</td>
      <td>0</td>
      <td>043-835-4161</td>
      <td>일반</td>
      <td>43</td>
      <td>충청북도</td>
    </tr>
  </tbody>
</table>
<p>900 rows × 6 columns</p>
</div>


