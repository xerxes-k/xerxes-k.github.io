**Table of contents**<a id='toc0_'></a>    
- [web clustering](#toc1_)    
  - [기초 상식](#toc1_1_)    
  - [웹의 3요소](#toc1_2_)    
  - [html 이해](#toc1_3_)    
    - [css 선택자](#toc1_3_1_)    
    - [select Vs. find_all](#toc1_3_2_)    
    - [속성 가져오기](#toc1_3_3_)    
  - [openpyxl을 이용해 excel로 저장하는 법](#toc1_4_)    
  - [csv로도 저장할 수 있다](#toc1_5_)    
  - [selenium이란](#toc1_6_)    
    - [select](#toc1_6_1_)    
  - [수료증](#toc1_7_)    

<!-- vscode-jupyter-toc-config
	numbering=false
	anchor=true
	flat=false
	minLevel=1
	maxLevel=6
	/vscode-jupyter-toc-config -->
<!-- THIS CELL WILL BE REPLACED ON TOC UPDATE. DO NOT WRITE YOUR TEXT IN THIS CELL -->

# <a id='toc1_'></a>[web clustering](#toc0_)
---

## <a id='toc1_1_'></a>[기초 상식](#toc0_)
---

hypertext: a software system that links topics on the screen to related information and graphics, which are typically accessed by a point-and-click method.

http : hypertext Transfer Protocol  
html : hypertext Markup Language

하이퍼 텍스트를 이용하려면 
- 하이퍼 텍스트를 보여줄 소프트웨어가 필요 : 웹 브라우저
- 하이퍼 텍스트를 만들 방법이 필요 : HTML

html 규칙을 국제표준으로 만들었다

하이퍼 텍스트로 다른 문서에 링크를 걸 때 내 문서가 아닌 다른 사람의 문서에 연결 할 수 있는 방법이 필요했다  
그래서 모두가 사용하는 주소체계를 만들었다. 그게 URL uniform resource locator이다

그러나 각자 url을 갖고 있어도 url 자체를 모르면 서로에게 연결 할 수가 없다  
그래서 url을 모아 검색할 수 있는 검색엔진들이 나왔다. url을 수집하기 위해 web crawling이라는 기술을 쓴다

지금 알고 있는 웹페이지에 접속해서 해당 웹페이지가 연결하는 url을 수집, 키워드를 연결해서 저장, 다시 그 url이 연결하는 url을 수집 ... 반복한다

![webcrawling](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=4050&directory=Screenshot%202020-12-08%20at%202.39.02%20PM.png&name=Screenshot+2020-12-08+at+2.39.02+PM.png)

만약 웹페이지에서 데이터를 수집한다면 이건 web scraping이라고 한다

## <a id='toc1_2_'></a>[웹의 3요소](#toc0_)
---
html, css, java script
- css: cascading style sheets 디자인을 담당
- java script: 동작을 담당

웹브라우져는 html만 보여주다가 점점 발전


```python
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
```


```python
from selenium.webdriver.support.ui import Select
```


```python
response = requests.get("https://workey.codeit.kr/ratings/index")
print(response.text)
```

    <!DOCTYPE html>
    <html lang="ko">
    <head>
      <title>티비랭킹닷컴</title>
      <meta charset="utf-8">
      <link href="https://fonts.googleapis.com/css?family=Noto+Sans+KR" rel="stylesheet">
      <style>
        /* body start */
        body {
          font-family: 'Noto Sans KR', sans-serif;
          margin: 0;
        }
    
        /* navigation bar start */
        .nav-bar {
          position: fixed;
          width: 100%;
          padding-top: 10px;
          padding-bottom: 10px;
          background-color: #ffffff;
          box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.14);
          z-index: 1;
        }
    
        .nav-bar #tv-image {
          margin-left: 78px;
          margin-right: 15px;
          height: 36px;
          vertical-align: middle;
        }
    
        .nav-bar span {
          font-weight: bold;
          color: #4a4a4a;
        }
    
        /* date picker start */
        .date-pick {
          padding-top: 56px;
          height: 200px;
          background-color: #efefef;
          margin-left: auto;
          margin-right: auto;
          position: relative;
        }
    
        .date-pick .search-box {
          text-align: center;
          position: absolute;
          display: block;
          left: 50%;
          transform: translateX(-50%);
        }
    
        .date-pick .search-box p {
          text-align: left;
        }
    
        .date-pick .search-box select {
          padding: 4px;
        }
    
        .date-pick .search-box .search-btn {
          display: inline-block;
          margin-left: 20px;
          padding: 3px 28px 4px 28px;
          border-radius: 4px;
          background-color: #00a9dc;
          font-weight: 300;
          font-size: 13.333px;
          height: 27px;
          box-sizing: border-box;
          color: #ffffff;
        }
    
        /* main body start */
    
        .container {
          margin-left: auto;
          margin-right: auto;
        }
    
        .row.top-table {
          background-color: #00a9dc;
          color: #ffffff;
          padding-top: 20px;
          padding-bottom: 20px;
        }
    
        table {
          border-collapse: collapse;
          border-spacing: 2px;
          font-size: 16px;
        }
    
        td, th {
          display: table-cell;
          color: #4a4a4a;
        }
    
        .row .rank {
          padding-left: 25px;
        }
    
        .row .channel {
          padding-left: 58px;
        }
    
        .row .program {
          padding-left: 41px;
        }
    
        .row .percent {
          color: #00a9dc;
          padding-left: 100px;
        }
    
        .top-table.row * {
          color: #ffffff;
          font-weight: 300;
        }
    
        .top-table.row .rank {
          padding-left: 17px;
          padding-right: 17px;
        }
    
        .top-table.row .channel {
          padding-right: 58px;
        }
    
        .top-table.row .program {
          padding-right: 41px;
        }
    
        .top-table.row .percent {
          padding-right: 28px;
        }
    
        .header-row {
          min-width: 391px;
          display: inline-block;
          text-align: center;
        }
      </style>
    </head>
    <body>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"
            integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
            crossorigin="anonymous">
    </script>
    
    <!-- NAVIGATION BAR -->
    <div class="nav-bar">
      <img src="/images/nielsen/group.png" id='tv-image'>
      <span>TV Ranking.com</span>
    </div>
    <!-- DATE PICKER -->
    <div class='date-pick'>
      <div style="height:55px;"></div>
      <div class='search-box'>
        <p style="font-size: 16px;color:#4a4a4a;margin-bottom: 4px;">날짜 검색</p>
        <section class="header-row">
          <select name="year" style="padding-right: 32px" class="getYear">
            <option selected="selected">2010</option>
            <option>2011</option>
            <option>2012</option>
            <option>2013</option>
            <option>2014</option>
            <option>2015</option>
            <option>2016</option>
            <option>2017</option>
            <option>2018</option>
          </select>
          <select class="getMonth" name="month" style="padding-right: 32px">
            <option selected="selected">1</option>
            <option>2</option>
            <option>3</option>
            <option>4</option>
            <option>5</option>
            <option>6</option>
            <option>7</option>
            <option>8</option>
            <option>9</option>
            <option>10</option>
            <option>11</option>
            <option>12</option>
          </select>
          <select id="weekSelectBox">
            <option value="0" selected="selected">2009.12.28 ~ 2010.01.03</option>
            <option value="1">2010.01.04 ~ 2010.01.10</option>
            <option value="2">2010.01.11 ~ 2010.01.17</option>
            <option value="3">2010.01.18 ~ 2010.01.24</option>
            <option value="4">2010.01.25 ~ 2010.01.31</option>
          </select>
          <div class="search-btn">
            search
          </div>
        </section>
      </div>
    </div>
    
    <!-- MAIN BODY -->
    <div class="container">
      <div class="box">
        <p style="font-size:18px;color:#4a4a4a;text-align: center;margin-top:60px; margin-bottom:15px;">가구시청률 TOP 10</p>
        <p style="font-size:14px;color:#9b9b9b;text-align: center;margin-bottom:25px">(분석기준: National, 유료플랫폼 가입 기구,
          단위:%)</p>
        <table style="margin-left: auto;margin-right: auto;" cellpadding="7">
          <tr height="64" class="top-table row">
            <th class="rank">순위</th>
            <th class="channel">채널</th>
            <th class="program">프로그램</th>
            <th class="percent">시청률</th>
          </tr>
          <tr class="row">
            <td class="rank">1</td>
            <td class="channel">KBS2</td>
            <td class="program">주말연속극(수상한삼형제)</td>
            <td class="percent">33.4</td>
          </tr>
          <tr class="row">
            <td class="rank">2</td>
            <td class="channel">KBS1</td>
            <td class="program">일일연속극(다함께차차차)</td>
            <td class="percent">33.1</td>
          </tr>
          <tr class="row">
            <td class="rank">3</td>
            <td class="channel">KBS2</td>
            <td class="program">해피선데이</td>
            <td class="percent">27.1</td>
          </tr>
          <tr class="row">
            <td class="rank">4</td>
            <td class="channel">MBC</td>
            <td class="program">MBC연기대상2부</td>
            <td class="percent">24.4</td>
          </tr>
          <tr class="row">
            <td class="rank">5</td>
            <td class="channel">SBS</td>
            <td class="program">주말극장(천만번사랑해)</td>
            <td class="percent">24.2</td>
          </tr>
          <tr class="row">
            <td class="rank">6</td>
            <td class="channel">MBC</td>
            <td class="program">MBC방송연예대상2부</td>
            <td class="percent">24.0</td>
          </tr>
          <tr class="row">
            <td class="rank">7</td>
            <td class="channel">MBC</td>
            <td class="program">MBC방송연예대상1부</td>
            <td class="percent">22.4</td>
          </tr>
          <tr class="row">
            <td class="rank">8</td>
            <td class="channel">SBS</td>
            <td class="program">SBS연예대상2부</td>
            <td class="percent">21.1</td>
          </tr>
          <tr class="row">
            <td class="rank">9</td>
            <td class="channel">MBC</td>
            <td class="program">주말기획드라마(보석비빔밥)</td>
            <td class="percent">20.9</td>
          </tr>
          <tr class="row">
            <td class="rank">10</td>
            <td class="channel">MBC</td>
            <td class="program">일일시트콤(지붕뚫고하이킥)</td>
            <td class="percent">19.9</td>
          </tr>
        </table>
      </div>
    </div>
    <script>
      $(".getMonth, .getYear").on("change", function () {
        window.location.assign("/ratings/index?year=" + $(".getYear").val() + "&month=" + $(".getMonth").val() + "&weekIndex=0");
    
      });
      $(".search-btn").on("click", function () {
        var index = $("#weekSelectBox").val();
        window.location.assign("/ratings/index?year=" + $(".getYear").val() + "&month=" + $(".getMonth").val() + "&weekIndex=" + index);
      });
    </script>
    </body>
    </html>
    
    


```python
# https://workey.codeit.kr/ratings/index?year=2010&month=1&weekIndex=0
rpages =[]
for y in range(3):
    for m in range(1,13):
        for w in range(5):
            response = requests.get(f"https://workey.codeit.kr/ratings/index?year=201{y}&month={m}&weekIndex={w}")
            rating_page = response.text
            rpages.append(rating_page)
len(rpages)
```




    180



## <a id='toc1_3_'></a>[html 이해](#toc0_)
---
웹 스크래핑으로 웹에서 데이터를 가져오려면 웹을 만들 때 쓰는 html을 이해해야 한다
- 꺽쇠로 <태그> 구성 됨
- 태그를 열면 태그를 닫아야 함 -> 트리 구조
- 속성 attribute을 가질 수 있다 -> 값을 담을 수 있다

https://www.w3schools.com/tags/default.asp

### <a id='toc1_3_1_'></a>[css 선택자](#toc0_)
---
- 제목이나 본문을 선택하려면 그냥 h2, p {}
- id 선택하려면 #id
- class 선택하려면 .class
- 이외에 지정하려면 [href="google.com"]

- or로 적용하려면 comma로 연결
h2, p, a{  
    color: royalblue;  
    text-align: center;  
}

- and로 연결하려면
b.class 처럼 그냥 붙여쓰면 된다

- 중첩된 요소로 가려면
그냥 띄어쓰기로 연결하면 된다

- 직속 자식?만 선택하려면
li > i 처럼 >로 연결하면 된다

- 모든 태그를 지칭하려면
*를 쓴다  
즉  
li *


```python
response = requests.get("https://workey.codeit.kr/ratings/index")
rpage = response.text

soup = BeautifulSoup(rpage, 'html.parser')
print(soup.prettify())
```

    <!DOCTYPE html>
    <html lang="ko">
     <head>
      <title>
       티비랭킹닷컴
      </title>
      <meta charset="utf-8"/>
      <link href="https://fonts.googleapis.com/css?family=Noto+Sans+KR" rel="stylesheet"/>
      <style>
       /* body start */
        body {
          font-family: 'Noto Sans KR', sans-serif;
          margin: 0;
        }
    
        /* navigation bar start */
        .nav-bar {
          position: fixed;
          width: 100%;
          padding-top: 10px;
          padding-bottom: 10px;
          background-color: #ffffff;
          box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.14);
          z-index: 1;
        }
    
        .nav-bar #tv-image {
          margin-left: 78px;
          margin-right: 15px;
          height: 36px;
          vertical-align: middle;
        }
    
        .nav-bar span {
          font-weight: bold;
          color: #4a4a4a;
        }
    
        /* date picker start */
        .date-pick {
          padding-top: 56px;
          height: 200px;
          background-color: #efefef;
          margin-left: auto;
          margin-right: auto;
          position: relative;
        }
    
        .date-pick .search-box {
          text-align: center;
          position: absolute;
          display: block;
          left: 50%;
          transform: translateX(-50%);
        }
    
        .date-pick .search-box p {
          text-align: left;
        }
    
        .date-pick .search-box select {
          padding: 4px;
        }
    
        .date-pick .search-box .search-btn {
          display: inline-block;
          margin-left: 20px;
          padding: 3px 28px 4px 28px;
          border-radius: 4px;
          background-color: #00a9dc;
          font-weight: 300;
          font-size: 13.333px;
          height: 27px;
          box-sizing: border-box;
          color: #ffffff;
        }
    
        /* main body start */
    
        .container {
          margin-left: auto;
          margin-right: auto;
        }
    
        .row.top-table {
          background-color: #00a9dc;
          color: #ffffff;
          padding-top: 20px;
          padding-bottom: 20px;
        }
    
        table {
          border-collapse: collapse;
          border-spacing: 2px;
          font-size: 16px;
        }
    
        td, th {
          display: table-cell;
          color: #4a4a4a;
        }
    
        .row .rank {
          padding-left: 25px;
        }
    
        .row .channel {
          padding-left: 58px;
        }
    
        .row .program {
          padding-left: 41px;
        }
    
        .row .percent {
          color: #00a9dc;
          padding-left: 100px;
        }
    
        .top-table.row * {
          color: #ffffff;
          font-weight: 300;
        }
    
        .top-table.row .rank {
          padding-left: 17px;
          padding-right: 17px;
        }
    
        .top-table.row .channel {
          padding-right: 58px;
        }
    
        .top-table.row .program {
          padding-right: 41px;
        }
    
        .top-table.row .percent {
          padding-right: 28px;
        }
    
        .header-row {
          min-width: 391px;
          display: inline-block;
          text-align: center;
        }
      </style>
     </head>
     <body>
      <script crossorigin="anonymous" integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4=" src="https://code.jquery.com/jquery-3.2.1.min.js">
      </script>
      <!-- NAVIGATION BAR -->
      <div class="nav-bar">
       <img id="tv-image" src="/images/nielsen/group.png"/>
       <span>
        TV Ranking.com
       </span>
      </div>
      <!-- DATE PICKER -->
      <div class="date-pick">
       <div style="height:55px;">
       </div>
       <div class="search-box">
        <p style="font-size: 16px;color:#4a4a4a;margin-bottom: 4px;">
         날짜 검색
        </p>
        <section class="header-row">
         <select class="getYear" name="year" style="padding-right: 32px">
          <option selected="selected">
           2010
          </option>
          <option>
           2011
          </option>
          <option>
           2012
          </option>
          <option>
           2013
          </option>
          <option>
           2014
          </option>
          <option>
           2015
          </option>
          <option>
           2016
          </option>
          <option>
           2017
          </option>
          <option>
           2018
          </option>
         </select>
         <select class="getMonth" name="month" style="padding-right: 32px">
          <option selected="selected">
           1
          </option>
          <option>
           2
          </option>
          <option>
           3
          </option>
          <option>
           4
          </option>
          <option>
           5
          </option>
          <option>
           6
          </option>
          <option>
           7
          </option>
          <option>
           8
          </option>
          <option>
           9
          </option>
          <option>
           10
          </option>
          <option>
           11
          </option>
          <option>
           12
          </option>
         </select>
         <select id="weekSelectBox">
          <option selected="selected" value="0">
           2009.12.28 ~ 2010.01.03
          </option>
          <option value="1">
           2010.01.04 ~ 2010.01.10
          </option>
          <option value="2">
           2010.01.11 ~ 2010.01.17
          </option>
          <option value="3">
           2010.01.18 ~ 2010.01.24
          </option>
          <option value="4">
           2010.01.25 ~ 2010.01.31
          </option>
         </select>
         <div class="search-btn">
          search
         </div>
        </section>
       </div>
      </div>
      <!-- MAIN BODY -->
      <div class="container">
       <div class="box">
        <p style="font-size:18px;color:#4a4a4a;text-align: center;margin-top:60px; margin-bottom:15px;">
         가구시청률 TOP 10
        </p>
        <p style="font-size:14px;color:#9b9b9b;text-align: center;margin-bottom:25px">
         (분석기준: National, 유료플랫폼 가입 기구,
          단위:%)
        </p>
        <table cellpadding="7" style="margin-left: auto;margin-right: auto;">
         <tr class="top-table row" height="64">
          <th class="rank">
           순위
          </th>
          <th class="channel">
           채널
          </th>
          <th class="program">
           프로그램
          </th>
          <th class="percent">
           시청률
          </th>
         </tr>
         <tr class="row">
          <td class="rank">
           1
          </td>
          <td class="channel">
           KBS2
          </td>
          <td class="program">
           주말연속극(수상한삼형제)
          </td>
          <td class="percent">
           33.4
          </td>
         </tr>
         <tr class="row">
          <td class="rank">
           2
          </td>
          <td class="channel">
           KBS1
          </td>
          <td class="program">
           일일연속극(다함께차차차)
          </td>
          <td class="percent">
           33.1
          </td>
         </tr>
         <tr class="row">
          <td class="rank">
           3
          </td>
          <td class="channel">
           KBS2
          </td>
          <td class="program">
           해피선데이
          </td>
          <td class="percent">
           27.1
          </td>
         </tr>
         <tr class="row">
          <td class="rank">
           4
          </td>
          <td class="channel">
           MBC
          </td>
          <td class="program">
           MBC연기대상2부
          </td>
          <td class="percent">
           24.4
          </td>
         </tr>
         <tr class="row">
          <td class="rank">
           5
          </td>
          <td class="channel">
           SBS
          </td>
          <td class="program">
           주말극장(천만번사랑해)
          </td>
          <td class="percent">
           24.2
          </td>
         </tr>
         <tr class="row">
          <td class="rank">
           6
          </td>
          <td class="channel">
           MBC
          </td>
          <td class="program">
           MBC방송연예대상2부
          </td>
          <td class="percent">
           24.0
          </td>
         </tr>
         <tr class="row">
          <td class="rank">
           7
          </td>
          <td class="channel">
           MBC
          </td>
          <td class="program">
           MBC방송연예대상1부
          </td>
          <td class="percent">
           22.4
          </td>
         </tr>
         <tr class="row">
          <td class="rank">
           8
          </td>
          <td class="channel">
           SBS
          </td>
          <td class="program">
           SBS연예대상2부
          </td>
          <td class="percent">
           21.1
          </td>
         </tr>
         <tr class="row">
          <td class="rank">
           9
          </td>
          <td class="channel">
           MBC
          </td>
          <td class="program">
           주말기획드라마(보석비빔밥)
          </td>
          <td class="percent">
           20.9
          </td>
         </tr>
         <tr class="row">
          <td class="rank">
           10
          </td>
          <td class="channel">
           MBC
          </td>
          <td class="program">
           일일시트콤(지붕뚫고하이킥)
          </td>
          <td class="percent">
           19.9
          </td>
         </tr>
        </table>
       </div>
      </div>
      <script>
       $(".getMonth, .getYear").on("change", function () {
        window.location.assign("/ratings/index?year=" + $(".getYear").val() + "&month=" + $(".getMonth").val() + "&weekIndex=0");
    
      });
      $(".search-btn").on("click", function () {
        var index = $("#weekSelectBox").val();
        window.location.assign("/ratings/index?year=" + $(".getYear").val() + "&month=" + $(".getMonth").val() + "&weekIndex=" + index);
      });
      </script>
     </body>
    </html>
    
    


```python
soup.select('title')
```




    [<title>티비랭킹닷컴</title>]



선택자를 써서 가져온다


```python
soup.select('table')
```




    [<table cellpadding="7" style="margin-left: auto;margin-right: auto;">
     <tr class="top-table row" height="64">
     <th class="rank">순위</th>
     <th class="channel">채널</th>
     <th class="program">프로그램</th>
     <th class="percent">시청률</th>
     </tr>
     <tr class="row">
     <td class="rank">1</td>
     <td class="channel">KBS2</td>
     <td class="program">주말연속극(수상한삼형제)</td>
     <td class="percent">33.4</td>
     </tr>
     <tr class="row">
     <td class="rank">2</td>
     <td class="channel">KBS1</td>
     <td class="program">일일연속극(다함께차차차)</td>
     <td class="percent">33.1</td>
     </tr>
     <tr class="row">
     <td class="rank">3</td>
     <td class="channel">KBS2</td>
     <td class="program">해피선데이</td>
     <td class="percent">27.1</td>
     </tr>
     <tr class="row">
     <td class="rank">4</td>
     <td class="channel">MBC</td>
     <td class="program">MBC연기대상2부</td>
     <td class="percent">24.4</td>
     </tr>
     <tr class="row">
     <td class="rank">5</td>
     <td class="channel">SBS</td>
     <td class="program">주말극장(천만번사랑해)</td>
     <td class="percent">24.2</td>
     </tr>
     <tr class="row">
     <td class="rank">6</td>
     <td class="channel">MBC</td>
     <td class="program">MBC방송연예대상2부</td>
     <td class="percent">24.0</td>
     </tr>
     <tr class="row">
     <td class="rank">7</td>
     <td class="channel">MBC</td>
     <td class="program">MBC방송연예대상1부</td>
     <td class="percent">22.4</td>
     </tr>
     <tr class="row">
     <td class="rank">8</td>
     <td class="channel">SBS</td>
     <td class="program">SBS연예대상2부</td>
     <td class="percent">21.1</td>
     </tr>
     <tr class="row">
     <td class="rank">9</td>
     <td class="channel">MBC</td>
     <td class="program">주말기획드라마(보석비빔밥)</td>
     <td class="percent">20.9</td>
     </tr>
     <tr class="row">
     <td class="rank">10</td>
     <td class="channel">MBC</td>
     <td class="program">일일시트콤(지붕뚫고하이킥)</td>
     <td class="percent">19.9</td>
     </tr>
     </table>]



td 이면서 class가 program인 걸 가져오자


```python
soup.select('td.program')
```




    [<td class="program">주말연속극(수상한삼형제)</td>,
     <td class="program">일일연속극(다함께차차차)</td>,
     <td class="program">해피선데이</td>,
     <td class="program">MBC연기대상2부</td>,
     <td class="program">주말극장(천만번사랑해)</td>,
     <td class="program">MBC방송연예대상2부</td>,
     <td class="program">MBC방송연예대상1부</td>,
     <td class="program">SBS연예대상2부</td>,
     <td class="program">주말기획드라마(보석비빔밥)</td>,
     <td class="program">일일시트콤(지붕뚫고하이킥)</td>]



리스트 요소에 get_text() 매소드를 써서 텍스트로 뽑을 수 있다


```python
titles = soup.select('td.program')
for tag in titles:
    print(tag.get_text())
```

    주말연속극(수상한삼형제)
    일일연속극(다함께차차차)
    해피선데이
    MBC연기대상2부
    주말극장(천만번사랑해)
    MBC방송연예대상2부
    MBC방송연예대상1부
    SBS연예대상2부
    주말기획드라마(보석비빔밥)
    일일시트콤(지붕뚫고하이킥)
    

가장 먼저 나오는 하나만 가져올 수도 있다


```python
soup.select_one('td.program')
```




    <td class="program">주말연속극(수상한삼형제)</td>




```python
response = requests.get("https://workey.codeit.kr/orangebottle/index")
rpage = response.text

soup = BeautifulSoup(rpage, 'html.parser')
print(soup.prettify())
```

    <!DOCTYPE html>
    <html>
     <head>
      <title>
       Orange bottle coffee
      </title>
      <meta charset="utf-8"/>
      <link href="https://fonts.googleapis.com/css?family=Noto+Sans+KR" rel="stylesheet"/>
      <style>
       body {
                font-family: 'Noto Sans KR', sans-serif;
                margin: 0;
                background-color: #ffffff;
            }
    
            /*navigation bar*/
            #bottle {
                margin-top: 12px;
                margin-bottom: 11px;
                margin-left: 79px;
                margin-right: 24px;
                vertical-align: middle;
                width: 13px;
            }
    
            #title {
                font-size: 14px;
                font-weight: bold;
                vertical-align: middle;
                color: #4a4a4a;
            }
    
            ul {
                display: inline;
                padding-left: 0;
            }
    
            li {
                float: right;
                list-style-type: none;
                font-size: 14px;
            }
    
            #subscribe {
                color: #f5a623;
                margin-right: 25px;
                line-height: 58px;
            }
    
            #signin {
                margin-right: 65px;
                line-height: 58px;
                color: #4a4a4a;
            }
    
            /*main image*/
            #mainimg {
                height: 533px;
                line-height: 533px;
                margin-bottom: 122px;
                background-image: url("/images/orangebottle/background.jpg");
                background-size: cover;
                background-position: center center;
                text-align: center;
            }
    
            #mainimg #maintext {
                line-height: normal;
                display: inline-block;
                vertical-align: middle;
                font-size: 25px;
                color: #ffffff;
            }
    
            /*branches*/
            .container {
                width: 1100px;
                margin-left: auto;
                margin-right: auto;
                overflow: hidden;
            }
    
            .container .branch {
                width: 25%;
                height: 164px;
                float: left;
                padding-left: 40px;
                padding-right: 40px;
                margin-top: 10px;
                margin-bottom: 80px;
                box-sizing: border-box;
            }
    
            .container .branch .city {
                display: inline-block;
                margin: 0;
                border-radius: 8px;
                padding: 5px 8px;
                font-size: 14px;
                color: white;
                background-color: #f5a623;
            }
    
            .container .branch .ave {
                margin: 12px 0;
                font-size: 16px;
                color: #f5a623;
            }
    
            .container .branch .address {
                margin: 12px 0;
                color: #4a4a4a;
                line-height: 1.6;
            }
    
            .container .branch img {
                vertical-align: middle;
                margin-right: 9px;
            }
    
            .container .branch .phoneNum {
                color: #818181;
            }
    
            /*signup*/
    
            #footer {
                width: 100%;
                height: 453px;
                background-color: #f9f9f9;
                float: left;
            }
    
            #footer h1 {
                margin-top: 75px;
                margin-bottom: 37px;
                font-size: 40px;
                font-weight: 300;
                text-align: center;
                color: #9b9b9b;
            }
    
            #footer h2 {
                font-size: 16px;
                text-align: center;
                color: #4a4a4a;
                margin-bottom: 58px;
            }
    
            #footer #signup {
                width: 646px;
                height: 70px;
                background-color: white;
                margin-left: auto;
                margin-right: auto;
            }
    
            #footer #signup input {
                border: none;
                font-size: 20px; /*원래는 16*/
                margin-top: 19px;
                margin-bottom: 27px;
                margin-left: 34px;
                color: #9b9b9b;
                width: 450px;
                height: 30px;
            }
    
            #footer #signup #submit {
                width: 130px;
                height: 70px;
                float: right;
                background-color: #f5a623;
                text-align: center;
                line-height: 70px;
            }
    
            #footer #signup a {
                text-decoration: none;
                color: #ffffff;
                font-size: 18px;
            }
      </style>
     </head>
     <body>
      <div id="navbar">
       <a href="#" style="text-decoration: none;color:#4a4a4a;">
        <img id="bottle" src="/images/orangebottle/logo.png"/>
        <span id="title">
         ORANGE BOTTLE COFFEE
        </span>
       </a>
       <ul>
        <a href="#" style="color:black;">
         <li id="signin">
          SIGN IN
         </li>
        </a>
        <a href="#">
         <li id="subscribe">
          SUBSCRIBE
         </li>
        </a>
       </ul>
      </div>
      <!-- main image -->
      <div id="mainimg">
       <div id="maintext">
        <h1>
         Find Your Orange Bottle Cafe
        </h1>
       </div>
      </div>
      <!-- cafe branches -->
      <div class="container">
       <div class="branch">
        <p class="city">
         San Jose
        </p>
        <p class="ave">
         Fairway
        </p>
        <p class="address">
         4823 Fairway Drive
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         707-514-0033
        </span>
       </div>
       <div class="branch">
        <p class="city">
         GREAT BARTON
        </p>
        <p class="ave">
         Lammas
        </p>
        <p class="address">
         106 Lammas Street
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         070 3460 5076
        </span>
       </div>
       <div class="branch">
        <p class="city">
         Hamilton
        </p>
        <p class="ave">
         Bridgeport
        </p>
        <p class="address">
         3791  Bridgeport Rd
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         905-389-4463
        </span>
       </div>
       <div class="branch">
        <p class="city">
         JERRAWA
        </p>
        <p class="ave">
         Marlin
        </p>
        <p class="address">
         40 Marlin Avenue
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         (02) 6175 8642
        </span>
       </div>
       <div class="branch">
        <p class="city">
         Rudersberg
        </p>
        <p class="ave">
         Pasewalker
        </p>
        <p class="address">
         Pasewalker Straße 5
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         07183 30 07 96
        </span>
       </div>
       <div class="branch">
        <p class="city">
         København K
        </p>
        <p class="ave">
         Toftvej
        </p>
        <p class="address">
         Toftvej 35
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         21-90-47700
        </span>
       </div>
       <div class="branch">
        <p class="city">
         Guadalajara
        </p>
        <p class="ave">
         Revolucion
        </p>
        <p class="address">
         Av. Revolucion 737
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         33 36175334
        </span>
       </div>
       <div class="branch">
        <p class="city">
         Poughkeepsie
        </p>
        <p class="ave">
         Old Dear Lane
        </p>
        <p class="address">
         4927 Old Dear Lane
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         845-857-0825
        </span>
       </div>
       <div class="branch">
        <p class="city">
         Elgin
        </p>
        <p class="ave">
         Pineview
        </p>
        <p class="address">
         2491 Pineview Drive
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         507-876-0713
        </span>
       </div>
       <div class="branch">
        <p class="city">
         Oak Brook
        </p>
        <p class="ave">
         Vesta
        </p>
        <p class="address">
         2591 Vesta Drive
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         773-757-1932
        </span>
       </div>
       <div class="branch">
        <p class="city">
         Annapolis Junction
        </p>
        <p class="ave">
         Bluff
        </p>
        <p class="address">
         889 Bluff Street
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         301-787-8206
        </span>
       </div>
       <div class="branch">
        <p class="city">
         Los Angeles
        </p>
        <p class="ave">
         Jett
        </p>
        <p class="address">
         1014 Jett Lane
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         310-718-6212
        </span>
       </div>
       <div class="branch">
        <p class="city">
         Arlington
        </p>
        <p class="ave">
         Single
        </p>
        <p class="address">
         3158 Single Street
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         781-646-1715
        </span>
       </div>
       <div class="branch">
        <p class="city">
         Syracuse
        </p>
        <p class="ave">
         Plainfield
        </p>
        <p class="address">
         3741 Plainfield Avenue
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         315-576-8242
        </span>
       </div>
       <div class="branch">
        <p class="city">
         San Mateo
        </p>
        <p class="ave">
         Thunder
        </p>
        <p class="address">
         2425 Thunder Road
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         650-577-7537
        </span>
       </div>
       <div class="branch">
        <p class="city">
         Valdosta
        </p>
        <p class="ave">
         Junkins
        </p>
        <p class="address">
         1022 Junkins Avenue
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         229-460-4970
        </span>
       </div>
       <div class="branch">
        <p class="city">
         Hialeah
        </p>
        <p class="ave">
         Poplar
        </p>
        <p class="address">
         101 Poplar Lane
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         305-540-4990
        </span>
       </div>
       <div class="branch">
        <p class="city">
         Lexington
        </p>
        <p class="ave">
         Straford
        </p>
        <p class="address">
         793 Straford Park
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         606-614-9190
        </span>
       </div>
       <div class="branch">
        <p class="city">
         Johnsonburg
        </p>
        <p class="ave">
         Custer
        </p>
        <p class="address">
         2566 Custer Street
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         814-965-6502
        </span>
       </div>
       <div class="branch">
        <p class="city">
         Hokkaido
        </p>
        <p class="ave">
         Kita
        </p>
        <p class="address">
         244-1192, Kita 6-jonishi, Abashiri-shi, Hokkaido
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         8134-191-6900
        </span>
       </div>
       <div class="branch">
        <p class="city">
         Port Chester
        </p>
        <p class="ave">
         Ward
        </p>
        <p class="address">
         1503 Ward Road
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         914-933-3946
        </span>
       </div>
       <div class="branch">
        <p class="city">
         Salt Lake City
        </p>
        <p class="ave">
         Kemper
        </p>
        <p class="address">
         4745 Kemper Lane
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         801-927-7191
        </span>
       </div>
       <div class="branch">
        <p class="city">
         Villaluenga del Rosario
        </p>
        <p class="ave">
         Vientos
        </p>
        <p class="address">
         C/ Rosa de los Vientos 36
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         736 301 706
        </span>
       </div>
       <div class="branch">
        <p class="city">
         London
        </p>
        <p class="ave">
         King Street
        </p>
        <p class="address">
         733 King Street EAST CENTRAL LONDON EC86 0YR
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         916-863-6154
        </span>
       </div>
       <div class="branch">
        <p class="city">
         GLOUCESTER
        </p>
        <p class="ave">
         New Road
        </p>
        <p class="address">
         8857 New Road GLOUCESTER GL79 3CZ
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         252-218-2526
        </span>
       </div>
       <div class="branch">
        <p class="city">
         NEWPORT
        </p>
        <p class="ave">
         George
        </p>
        <p class="address">
         760 George Street NEWPORT NP73 0CH
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         803-535-5627
        </span>
       </div>
       <div class="branch">
        <p class="city">
         TAUNTON
        </p>
        <p class="ave">
         The Green
        </p>
        <p class="address">
         749 The Green TAUNTON TA27 9JQ
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         580-730-2253
        </span>
       </div>
       <div class="branch">
        <p class="city">
         SOUTHEND-ON-SEA
        </p>
        <p class="ave">
         Springfield
        </p>
        <p class="address">
         271 Springfield Road SOUTHEND-ON-SEA SS98 1PA
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         240-597-0099
        </span>
       </div>
       <div class="branch">
        <p class="city">
         SHEFFIELD
        </p>
        <p class="ave">
         Highfield
        </p>
        <p class="address">
         500 Highfield Road SHEFFIELD S98 6VM
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         210-727-9560
        </span>
       </div>
       <div class="branch">
        <p class="city">
         HULL
        </p>
        <p class="ave">
         Albert
        </p>
        <p class="address">
         8772 Albert Road HULL HU2 6SN
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         919-887-6912
        </span>
       </div>
       <div class="branch">
        <p class="city">
         SHREWSBURY
        </p>
        <p class="ave">
         Church
        </p>
        <p class="address">
         38 Church Street SHREWSBURY SY79 9TY
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         614-449-8617
        </span>
       </div>
       <div class="branch">
        <p class="city">
         DURHAM
        </p>
        <p class="ave">
         DURHAM
        </p>
        <p class="address">
         12 New Road DURHAM DH78 4XK
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         830-229-4983
        </span>
       </div>
       <div class="branch">
        <p class="city">
         Honolulu
        </p>
        <p class="ave">
         Don Jackson
        </p>
        <p class="address">
         4153 Don Jackson Lane
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         303-284-0638
        </span>
       </div>
       <div class="branch">
        <p class="city">
         Wayne
        </p>
        <p class="ave">
         Bombardier
        </p>
        <p class="address">
         2438 Bombardier Way
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         734-981-4470
        </span>
       </div>
       <div class="branch">
        <p class="city">
         Milton
        </p>
        <p class="ave">
         Courtright
        </p>
        <p class="address">
         3258 Courtright Street
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         701-496-3125
        </span>
       </div>
       <div class="branch">
        <p class="city">
         NEWCASTLE
        </p>
        <p class="ave">
         The Grove
        </p>
        <p class="address">
         9982 The Grove NEWCASTLE UPON TYNE NE21 0RM
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         605-677-5038
        </span>
       </div>
       <div class="branch">
        <p class="city">
         BRISTOL
        </p>
        <p class="ave">
         Richmond
        </p>
        <p class="address">
         8253 Richmond Road BRISTOL BS70 9LU
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         209-848-9572
        </span>
       </div>
       <div class="branch">
        <p class="city">
         BOURNEMOUTH
        </p>
        <p class="ave">
         Broadway
        </p>
        <p class="address">
         22 Broadway BOURNEMOUTH BH73 8ON
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         760-464-6831
        </span>
       </div>
       <div class="branch">
        <p class="city">
         LEICESTER
        </p>
        <p class="ave">
         Green Lane
        </p>
        <p class="address">
         748 Green Lane LEICESTER LE77 6VE
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         508-272-0114
        </span>
       </div>
       <div class="branch">
        <p class="city">
         SUNDERLAND
        </p>
        <p class="ave">
         New Road
        </p>
        <p class="address">
         48 New Road SUNDERLAND SR39 2NY
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         845-915-5076
        </span>
       </div>
       <div class="branch">
        <p class="city">
         BOLTON
        </p>
        <p class="ave">
         North Street
        </p>
        <p class="address">
         19 North Street BOLTON BL77 4TC
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         973-640-3581
        </span>
       </div>
       <div class="branch">
        <p class="city">
         SOUTHAMPTON
        </p>
        <p class="ave">
         King Street
        </p>
        <p class="address">
         60 King Street SOUTHAMPTON SO75 5PZ
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         541-579-1559
        </span>
       </div>
       <div class="branch">
        <p class="city">
         BLACKPOOL
        </p>
        <p class="ave">
         Highfield
        </p>
        <p class="address">
         8579 Highfield Road BLACKPOOL FY68 1LM
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         336-212-0408
        </span>
       </div>
       <div class="branch">
        <p class="city">
         DARLINGTON
        </p>
        <p class="ave">
         High Street
        </p>
        <p class="address">
         9175 High Street DARLINGTON DL86 7BQ
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         845-340-3808
        </span>
       </div>
       <div class="branch">
        <p class="city">
         LIVERPOOL
        </p>
        <p class="ave">
         Main Road
        </p>
        <p class="address">
         100 Main Road LIVERPOOL L80 4XI
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         561-526-2625
        </span>
       </div>
       <div class="branch">
        <p class="city">
         MANCHESTER
        </p>
        <p class="ave">
         Park Lane
        </p>
        <p class="address">
         52 Park Lane MANCHESTER M8 0KJ
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         801-608-1332
        </span>
       </div>
       <div class="branch">
        <p class="city">
         SHEFFIELD
        </p>
        <p class="ave">
         Kings Road
        </p>
        <p class="address">
         79 Kings Road SHEFFIELD S88 2KY
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         510-214-0266
        </span>
       </div>
       <div class="branch">
        <p class="city">
         BOLTON
        </p>
        <p class="ave">
         Mill
        </p>
        <p class="address">
         95 Mill Road BOLTON BL48 9OR
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         785-253-0084
        </span>
       </div>
       <div class="branch">
        <p class="city">
         SWANSEA
        </p>
        <p class="ave">
         South
        </p>
        <p class="address">
         466 South Street SWANSEA SA34 7PT
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         585-749-2163
        </span>
       </div>
       <div class="branch">
        <p class="city">
         LEEDS
        </p>
        <p class="ave">
         Mill Lane
        </p>
        <p class="address">
         308 Mill Lane LEEDS LS35 5JS
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         312-362-2484
        </span>
       </div>
       <div class="branch">
        <p class="city">
         SWANSEA
        </p>
        <p class="ave">
         York Road
        </p>
        <p class="address">
         222 York Road SWANSEA SA87 4WS
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         570-603-5788
        </span>
       </div>
       <div class="branch">
        <p class="city">
         CARDIFF
        </p>
        <p class="ave">
         West Street
        </p>
        <p class="address">
         125 West Street CARDIFF CF95 6CN
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         802-738-8477
        </span>
       </div>
       <div class="branch">
        <p class="city">
         LEICESTER
        </p>
        <p class="ave">
         New Road
        </p>
        <p class="address">
         64 New Road LEICESTER LE37 3VW
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         507-771-8684
        </span>
       </div>
       <div class="branch">
        <p class="city">
         SOUTHAMPTON
        </p>
        <p class="ave">
         Main Street
        </p>
        <p class="address">
         90 Main Street SOUTHAMPTON SO41 5RP
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         720-634-0176
        </span>
       </div>
       <div class="branch">
        <p class="city">
         IPSWICH
        </p>
        <p class="ave">
         Stanley Road
        </p>
        <p class="address">
         8339 Stanley Road IPSWICH IP79 6SN
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         313-930-0331
        </span>
       </div>
       <div class="branch">
        <p class="city">
         Tokyo
        </p>
        <p class="ave">
         Ebisu
        </p>
        <p class="address">
         481-1228, Ebisu Ebisugadempureisu(28-kai), Shibuya-ku
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         8188-165-7118
        </span>
       </div>
       <div class="branch">
        <p class="city">
         Seoul
        </p>
        <p class="ave">
         Gongdeok
        </p>
        <p class="address">
         310-5, Samseongraemiangongdeok 3 chaapateu, Gongdeok-dong, Mapo-gu
        </p>
        <img src="/images/orangebottle/phone_icon.png" width="20px"/>
        <span class="phoneNum">
         02-455-1973
        </span>
       </div>
      </div>
      <!-- signup -->
      <div id="footer">
       <h1>
        SIGN UP
       </h1>
       <h2>
        Sign up for stories, coffee tips, and brewing equipment
       </h2>
       <div id="signup">
        <input placeholder="Your email here" type="text"/>
        <a href="#" id="submit">
         SIGN UP
        </a>
       </div>
      </div>
     </body>
    </html>
    
    


```python
phn = []
numbers = soup.select('.phoneNum')
for number in numbers:
    phn.append(number.get_text())
```


```python
phn
```




    ['707-514-0033',
     '070 3460 5076',
     '905-389-4463',
     '(02) 6175 8642',
     '07183 30 07 96',
     '21-90-47700',
     '33 36175334',
     '845-857-0825',
     '507-876-0713',
     '773-757-1932',
     '301-787-8206',
     '310-718-6212',
     '781-646-1715',
     '315-576-8242',
     '650-577-7537',
     '229-460-4970',
     '305-540-4990',
     '606-614-9190',
     '814-965-6502',
     '8134-191-6900',
     '914-933-3946',
     '801-927-7191',
     '736 301 706',
     '916-863-6154',
     '252-218-2526',
     '803-535-5627',
     '580-730-2253',
     '240-597-0099',
     '210-727-9560',
     '919-887-6912',
     '614-449-8617',
     '830-229-4983',
     '303-284-0638',
     '734-981-4470',
     '701-496-3125',
     '605-677-5038',
     '209-848-9572',
     '760-464-6831',
     '508-272-0114',
     '845-915-5076',
     '973-640-3581',
     '541-579-1559',
     '336-212-0408',
     '845-340-3808',
     '561-526-2625',
     '801-608-1332',
     '510-214-0266',
     '785-253-0084',
     '585-749-2163',
     '312-362-2484',
     '570-603-5788',
     '802-738-8477',
     '507-771-8684',
     '720-634-0176',
     '313-930-0331',
     '8188-165-7118',
     '02-455-1973']




```python
response = requests.get("https://workey.codeit.kr/ratings/index")
rpage = response.text

soup = BeautifulSoup(rpage, 'html.parser')
tags = soup.select('td')[:4]

for tag in tags:
    print(tag.get_text())
```

    1
    KBS2
    주말연속극(수상한삼형제)
    33.4
    


```python
tr_1 = soup.select('tr')[1]
td_1 = tr_1.select('td')
for tag in td_1:
    print(tag.get_text())
```

    1
    KBS2
    주말연속극(수상한삼형제)
    33.4
    


```python
response = requests.get("https://workey.codeit.kr/orangebottle/index")
rpage = response.text

soup = BeautifulSoup(rpage, 'html.parser')
soup.prettify()
```




    '<!DOCTYPE html>\n<html>\n <head>\n  <title>\n   Orange bottle coffee\n  </title>\n  <meta charset="utf-8"/>\n  <link href="https://fonts.googleapis.com/css?family=Noto+Sans+KR" rel="stylesheet"/>\n  <style>\n   body {\n            font-family: \'Noto Sans KR\', sans-serif;\n            margin: 0;\n            background-color: #ffffff;\n        }\n\n        /*navigation bar*/\n        #bottle {\n            margin-top: 12px;\n            margin-bottom: 11px;\n            margin-left: 79px;\n            margin-right: 24px;\n            vertical-align: middle;\n            width: 13px;\n        }\n\n        #title {\n            font-size: 14px;\n            font-weight: bold;\n            vertical-align: middle;\n            color: #4a4a4a;\n        }\n\n        ul {\n            display: inline;\n            padding-left: 0;\n        }\n\n        li {\n            float: right;\n            list-style-type: none;\n            font-size: 14px;\n        }\n\n        #subscribe {\n            color: #f5a623;\n            margin-right: 25px;\n            line-height: 58px;\n        }\n\n        #signin {\n            margin-right: 65px;\n            line-height: 58px;\n            color: #4a4a4a;\n        }\n\n        /*main image*/\n        #mainimg {\n            height: 533px;\n            line-height: 533px;\n            margin-bottom: 122px;\n            background-image: url("/images/orangebottle/background.jpg");\n            background-size: cover;\n            background-position: center center;\n            text-align: center;\n        }\n\n        #mainimg #maintext {\n            line-height: normal;\n            display: inline-block;\n            vertical-align: middle;\n            font-size: 25px;\n            color: #ffffff;\n        }\n\n        /*branches*/\n        .container {\n            width: 1100px;\n            margin-left: auto;\n            margin-right: auto;\n            overflow: hidden;\n        }\n\n        .container .branch {\n            width: 25%;\n            height: 164px;\n            float: left;\n            padding-left: 40px;\n            padding-right: 40px;\n            margin-top: 10px;\n            margin-bottom: 80px;\n            box-sizing: border-box;\n        }\n\n        .container .branch .city {\n            display: inline-block;\n            margin: 0;\n            border-radius: 8px;\n            padding: 5px 8px;\n            font-size: 14px;\n            color: white;\n            background-color: #f5a623;\n        }\n\n        .container .branch .ave {\n            margin: 12px 0;\n            font-size: 16px;\n            color: #f5a623;\n        }\n\n        .container .branch .address {\n            margin: 12px 0;\n            color: #4a4a4a;\n            line-height: 1.6;\n        }\n\n        .container .branch img {\n            vertical-align: middle;\n            margin-right: 9px;\n        }\n\n        .container .branch .phoneNum {\n            color: #818181;\n        }\n\n        /*signup*/\n\n        #footer {\n            width: 100%;\n            height: 453px;\n            background-color: #f9f9f9;\n            float: left;\n        }\n\n        #footer h1 {\n            margin-top: 75px;\n            margin-bottom: 37px;\n            font-size: 40px;\n            font-weight: 300;\n            text-align: center;\n            color: #9b9b9b;\n        }\n\n        #footer h2 {\n            font-size: 16px;\n            text-align: center;\n            color: #4a4a4a;\n            margin-bottom: 58px;\n        }\n\n        #footer #signup {\n            width: 646px;\n            height: 70px;\n            background-color: white;\n            margin-left: auto;\n            margin-right: auto;\n        }\n\n        #footer #signup input {\n            border: none;\n            font-size: 20px; /*원래는 16*/\n            margin-top: 19px;\n            margin-bottom: 27px;\n            margin-left: 34px;\n            color: #9b9b9b;\n            width: 450px;\n            height: 30px;\n        }\n\n        #footer #signup #submit {\n            width: 130px;\n            height: 70px;\n            float: right;\n            background-color: #f5a623;\n            text-align: center;\n            line-height: 70px;\n        }\n\n        #footer #signup a {\n            text-decoration: none;\n            color: #ffffff;\n            font-size: 18px;\n        }\n  </style>\n </head>\n <body>\n  <div id="navbar">\n   <a href="#" style="text-decoration: none;color:#4a4a4a;">\n    <img id="bottle" src="/images/orangebottle/logo.png"/>\n    <span id="title">\n     ORANGE BOTTLE COFFEE\n    </span>\n   </a>\n   <ul>\n    <a href="#" style="color:black;">\n     <li id="signin">\n      SIGN IN\n     </li>\n    </a>\n    <a href="#">\n     <li id="subscribe">\n      SUBSCRIBE\n     </li>\n    </a>\n   </ul>\n  </div>\n  <!-- main image -->\n  <div id="mainimg">\n   <div id="maintext">\n    <h1>\n     Find Your Orange Bottle Cafe\n    </h1>\n   </div>\n  </div>\n  <!-- cafe branches -->\n  <div class="container">\n   <div class="branch">\n    <p class="city">\n     San Jose\n    </p>\n    <p class="ave">\n     Fairway\n    </p>\n    <p class="address">\n     4823 Fairway Drive\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     707-514-0033\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     GREAT BARTON\n    </p>\n    <p class="ave">\n     Lammas\n    </p>\n    <p class="address">\n     106 Lammas Street\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     070 3460 5076\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Hamilton\n    </p>\n    <p class="ave">\n     Bridgeport\n    </p>\n    <p class="address">\n     3791  Bridgeport Rd\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     905-389-4463\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     JERRAWA\n    </p>\n    <p class="ave">\n     Marlin\n    </p>\n    <p class="address">\n     40 Marlin Avenue\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     (02) 6175 8642\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Rudersberg\n    </p>\n    <p class="ave">\n     Pasewalker\n    </p>\n    <p class="address">\n     Pasewalker Straße 5\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     07183 30 07 96\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     København K\n    </p>\n    <p class="ave">\n     Toftvej\n    </p>\n    <p class="address">\n     Toftvej 35\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     21-90-47700\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Guadalajara\n    </p>\n    <p class="ave">\n     Revolucion\n    </p>\n    <p class="address">\n     Av. Revolucion 737\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     33 36175334\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Poughkeepsie\n    </p>\n    <p class="ave">\n     Old Dear Lane\n    </p>\n    <p class="address">\n     4927 Old Dear Lane\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     845-857-0825\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Elgin\n    </p>\n    <p class="ave">\n     Pineview\n    </p>\n    <p class="address">\n     2491 Pineview Drive\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     507-876-0713\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Oak Brook\n    </p>\n    <p class="ave">\n     Vesta\n    </p>\n    <p class="address">\n     2591 Vesta Drive\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     773-757-1932\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Annapolis Junction\n    </p>\n    <p class="ave">\n     Bluff\n    </p>\n    <p class="address">\n     889 Bluff Street\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     301-787-8206\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Los Angeles\n    </p>\n    <p class="ave">\n     Jett\n    </p>\n    <p class="address">\n     1014 Jett Lane\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     310-718-6212\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Arlington\n    </p>\n    <p class="ave">\n     Single\n    </p>\n    <p class="address">\n     3158 Single Street\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     781-646-1715\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Syracuse\n    </p>\n    <p class="ave">\n     Plainfield\n    </p>\n    <p class="address">\n     3741 Plainfield Avenue\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     315-576-8242\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     San Mateo\n    </p>\n    <p class="ave">\n     Thunder\n    </p>\n    <p class="address">\n     2425 Thunder Road\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     650-577-7537\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Valdosta\n    </p>\n    <p class="ave">\n     Junkins\n    </p>\n    <p class="address">\n     1022 Junkins Avenue\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     229-460-4970\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Hialeah\n    </p>\n    <p class="ave">\n     Poplar\n    </p>\n    <p class="address">\n     101 Poplar Lane\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     305-540-4990\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Lexington\n    </p>\n    <p class="ave">\n     Straford\n    </p>\n    <p class="address">\n     793 Straford Park\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     606-614-9190\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Johnsonburg\n    </p>\n    <p class="ave">\n     Custer\n    </p>\n    <p class="address">\n     2566 Custer Street\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     814-965-6502\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Hokkaido\n    </p>\n    <p class="ave">\n     Kita\n    </p>\n    <p class="address">\n     244-1192, Kita 6-jonishi, Abashiri-shi, Hokkaido\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     8134-191-6900\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Port Chester\n    </p>\n    <p class="ave">\n     Ward\n    </p>\n    <p class="address">\n     1503 Ward Road\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     914-933-3946\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Salt Lake City\n    </p>\n    <p class="ave">\n     Kemper\n    </p>\n    <p class="address">\n     4745 Kemper Lane\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     801-927-7191\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Villaluenga del Rosario\n    </p>\n    <p class="ave">\n     Vientos\n    </p>\n    <p class="address">\n     C/ Rosa de los Vientos 36\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     736 301 706\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     London\n    </p>\n    <p class="ave">\n     King Street\n    </p>\n    <p class="address">\n     733 King Street EAST CENTRAL LONDON EC86 0YR\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     916-863-6154\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     GLOUCESTER\n    </p>\n    <p class="ave">\n     New Road\n    </p>\n    <p class="address">\n     8857 New Road GLOUCESTER GL79 3CZ\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     252-218-2526\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     NEWPORT\n    </p>\n    <p class="ave">\n     George\n    </p>\n    <p class="address">\n     760 George Street NEWPORT NP73 0CH\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     803-535-5627\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     TAUNTON\n    </p>\n    <p class="ave">\n     The Green\n    </p>\n    <p class="address">\n     749 The Green TAUNTON TA27 9JQ\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     580-730-2253\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     SOUTHEND-ON-SEA\n    </p>\n    <p class="ave">\n     Springfield\n    </p>\n    <p class="address">\n     271 Springfield Road SOUTHEND-ON-SEA SS98 1PA\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     240-597-0099\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     SHEFFIELD\n    </p>\n    <p class="ave">\n     Highfield\n    </p>\n    <p class="address">\n     500 Highfield Road SHEFFIELD S98 6VM\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     210-727-9560\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     HULL\n    </p>\n    <p class="ave">\n     Albert\n    </p>\n    <p class="address">\n     8772 Albert Road HULL HU2 6SN\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     919-887-6912\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     SHREWSBURY\n    </p>\n    <p class="ave">\n     Church\n    </p>\n    <p class="address">\n     38 Church Street SHREWSBURY SY79 9TY\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     614-449-8617\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     DURHAM\n    </p>\n    <p class="ave">\n     DURHAM\n    </p>\n    <p class="address">\n     12 New Road DURHAM DH78 4XK\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     830-229-4983\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Honolulu\n    </p>\n    <p class="ave">\n     Don Jackson\n    </p>\n    <p class="address">\n     4153 Don Jackson Lane\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     303-284-0638\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Wayne\n    </p>\n    <p class="ave">\n     Bombardier\n    </p>\n    <p class="address">\n     2438 Bombardier Way\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     734-981-4470\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Milton\n    </p>\n    <p class="ave">\n     Courtright\n    </p>\n    <p class="address">\n     3258 Courtright Street\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     701-496-3125\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     NEWCASTLE\n    </p>\n    <p class="ave">\n     The Grove\n    </p>\n    <p class="address">\n     9982 The Grove NEWCASTLE UPON TYNE NE21 0RM\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     605-677-5038\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     BRISTOL\n    </p>\n    <p class="ave">\n     Richmond\n    </p>\n    <p class="address">\n     8253 Richmond Road BRISTOL BS70 9LU\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     209-848-9572\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     BOURNEMOUTH\n    </p>\n    <p class="ave">\n     Broadway\n    </p>\n    <p class="address">\n     22 Broadway BOURNEMOUTH BH73 8ON\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     760-464-6831\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     LEICESTER\n    </p>\n    <p class="ave">\n     Green Lane\n    </p>\n    <p class="address">\n     748 Green Lane LEICESTER LE77 6VE\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     508-272-0114\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     SUNDERLAND\n    </p>\n    <p class="ave">\n     New Road\n    </p>\n    <p class="address">\n     48 New Road SUNDERLAND SR39 2NY\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     845-915-5076\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     BOLTON\n    </p>\n    <p class="ave">\n     North Street\n    </p>\n    <p class="address">\n     19 North Street BOLTON BL77 4TC\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     973-640-3581\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     SOUTHAMPTON\n    </p>\n    <p class="ave">\n     King Street\n    </p>\n    <p class="address">\n     60 King Street SOUTHAMPTON SO75 5PZ\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     541-579-1559\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     BLACKPOOL\n    </p>\n    <p class="ave">\n     Highfield\n    </p>\n    <p class="address">\n     8579 Highfield Road BLACKPOOL FY68 1LM\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     336-212-0408\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     DARLINGTON\n    </p>\n    <p class="ave">\n     High Street\n    </p>\n    <p class="address">\n     9175 High Street DARLINGTON DL86 7BQ\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     845-340-3808\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     LIVERPOOL\n    </p>\n    <p class="ave">\n     Main Road\n    </p>\n    <p class="address">\n     100 Main Road LIVERPOOL L80 4XI\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     561-526-2625\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     MANCHESTER\n    </p>\n    <p class="ave">\n     Park Lane\n    </p>\n    <p class="address">\n     52 Park Lane MANCHESTER M8 0KJ\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     801-608-1332\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     SHEFFIELD\n    </p>\n    <p class="ave">\n     Kings Road\n    </p>\n    <p class="address">\n     79 Kings Road SHEFFIELD S88 2KY\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     510-214-0266\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     BOLTON\n    </p>\n    <p class="ave">\n     Mill\n    </p>\n    <p class="address">\n     95 Mill Road BOLTON BL48 9OR\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     785-253-0084\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     SWANSEA\n    </p>\n    <p class="ave">\n     South\n    </p>\n    <p class="address">\n     466 South Street SWANSEA SA34 7PT\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     585-749-2163\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     LEEDS\n    </p>\n    <p class="ave">\n     Mill Lane\n    </p>\n    <p class="address">\n     308 Mill Lane LEEDS LS35 5JS\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     312-362-2484\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     SWANSEA\n    </p>\n    <p class="ave">\n     York Road\n    </p>\n    <p class="address">\n     222 York Road SWANSEA SA87 4WS\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     570-603-5788\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     CARDIFF\n    </p>\n    <p class="ave">\n     West Street\n    </p>\n    <p class="address">\n     125 West Street CARDIFF CF95 6CN\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     802-738-8477\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     LEICESTER\n    </p>\n    <p class="ave">\n     New Road\n    </p>\n    <p class="address">\n     64 New Road LEICESTER LE37 3VW\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     507-771-8684\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     SOUTHAMPTON\n    </p>\n    <p class="ave">\n     Main Street\n    </p>\n    <p class="address">\n     90 Main Street SOUTHAMPTON SO41 5RP\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     720-634-0176\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     IPSWICH\n    </p>\n    <p class="ave">\n     Stanley Road\n    </p>\n    <p class="address">\n     8339 Stanley Road IPSWICH IP79 6SN\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     313-930-0331\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Tokyo\n    </p>\n    <p class="ave">\n     Ebisu\n    </p>\n    <p class="address">\n     481-1228, Ebisu Ebisugadempureisu(28-kai), Shibuya-ku\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     8188-165-7118\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Seoul\n    </p>\n    <p class="ave">\n     Gongdeok\n    </p>\n    <p class="address">\n     310-5, Samseongraemiangongdeok 3 chaapateu, Gongdeok-dong, Mapo-gu\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     02-455-1973\n    </span>\n   </div>\n  </div>\n  <!-- signup -->\n  <div id="footer">\n   <h1>\n    SIGN UP\n   </h1>\n   <h2>\n    Sign up for stories, coffee tips, and brewing equipment\n   </h2>\n   <div id="signup">\n    <input placeholder="Your email here" type="text"/>\n    <a href="#" id="submit">\n     SIGN UP\n    </a>\n   </div>\n  </div>\n </body>\n</html>\n'




```python
print(soup.select('.branch')[0])
print(soup.select('.branch .city')[0])
print(soup.select('.branch .address')[0])
print(soup.select('.branch .phoneNum')[0])
```

    <div class="branch">
    <p class="city">San Jose</p>
    <p class="ave">Fairway</p>
    <p class="address">4823 Fairway Drive</p>
    <img src="/images/orangebottle/phone_icon.png" width="20px"/>
    <span class="phoneNum">707-514-0033</span>
    </div>
    <p class="city">San Jose</p>
    <p class="address">4823 Fairway Drive</p>
    <span class="phoneNum">707-514-0033</span>
    

- 아래 처럼 하면 strip()을 했는데도 \n 같은 게 묻어 나온다


```python
branch = soup.select('.branch')
st = []
for tag in branch:
    st.append(tag.get_text().strip())
st
```




    ['San Jose\nFairway\n4823 Fairway Drive\n\n707-514-0033',
     'GREAT BARTON\nLammas\n106 Lammas Street\n\n070 3460 5076',
     'Hamilton\nBridgeport\n3791  Bridgeport Rd\n\n905-389-4463',
     'JERRAWA\nMarlin\n40 Marlin Avenue\n\n(02) 6175 8642',
     'Rudersberg\nPasewalker\nPasewalker Straße 5\n\n07183 30 07 96',
     'København K\nToftvej\nToftvej 35\n\n21-90-47700',
     'Guadalajara\nRevolucion\nAv. Revolucion 737\n\n33 36175334',
     'Poughkeepsie\nOld Dear Lane\n4927 Old Dear Lane\n\n845-857-0825',
     'Elgin\nPineview\n2491 Pineview Drive\n\n507-876-0713',
     'Oak Brook\nVesta\n2591 Vesta Drive\n\n773-757-1932',
     'Annapolis Junction\nBluff\n889 Bluff Street\n\n301-787-8206',
     'Los Angeles\nJett\n1014 Jett Lane\n\n310-718-6212',
     'Arlington\nSingle\n3158 Single Street\n\n781-646-1715',
     'Syracuse\nPlainfield\n3741 Plainfield Avenue\n\n315-576-8242',
     'San Mateo\nThunder\n2425 Thunder Road\n\n650-577-7537',
     'Valdosta\nJunkins\n1022 Junkins Avenue\n\n229-460-4970',
     'Hialeah\nPoplar\n101 Poplar Lane\n\n305-540-4990',
     'Lexington\nStraford\n793 Straford Park\n\n606-614-9190',
     'Johnsonburg\nCuster\n2566 Custer Street\n\n814-965-6502',
     'Hokkaido\nKita\n244-1192, Kita 6-jonishi, Abashiri-shi, Hokkaido\n\n8134-191-6900',
     'Port Chester\nWard\n1503 Ward Road\n\n914-933-3946',
     'Salt Lake City\nKemper\n4745 Kemper Lane\n\n801-927-7191',
     'Villaluenga del Rosario\nVientos\nC/ Rosa de los Vientos 36\n\n736 301 706',
     'London\nKing Street\n733 King Street EAST CENTRAL LONDON EC86 0YR\n\n916-863-6154',
     'GLOUCESTER\nNew Road\n8857 New Road GLOUCESTER GL79 3CZ\n\n252-218-2526',
     'NEWPORT\nGeorge\n760 George Street NEWPORT NP73 0CH\n\n803-535-5627',
     'TAUNTON\nThe Green\n749 The Green TAUNTON TA27 9JQ\n\n580-730-2253',
     'SOUTHEND-ON-SEA\nSpringfield\n271 Springfield Road SOUTHEND-ON-SEA SS98 1PA\n\n240-597-0099',
     'SHEFFIELD\nHighfield\n500 Highfield Road SHEFFIELD S98 6VM\n\n210-727-9560',
     'HULL\nAlbert\n8772 Albert Road HULL HU2 6SN\n\n919-887-6912',
     'SHREWSBURY\nChurch\n38 Church Street SHREWSBURY SY79 9TY\n\n614-449-8617',
     'DURHAM\nDURHAM\n12 New Road DURHAM DH78 4XK\n\n830-229-4983',
     'Honolulu\nDon Jackson\n4153 Don Jackson Lane\n\n303-284-0638',
     'Wayne\nBombardier\n2438 Bombardier Way\n\n734-981-4470',
     'Milton\nCourtright\n3258 Courtright Street\n\n701-496-3125',
     'NEWCASTLE\nThe Grove\n9982 The Grove NEWCASTLE UPON TYNE NE21 0RM\n\n605-677-5038',
     'BRISTOL\nRichmond\n8253 Richmond Road BRISTOL BS70 9LU\n\n209-848-9572',
     'BOURNEMOUTH\nBroadway\n22 Broadway BOURNEMOUTH BH73 8ON\n\n760-464-6831',
     'LEICESTER\nGreen Lane\n748 Green Lane LEICESTER LE77 6VE\n\n508-272-0114',
     'SUNDERLAND\nNew Road\n48 New Road SUNDERLAND SR39 2NY\n\n845-915-5076',
     'BOLTON\nNorth Street\n19 North Street BOLTON BL77 4TC\n\n973-640-3581',
     'SOUTHAMPTON\nKing Street\n60 King Street SOUTHAMPTON SO75 5PZ\n\n541-579-1559',
     'BLACKPOOL\nHighfield\n8579 Highfield Road BLACKPOOL FY68 1LM\n\n336-212-0408',
     'DARLINGTON\nHigh Street\n9175 High Street DARLINGTON DL86 7BQ\n\n845-340-3808',
     'LIVERPOOL\nMain Road\n100 Main Road LIVERPOOL L80 4XI\n\n561-526-2625',
     'MANCHESTER\nPark Lane\n52 Park Lane MANCHESTER M8 0KJ\n\n801-608-1332',
     'SHEFFIELD\nKings Road\n79 Kings Road SHEFFIELD S88 2KY\n\n510-214-0266',
     'BOLTON\nMill\n95 Mill Road BOLTON BL48 9OR\n\n785-253-0084',
     'SWANSEA\nSouth\n466 South Street SWANSEA SA34 7PT\n\n585-749-2163',
     'LEEDS\nMill Lane\n308 Mill Lane LEEDS LS35 5JS\n\n312-362-2484',
     'SWANSEA\nYork Road\n222 York Road SWANSEA SA87 4WS\n\n570-603-5788',
     'CARDIFF\nWest Street\n125 West Street CARDIFF CF95 6CN\n\n802-738-8477',
     'LEICESTER\nNew Road\n64 New Road LEICESTER LE37 3VW\n\n507-771-8684',
     'SOUTHAMPTON\nMain Street\n90 Main Street SOUTHAMPTON SO41 5RP\n\n720-634-0176',
     'IPSWICH\nStanley Road\n8339 Stanley Road IPSWICH IP79 6SN\n\n313-930-0331',
     'Tokyo\nEbisu\n481-1228, Ebisu Ebisugadempureisu(28-kai), Shibuya-ku\n\n8188-165-7118',
     'Seoul\nGongdeok\n310-5, Samseongraemiangongdeok 3 chaapateu, Gongdeok-dong, Mapo-gu\n\n02-455-1973']



- 그럴 땐 stripped_strings를 쓰면 깔끔하게 뽑을 수 있다


```python
branch = soup.select('.branch')
st = []
for tag in branch:
    wh = tag.stripped_strings
    st.append(list(wh))    
st
```




    [['San Jose', 'Fairway', '4823 Fairway Drive', '707-514-0033'],
     ['GREAT BARTON', 'Lammas', '106 Lammas Street', '070 3460 5076'],
     ['Hamilton', 'Bridgeport', '3791  Bridgeport Rd', '905-389-4463'],
     ['JERRAWA', 'Marlin', '40 Marlin Avenue', '(02) 6175 8642'],
     ['Rudersberg', 'Pasewalker', 'Pasewalker Straße 5', '07183 30 07 96'],
     ['København K', 'Toftvej', 'Toftvej 35', '21-90-47700'],
     ['Guadalajara', 'Revolucion', 'Av. Revolucion 737', '33 36175334'],
     ['Poughkeepsie', 'Old Dear Lane', '4927 Old Dear Lane', '845-857-0825'],
     ['Elgin', 'Pineview', '2491 Pineview Drive', '507-876-0713'],
     ['Oak Brook', 'Vesta', '2591 Vesta Drive', '773-757-1932'],
     ['Annapolis Junction', 'Bluff', '889 Bluff Street', '301-787-8206'],
     ['Los Angeles', 'Jett', '1014 Jett Lane', '310-718-6212'],
     ['Arlington', 'Single', '3158 Single Street', '781-646-1715'],
     ['Syracuse', 'Plainfield', '3741 Plainfield Avenue', '315-576-8242'],
     ['San Mateo', 'Thunder', '2425 Thunder Road', '650-577-7537'],
     ['Valdosta', 'Junkins', '1022 Junkins Avenue', '229-460-4970'],
     ['Hialeah', 'Poplar', '101 Poplar Lane', '305-540-4990'],
     ['Lexington', 'Straford', '793 Straford Park', '606-614-9190'],
     ['Johnsonburg', 'Custer', '2566 Custer Street', '814-965-6502'],
     ['Hokkaido',
      'Kita',
      '244-1192, Kita 6-jonishi, Abashiri-shi, Hokkaido',
      '8134-191-6900'],
     ['Port Chester', 'Ward', '1503 Ward Road', '914-933-3946'],
     ['Salt Lake City', 'Kemper', '4745 Kemper Lane', '801-927-7191'],
     ['Villaluenga del Rosario',
      'Vientos',
      'C/ Rosa de los Vientos 36',
      '736 301 706'],
     ['London',
      'King Street',
      '733 King Street EAST CENTRAL LONDON EC86 0YR',
      '916-863-6154'],
     ['GLOUCESTER',
      'New Road',
      '8857 New Road GLOUCESTER GL79 3CZ',
      '252-218-2526'],
     ['NEWPORT', 'George', '760 George Street NEWPORT NP73 0CH', '803-535-5627'],
     ['TAUNTON', 'The Green', '749 The Green TAUNTON TA27 9JQ', '580-730-2253'],
     ['SOUTHEND-ON-SEA',
      'Springfield',
      '271 Springfield Road SOUTHEND-ON-SEA SS98 1PA',
      '240-597-0099'],
     ['SHEFFIELD',
      'Highfield',
      '500 Highfield Road SHEFFIELD S98 6VM',
      '210-727-9560'],
     ['HULL', 'Albert', '8772 Albert Road HULL HU2 6SN', '919-887-6912'],
     ['SHREWSBURY',
      'Church',
      '38 Church Street SHREWSBURY SY79 9TY',
      '614-449-8617'],
     ['DURHAM', 'DURHAM', '12 New Road DURHAM DH78 4XK', '830-229-4983'],
     ['Honolulu', 'Don Jackson', '4153 Don Jackson Lane', '303-284-0638'],
     ['Wayne', 'Bombardier', '2438 Bombardier Way', '734-981-4470'],
     ['Milton', 'Courtright', '3258 Courtright Street', '701-496-3125'],
     ['NEWCASTLE',
      'The Grove',
      '9982 The Grove NEWCASTLE UPON TYNE NE21 0RM',
      '605-677-5038'],
     ['BRISTOL',
      'Richmond',
      '8253 Richmond Road BRISTOL BS70 9LU',
      '209-848-9572'],
     ['BOURNEMOUTH',
      'Broadway',
      '22 Broadway BOURNEMOUTH BH73 8ON',
      '760-464-6831'],
     ['LEICESTER',
      'Green Lane',
      '748 Green Lane LEICESTER LE77 6VE',
      '508-272-0114'],
     ['SUNDERLAND', 'New Road', '48 New Road SUNDERLAND SR39 2NY', '845-915-5076'],
     ['BOLTON', 'North Street', '19 North Street BOLTON BL77 4TC', '973-640-3581'],
     ['SOUTHAMPTON',
      'King Street',
      '60 King Street SOUTHAMPTON SO75 5PZ',
      '541-579-1559'],
     ['BLACKPOOL',
      'Highfield',
      '8579 Highfield Road BLACKPOOL FY68 1LM',
      '336-212-0408'],
     ['DARLINGTON',
      'High Street',
      '9175 High Street DARLINGTON DL86 7BQ',
      '845-340-3808'],
     ['LIVERPOOL', 'Main Road', '100 Main Road LIVERPOOL L80 4XI', '561-526-2625'],
     ['MANCHESTER', 'Park Lane', '52 Park Lane MANCHESTER M8 0KJ', '801-608-1332'],
     ['SHEFFIELD',
      'Kings Road',
      '79 Kings Road SHEFFIELD S88 2KY',
      '510-214-0266'],
     ['BOLTON', 'Mill', '95 Mill Road BOLTON BL48 9OR', '785-253-0084'],
     ['SWANSEA', 'South', '466 South Street SWANSEA SA34 7PT', '585-749-2163'],
     ['LEEDS', 'Mill Lane', '308 Mill Lane LEEDS LS35 5JS', '312-362-2484'],
     ['SWANSEA', 'York Road', '222 York Road SWANSEA SA87 4WS', '570-603-5788'],
     ['CARDIFF',
      'West Street',
      '125 West Street CARDIFF CF95 6CN',
      '802-738-8477'],
     ['LEICESTER', 'New Road', '64 New Road LEICESTER LE37 3VW', '507-771-8684'],
     ['SOUTHAMPTON',
      'Main Street',
      '90 Main Street SOUTHAMPTON SO41 5RP',
      '720-634-0176'],
     ['IPSWICH',
      'Stanley Road',
      '8339 Stanley Road IPSWICH IP79 6SN',
      '313-930-0331'],
     ['Tokyo',
      'Ebisu',
      '481-1228, Ebisu Ebisugadempureisu(28-kai), Shibuya-ku',
      '8188-165-7118'],
     ['Seoul',
      'Gongdeok',
      '310-5, Samseongraemiangongdeok 3 chaapateu, Gongdeok-dong, Mapo-gu',
      '02-455-1973']]




```python
branch = soup.select('.branch .city')[0].get_text()
branch
```




    'San Jose'




```python
branch_infos = []
branch = soup.select('.branch')
name = soup.select('.branch .city')
addr = soup.select('.branch .address')
phnm = soup.select('.branch .phoneNum')
for n in range(len(branch)):
    branch_infos.append([name[n].get_text(), addr[n].get_text(), phnm[n].get_text()])
branch_infos
```




    [['San Jose', '4823 Fairway Drive', '707-514-0033'],
     ['GREAT BARTON', '106 Lammas Street', '070 3460 5076'],
     ['Hamilton', '3791  Bridgeport Rd', '905-389-4463'],
     ['JERRAWA', '40 Marlin Avenue', '(02) 6175 8642'],
     ['Rudersberg', 'Pasewalker Straße 5', '07183 30 07 96'],
     ['København K', 'Toftvej 35', '21-90-47700'],
     ['Guadalajara', 'Av. Revolucion 737', '33 36175334'],
     ['Poughkeepsie', '4927 Old Dear Lane', '845-857-0825'],
     ['Elgin', '2491 Pineview Drive', '507-876-0713'],
     ['Oak Brook', '2591 Vesta Drive', '773-757-1932'],
     ['Annapolis Junction', '889 Bluff Street', '301-787-8206'],
     ['Los Angeles', '1014 Jett Lane', '310-718-6212'],
     ['Arlington', '3158 Single Street', '781-646-1715'],
     ['Syracuse', '3741 Plainfield Avenue', '315-576-8242'],
     ['San Mateo', '2425 Thunder Road', '650-577-7537'],
     ['Valdosta', '1022 Junkins Avenue', '229-460-4970'],
     ['Hialeah', '101 Poplar Lane', '305-540-4990'],
     ['Lexington', '793 Straford Park', '606-614-9190'],
     ['Johnsonburg', '2566 Custer Street', '814-965-6502'],
     ['Hokkaido',
      '244-1192, Kita 6-jonishi, Abashiri-shi, Hokkaido',
      '8134-191-6900'],
     ['Port Chester', '1503 Ward Road', '914-933-3946'],
     ['Salt Lake City', '4745 Kemper Lane', '801-927-7191'],
     ['Villaluenga del Rosario', 'C/ Rosa de los Vientos 36', '736 301 706'],
     ['London', '733 King Street EAST CENTRAL LONDON EC86 0YR', '916-863-6154'],
     ['GLOUCESTER', '8857 New Road GLOUCESTER GL79 3CZ', '252-218-2526'],
     ['NEWPORT', '760 George Street NEWPORT NP73 0CH', '803-535-5627'],
     ['TAUNTON', '749 The Green TAUNTON TA27 9JQ', '580-730-2253'],
     ['SOUTHEND-ON-SEA',
      '271 Springfield Road SOUTHEND-ON-SEA SS98 1PA',
      '240-597-0099'],
     ['SHEFFIELD', '500 Highfield Road SHEFFIELD S98 6VM', '210-727-9560'],
     ['HULL', '8772 Albert Road HULL HU2 6SN', '919-887-6912'],
     ['SHREWSBURY', '38 Church Street SHREWSBURY SY79 9TY', '614-449-8617'],
     ['DURHAM', '12 New Road DURHAM DH78 4XK', '830-229-4983'],
     ['Honolulu', '4153 Don Jackson Lane', '303-284-0638'],
     ['Wayne', '2438 Bombardier Way', '734-981-4470'],
     ['Milton', '3258 Courtright Street', '701-496-3125'],
     ['NEWCASTLE', '9982 The Grove NEWCASTLE UPON TYNE NE21 0RM', '605-677-5038'],
     ['BRISTOL', '8253 Richmond Road BRISTOL BS70 9LU', '209-848-9572'],
     ['BOURNEMOUTH', '22 Broadway BOURNEMOUTH BH73 8ON', '760-464-6831'],
     ['LEICESTER', '748 Green Lane LEICESTER LE77 6VE', '508-272-0114'],
     ['SUNDERLAND', '48 New Road SUNDERLAND SR39 2NY', '845-915-5076'],
     ['BOLTON', '19 North Street BOLTON BL77 4TC', '973-640-3581'],
     ['SOUTHAMPTON', '60 King Street SOUTHAMPTON SO75 5PZ', '541-579-1559'],
     ['BLACKPOOL', '8579 Highfield Road BLACKPOOL FY68 1LM', '336-212-0408'],
     ['DARLINGTON', '9175 High Street DARLINGTON DL86 7BQ', '845-340-3808'],
     ['LIVERPOOL', '100 Main Road LIVERPOOL L80 4XI', '561-526-2625'],
     ['MANCHESTER', '52 Park Lane MANCHESTER M8 0KJ', '801-608-1332'],
     ['SHEFFIELD', '79 Kings Road SHEFFIELD S88 2KY', '510-214-0266'],
     ['BOLTON', '95 Mill Road BOLTON BL48 9OR', '785-253-0084'],
     ['SWANSEA', '466 South Street SWANSEA SA34 7PT', '585-749-2163'],
     ['LEEDS', '308 Mill Lane LEEDS LS35 5JS', '312-362-2484'],
     ['SWANSEA', '222 York Road SWANSEA SA87 4WS', '570-603-5788'],
     ['CARDIFF', '125 West Street CARDIFF CF95 6CN', '802-738-8477'],
     ['LEICESTER', '64 New Road LEICESTER LE37 3VW', '507-771-8684'],
     ['SOUTHAMPTON', '90 Main Street SOUTHAMPTON SO41 5RP', '720-634-0176'],
     ['IPSWICH', '8339 Stanley Road IPSWICH IP79 6SN', '313-930-0331'],
     ['Tokyo',
      '481-1228, Ebisu Ebisugadempureisu(28-kai), Shibuya-ku',
      '8188-165-7118'],
     ['Seoul',
      '310-5, Samseongraemiangongdeok 3 chaapateu, Gongdeok-dong, Mapo-gu',
      '02-455-1973']]



### <a id='toc1_3_2_'></a>[select Vs. find_all](#toc0_)
---
- select는 css 선택자를 쓰지만 find_all은 여러 파라미터를 쓴다


```python
response = requests.get("https://workey.codeit.kr/music/index")
text_response = response.text
soup = BeautifulSoup(text_response, 'html.parser')
soup.prettify()

```




    '<!DOCTYPE html>\n<html lang="ko">\n <head>\n  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js">\n  </script>\n  <script src="https://unpkg.com/axios/dist/axios.min.js">\n  </script>\n  <meta charset="utf-8"/>\n  <title>\n   Codeit Music\n  </title>\n  <style>\n   body {\n      margin: 0;\n    }\n\n    a {\n      text-decoration: none;\n      color: inherit;\n    }\n\n    img {\n      vertical-align: middle;\n    }\n\n    ul {\n      list-style: none;\n      padding: 0;\n      margin: 0;\n    }\n\n    * {\n      box-sizing: border-box;\n    }\n\n    .header {\n      position: fixed;\n      top: 0;\n      left: 0;\n      width: 100%;\n      height: 60px;\n      background-color: #ffffff;\n      overflow: hidden;\n      z-index: 1;\n    }\n\n    .nav-warpper {\n      max-width: 1163px;\n      margin: 0 auto;\n      height: 100%;\n      line-height: 60px;\n      padding: 0 20px\n    }\n\n    .header__logo .logo-img {\n      width: 34px;\n      margin-right: 25px;\n    }\n\n    .header__nav {\n      display: inline-block;\n      vertical-align: middle;\n    }\n\n    .header__nav .menu {\n      float: left;\n      font-size: 16px;\n      color: #4a4a4a;\n      margin-right: 21px;\n    }\n\n    .header__search {\n      display: inline-block;\n      vertical-align: middle;\n      margin: 0 53px;\n      width: 397px;\n      height: 36px;\n      line-height: 36px;\n      border-radius: 22px;\n      border: 1px solid #4a90e2;\n      padding: 0 13px;\n    }\n\n    .header__search .icon {\n      width: 24px;\n      margin-right: 4px;\n    }\n\n    .header__search .input {\n      border: none;\n      outline: none;\n      font-size: 14px;\n      background: transparent;\n      width: calc(100% - 35px);\n    }\n\n    .header__user {\n      display: inline-block;\n      float: right;\n    }\n\n    .header__user .name {\n      font-size: 14px;\n      color: #4a4a4a;\n      margin-right: 14px;\n    }\n\n    .header__user .profile {\n      width: 30px;\n    }\n\n    .main {\n      min-height: calc(100vh - 60px);\n      padding-top: 60px;\n      background-color: #fafafa;\n      position: relative;\n      overflow: hidden;\n    }\n\n    .main section {\n      float: left;\n    }\n\n    .contents-warpper {\n      max-width: 991px;\n      margin: 0 auto;\n      padding: 34px 0;\n    }\n\n    .main__sidebar {\n      width: 231px;\n      margin-right: 23px;\n    }\n\n    .main__sidebar article {\n      width: 100%;\n      border-radius: 7px;\n      background-color: #ffffff;\n      padding: 17px 13px 5px;\n      margin-bottom: 32px;\n    }\n\n    .main__sidebar .popular__title,\n    .main__sidebar .rank__title {\n      margin: 0 0 24px;\n      font-size: 14px;\n      font-weight: bold;\n      color: #4a4a4a;\n    }\n\n    .main__sidebar .list {\n      font-size: 14px;\n      color: #4a4a4a;\n      margin-bottom: 12px;\n    }\n\n    .main__sidebar .list__index {\n      display: inline-block;\n      width: 18px;\n      height: 18px;\n      line-height: 1.8;\n      text-align: center;\n      font-size: 11px;\n      font-weight: bold;\n      border-radius: 6px;\n      color: #ffffff;\n      background-color: #dbdbdb;\n    }\n\n    .main__sidebar .list__index.blue {\n      background-color: #2391e9;\n    }\n\n    .main__sidebar .popular__order .list__index {\n      margin-right: 18px;\n    }\n\n    .main__sidebar .rank__order .list__index {\n      margin-right: 10px;\n    }\n\n    .main__sidebar .list__rating {\n      font-size: 14px;\n      font-weight: normal;\n      color: #9b9b9b;\n      text-align: center;\n      width: 25px;\n      display: inline-block;\n    }\n\n    .main__sidebar .und {\n      width: 8px;\n      vertical-align: unset;\n      margin-right: 2px;\n    }\n\n    .main__sidebar .dash {\n      display: inline-block;\n      width: 6px;\n      height: 1px;\n      background-color: #979797;\n      vertical-align: super;\n      margin-right: 3px;\n      margin-left: 1px;\n    }\n\n    .main__listWrapper {\n      width: 737px;\n    }\n\n    .main__listWrapper .playlist {\n      width: 100%;\n      height: 240px;\n      border-radius: 7px;\n      box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.15);\n      position: relative;\n      overflow: hidden;\n      background-color: #ffffff;\n      margin-bottom: 34px;\n    }\n\n    .main__listWrapper .playlist__theme {\n      width: 68px;\n      border-bottom: 1px solid #ffffff;\n      position: absolute;\n      top: 23px;\n      left: 26px;\n      margin: 0;\n      color: #ffffff;\n      text-align: center;\n      padding-bottom: 8px;\n      font-size: 14px;\n      font-weight: bold;\n    }\n\n    .main__listWrapper .playlist__img {\n      width: 397px;\n      float: left;\n    }\n\n    .main__listWrapper .playlist__meta {\n      padding: 22px 19px;\n      float: left;\n      width: 340px;\n    }\n\n    .main__listWrapper .playlist__meta .owner {\n      width: 60px;\n      float: left;\n      margin-right: 15px;\n    }\n\n    .main__listWrapper .playlist__meta .title {\n      margin: 0;\n      font-size: 20px;\n      font-weight: normal;\n      color: #4a4a4a;\n      word-break: keep-all;\n      height: 48px;\n    }\n\n    .main__listWrapper .playlist__meta .tags {\n      margin: 45px 0 16px;\n      padding-bottom: 15px;\n      border-bottom: 1px solid #9b9b9b;\n      color: #9b9b9b;\n      font-size: 14px;\n      line-height: 1.7;\n    }\n\n    .main__listWrapper .playlist__meta .data img {\n      width: 20px;\n    }\n\n    .main__listWrapper .playlist__meta .data span {\n      vertical-align: middle;\n      margin-left: 6px;\n      margin-right: 16px;\n    }\n\n    @media (max-width: 991px) {\n      body * {\n        display: none;\n      }\n\n      body {\n        width: 100vw;\n        height: 100vh;\n        background-color: rgba(0, 0, 0, 0.8);\n      }\n\n      body::after {\n        display: block;\n        content: \'지원하지 않는 화면 크기 입니다. 브라우저 크기를 넓혀주세요.\';\n        position: absolute;\n        top: 50%;\n        left: 50%;\n        width: 230px;\n        word-break: keep-all;\n        text-align: center;\n        line-height: 1.7;\n        font-size: 18px;\n        color: #ffffff;\n        transform: translate(-50%, -50%);\n      }\n    }\n  </style>\n </head>\n <body>\n  <header class="header">\n   <nav class="nav-warpper">\n    <a class="header__logo" href="#">\n     <img alt="logo" class="logo-img" src="/images/music/logo.png"/>\n    </a>\n    <ul class="header__nav">\n     <li class="menu">\n      <a href="#">\n       인기차트\n      </a>\n     </li>\n     <li class="menu">\n      <a href="#">\n       추천음악\n      </a>\n     </li>\n     <li class="menu">\n      <a href="#">\n       뮤직비디오\n      </a>\n     </li>\n    </ul>\n    <div class="header__search">\n     <img class="icon" src="/images/music/search.png"/>\n     <input class="input" placeholder="오늘은 무슨 음악을 들을까?" type="text"/>\n    </div>\n    <div class="header__user">\n     <span class="name">\n      강영훈\n     </span>\n     <img alt="user" class="profile" src="/images/music/user.png"/>\n    </div>\n   </nav>\n  </header>\n  <div class="main">\n   <div class="contents-warpper">\n    <section class="main__sidebar">\n     <article class="popular">\n      <h3 class="popular__title">\n       인기 아티스트\n      </h3>\n      <ul class="popular__order">\n       <li class="list">\n        <span class="list__index blue">\n         1\n        </span>\n        아이유 (IU)\n       </li>\n       <li class="list">\n        <span class="list__index blue">\n         2\n        </span>\n        방탄소년단\n       </li>\n       <li class="list">\n        <span class="list__index blue">\n         3\n        </span>\n        Red Velvet (레드벨벳)\n       </li>\n       <li class="list">\n        <span class="list__index">\n         4\n        </span>\n        IKON\n       </li>\n       <li class="list">\n        <span class="list__index">\n         5\n        </span>\n        멜로망스\n       </li>\n       <li class="list">\n        <span class="list__index">\n         6\n        </span>\n        다비치\n       </li>\n       <li class="list">\n        <span class="list__index">\n         7\n        </span>\n        윤딴딴\n       </li>\n       <li class="list">\n        <span class="list__index">\n         8\n        </span>\n        수지 (SUZY)\n       </li>\n       <li class="list">\n        <span class="list__index">\n         9\n        </span>\n        김동률\n       </li>\n       <li class="list">\n        <span class="list__index">\n         10\n        </span>\n        폴킴\n       </li>\n      </ul>\n     </article>\n     <article class="rank">\n      <h3 class="rank__title">\n       검색어 순위\n      </h3>\n      <ul class="rank__order">\n       <li class="list">\n        <span class="list__index blue">\n         1\n        </span>\n        <b class="list__rating">\n         <i class="dash">\n         </i>\n         0\n        </b>\n        Queen\n       </li>\n       <li class="list">\n        <span class="list__index blue">\n         2\n        </span>\n        <b class="list__rating">\n         <i class="dash">\n         </i>\n         0\n        </b>\n        방탄소년단\n       </li>\n       <li class="list">\n        <span class="list__index blue">\n         3\n        </span>\n        <b class="list__rating">\n         <i class="dash">\n         </i>\n         0\n        </b>\n        아이유\n       </li>\n       <li class="list">\n        <span class="list__index">\n         4\n        </span>\n        <b class="list__rating">\n         <img alt="up" class="und" src="/images/music/up.png"/>\n         7\n        </b>\n        거미\n       </li>\n       <li class="list">\n        <span class="list__index">\n         5\n        </span>\n        <b class="list__rating">\n         <img alt="down" class="und" src="/images/music/down.png"/>\n         1\n        </b>\n        폴킴\n       </li>\n       <li class="list">\n        <span class="list__index">\n         6\n        </span>\n        <b class="list__rating">\n         <img alt="up" class="und" src="/images/music/up.png"/>\n         1\n        </b>\n        김범수\n       </li>\n       <li class="list">\n        <span class="list__index">\n         7\n        </span>\n        <b class="list__rating">\n         <img alt="up" class="und" src="/images/music/up.png"/>\n         6\n        </b>\n        헤이즈\n       </li>\n       <li class="list">\n        <span class="list__index">\n         8\n        </span>\n        <b class="list__rating">\n         <img alt="down" class="und" src="/images/music/down.png"/>\n         2\n        </b>\n        트와이스\n       </li>\n       <li class="list">\n        <span class="list__index">\n         9\n        </span>\n        <b class="list__rating">\n         <img alt="up" class="und" src="/images/music/up.png"/>\n         7\n        </b>\n        박효신\n       </li>\n       <li class="list">\n        <span class="list__index">\n         10\n        </span>\n        <b class="list__rating">\n         <i class="dash">\n         </i>\n         0\n        </b>\n        신용재\n       </li>\n      </ul>\n     </article>\n    </section>\n    <section class="main__listWrapper" id="list-container">\n     <article class="playlist" v-bind:key="index" v-for="(item, index) in playlist">\n      <h5 class="playlist__theme">\n       {{item.category}}\n      </h5>\n      <img :src="item.imageUrl" alt="background" class="playlist__img"/>\n      <div class="playlist__meta">\n       <img :src="item.authorProfileImageUrl" alt="owner" class="owner"/>\n       <h3 class="title">\n        {{item.title}}\n       </h3>\n       <p class="tags">\n        <a class="tag" href="#" v-bind:key="index" v-for="(tag, index) in item.tags">\n         #{{tag}}\n        </a>\n       </p>\n       <div class="data">\n        <img alt="like" class="data__like-img" src="/images/music/like.png"/>\n        <span class="data__like-count">\n         {{item.likeCount}}\n        </span>\n        <img alt="music" class="data__music-img" src="/images/music/music.png"/>\n        <span class="data__music-count">\n         {{item.trackCount}}\n        </span>\n       </div>\n      </div>\n     </article>\n    </section>\n   </div>\n  </div>\n  <script src="/js/music.js">\n  </script>\n </body>\n</html>\n'




```python
tags = soup.select('ul.rank__order li')
popular_searches = []
for tag in tags:
    line = list(tag.stripped_strings)
    popular_searches.append(line[2])
popular_searches
```




    ['Queen', '방탄소년단', '아이유', '거미', '폴킴', '김범수', '헤이즈', '트와이스', '박효신', '신용재']



### <a id='toc1_3_3_'></a>[속성 가져오기](#toc0_)
---
태그 안에 있는 속성은 사전 형태로 저장돼있다

tag['attr']로 가져올 수 있고  
tag.attrs 로 확인 할 수 있다


```python
soup.select_one('img')['src']
```




    '/images/music/logo.png'



## <a id='toc1_4_'></a>[openpyxl을 이용해 excel로 저장하는 법](#toc0_)
---


```python
wb = Workbook(write_only=True)
ws = wb.create_sheet('ratings')
```


```python
ws.append(['rank', 'channel', 'name', 'rate'])
```


```python
response = requests.get("https://workey.codeit.kr/ratings/index")
rpage = response.text

soup = BeautifulSoup(rpage, 'html.parser')
```


```python
soup.select('tr')[1:]
```




    [<tr class="row">
     <td class="rank">1</td>
     <td class="channel">KBS2</td>
     <td class="program">주말연속극(수상한삼형제)</td>
     <td class="percent">33.4</td>
     </tr>,
     <tr class="row">
     <td class="rank">2</td>
     <td class="channel">KBS1</td>
     <td class="program">일일연속극(다함께차차차)</td>
     <td class="percent">33.1</td>
     </tr>,
     <tr class="row">
     <td class="rank">3</td>
     <td class="channel">KBS2</td>
     <td class="program">해피선데이</td>
     <td class="percent">27.1</td>
     </tr>,
     <tr class="row">
     <td class="rank">4</td>
     <td class="channel">MBC</td>
     <td class="program">MBC연기대상2부</td>
     <td class="percent">24.4</td>
     </tr>,
     <tr class="row">
     <td class="rank">5</td>
     <td class="channel">SBS</td>
     <td class="program">주말극장(천만번사랑해)</td>
     <td class="percent">24.2</td>
     </tr>,
     <tr class="row">
     <td class="rank">6</td>
     <td class="channel">MBC</td>
     <td class="program">MBC방송연예대상2부</td>
     <td class="percent">24.0</td>
     </tr>,
     <tr class="row">
     <td class="rank">7</td>
     <td class="channel">MBC</td>
     <td class="program">MBC방송연예대상1부</td>
     <td class="percent">22.4</td>
     </tr>,
     <tr class="row">
     <td class="rank">8</td>
     <td class="channel">SBS</td>
     <td class="program">SBS연예대상2부</td>
     <td class="percent">21.1</td>
     </tr>,
     <tr class="row">
     <td class="rank">9</td>
     <td class="channel">MBC</td>
     <td class="program">주말기획드라마(보석비빔밥)</td>
     <td class="percent">20.9</td>
     </tr>,
     <tr class="row">
     <td class="rank">10</td>
     <td class="channel">MBC</td>
     <td class="program">일일시트콤(지붕뚫고하이킥)</td>
     <td class="percent">19.9</td>
     </tr>]




```python
for tr in soup.select('tr')[1:]:
    td = tr.select('td')
    row = [
        td[0].get_text(), #rank
        td[1].get_text(), #channel
        td[2].get_text(), #name
        td[3].get_text() # rate
    ]
    ws.append(row)
# wb.save('20110jan1w.xlsx')
```


```python
response = requests.get("https://workey.codeit.kr/orangebottle/index")
rpage = response.text

soup = BeautifulSoup(rpage, 'html.parser')
soup.prettify()
```




    '<!DOCTYPE html>\n<html>\n <head>\n  <title>\n   Orange bottle coffee\n  </title>\n  <meta charset="utf-8"/>\n  <link href="https://fonts.googleapis.com/css?family=Noto+Sans+KR" rel="stylesheet"/>\n  <style>\n   body {\n            font-family: \'Noto Sans KR\', sans-serif;\n            margin: 0;\n            background-color: #ffffff;\n        }\n\n        /*navigation bar*/\n        #bottle {\n            margin-top: 12px;\n            margin-bottom: 11px;\n            margin-left: 79px;\n            margin-right: 24px;\n            vertical-align: middle;\n            width: 13px;\n        }\n\n        #title {\n            font-size: 14px;\n            font-weight: bold;\n            vertical-align: middle;\n            color: #4a4a4a;\n        }\n\n        ul {\n            display: inline;\n            padding-left: 0;\n        }\n\n        li {\n            float: right;\n            list-style-type: none;\n            font-size: 14px;\n        }\n\n        #subscribe {\n            color: #f5a623;\n            margin-right: 25px;\n            line-height: 58px;\n        }\n\n        #signin {\n            margin-right: 65px;\n            line-height: 58px;\n            color: #4a4a4a;\n        }\n\n        /*main image*/\n        #mainimg {\n            height: 533px;\n            line-height: 533px;\n            margin-bottom: 122px;\n            background-image: url("/images/orangebottle/background.jpg");\n            background-size: cover;\n            background-position: center center;\n            text-align: center;\n        }\n\n        #mainimg #maintext {\n            line-height: normal;\n            display: inline-block;\n            vertical-align: middle;\n            font-size: 25px;\n            color: #ffffff;\n        }\n\n        /*branches*/\n        .container {\n            width: 1100px;\n            margin-left: auto;\n            margin-right: auto;\n            overflow: hidden;\n        }\n\n        .container .branch {\n            width: 25%;\n            height: 164px;\n            float: left;\n            padding-left: 40px;\n            padding-right: 40px;\n            margin-top: 10px;\n            margin-bottom: 80px;\n            box-sizing: border-box;\n        }\n\n        .container .branch .city {\n            display: inline-block;\n            margin: 0;\n            border-radius: 8px;\n            padding: 5px 8px;\n            font-size: 14px;\n            color: white;\n            background-color: #f5a623;\n        }\n\n        .container .branch .ave {\n            margin: 12px 0;\n            font-size: 16px;\n            color: #f5a623;\n        }\n\n        .container .branch .address {\n            margin: 12px 0;\n            color: #4a4a4a;\n            line-height: 1.6;\n        }\n\n        .container .branch img {\n            vertical-align: middle;\n            margin-right: 9px;\n        }\n\n        .container .branch .phoneNum {\n            color: #818181;\n        }\n\n        /*signup*/\n\n        #footer {\n            width: 100%;\n            height: 453px;\n            background-color: #f9f9f9;\n            float: left;\n        }\n\n        #footer h1 {\n            margin-top: 75px;\n            margin-bottom: 37px;\n            font-size: 40px;\n            font-weight: 300;\n            text-align: center;\n            color: #9b9b9b;\n        }\n\n        #footer h2 {\n            font-size: 16px;\n            text-align: center;\n            color: #4a4a4a;\n            margin-bottom: 58px;\n        }\n\n        #footer #signup {\n            width: 646px;\n            height: 70px;\n            background-color: white;\n            margin-left: auto;\n            margin-right: auto;\n        }\n\n        #footer #signup input {\n            border: none;\n            font-size: 20px; /*원래는 16*/\n            margin-top: 19px;\n            margin-bottom: 27px;\n            margin-left: 34px;\n            color: #9b9b9b;\n            width: 450px;\n            height: 30px;\n        }\n\n        #footer #signup #submit {\n            width: 130px;\n            height: 70px;\n            float: right;\n            background-color: #f5a623;\n            text-align: center;\n            line-height: 70px;\n        }\n\n        #footer #signup a {\n            text-decoration: none;\n            color: #ffffff;\n            font-size: 18px;\n        }\n  </style>\n </head>\n <body>\n  <div id="navbar">\n   <a href="#" style="text-decoration: none;color:#4a4a4a;">\n    <img id="bottle" src="/images/orangebottle/logo.png"/>\n    <span id="title">\n     ORANGE BOTTLE COFFEE\n    </span>\n   </a>\n   <ul>\n    <a href="#" style="color:black;">\n     <li id="signin">\n      SIGN IN\n     </li>\n    </a>\n    <a href="#">\n     <li id="subscribe">\n      SUBSCRIBE\n     </li>\n    </a>\n   </ul>\n  </div>\n  <!-- main image -->\n  <div id="mainimg">\n   <div id="maintext">\n    <h1>\n     Find Your Orange Bottle Cafe\n    </h1>\n   </div>\n  </div>\n  <!-- cafe branches -->\n  <div class="container">\n   <div class="branch">\n    <p class="city">\n     San Jose\n    </p>\n    <p class="ave">\n     Fairway\n    </p>\n    <p class="address">\n     4823 Fairway Drive\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     707-514-0033\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     GREAT BARTON\n    </p>\n    <p class="ave">\n     Lammas\n    </p>\n    <p class="address">\n     106 Lammas Street\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     070 3460 5076\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Hamilton\n    </p>\n    <p class="ave">\n     Bridgeport\n    </p>\n    <p class="address">\n     3791  Bridgeport Rd\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     905-389-4463\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     JERRAWA\n    </p>\n    <p class="ave">\n     Marlin\n    </p>\n    <p class="address">\n     40 Marlin Avenue\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     (02) 6175 8642\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Rudersberg\n    </p>\n    <p class="ave">\n     Pasewalker\n    </p>\n    <p class="address">\n     Pasewalker Straße 5\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     07183 30 07 96\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     København K\n    </p>\n    <p class="ave">\n     Toftvej\n    </p>\n    <p class="address">\n     Toftvej 35\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     21-90-47700\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Guadalajara\n    </p>\n    <p class="ave">\n     Revolucion\n    </p>\n    <p class="address">\n     Av. Revolucion 737\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     33 36175334\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Poughkeepsie\n    </p>\n    <p class="ave">\n     Old Dear Lane\n    </p>\n    <p class="address">\n     4927 Old Dear Lane\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     845-857-0825\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Elgin\n    </p>\n    <p class="ave">\n     Pineview\n    </p>\n    <p class="address">\n     2491 Pineview Drive\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     507-876-0713\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Oak Brook\n    </p>\n    <p class="ave">\n     Vesta\n    </p>\n    <p class="address">\n     2591 Vesta Drive\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     773-757-1932\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Annapolis Junction\n    </p>\n    <p class="ave">\n     Bluff\n    </p>\n    <p class="address">\n     889 Bluff Street\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     301-787-8206\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Los Angeles\n    </p>\n    <p class="ave">\n     Jett\n    </p>\n    <p class="address">\n     1014 Jett Lane\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     310-718-6212\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Arlington\n    </p>\n    <p class="ave">\n     Single\n    </p>\n    <p class="address">\n     3158 Single Street\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     781-646-1715\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Syracuse\n    </p>\n    <p class="ave">\n     Plainfield\n    </p>\n    <p class="address">\n     3741 Plainfield Avenue\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     315-576-8242\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     San Mateo\n    </p>\n    <p class="ave">\n     Thunder\n    </p>\n    <p class="address">\n     2425 Thunder Road\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     650-577-7537\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Valdosta\n    </p>\n    <p class="ave">\n     Junkins\n    </p>\n    <p class="address">\n     1022 Junkins Avenue\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     229-460-4970\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Hialeah\n    </p>\n    <p class="ave">\n     Poplar\n    </p>\n    <p class="address">\n     101 Poplar Lane\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     305-540-4990\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Lexington\n    </p>\n    <p class="ave">\n     Straford\n    </p>\n    <p class="address">\n     793 Straford Park\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     606-614-9190\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Johnsonburg\n    </p>\n    <p class="ave">\n     Custer\n    </p>\n    <p class="address">\n     2566 Custer Street\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     814-965-6502\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Hokkaido\n    </p>\n    <p class="ave">\n     Kita\n    </p>\n    <p class="address">\n     244-1192, Kita 6-jonishi, Abashiri-shi, Hokkaido\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     8134-191-6900\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Port Chester\n    </p>\n    <p class="ave">\n     Ward\n    </p>\n    <p class="address">\n     1503 Ward Road\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     914-933-3946\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Salt Lake City\n    </p>\n    <p class="ave">\n     Kemper\n    </p>\n    <p class="address">\n     4745 Kemper Lane\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     801-927-7191\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Villaluenga del Rosario\n    </p>\n    <p class="ave">\n     Vientos\n    </p>\n    <p class="address">\n     C/ Rosa de los Vientos 36\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     736 301 706\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     London\n    </p>\n    <p class="ave">\n     King Street\n    </p>\n    <p class="address">\n     733 King Street EAST CENTRAL LONDON EC86 0YR\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     916-863-6154\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     GLOUCESTER\n    </p>\n    <p class="ave">\n     New Road\n    </p>\n    <p class="address">\n     8857 New Road GLOUCESTER GL79 3CZ\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     252-218-2526\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     NEWPORT\n    </p>\n    <p class="ave">\n     George\n    </p>\n    <p class="address">\n     760 George Street NEWPORT NP73 0CH\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     803-535-5627\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     TAUNTON\n    </p>\n    <p class="ave">\n     The Green\n    </p>\n    <p class="address">\n     749 The Green TAUNTON TA27 9JQ\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     580-730-2253\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     SOUTHEND-ON-SEA\n    </p>\n    <p class="ave">\n     Springfield\n    </p>\n    <p class="address">\n     271 Springfield Road SOUTHEND-ON-SEA SS98 1PA\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     240-597-0099\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     SHEFFIELD\n    </p>\n    <p class="ave">\n     Highfield\n    </p>\n    <p class="address">\n     500 Highfield Road SHEFFIELD S98 6VM\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     210-727-9560\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     HULL\n    </p>\n    <p class="ave">\n     Albert\n    </p>\n    <p class="address">\n     8772 Albert Road HULL HU2 6SN\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     919-887-6912\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     SHREWSBURY\n    </p>\n    <p class="ave">\n     Church\n    </p>\n    <p class="address">\n     38 Church Street SHREWSBURY SY79 9TY\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     614-449-8617\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     DURHAM\n    </p>\n    <p class="ave">\n     DURHAM\n    </p>\n    <p class="address">\n     12 New Road DURHAM DH78 4XK\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     830-229-4983\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Honolulu\n    </p>\n    <p class="ave">\n     Don Jackson\n    </p>\n    <p class="address">\n     4153 Don Jackson Lane\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     303-284-0638\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Wayne\n    </p>\n    <p class="ave">\n     Bombardier\n    </p>\n    <p class="address">\n     2438 Bombardier Way\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     734-981-4470\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Milton\n    </p>\n    <p class="ave">\n     Courtright\n    </p>\n    <p class="address">\n     3258 Courtright Street\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     701-496-3125\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     NEWCASTLE\n    </p>\n    <p class="ave">\n     The Grove\n    </p>\n    <p class="address">\n     9982 The Grove NEWCASTLE UPON TYNE NE21 0RM\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     605-677-5038\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     BRISTOL\n    </p>\n    <p class="ave">\n     Richmond\n    </p>\n    <p class="address">\n     8253 Richmond Road BRISTOL BS70 9LU\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     209-848-9572\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     BOURNEMOUTH\n    </p>\n    <p class="ave">\n     Broadway\n    </p>\n    <p class="address">\n     22 Broadway BOURNEMOUTH BH73 8ON\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     760-464-6831\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     LEICESTER\n    </p>\n    <p class="ave">\n     Green Lane\n    </p>\n    <p class="address">\n     748 Green Lane LEICESTER LE77 6VE\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     508-272-0114\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     SUNDERLAND\n    </p>\n    <p class="ave">\n     New Road\n    </p>\n    <p class="address">\n     48 New Road SUNDERLAND SR39 2NY\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     845-915-5076\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     BOLTON\n    </p>\n    <p class="ave">\n     North Street\n    </p>\n    <p class="address">\n     19 North Street BOLTON BL77 4TC\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     973-640-3581\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     SOUTHAMPTON\n    </p>\n    <p class="ave">\n     King Street\n    </p>\n    <p class="address">\n     60 King Street SOUTHAMPTON SO75 5PZ\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     541-579-1559\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     BLACKPOOL\n    </p>\n    <p class="ave">\n     Highfield\n    </p>\n    <p class="address">\n     8579 Highfield Road BLACKPOOL FY68 1LM\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     336-212-0408\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     DARLINGTON\n    </p>\n    <p class="ave">\n     High Street\n    </p>\n    <p class="address">\n     9175 High Street DARLINGTON DL86 7BQ\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     845-340-3808\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     LIVERPOOL\n    </p>\n    <p class="ave">\n     Main Road\n    </p>\n    <p class="address">\n     100 Main Road LIVERPOOL L80 4XI\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     561-526-2625\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     MANCHESTER\n    </p>\n    <p class="ave">\n     Park Lane\n    </p>\n    <p class="address">\n     52 Park Lane MANCHESTER M8 0KJ\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     801-608-1332\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     SHEFFIELD\n    </p>\n    <p class="ave">\n     Kings Road\n    </p>\n    <p class="address">\n     79 Kings Road SHEFFIELD S88 2KY\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     510-214-0266\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     BOLTON\n    </p>\n    <p class="ave">\n     Mill\n    </p>\n    <p class="address">\n     95 Mill Road BOLTON BL48 9OR\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     785-253-0084\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     SWANSEA\n    </p>\n    <p class="ave">\n     South\n    </p>\n    <p class="address">\n     466 South Street SWANSEA SA34 7PT\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     585-749-2163\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     LEEDS\n    </p>\n    <p class="ave">\n     Mill Lane\n    </p>\n    <p class="address">\n     308 Mill Lane LEEDS LS35 5JS\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     312-362-2484\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     SWANSEA\n    </p>\n    <p class="ave">\n     York Road\n    </p>\n    <p class="address">\n     222 York Road SWANSEA SA87 4WS\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     570-603-5788\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     CARDIFF\n    </p>\n    <p class="ave">\n     West Street\n    </p>\n    <p class="address">\n     125 West Street CARDIFF CF95 6CN\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     802-738-8477\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     LEICESTER\n    </p>\n    <p class="ave">\n     New Road\n    </p>\n    <p class="address">\n     64 New Road LEICESTER LE37 3VW\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     507-771-8684\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     SOUTHAMPTON\n    </p>\n    <p class="ave">\n     Main Street\n    </p>\n    <p class="address">\n     90 Main Street SOUTHAMPTON SO41 5RP\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     720-634-0176\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     IPSWICH\n    </p>\n    <p class="ave">\n     Stanley Road\n    </p>\n    <p class="address">\n     8339 Stanley Road IPSWICH IP79 6SN\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     313-930-0331\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Tokyo\n    </p>\n    <p class="ave">\n     Ebisu\n    </p>\n    <p class="address">\n     481-1228, Ebisu Ebisugadempureisu(28-kai), Shibuya-ku\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     8188-165-7118\n    </span>\n   </div>\n   <div class="branch">\n    <p class="city">\n     Seoul\n    </p>\n    <p class="ave">\n     Gongdeok\n    </p>\n    <p class="address">\n     310-5, Samseongraemiangongdeok 3 chaapateu, Gongdeok-dong, Mapo-gu\n    </p>\n    <img src="/images/orangebottle/phone_icon.png" width="20px"/>\n    <span class="phoneNum">\n     02-455-1973\n    </span>\n   </div>\n  </div>\n  <!-- signup -->\n  <div id="footer">\n   <h1>\n    SIGN UP\n   </h1>\n   <h2>\n    Sign up for stories, coffee tips, and brewing equipment\n   </h2>\n   <div id="signup">\n    <input placeholder="Your email here" type="text"/>\n    <a href="#" id="submit">\n     SIGN UP\n    </a>\n   </div>\n  </div>\n </body>\n</html>\n'




```python
branch = soup.select('.branch')
st = []
for tag in branch:
    wh = tag.stripped_strings
    st.append(list(wh))    
st
```




    [['San Jose', 'Fairway', '4823 Fairway Drive', '707-514-0033'],
     ['GREAT BARTON', 'Lammas', '106 Lammas Street', '070 3460 5076'],
     ['Hamilton', 'Bridgeport', '3791  Bridgeport Rd', '905-389-4463'],
     ['JERRAWA', 'Marlin', '40 Marlin Avenue', '(02) 6175 8642'],
     ['Rudersberg', 'Pasewalker', 'Pasewalker Straße 5', '07183 30 07 96'],
     ['København K', 'Toftvej', 'Toftvej 35', '21-90-47700'],
     ['Guadalajara', 'Revolucion', 'Av. Revolucion 737', '33 36175334'],
     ['Poughkeepsie', 'Old Dear Lane', '4927 Old Dear Lane', '845-857-0825'],
     ['Elgin', 'Pineview', '2491 Pineview Drive', '507-876-0713'],
     ['Oak Brook', 'Vesta', '2591 Vesta Drive', '773-757-1932'],
     ['Annapolis Junction', 'Bluff', '889 Bluff Street', '301-787-8206'],
     ['Los Angeles', 'Jett', '1014 Jett Lane', '310-718-6212'],
     ['Arlington', 'Single', '3158 Single Street', '781-646-1715'],
     ['Syracuse', 'Plainfield', '3741 Plainfield Avenue', '315-576-8242'],
     ['San Mateo', 'Thunder', '2425 Thunder Road', '650-577-7537'],
     ['Valdosta', 'Junkins', '1022 Junkins Avenue', '229-460-4970'],
     ['Hialeah', 'Poplar', '101 Poplar Lane', '305-540-4990'],
     ['Lexington', 'Straford', '793 Straford Park', '606-614-9190'],
     ['Johnsonburg', 'Custer', '2566 Custer Street', '814-965-6502'],
     ['Hokkaido',
      'Kita',
      '244-1192, Kita 6-jonishi, Abashiri-shi, Hokkaido',
      '8134-191-6900'],
     ['Port Chester', 'Ward', '1503 Ward Road', '914-933-3946'],
     ['Salt Lake City', 'Kemper', '4745 Kemper Lane', '801-927-7191'],
     ['Villaluenga del Rosario',
      'Vientos',
      'C/ Rosa de los Vientos 36',
      '736 301 706'],
     ['London',
      'King Street',
      '733 King Street EAST CENTRAL LONDON EC86 0YR',
      '916-863-6154'],
     ['GLOUCESTER',
      'New Road',
      '8857 New Road GLOUCESTER GL79 3CZ',
      '252-218-2526'],
     ['NEWPORT', 'George', '760 George Street NEWPORT NP73 0CH', '803-535-5627'],
     ['TAUNTON', 'The Green', '749 The Green TAUNTON TA27 9JQ', '580-730-2253'],
     ['SOUTHEND-ON-SEA',
      'Springfield',
      '271 Springfield Road SOUTHEND-ON-SEA SS98 1PA',
      '240-597-0099'],
     ['SHEFFIELD',
      'Highfield',
      '500 Highfield Road SHEFFIELD S98 6VM',
      '210-727-9560'],
     ['HULL', 'Albert', '8772 Albert Road HULL HU2 6SN', '919-887-6912'],
     ['SHREWSBURY',
      'Church',
      '38 Church Street SHREWSBURY SY79 9TY',
      '614-449-8617'],
     ['DURHAM', 'DURHAM', '12 New Road DURHAM DH78 4XK', '830-229-4983'],
     ['Honolulu', 'Don Jackson', '4153 Don Jackson Lane', '303-284-0638'],
     ['Wayne', 'Bombardier', '2438 Bombardier Way', '734-981-4470'],
     ['Milton', 'Courtright', '3258 Courtright Street', '701-496-3125'],
     ['NEWCASTLE',
      'The Grove',
      '9982 The Grove NEWCASTLE UPON TYNE NE21 0RM',
      '605-677-5038'],
     ['BRISTOL',
      'Richmond',
      '8253 Richmond Road BRISTOL BS70 9LU',
      '209-848-9572'],
     ['BOURNEMOUTH',
      'Broadway',
      '22 Broadway BOURNEMOUTH BH73 8ON',
      '760-464-6831'],
     ['LEICESTER',
      'Green Lane',
      '748 Green Lane LEICESTER LE77 6VE',
      '508-272-0114'],
     ['SUNDERLAND', 'New Road', '48 New Road SUNDERLAND SR39 2NY', '845-915-5076'],
     ['BOLTON', 'North Street', '19 North Street BOLTON BL77 4TC', '973-640-3581'],
     ['SOUTHAMPTON',
      'King Street',
      '60 King Street SOUTHAMPTON SO75 5PZ',
      '541-579-1559'],
     ['BLACKPOOL',
      'Highfield',
      '8579 Highfield Road BLACKPOOL FY68 1LM',
      '336-212-0408'],
     ['DARLINGTON',
      'High Street',
      '9175 High Street DARLINGTON DL86 7BQ',
      '845-340-3808'],
     ['LIVERPOOL', 'Main Road', '100 Main Road LIVERPOOL L80 4XI', '561-526-2625'],
     ['MANCHESTER', 'Park Lane', '52 Park Lane MANCHESTER M8 0KJ', '801-608-1332'],
     ['SHEFFIELD',
      'Kings Road',
      '79 Kings Road SHEFFIELD S88 2KY',
      '510-214-0266'],
     ['BOLTON', 'Mill', '95 Mill Road BOLTON BL48 9OR', '785-253-0084'],
     ['SWANSEA', 'South', '466 South Street SWANSEA SA34 7PT', '585-749-2163'],
     ['LEEDS', 'Mill Lane', '308 Mill Lane LEEDS LS35 5JS', '312-362-2484'],
     ['SWANSEA', 'York Road', '222 York Road SWANSEA SA87 4WS', '570-603-5788'],
     ['CARDIFF',
      'West Street',
      '125 West Street CARDIFF CF95 6CN',
      '802-738-8477'],
     ['LEICESTER', 'New Road', '64 New Road LEICESTER LE37 3VW', '507-771-8684'],
     ['SOUTHAMPTON',
      'Main Street',
      '90 Main Street SOUTHAMPTON SO41 5RP',
      '720-634-0176'],
     ['IPSWICH',
      'Stanley Road',
      '8339 Stanley Road IPSWICH IP79 6SN',
      '313-930-0331'],
     ['Tokyo',
      'Ebisu',
      '481-1228, Ebisu Ebisugadempureisu(28-kai), Shibuya-ku',
      '8188-165-7118'],
     ['Seoul',
      'Gongdeok',
      '310-5, Samseongraemiangongdeok 3 chaapateu, Gongdeok-dong, Mapo-gu',
      '02-455-1973']]




```python
wb = Workbook(write_only=True)
ws = wb.create_sheet('branch')
```


```python
ws.append(['name', 'address', 'phone number'])
```


```python
branch_infos = []
branch = soup.select('.branch')
name = soup.select('.branch .city')
addr = soup.select('.branch .address')
phnm = soup.select('.branch .phoneNum')
for n in range(len(branch)):
    ws.append([name[n].get_text(), addr[n].get_text(), phnm[n].get_text()])
wb.save('orangebottle.xlsx')
```

## <a id='toc1_5_'></a>[csv로도 저장할 수 있다](#toc0_)


```python
csv_file = open('oragneb.csv', 'w', encoding='utf-8')
csv_writer = csv.writer(csv_file)
```


```python
csv_writer.writerow(['name', 'address', 'phone number'])
```




    27




```python
branch_infos = []
branch = soup.select('.branch')
name = soup.select('.branch .city')
addr = soup.select('.branch .address')
phnm = soup.select('.branch .phoneNum')
for n in range(len(branch)):
    csv_writer.writerow([name[n].get_text(), addr[n].get_text(), phnm[n].get_text()])
csv_file.close()
```


```python
# https://workey.codeit.kr/ratings/index?year=2010&month=1&weekIndex=0

wb = Workbook(write_only=True)

for y in range(3):
    ws = wb.create_sheet(f'201{y}')
    ws.append(['period', 'rank', 'channel', 'name', 'rate'])
    for m in range(1,13):
        for w in range(5):
            response = requests.get(f"https://workey.codeit.kr/ratings/index?year=201{y}&month={m}&weekIndex={w}")
            rating_page = response.text
            soup = BeautifulSoup(rating_page, 'html.parser')
            
            for tr in soup.select('tr')[1:]:
                td = tr.select('td')
                period = f"201{y}-{m}-{w+1}"
                row = [
                    period, #period
                    td[0].get_text(), #rank
                    td[1].get_text(), #channel
                    td[2].get_text(), #name
                    td[3].get_text() # rate
                ]
                ws.append(row)
wb.save('ratingsindex.xlsx')
            
```

    Exception ignored in: <generator object WorksheetWriter.get_stream at 0x000001D3F8DE4970>
    Traceback (most recent call last):
      File "c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\openpyxl\worksheet\_writer.py", line 289, in get_stream
        with xf.element("worksheet", xmlns=SHEET_MAIN_NS):
      File "src\lxml\serializer.pxi", line 1834, in lxml.etree._FileWriterElement.__exit__
      File "src\lxml\serializer.pxi", line 1570, in lxml.etree._IncrementalFileWriter._write_end_element
    lxml.etree.LxmlSyntaxError: inconsistent exit action in context manager
    Exception ignored in: <generator object WriteOnlyWorksheet._write_rows at 0x000001D3F8DE4BA0>
    Traceback (most recent call last):
      File "c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\openpyxl\worksheet\_write_only.py", line 66, in _write_rows
        with xf.element("sheetData"):
      File "src\lxml\serializer.pxi", line 1834, in lxml.etree._FileWriterElement.__exit__
      File "src\lxml\serializer.pxi", line 1568, in lxml.etree._IncrementalFileWriter._write_end_element
    lxml.etree.LxmlSyntaxError: not in an element
    


```python
# https://workey.codeit.kr/ratings/index?year=2010&month=1&weekIndex=0

wb = Workbook(write_only=True)
ws = wb.create_sheet('sbs')
ws.append(['period', 'rank', 'name', 'rate'])

for y in range(9):
    for m in range(1,13):
        for w in range(5):
            response = requests.get(f"https://workey.codeit.kr/ratings/index?year=201{y}&month={m}&weekIndex={w}")
            rating_page = response.text
            soup = BeautifulSoup(rating_page, 'html.parser')            
            for tr in soup.select('tr')[1:]:
                td = tr.select('td')
                period = f"201{y}-{m}-{w+1}"
                row = [
                    period, #period
                    td[0].get_text(), #rank
                    # td[1].get_text(), #channel
                    td[2].get_text(), #name
                    td[3].get_text() # rate
                ]
                if td[1].get_text() == 'SBS':
                    ws.append(row)
wb.save('sbs.xlsx')
            
```

## <a id='toc1_6_'></a>[selenium이란](#toc0_)
---
selenium automates browsers 브라우저를 자동화해준다  
클릭, 스크롤, 입력 등을 자동화 한다

약간 매크로 같네?


```python
driver = webdriver.Chrome()
driver.get('https://codeit.kr')
driver.quit()
```

wait의 종류들  
https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html#module-selenium.webdriver.support.expected_conditions

동작 종류들  
https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.action_chains.html

아래 beautiful soup을 selenium으로 구현하면

```python
response = requests.get("https://workey.codeit.kr/orangebottle/index")
rpage = response.text

soup = BeautifulSoup(rpage, 'html.parser')
branch = soup.select('.branch')
st = []
for tag in branch:
    wh = tag.stripped_strings
    st.append(list(wh))    
st
```


```python
driver = webdriver.Chrome()
# driver.implicitly_wait(3)
br = []

driver.get("https://workey.codeit.kr/orangebottle/index")
branch = driver.find_elements(By.CSS_SELECTOR, '.branch')
for b in branch:
    mat = list(b.text.split('\n')) # 크 split으로 쪼개면 된다 천재!!!!!!!!!!
    row = [
        mat[0], # name
        mat[2], # address
        mat[3] # phone number
        ]
    br.append(row)
br
```




    [['San Jose', '4823 Fairway Drive', '707-514-0033'],
     ['GREAT BARTON', '106 Lammas Street', '070 3460 5076'],
     ['Hamilton', '3791 Bridgeport Rd', '905-389-4463'],
     ['JERRAWA', '40 Marlin Avenue', '(02) 6175 8642'],
     ['Rudersberg', 'Pasewalker Straße 5', '07183 30 07 96'],
     ['København K', 'Toftvej 35', '21-90-47700'],
     ['Guadalajara', 'Av. Revolucion 737', '33 36175334'],
     ['Poughkeepsie', '4927 Old Dear Lane', '845-857-0825'],
     ['Elgin', '2491 Pineview Drive', '507-876-0713'],
     ['Oak Brook', '2591 Vesta Drive', '773-757-1932'],
     ['Annapolis Junction', '889 Bluff Street', '301-787-8206'],
     ['Los Angeles', '1014 Jett Lane', '310-718-6212'],
     ['Arlington', '3158 Single Street', '781-646-1715'],
     ['Syracuse', '3741 Plainfield Avenue', '315-576-8242'],
     ['San Mateo', '2425 Thunder Road', '650-577-7537'],
     ['Valdosta', '1022 Junkins Avenue', '229-460-4970'],
     ['Hialeah', '101 Poplar Lane', '305-540-4990'],
     ['Lexington', '793 Straford Park', '606-614-9190'],
     ['Johnsonburg', '2566 Custer Street', '814-965-6502'],
     ['Hokkaido',
      '244-1192, Kita 6-jonishi, Abashiri-shi, Hokkaido',
      '8134-191-6900'],
     ['Port Chester', '1503 Ward Road', '914-933-3946'],
     ['Salt Lake City', '4745 Kemper Lane', '801-927-7191'],
     ['Villaluenga del Rosario', 'C/ Rosa de los Vientos 36', '736 301 706'],
     ['London', '733 King Street EAST CENTRAL LONDON EC86 0YR', '916-863-6154'],
     ['GLOUCESTER', '8857 New Road GLOUCESTER GL79 3CZ', '252-218-2526'],
     ['NEWPORT', '760 George Street NEWPORT NP73 0CH', '803-535-5627'],
     ['TAUNTON', '749 The Green TAUNTON TA27 9JQ', '580-730-2253'],
     ['SOUTHEND-ON-SEA',
      '271 Springfield Road SOUTHEND-ON-SEA SS98 1PA',
      '240-597-0099'],
     ['SHEFFIELD', '500 Highfield Road SHEFFIELD S98 6VM', '210-727-9560'],
     ['HULL', '8772 Albert Road HULL HU2 6SN', '919-887-6912'],
     ['SHREWSBURY', '38 Church Street SHREWSBURY SY79 9TY', '614-449-8617'],
     ['DURHAM', '12 New Road DURHAM DH78 4XK', '830-229-4983'],
     ['Honolulu', '4153 Don Jackson Lane', '303-284-0638'],
     ['Wayne', '2438 Bombardier Way', '734-981-4470'],
     ['Milton', '3258 Courtright Street', '701-496-3125'],
     ['NEWCASTLE', '9982 The Grove NEWCASTLE UPON TYNE NE21 0RM', '605-677-5038'],
     ['BRISTOL', '8253 Richmond Road BRISTOL BS70 9LU', '209-848-9572'],
     ['BOURNEMOUTH', '22 Broadway BOURNEMOUTH BH73 8ON', '760-464-6831'],
     ['LEICESTER', '748 Green Lane LEICESTER LE77 6VE', '508-272-0114'],
     ['SUNDERLAND', '48 New Road SUNDERLAND SR39 2NY', '845-915-5076'],
     ['BOLTON', '19 North Street BOLTON BL77 4TC', '973-640-3581'],
     ['SOUTHAMPTON', '60 King Street SOUTHAMPTON SO75 5PZ', '541-579-1559'],
     ['BLACKPOOL', '8579 Highfield Road BLACKPOOL FY68 1LM', '336-212-0408'],
     ['DARLINGTON', '9175 High Street DARLINGTON DL86 7BQ', '845-340-3808'],
     ['LIVERPOOL', '100 Main Road LIVERPOOL L80 4XI', '561-526-2625'],
     ['MANCHESTER', '52 Park Lane MANCHESTER M8 0KJ', '801-608-1332'],
     ['SHEFFIELD', '79 Kings Road SHEFFIELD S88 2KY', '510-214-0266'],
     ['BOLTON', '95 Mill Road BOLTON BL48 9OR', '785-253-0084'],
     ['SWANSEA', '466 South Street SWANSEA SA34 7PT', '585-749-2163'],
     ['LEEDS', '308 Mill Lane LEEDS LS35 5JS', '312-362-2484'],
     ['SWANSEA', '222 York Road SWANSEA SA87 4WS', '570-603-5788'],
     ['CARDIFF', '125 West Street CARDIFF CF95 6CN', '802-738-8477'],
     ['LEICESTER', '64 New Road LEICESTER LE37 3VW', '507-771-8684'],
     ['SOUTHAMPTON', '90 Main Street SOUTHAMPTON SO41 5RP', '720-634-0176'],
     ['IPSWICH', '8339 Stanley Road IPSWICH IP79 6SN', '313-930-0331'],
     ['Tokyo',
      '481-1228, Ebisu Ebisugadempureisu(28-kai), Shibuya-ku',
      '8188-165-7118'],
     ['Seoul',
      '310-5, Samseongraemiangongdeok 3 chaapateu, Gongdeok-dong, Mapo-gu',
      '02-455-1973']]




```python
driver = webdriver.Chrome()
driver.get("https://workey.codeit.kr/orangebottle/index")
driver.execute_script('window.scrollTo(0, 1000);')
height = driver.execute_script('return document.body.scrollHeight')
print(height)
```

    4977
    

- 내용이 끝날 때까지 스크롤하기


```python
last_h = driver.execute_script('return documnet.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(0.5)
    new_h = driver.execute_script('return documnet.body.scrollHeight')
    if new_h == last_h:
        break
    last_h = new_h
```


```python
driver = webdriver.Chrome()
driver.get("https://workey.codeit.kr/orangebottle/index")
# driver.execute_script('window.scrollTo(0, 1000);')
last_h = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(0.5)
    new_h = driver.execute_script('return document.body.scrollHeight')
    if new_h == last_h:
        break
    last_h = new_h
```

ㅋㅋㅋㅋㅋㅋㅋ 여러번 틀린 패턴 find_elements 가 아니라 element해놓고 iterable 하지 않다고 갸우뚱!

하 진짜 한참 고생했네 코드가 맞는데 왜 오류가 뜨지 했더니  
ElementNotInteractableException 이 에러는 엘리먼트가 상호작용 할 수 없을 때 뜨는 거다  
왜 상호작용 할 수 없나 봤더니 DOM 상에 있지만 display 되지 않거나 viewport 안에 스크롤 되지 못 할 때도 그렇다고 한다  
그래서 아차 싶어서 브라우저가 켜질 때 최대화면으로 열어주니 잘만 된다 ... 후 참말로 !!!  
https://www.selenium.dev/selenium/docs/api/java/org/openqa/selenium/ElementNotInteractableException.html

누가 질문 달고 스스로 답변한 내용에서 web driver로 창을 최대화 할 수 있는 코드도 찾았다

아예 java script로 닫기 버튼을 누르게 수행하는 방법도 있다고 한다  
구글링으로 찾았다고 한다 존경스럽다  
```python
element = driver.find_element_by_css_selector('.close-btn')

driver.execute_script("arguments[0].click();", element)
```


```python
# 사이트 로딩
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://workey.codeit.kr/costagram/index")
# driver.fullscreen_window()

# 창 최대화 ## 닫기 버튼을 할 때 창에 안 보이면 클릭으로 하지 못 한다
driver.maximize_window()
# driver.minimize_window()

# 엑셀을 만든다
wb = Workbook(write_only=True)
ws = wb.create_sheet('costagram')
ws.append(['img_url', 'content', 'hashtag', 'likes', 'replies'])

# 이미지 url 리스트를 만든다
urls = []

# 로그인
driver.find_element(By.CSS_SELECTOR, '.top-nav__login-link').click()
driver.find_element(By.CSS_SELECTOR, '.login-container__login-input').send_keys('codeit')
driver.find_element(By.CSS_SELECTOR, '.login-container__password-input').send_keys('datascience')
driver.find_element(By.CSS_SELECTOR, '.login-container__login-button').click()

# 스크롤을 끝까지 내리고
last_h = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(0.5)
    new_h = driver.execute_script('return document.body.scrollHeight')
    if new_h == last_h:
        break
    last_h = new_h
    


# 포스팅이 있는 만큼 반복한다

# driver.find_element(By.CSS_SELECTOR, 'div .post').click()
posts = driver.find_elements(By.CSS_SELECTOR, 'div .post')
# close = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.close-btn')))
for post in posts:
    post.click()
    # 내용을 수집한다
    txt = driver.find_element(By.CSS_SELECTOR, '.content__text').text
    img = driver.find_element(By.CSS_SELECTOR, '.post-container__image').get_attribute('style').split('\"')[1] # 이건 컨닝했다
    url = "https://workey.codeit.kr/" + img
    tag = driver.find_element(By.CSS_SELECTOR, '.content__tag').text    
    likes = driver.find_element(By.CSS_SELECTOR, '.content__like-count').text
    replies = driver.find_element(By.CSS_SELECTOR, '.content__comment-count').text
        
    row = [
        url,
        txt,
        tag,
        likes,
        replies        
    ]
    # 워크시트에 붙인다
    ws.append(row)
    # 이미지 다운로드를 위해 url을 리스트에 넣는다
    urls.append(url)
    # 종료 버튼을 찾고 누른다
    close = driver.find_element(By.CLASS_NAME, 'close-btn')
    close.click()


#저장하고
wb.save('costa.xlsx')

#이미지를 다운 받는다
for i in range(len(urls)):
    img = urls[i]
    response = requests.get(img)
    filename = f'post{i}.jpeg'
    with open('./imgs/' + filename, 'wb+') as f:
        f.write(response.content)

# 웹 드라이버 종료
driver.quit()
```

### <a id='toc1_6_1_'></a>[select](#toc0_)
---

url 주소가 바뀌는 게 아니라 화면에서 옵션을 골라야 하는 경우

혼자 실습

인덴테이션 차이로 결과가 두 번 출력되길래 py 만들어서 디버깅 했다  
확실히 디버깅 해야 왜 그런지 알 수 있다  
의도대로 되지 않으면 꼭 디버깅 해보자


```python
########## version_1
########## 너무 느리다 bs4를 같이 섞어볼까?

################# 사이트 로딩
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("http://info.nec.go.kr/main/showDocument.xhtml?electionId=0000000000&topMenuId=CP&secondMenuId=CPRI03")
#혹시 모르니 창 최대화
driver.maximize_window()

################# 엑셀을 만든다
# wb = Workbook(write_only=True)
# ws = wb.create_sheet('election')
# ws.append(['region', 'party', 'name', 'sex', 'dateofbirth', 'occupation', 'education', 'etc'])


################# 옵션 설정을 위한 셀렉트 준비

# prev = driver.find_element(By.CSS_SELECTOR, '.eright')
# cand = driver.find_element(By.CSS_SELECTOR, '.m_CPon')
# prevcand = driver.find_element(By.CSS_SELECTOR, '.m_CPon')
congress = driver.find_element(By.CSS_SELECTOR, '#electionType2')
year = driver.find_element(By.CSS_SELECTOR, '#electionName')
election = driver.find_element(By.CSS_SELECTOR, '#electionCode')
code = driver.find_element(By.CSS_SELECTOR, '#cityCode')
btn = driver.find_element(By.CSS_SELECTOR, '#searchBtn')

# # 옵션 이름으로 선택 (웹사이트에서 보이는 옵션 이름)
# cityCode_select.select_by_visible_text('서울특별시')

# # 옵션의 value로 선택 ('서울특별시' 옵션의 value는 1100)
# cityCode_select.select_by_value('1100')

# # 옵션의 인덱스로 선택 ('서울특별시'는 두 번째 옵션)
# cityCode_select.select_by_index(1)
# prev.click()
congress.click()
for i in range(1, 4):
    Select(year).select_by_index(i)
    WebDriverWait(driver, 3).until(EC.visibility_of(election))
    Select(election).select_by_value('2')
    WebDriverWait(driver, 3).until(EC.visibility_of(code))
    Select(code).select_by_index(1)
    btn.click()
    trs = driver.find_elements(By.CSS_SELECTOR, 'tbody tr')
    for tr in trs:
        tds = tr.find_elements(By.CSS_SELECTOR, 'td')
        lt = []
        for td in tds:            
            lt.append(td.text)
        # print(lt)
        if lt:
            if lt[1] == '1':
                reg = lt[0]
                par = lt[2]
                name = lt[3].split('\n')[0] + lt[3].split('\n')[1]
                sex = lt[4]
                dob = lt[5].split('\n')[0] + lt[5].split('\n')[1]
                occ = lt[6]
                edu = lt[7]
                etc = lt[8]
                print(reg, par, name, sex, dob, occ, edu, etc)
                # ws.append(lt)
# wb.save('election.xlsx')
# driver.quit()
            
        # td = tr.text.split(' ')
        # if td[0]:            
        #     region = td[0]
        #     party = td[2]            
        #     name = td[3].split('\n')[0] + td[3].split('\n')[1]
        #     sex = td[4]
        #     dateofbirth = td[5].split('\n')[0] + td[5].split('\n')[1]
        #     occupation = td[6]
        
    # row = [
        
    # ]
    
```

    종로구 더불어민주당 이낙연(李洛淵) 남 1952.12.20(67세) 정당인 서울대학교 법과대학 법학과 졸업 (현)민주당 코로나19국난극복위원장
    (전)제45대 국무총리
    중구성동구갑 더불어민주당 홍익표(洪翼杓) 남 1967.11.20(52세) 정치인 한양대학교 대학원 정치외교학과 졸업(정치학박사) (현)국회의원(제19대.20대)
    (전)더불어민주당 수석대변인
    

    Exception ignored in: <generator object WorksheetWriter.get_stream at 0x000002BDF2E23760>
    Traceback (most recent call last):
      File "c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\openpyxl\worksheet\_writer.py", line 289, in get_stream
        with xf.element("worksheet", xmlns=SHEET_MAIN_NS):
      File "src\lxml\serializer.pxi", line 1834, in lxml.etree._FileWriterElement.__exit__
      File "src\lxml\serializer.pxi", line 1570, in lxml.etree._IncrementalFileWriter._write_end_element
    lxml.etree.LxmlSyntaxError: inconsistent exit action in context manager
    Exception ignored in: <generator object WriteOnlyWorksheet._write_rows at 0x000002BDF2E23990>
    Traceback (most recent call last):
      File "c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\openpyxl\worksheet\_write_only.py", line 66, in _write_rows
        with xf.element("sheetData"):
      File "src\lxml\serializer.pxi", line 1834, in lxml.etree._FileWriterElement.__exit__
      File "src\lxml\serializer.pxi", line 1568, in lxml.etree._IncrementalFileWriter._write_end_element
    lxml.etree.LxmlSyntaxError: not in an element
    


    ---------------------------------------------------------------------------

    WebDriverException                        Traceback (most recent call last)

    Cell In[43], line 44
         42 trs = driver.find_elements(By.CSS_SELECTOR, 'tbody tr')
         43 for tr in trs:
    ---> 44     tds = tr.find_elements(By.CSS_SELECTOR, 'td')
         45     lt = []
         46     for td in tds:            
    

    File c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\selenium\webdriver\remote\webelement.py:439, in WebElement.find_elements(self, by, value)
        436     by = By.CSS_SELECTOR
        437     value = f'[name="{value}"]'
    --> 439 return self._execute(Command.FIND_CHILD_ELEMENTS, {"using": by, "value": value})["value"]
    

    File c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\selenium\webdriver\remote\webelement.py:395, in WebElement._execute(self, command, params)
        393     params = {}
        394 params["id"] = self._id
    --> 395 return self._parent.execute(command, params)
    

    File c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\selenium\webdriver\remote\webdriver.py:346, in WebDriver.execute(self, driver_command, params)
        344 response = self.command_executor.execute(driver_command, params)
        345 if response:
    --> 346     self.error_handler.check_response(response)
        347     response["value"] = self._unwrap_value(response.get("value", None))
        348     return response
    

    File c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\selenium\webdriver\remote\errorhandler.py:245, in ErrorHandler.check_response(self, response)
        243         alert_text = value["alert"].get("text")
        244     raise exception_class(message, screen, stacktrace, alert_text)  # type: ignore[call-arg]  # mypy is not smart enough here
    --> 245 raise exception_class(message, screen, stacktrace)
    

    WebDriverException: Message: disconnected: unable to send message to renderer
      (failed to check if window was closed: disconnected: not connected to DevTools)
      (Session info: chrome=114.0.5735.134)
    Stacktrace:
    Backtrace:
    	GetHandleVerifier [0x0057A813+48355]
    	(No symbol) [0x0050C4B1]
    	(No symbol) [0x00415358]
    	(No symbol) [0x00407120]
    	(No symbol) [0x004077AA]
    	(No symbol) [0x00417271]
    	(No symbol) [0x0041781F]
    	(No symbol) [0x004199E1]
    	(No symbol) [0x00419A80]
    	(No symbol) [0x0044061C]
    	(No symbol) [0x00440B3B]
    	(No symbol) [0x00439D41]
    	(No symbol) [0x0045A784]
    	(No symbol) [0x00439A36]
    	(No symbol) [0x0045AA94]
    	(No symbol) [0x0046C922]
    	(No symbol) [0x0045A536]
    	(No symbol) [0x004382DC]
    	(No symbol) [0x004393DD]
    	GetHandleVerifier [0x007DAABD+2539405]
    	GetHandleVerifier [0x0081A78F+2800735]
    	GetHandleVerifier [0x0081456C+2775612]
    	GetHandleVerifier [0x006051E0+616112]
    	(No symbol) [0x00515F8C]
    	(No symbol) [0x00512328]
    	(No symbol) [0x0051240B]
    	(No symbol) [0x00504FF7]
    	BaseThreadInitThunk [0x767B0419+25]
    	RtlGetAppContainerNamedObjectPath [0x77B4662D+237]
    	RtlGetAppContainerNamedObjectPath [0x77B465FD+189]
    



```python
lt = ['']
print(lt)
```

    ['']
    


```python
bool(lt[0])
```




    False




```python
########## version_2 SE + BS4
########## 훨~~~~~~~~~~~~~씬 빨라졌다 bs4는 html을 text로 들고 온 다음 정보만 파싱해서 그런걸까?

################# 사이트 로딩
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("http://info.nec.go.kr/main/showDocument.xhtml?electionId=0000000000&topMenuId=CP&secondMenuId=CPRI03")
#혹시 모르니 창 최대화
driver.maximize_window()

################# 엑셀을 만든다
wb = Workbook(write_only=True)
ws = wb.create_sheet('election')
ws.append(['region', 'party', 'name', 'sex', 'dateofbirth', 'occupation', 'education', 'etc'])


################# 옵션 설정을 위한 셀렉트 준비

congress = driver.find_element(By.CSS_SELECTOR, '#electionType2')
year = driver.find_element(By.CSS_SELECTOR, '#electionName')
election = driver.find_element(By.CSS_SELECTOR, '#electionCode')
code = driver.find_element(By.CSS_SELECTOR, '#cityCode')
btn = driver.find_element(By.CSS_SELECTOR, '#searchBtn')
congress.click()

# 연도 마다 돌아가면서
for i in range(1, 4):
    Select(year).select_by_index(i)
    WebDriverWait(driver, 3).until(EC.visibility_of(election))
    Select(election).select_by_value('2')
    WebDriverWait(driver, 3).until(EC.visibility_of(code))
    Select(code).select_by_index(1)
    btn.click()
    year = driver.find_element(By.CSS_SELECTOR, '#electionName')
    election = driver.find_element(By.CSS_SELECTOR, '#electionCode')
    code = driver.find_element(By.CSS_SELECTOR, '#cityCode')
    btn = driver.find_element(By.CSS_SELECTOR, '#searchBtn')
    
    # html을 bs4로 파싱하기
    elec_page = driver.page_source
    soup = BeautifulSoup(elec_page, 'html.parser')
    trs = soup.select('tbody tr')
    for tr in trs:
        tds = tr.select('td')
        lt = []
        for td in tds:
            lt.append(td.get_text())
        # print(lt)
        # reg = lt[0]
        # par = lt[2]
        # name = lt[3]
        # sex = lt[4]
        # dob = lt[5]
        # occ = lt[6]
        # edu = lt[7]
        # etc = lt[8]
        ws.append(lt)

wb.save('election.xlsx')        

driver.quit()
```

    Exception ignored in: <generator object WorksheetWriter.get_stream at 0x000002BDF3033300>
    Traceback (most recent call last):
      File "c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\openpyxl\worksheet\_writer.py", line 289, in get_stream
        with xf.element("worksheet", xmlns=SHEET_MAIN_NS):
      File "src\lxml\serializer.pxi", line 1834, in lxml.etree._FileWriterElement.__exit__
      File "src\lxml\serializer.pxi", line 1570, in lxml.etree._IncrementalFileWriter._write_end_element
    lxml.etree.LxmlSyntaxError: inconsistent exit action in context manager
    Exception ignored in: <generator object WriteOnlyWorksheet._write_rows at 0x000002BDF30330D0>
    Traceback (most recent call last):
      File "c:\Users\moonlight\AppData\Local\Programs\Python\Python310\lib\site-packages\openpyxl\worksheet\_write_only.py", line 66, in _write_rows
        with xf.element("sheetData"):
      File "src\lxml\serializer.pxi", line 1834, in lxml.etree._FileWriterElement.__exit__
      File "src\lxml\serializer.pxi", line 1568, in lxml.etree._IncrementalFileWriter._write_end_element
    lxml.etree.LxmlSyntaxError: not in an element
    

## <a id='toc1_7_'></a>[수료증](https://www.codeit.kr/certificates/qEP3S-5YA0Q-fIyzW-uGEZw) [&#8593;](#toc0_)
