---
layout: single
title:  "natural language processing "
---

**Table of contents**<a id='toc0_'></a>    
- [natural language processing](#toc1_)    
  - [NLP 종류](#toc1_1_)    
    - [rule based approach](#toc1_1_1_)    
    - [전처리](#toc1_1_2_)    
      - [cleaning](#toc1_1_2_1_)    
        - [불용어 stopword](#toc1_1_2_1_1_)    
      - [정규화 normalization](#toc1_1_2_2_)    
      - [문장 토큰화 sentence tokenization](#toc1_1_2_3_)    
        - [POS part of speech tagging](#toc1_1_2_3_1_)    
        - [Penn Treebank POS tag](#toc1_1_2_3_2_)    
        - [word net](#toc1_1_2_3_3_)    
        - [표제어(사전적 어원) lemma 추출](#toc1_1_2_3_4_)    
      - [정수 인코딩 ineger encoding](#toc1_1_2_4_)    
        - [Padding](#toc1_1_2_4_1_)    
    - [감성 분석 sentiment analysis](#toc1_1_3_)    
      - [sentiwordnet은 감성 정보를 갖고 있다. wordnet의 단어 품사 순번 정보를 받아 올 수도 있다](#toc1_1_3_1_)    
      - [VADER valence aware dictionary and sentiment reasoner 감성 분석용 알고리즘](#toc1_1_3_2_)    
  - [국어](#toc1_2_)    
  - [수료증](#toc1_3_)    

<!-- vscode-jupyter-toc-config
	numbering=false
	anchor=true
	flat=false
	minLevel=1
	maxLevel=6
	/vscode-jupyter-toc-config -->
<!-- THIS CELL WILL BE REPLACED ON TOC UPDATE. DO NOT WRITE YOUR TEXT IN THIS CELL -->

# <a id='toc1_'></a>[natural language processing](#toc0_)

natural language : not artificial language  
artificial language : language intentionally constructed for interaction

natural language processing : making it easy for computers to analyze materials in natural language  
NLP involves natural language understanding, natural language generation

## <a id='toc1_1_'></a>[NLP 종류](#toc0_)
---
1. rule based approach
2. statistics based approach >>> machine learning use this approach

### <a id='toc1_1_1_'></a>[rule based approach](#toc0_)
---

difficulties:
1. 重義 homonym 표면적으로 동일한 단어가 여러 뜻을 나타낸다
2. paraphrase 동일한 뜻을 다양하게 표현한다
3. 단어 사이의 관계를 단어만으로 연결하기 어렵다
4. 국어의 띄어쓰기, 접사, 조사, 어순

### <a id='toc1_1_2_'></a>[전처리](#toc0_)
---

- 정제 cleaning: 오류, 비중요 제거
- 정규화: 중첩 >>> 통합
- 정수 인코딩: 인덱싱
- 토큰화 tokenization

#### <a id='toc1_1_2_1_'></a>[cleaning](#toc0_)
---

처리하기 위한 말뭉치를 corpus라 부른다  
이를 분석하기 위해 쪼갠 단위를 token이라 한다


```python
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.corpus import sentiwordnet as swn
from collections import Counter
from nltk.stem import PorterStemmer, LancasterStemmer, WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
```


```python
nltk.download('punkt')
```

    [nltk_data] Downloading package punkt to
    [nltk_data]     C:\Users\moonlight\AppData\Roaming\nltk_data...
    [nltk_data]   Package punkt is already up-to-date!
    




    True




```python
text = "Although it's not a happily-ever-after ending, it is very realistic."

# 단어 토큰화
tokenized_words = word_tokenize(text)

print(tokenized_words)
```

    ['Although', 'it', "'s", 'not', 'a', 'happily-ever-after', 'ending', ',', 'it', 'is', 'very', 'realistic', '.']
    


```python
from text import TEXT
print(TEXT)
```

    After reading the comments for this movie, I am not sure whether I should be angry, sad or sickened. Seeing comments typical of people who a)know absolutely nothing about the military or b)who base everything they think they know on movies like this or on CNN reports about Abu-Gharib makes me wonder about the state of intellectual stimulation in the world. At the time I type this the number of people in the US military: 1.4 million on Active Duty with another almost 900,000 in the Guard and Reserves for a total of roughly 2.3 million. The number of people indicted for abuses at at Abu-Gharib: Currently less than 20 That makes the total of people indicted .00083% of the total military. Even if you indict every single military member that ever stepped in to Abu-Gharib, you would not come close to making that a whole number.  The flaws in this movie would take YEARS to cover. I understand that it's supposed to be sarcastic, but in reality, the writer and director are trying to make commentary about the state of the military without an enemy to fight. In reality, the US military has been at its busiest when there are not conflicts going on. The military is the first called for disaster relief and humanitarian aid missions. When the tsunami hit Indonesia, devestating the region, the US military was the first on the scene. When the chaos of the situation overwhelmed the local governments, it was military leadership who looked at their people, the same people this movie mocks, and said make it happen. Within hours, food aid was reaching isolated villages. Within days, airfields were built, cargo aircraft started landing and a food distribution system was up and running. Hours and days, not weeks and months. Yes there are unscrupulous people in the US military. But then, there are in every walk of life, every occupation. But to see people on this website decide that 2.3 million men and women are all criminal, with nothing on their minds but thoughts of destruction or mayhem is an absolute disservice to the things that they do every day. One person on this website even went so far as to say that military members are in it for personal gain. Wow! Entry level personnel make just under $8.00 an hour assuming a 40 hour work week. Of course, many work much more than 40 hours a week and those in harm's way typically put in 16-18 hour days for months on end. That makes the pay well under minimum wage. So much for personal gain. I beg you, please make yourself familiar with the world around you. Go to a nearby base, get a visitor pass and meet some of the men and women you are so quick to disparage. You would be surprised. The military no longer accepts people in lieu of prison time. They require a minimum of a GED and prefer a high school diploma. The middle ranks are expected to get a minimum of undergraduate degrees and the upper ranks are encouraged to get advanced degrees.
    
    


```python
tokened = word_tokenize(TEXT)
voca = Counter(tokened)
voca
```




    Counter({'the': 30,
             '.': 28,
             ',': 21,
             'of': 15,
             'and': 14,
             'to': 13,
             'a': 12,
             'military': 12,
             'in': 12,
             'people': 9,
             'on': 9,
             'are': 9,
             'for': 7,
             'this': 7,
             'that': 6,
             'I': 5,
             'The': 5,
             'you': 5,
             'not': 4,
             'or': 4,
             'about': 4,
             'US': 4,
             'at': 4,
             'every': 4,
             'it': 4,
             'make': 4,
             'was': 4,
             'movie': 3,
             'be': 3,
             'who': 3,
             'they': 3,
             'Abu-Gharib': 3,
             'makes': 3,
             'number': 3,
             'million': 3,
             'with': 3,
             'total': 3,
             'would': 3,
             'an': 3,
             'there': 3,
             'days': 3,
             'hour': 3,
             'minimum': 3,
             'get': 3,
             'comments': 2,
             ')': 2,
             'know': 2,
             'nothing': 2,
             'base': 2,
             'state': 2,
             'world': 2,
             'time': 2,
             ':': 2,
             '2.3': 2,
             'indicted': 2,
             'than': 2,
             'That': 2,
             "'s": 2,
             'but': 2,
             'reality': 2,
             'is': 2,
             'first': 2,
             'aid': 2,
             'When': 2,
             'their': 2,
             'Within': 2,
             'hours': 2,
             'food': 2,
             'months': 2,
             'But': 2,
             'website': 2,
             'men': 2,
             'women': 2,
             'so': 2,
             'personal': 2,
             'gain': 2,
             'under': 2,
             '40': 2,
             'work': 2,
             'week': 2,
             'much': 2,
             'ranks': 2,
             'degrees': 2,
             'After': 1,
             'reading': 1,
             'am': 1,
             'sure': 1,
             'whether': 1,
             'should': 1,
             'angry': 1,
             'sad': 1,
             'sickened': 1,
             'Seeing': 1,
             'typical': 1,
             'absolutely': 1,
             'b': 1,
             'everything': 1,
             'think': 1,
             'movies': 1,
             'like': 1,
             'CNN': 1,
             'reports': 1,
             'me': 1,
             'wonder': 1,
             'intellectual': 1,
             'stimulation': 1,
             'At': 1,
             'type': 1,
             '1.4': 1,
             'Active': 1,
             'Duty': 1,
             'another': 1,
             'almost': 1,
             '900,000': 1,
             'Guard': 1,
             'Reserves': 1,
             'roughly': 1,
             'abuses': 1,
             'Currently': 1,
             'less': 1,
             '20': 1,
             '.00083': 1,
             '%': 1,
             'Even': 1,
             'if': 1,
             'indict': 1,
             'single': 1,
             'member': 1,
             'ever': 1,
             'stepped': 1,
             'come': 1,
             'close': 1,
             'making': 1,
             'whole': 1,
             'flaws': 1,
             'take': 1,
             'YEARS': 1,
             'cover': 1,
             'understand': 1,
             'supposed': 1,
             'sarcastic': 1,
             'writer': 1,
             'director': 1,
             'trying': 1,
             'commentary': 1,
             'without': 1,
             'enemy': 1,
             'fight': 1,
             'In': 1,
             'has': 1,
             'been': 1,
             'its': 1,
             'busiest': 1,
             'when': 1,
             'conflicts': 1,
             'going': 1,
             'called': 1,
             'disaster': 1,
             'relief': 1,
             'humanitarian': 1,
             'missions': 1,
             'tsunami': 1,
             'hit': 1,
             'Indonesia': 1,
             'devestating': 1,
             'region': 1,
             'scene': 1,
             'chaos': 1,
             'situation': 1,
             'overwhelmed': 1,
             'local': 1,
             'governments': 1,
             'leadership': 1,
             'looked': 1,
             'same': 1,
             'mocks': 1,
             'said': 1,
             'happen': 1,
             'reaching': 1,
             'isolated': 1,
             'villages': 1,
             'airfields': 1,
             'were': 1,
             'built': 1,
             'cargo': 1,
             'aircraft': 1,
             'started': 1,
             'landing': 1,
             'distribution': 1,
             'system': 1,
             'up': 1,
             'running': 1,
             'Hours': 1,
             'weeks': 1,
             'Yes': 1,
             'unscrupulous': 1,
             'then': 1,
             'walk': 1,
             'life': 1,
             'occupation': 1,
             'see': 1,
             'decide': 1,
             'all': 1,
             'criminal': 1,
             'minds': 1,
             'thoughts': 1,
             'destruction': 1,
             'mayhem': 1,
             'absolute': 1,
             'disservice': 1,
             'things': 1,
             'do': 1,
             'day': 1,
             'One': 1,
             'person': 1,
             'even': 1,
             'went': 1,
             'far': 1,
             'as': 1,
             'say': 1,
             'members': 1,
             'Wow': 1,
             '!': 1,
             'Entry': 1,
             'level': 1,
             'personnel': 1,
             'just': 1,
             '$': 1,
             '8.00': 1,
             'assuming': 1,
             'Of': 1,
             'course': 1,
             'many': 1,
             'more': 1,
             'those': 1,
             'harm': 1,
             'way': 1,
             'typically': 1,
             'put': 1,
             '16-18': 1,
             'end': 1,
             'pay': 1,
             'well': 1,
             'wage': 1,
             'So': 1,
             'beg': 1,
             'please': 1,
             'yourself': 1,
             'familiar': 1,
             'around': 1,
             'Go': 1,
             'nearby': 1,
             'visitor': 1,
             'pass': 1,
             'meet': 1,
             'some': 1,
             'quick': 1,
             'disparage': 1,
             'You': 1,
             'surprised': 1,
             'no': 1,
             'longer': 1,
             'accepts': 1,
             'lieu': 1,
             'prison': 1,
             'They': 1,
             'require': 1,
             'GED': 1,
             'prefer': 1,
             'high': 1,
             'school': 1,
             'diploma': 1,
             'middle': 1,
             'expected': 1,
             'undergraduate': 1,
             'upper': 1,
             'encouraged': 1,
             'advanced': 1})




```python
scarce = [key for key, value in voca.items() if value > 2]
len(scarce)
######################### seldom에 들어있지 않은 걸 수집하면 단어가 나올 때 마다 중복해서 리스트에 들어간다
######################### 그러나 Count에서 빈도수가 큰 것만 직접 들어가라고 하면 딱 한번만 리스트에 담긴다
```




    44




```python
seldom = [key for key, value in voca.items() if value <= 2]
len(seldom)
```




    234




```python
token = [word for word in tokened if word not in seldom]
len(token)
```




    306




```python
len(seldom)
```




    234




```python
len(token)
```




    306




```python
nshort = [word for word in token if len(word) > 2]
len(nshort)
```




    169




```python
def by_freq(tokenized, n):
    """remove infrequent words"""
    vocab = Counter(tokenized) # make a dict of {word : frequency}
    uncommon = [key for key, value in vocab.items() if value <= n] # make a list of infrequent words    
    common = [word for word in tokenized if word not in uncommon]
    return common
```


```python
def by_len(tokened, n):
    longgy = [word for word in tokened if len(word) > n]
    return longgy
```


```python
freqlen = by_len(by_freq(tokened, 2), 2)
freqlen
```




    ['the',
     'for',
     'this',
     'movie',
     'not',
     'people',
     'who',
     'about',
     'the',
     'military',
     'who',
     'they',
     'they',
     'this',
     'about',
     'Abu-Gharib',
     'makes',
     'about',
     'the',
     'the',
     'the',
     'this',
     'the',
     'number',
     'people',
     'the',
     'military',
     'million',
     'with',
     'the',
     'and',
     'for',
     'total',
     'million',
     'The',
     'number',
     'people',
     'for',
     'Abu-Gharib',
     'makes',
     'the',
     'total',
     'people',
     'the',
     'total',
     'military',
     'you',
     'every',
     'military',
     'that',
     'Abu-Gharib',
     'you',
     'would',
     'not',
     'that',
     'number',
     'The',
     'this',
     'movie',
     'would',
     'that',
     'the',
     'and',
     'are',
     'make',
     'about',
     'the',
     'the',
     'military',
     'the',
     'military',
     'there',
     'are',
     'not',
     'The',
     'military',
     'the',
     'for',
     'and',
     'the',
     'the',
     'the',
     'military',
     'was',
     'the',
     'the',
     'the',
     'the',
     'the',
     'was',
     'military',
     'who',
     'people',
     'the',
     'people',
     'this',
     'movie',
     'and',
     'make',
     'was',
     'days',
     'and',
     'was',
     'and',
     'and',
     'days',
     'not',
     'and',
     'there',
     'are',
     'people',
     'the',
     'military',
     'there',
     'are',
     'every',
     'every',
     'people',
     'this',
     'that',
     'million',
     'and',
     'are',
     'with',
     'the',
     'that',
     'they',
     'every',
     'this',
     'that',
     'military',
     'are',
     'for',
     'make',
     'hour',
     'hour',
     'and',
     'hour',
     'days',
     'for',
     'makes',
     'the',
     'minimum',
     'for',
     'you',
     'make',
     'with',
     'the',
     'you',
     'get',
     'and',
     'the',
     'and',
     'you',
     'are',
     'would',
     'The',
     'military',
     'people',
     'minimum',
     'and',
     'The',
     'are',
     'get',
     'minimum',
     'and',
     'the',
     'are',
     'get']




```python
Counter(TEXT)
```




    Counter({' ': 519,
             'e': 275,
             't': 209,
             'a': 178,
             'i': 173,
             'o': 173,
             'n': 151,
             'r': 141,
             's': 130,
             'h': 114,
             'l': 93,
             'm': 86,
             'd': 79,
             'u': 79,
             'y': 53,
             'p': 49,
             'c': 44,
             'w': 41,
             'f': 40,
             'g': 38,
             'b': 34,
             '.': 33,
             'k': 25,
             'v': 23,
             ',': 22,
             '0': 13,
             'T': 8,
             'A': 7,
             'I': 7,
             'S': 7,
             'G': 6,
             'W': 5,
             '-': 4,
             'U': 4,
             'E': 4,
             '1': 3,
             '4': 3,
             '2': 3,
             '3': 3,
             '8': 3,
             'Y': 3,
             ')': 2,
             'C': 2,
             'N': 2,
             ':': 2,
             'D': 2,
             'R': 2,
             "'": 2,
             'B': 2,
             'O': 2,
             'q': 2,
             '9': 1,
             '%': 1,
             'H': 1,
             '!': 1,
             'j': 1,
             '$': 1,
             '6': 1,
             'x': 1,
             '\n': 1})



##### <a id='toc1_1_2_1_1_'></a>[불용어 stopword](#toc0_)
---
분석 목적에 부합하지 않아 의미가 없는 단어  
불용어 세트를 만들어 놓고 해당 리스트에 있는 건 없애버린다


```python
nltk.download('stopwords')
stopset = set(stopwords.words('english'))
```

    [nltk_data] Downloading package stopwords to
    [nltk_data]     C:\Users\moonlight\AppData\Roaming\nltk_data...
    [nltk_data]   Package stopwords is already up-to-date!
    


```python
len(stopset)
```




    179




```python
stopset.add('hello')
stopset.remove('me')
stopset.remove('itself')
len(stopset)
```




    178




```python
def by_stop(tokenized_words, stop):
    new = [word for word in tokenized_words if word not in stop]
    return new
```


```python
fls = by_stop(freqlen, stopset)
fls
```




    ['movie',
     'people',
     'military',
     'Abu-Gharib',
     'makes',
     'number',
     'people',
     'military',
     'million',
     'total',
     'million',
     'The',
     'number',
     'people',
     'Abu-Gharib',
     'makes',
     'total',
     'people',
     'total',
     'military',
     'every',
     'military',
     'Abu-Gharib',
     'would',
     'number',
     'The',
     'movie',
     'would',
     'make',
     'military',
     'military',
     'The',
     'military',
     'military',
     'military',
     'people',
     'people',
     'movie',
     'make',
     'days',
     'days',
     'people',
     'military',
     'every',
     'every',
     'people',
     'million',
     'every',
     'military',
     'make',
     'hour',
     'hour',
     'hour',
     'days',
     'makes',
     'minimum',
     'make',
     'get',
     'would',
     'The',
     'military',
     'people',
     'minimum',
     'The',
     'get',
     'minimum',
     'get']



#### <a id='toc1_1_2_2_'></a>[정규화 normalization](#toc0_)
---

똑같은 뜻을 나타내는데 다른 문자를 쓸 때 정규화 normalization을 해준다  
예) Korea, ROK, Republic of Korea, South Korea

1. 대소문자 통합 : 대체로 소문자로 바꿔놓고 시작
2. 규칙 기반 정규화 : 동의어 사전을 만들고 통일하고 시작
3. 어간 추출 : 알고리즘에 따라 단어의 핵심이 되는 어간 stem 추출
4. 표제어 추출


```python
text = "What can I do for you? Do your homework now."

# 소문자로 변환
print(text.lower())
```

    what can i do for you? do your homework now.
    


```python
pstemmer = PorterStemmer()
lstemmer = LancasterStemmer()
```


```python
new = [pstemmer.stem(word) for word in tokened]
new
```




    ['after',
     'read',
     'the',
     'comment',
     'for',
     'thi',
     'movi',
     ',',
     'i',
     'am',
     'not',
     'sure',
     'whether',
     'i',
     'should',
     'be',
     'angri',
     ',',
     'sad',
     'or',
     'sicken',
     '.',
     'see',
     'comment',
     'typic',
     'of',
     'peopl',
     'who',
     'a',
     ')',
     'know',
     'absolut',
     'noth',
     'about',
     'the',
     'militari',
     'or',
     'b',
     ')',
     'who',
     'base',
     'everyth',
     'they',
     'think',
     'they',
     'know',
     'on',
     'movi',
     'like',
     'thi',
     'or',
     'on',
     'cnn',
     'report',
     'about',
     'abu-gharib',
     'make',
     'me',
     'wonder',
     'about',
     'the',
     'state',
     'of',
     'intellectu',
     'stimul',
     'in',
     'the',
     'world',
     '.',
     'at',
     'the',
     'time',
     'i',
     'type',
     'thi',
     'the',
     'number',
     'of',
     'peopl',
     'in',
     'the',
     'us',
     'militari',
     ':',
     '1.4',
     'million',
     'on',
     'activ',
     'duti',
     'with',
     'anoth',
     'almost',
     '900,000',
     'in',
     'the',
     'guard',
     'and',
     'reserv',
     'for',
     'a',
     'total',
     'of',
     'roughli',
     '2.3',
     'million',
     '.',
     'the',
     'number',
     'of',
     'peopl',
     'indict',
     'for',
     'abus',
     'at',
     'at',
     'abu-gharib',
     ':',
     'current',
     'less',
     'than',
     '20',
     'that',
     'make',
     'the',
     'total',
     'of',
     'peopl',
     'indict',
     '.00083',
     '%',
     'of',
     'the',
     'total',
     'militari',
     '.',
     'even',
     'if',
     'you',
     'indict',
     'everi',
     'singl',
     'militari',
     'member',
     'that',
     'ever',
     'step',
     'in',
     'to',
     'abu-gharib',
     ',',
     'you',
     'would',
     'not',
     'come',
     'close',
     'to',
     'make',
     'that',
     'a',
     'whole',
     'number',
     '.',
     'the',
     'flaw',
     'in',
     'thi',
     'movi',
     'would',
     'take',
     'year',
     'to',
     'cover',
     '.',
     'i',
     'understand',
     'that',
     'it',
     "'s",
     'suppos',
     'to',
     'be',
     'sarcast',
     ',',
     'but',
     'in',
     'realiti',
     ',',
     'the',
     'writer',
     'and',
     'director',
     'are',
     'tri',
     'to',
     'make',
     'commentari',
     'about',
     'the',
     'state',
     'of',
     'the',
     'militari',
     'without',
     'an',
     'enemi',
     'to',
     'fight',
     '.',
     'in',
     'realiti',
     ',',
     'the',
     'us',
     'militari',
     'ha',
     'been',
     'at',
     'it',
     'busiest',
     'when',
     'there',
     'are',
     'not',
     'conflict',
     'go',
     'on',
     '.',
     'the',
     'militari',
     'is',
     'the',
     'first',
     'call',
     'for',
     'disast',
     'relief',
     'and',
     'humanitarian',
     'aid',
     'mission',
     '.',
     'when',
     'the',
     'tsunami',
     'hit',
     'indonesia',
     ',',
     'devest',
     'the',
     'region',
     ',',
     'the',
     'us',
     'militari',
     'wa',
     'the',
     'first',
     'on',
     'the',
     'scene',
     '.',
     'when',
     'the',
     'chao',
     'of',
     'the',
     'situat',
     'overwhelm',
     'the',
     'local',
     'govern',
     ',',
     'it',
     'wa',
     'militari',
     'leadership',
     'who',
     'look',
     'at',
     'their',
     'peopl',
     ',',
     'the',
     'same',
     'peopl',
     'thi',
     'movi',
     'mock',
     ',',
     'and',
     'said',
     'make',
     'it',
     'happen',
     '.',
     'within',
     'hour',
     ',',
     'food',
     'aid',
     'wa',
     'reach',
     'isol',
     'villag',
     '.',
     'within',
     'day',
     ',',
     'airfield',
     'were',
     'built',
     ',',
     'cargo',
     'aircraft',
     'start',
     'land',
     'and',
     'a',
     'food',
     'distribut',
     'system',
     'wa',
     'up',
     'and',
     'run',
     '.',
     'hour',
     'and',
     'day',
     ',',
     'not',
     'week',
     'and',
     'month',
     '.',
     'ye',
     'there',
     'are',
     'unscrupul',
     'peopl',
     'in',
     'the',
     'us',
     'militari',
     '.',
     'but',
     'then',
     ',',
     'there',
     'are',
     'in',
     'everi',
     'walk',
     'of',
     'life',
     ',',
     'everi',
     'occup',
     '.',
     'but',
     'to',
     'see',
     'peopl',
     'on',
     'thi',
     'websit',
     'decid',
     'that',
     '2.3',
     'million',
     'men',
     'and',
     'women',
     'are',
     'all',
     'crimin',
     ',',
     'with',
     'noth',
     'on',
     'their',
     'mind',
     'but',
     'thought',
     'of',
     'destruct',
     'or',
     'mayhem',
     'is',
     'an',
     'absolut',
     'disservic',
     'to',
     'the',
     'thing',
     'that',
     'they',
     'do',
     'everi',
     'day',
     '.',
     'one',
     'person',
     'on',
     'thi',
     'websit',
     'even',
     'went',
     'so',
     'far',
     'as',
     'to',
     'say',
     'that',
     'militari',
     'member',
     'are',
     'in',
     'it',
     'for',
     'person',
     'gain',
     '.',
     'wow',
     '!',
     'entri',
     'level',
     'personnel',
     'make',
     'just',
     'under',
     '$',
     '8.00',
     'an',
     'hour',
     'assum',
     'a',
     '40',
     'hour',
     'work',
     'week',
     '.',
     'of',
     'cours',
     ',',
     'mani',
     'work',
     'much',
     'more',
     'than',
     '40',
     'hour',
     'a',
     'week',
     'and',
     'those',
     'in',
     'harm',
     "'s",
     'way',
     'typic',
     'put',
     'in',
     '16-18',
     'hour',
     'day',
     'for',
     'month',
     'on',
     'end',
     '.',
     'that',
     'make',
     'the',
     'pay',
     'well',
     'under',
     'minimum',
     'wage',
     '.',
     'so',
     'much',
     'for',
     'person',
     'gain',
     '.',
     'i',
     'beg',
     'you',
     ',',
     'pleas',
     'make',
     'yourself',
     'familiar',
     'with',
     'the',
     'world',
     'around',
     'you',
     '.',
     'go',
     'to',
     'a',
     'nearbi',
     'base',
     ',',
     'get',
     'a',
     'visitor',
     'pass',
     'and',
     'meet',
     'some',
     'of',
     'the',
     'men',
     'and',
     'women',
     'you',
     'are',
     'so',
     'quick',
     'to',
     'disparag',
     '.',
     'you',
     'would',
     'be',
     'surpris',
     '.',
     'the',
     'militari',
     'no',
     'longer',
     'accept',
     'peopl',
     'in',
     'lieu',
     'of',
     'prison',
     'time',
     '.',
     'they',
     'requir',
     'a',
     'minimum',
     'of',
     'a',
     'ged',
     'and',
     'prefer',
     'a',
     'high',
     'school',
     'diploma',
     '.',
     'the',
     'middl',
     'rank',
     'are',
     'expect',
     'to',
     'get',
     'a',
     'minimum',
     'of',
     'undergradu',
     'degre',
     'and',
     'the',
     'upper',
     'rank',
     'are',
     'encourag',
     'to',
     'get',
     'advanc',
     'degre',
     '.']




```python
lnew = [lstemmer.stem(word) for word in tokened]
lnew
```




    ['aft',
     'read',
     'the',
     'com',
     'for',
     'thi',
     'movy',
     ',',
     'i',
     'am',
     'not',
     'sur',
     'wheth',
     'i',
     'should',
     'be',
     'angry',
     ',',
     'sad',
     'or',
     'sick',
     '.',
     'see',
     'com',
     'typ',
     'of',
     'peopl',
     'who',
     'a',
     ')',
     'know',
     'absolv',
     'noth',
     'about',
     'the',
     'milit',
     'or',
     'b',
     ')',
     'who',
     'bas',
     'everyth',
     'they',
     'think',
     'they',
     'know',
     'on',
     'movy',
     'lik',
     'thi',
     'or',
     'on',
     'cnn',
     'report',
     'about',
     'abu-gharib',
     'mak',
     'me',
     'wond',
     'about',
     'the',
     'stat',
     'of',
     'intellect',
     'stim',
     'in',
     'the',
     'world',
     '.',
     'at',
     'the',
     'tim',
     'i',
     'typ',
     'thi',
     'the',
     'numb',
     'of',
     'peopl',
     'in',
     'the',
     'us',
     'milit',
     ':',
     '1.4',
     'mil',
     'on',
     'act',
     'duty',
     'with',
     'anoth',
     'almost',
     '900,000',
     'in',
     'the',
     'guard',
     'and',
     'reserv',
     'for',
     'a',
     'tot',
     'of',
     'rough',
     '2.3',
     'mil',
     '.',
     'the',
     'numb',
     'of',
     'peopl',
     'indict',
     'for',
     'abus',
     'at',
     'at',
     'abu-gharib',
     ':',
     'cur',
     'less',
     'than',
     '20',
     'that',
     'mak',
     'the',
     'tot',
     'of',
     'peopl',
     'indict',
     '.00083',
     '%',
     'of',
     'the',
     'tot',
     'milit',
     '.',
     'ev',
     'if',
     'you',
     'indict',
     'every',
     'singl',
     'milit',
     'memb',
     'that',
     'ev',
     'step',
     'in',
     'to',
     'abu-gharib',
     ',',
     'you',
     'would',
     'not',
     'com',
     'clos',
     'to',
     'mak',
     'that',
     'a',
     'whol',
     'numb',
     '.',
     'the',
     'flaw',
     'in',
     'thi',
     'movy',
     'would',
     'tak',
     'year',
     'to',
     'cov',
     '.',
     'i',
     'understand',
     'that',
     'it',
     "'s",
     'suppos',
     'to',
     'be',
     'sarcast',
     ',',
     'but',
     'in',
     'real',
     ',',
     'the',
     'writ',
     'and',
     'direct',
     'ar',
     'try',
     'to',
     'mak',
     'com',
     'about',
     'the',
     'stat',
     'of',
     'the',
     'milit',
     'without',
     'an',
     'enemy',
     'to',
     'fight',
     '.',
     'in',
     'real',
     ',',
     'the',
     'us',
     'milit',
     'has',
     'been',
     'at',
     'it',
     'busiest',
     'when',
     'ther',
     'ar',
     'not',
     'conflict',
     'going',
     'on',
     '.',
     'the',
     'milit',
     'is',
     'the',
     'first',
     'cal',
     'for',
     'disast',
     'reliev',
     'and',
     'humanit',
     'aid',
     'miss',
     '.',
     'when',
     'the',
     'tsunam',
     'hit',
     'indones',
     ',',
     'devest',
     'the',
     'reg',
     ',',
     'the',
     'us',
     'milit',
     'was',
     'the',
     'first',
     'on',
     'the',
     'scen',
     '.',
     'when',
     'the',
     'chao',
     'of',
     'the',
     'situ',
     'overwhelm',
     'the',
     'loc',
     'govern',
     ',',
     'it',
     'was',
     'milit',
     'lead',
     'who',
     'look',
     'at',
     'their',
     'peopl',
     ',',
     'the',
     'sam',
     'peopl',
     'thi',
     'movy',
     'mock',
     ',',
     'and',
     'said',
     'mak',
     'it',
     'hap',
     '.',
     'within',
     'hour',
     ',',
     'food',
     'aid',
     'was',
     'reach',
     'isol',
     'vil',
     '.',
     'within',
     'day',
     ',',
     'airfield',
     'wer',
     'built',
     ',',
     'cargo',
     'aircraft',
     'start',
     'land',
     'and',
     'a',
     'food',
     'distribut',
     'system',
     'was',
     'up',
     'and',
     'run',
     '.',
     'hour',
     'and',
     'day',
     ',',
     'not',
     'week',
     'and',
     'month',
     '.',
     'ye',
     'ther',
     'ar',
     'unscrup',
     'peopl',
     'in',
     'the',
     'us',
     'milit',
     '.',
     'but',
     'then',
     ',',
     'ther',
     'ar',
     'in',
     'every',
     'walk',
     'of',
     'lif',
     ',',
     'every',
     'occup',
     '.',
     'but',
     'to',
     'see',
     'peopl',
     'on',
     'thi',
     'websit',
     'decid',
     'that',
     '2.3',
     'mil',
     'men',
     'and',
     'wom',
     'ar',
     'al',
     'crimin',
     ',',
     'with',
     'noth',
     'on',
     'their',
     'mind',
     'but',
     'thought',
     'of',
     'destruct',
     'or',
     'mayhem',
     'is',
     'an',
     'absolv',
     'disserv',
     'to',
     'the',
     'thing',
     'that',
     'they',
     'do',
     'every',
     'day',
     '.',
     'on',
     'person',
     'on',
     'thi',
     'websit',
     'ev',
     'went',
     'so',
     'far',
     'as',
     'to',
     'say',
     'that',
     'milit',
     'memb',
     'ar',
     'in',
     'it',
     'for',
     'person',
     'gain',
     '.',
     'wow',
     '!',
     'entry',
     'level',
     'personnel',
     'mak',
     'just',
     'und',
     '$',
     '8.00',
     'an',
     'hour',
     'assum',
     'a',
     '40',
     'hour',
     'work',
     'week',
     '.',
     'of',
     'cours',
     ',',
     'many',
     'work',
     'much',
     'mor',
     'than',
     '40',
     'hour',
     'a',
     'week',
     'and',
     'thos',
     'in',
     'harm',
     "'s",
     'way',
     'typ',
     'put',
     'in',
     '16-18',
     'hour',
     'day',
     'for',
     'month',
     'on',
     'end',
     '.',
     'that',
     'mak',
     'the',
     'pay',
     'wel',
     'und',
     'minim',
     'wag',
     '.',
     'so',
     'much',
     'for',
     'person',
     'gain',
     '.',
     'i',
     'beg',
     'you',
     ',',
     'pleas',
     'mak',
     'yourself',
     'famili',
     'with',
     'the',
     'world',
     'around',
     'you',
     '.',
     'go',
     'to',
     'a',
     'nearby',
     'bas',
     ',',
     'get',
     'a',
     'visit',
     'pass',
     'and',
     'meet',
     'som',
     'of',
     'the',
     'men',
     'and',
     'wom',
     'you',
     'ar',
     'so',
     'quick',
     'to',
     'disp',
     '.',
     'you',
     'would',
     'be',
     'surpr',
     '.',
     'the',
     'milit',
     'no',
     'long',
     'acceiv',
     'peopl',
     'in',
     'lieu',
     'of',
     'prison',
     'tim',
     '.',
     'they',
     'requir',
     'a',
     'minim',
     'of',
     'a',
     'ged',
     'and',
     'pref',
     'a',
     'high',
     'school',
     'diplom',
     '.',
     'the',
     'middl',
     'rank',
     'ar',
     'expect',
     'to',
     'get',
     'a',
     'minim',
     'of',
     'undergradu',
     'degr',
     'and',
     'the',
     'up',
     'rank',
     'ar',
     'enco',
     'to',
     'get',
     'adv',
     'degr',
     '.']




```python
def by_pstem(tokened):
    pstemmer = PorterStemmer()
    new = [pstemmer.stem(word) for word in tokened]
    return new
```


```python
db = pd.read_csv('imdb.tsv', delimiter='\\t')
```

    C:\Users\moonlight\AppData\Local\Temp\ipykernel_4524\650949466.py:1: ParserWarning: Falling back to the 'python' engine because the 'c' engine does not support regex separators (separators > 1 char and different from '\s+' are interpreted as regex); you can avoid this warning by specifying engine='python'.
      db = pd.read_csv('imdb.tsv', delimiter='\\t')
    


```python
db
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
      <th>review</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>"Watching Time Chasers, it obvious that it was...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>I saw this film about 20 years ago and remembe...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Minor Spoilers In New York, Joan Barnard (Elvi...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>I went to see this film with a great deal of e...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>"Yes, I agree with everyone on this site this ...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>"Jennifer Ehle was sparkling in \""Pride and P...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Amy Poehler is a terrific comedian on Saturday...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>"A plane carrying employees of a large biotech...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>A well made, gritty science fiction movie, it ...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>"Incredibly dumb and utterly predictable story...</td>
    </tr>
  </tbody>
</table>
</div>




```python
db['review'] = db['review'].str.lower()
db
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
      <th>review</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>"watching time chasers, it obvious that it was...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>i saw this film about 20 years ago and remembe...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>minor spoilers in new york, joan barnard (elvi...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>i went to see this film with a great deal of e...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>"yes, i agree with everyone on this site this ...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>"jennifer ehle was sparkling in \""pride and p...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>amy poehler is a terrific comedian on saturday...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>"a plane carrying employees of a large biotech...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>a well made, gritty science fiction movie, it ...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>"incredibly dumb and utterly predictable story...</td>
    </tr>
  </tbody>
</table>
</div>



apply()는 파라미터로 함수 이름을 전달하여 데이터 프레임 전체에 동일한 함수를 적용시킨다  
데이터 프레임 각 행에 해당 함수를 적용


```python
db['review'] = db['review'].apply(word_tokenize)
db
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
      <th>review</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>[``, watching, time, chasers, ,, it, obvious, ...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>[i, saw, this, film, about, 20, years, ago, an...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>[minor, spoilers, in, new, york, ,, joan, barn...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>[i, went, to, see, this, film, with, a, great,...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>[``, yes, ,, i, agree, with, everyone, on, thi...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>[``, jennifer, ehle, was, sparkling, in, \, ''...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>[amy, poehler, is, a, terrific, comedian, on, ...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>[``, a, plane, carrying, employees, of, a, lar...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>[a, well, made, ,, gritty, science, fiction, m...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>[``, incredibly, dumb, and, utterly, predictab...</td>
    </tr>
  </tbody>
</table>
</div>




```python
db['review'][0]
```




    ['``',
     'watching',
     'time',
     'chasers',
     ',',
     'it',
     'obvious',
     'that',
     'it',
     'was',
     'made',
     'by',
     'a',
     'bunch',
     'of',
     'friends',
     '.',
     'maybe',
     'they',
     'were',
     'sitting',
     'around',
     'one',
     'day',
     'in',
     'film',
     'school',
     'and',
     'said',
     ',',
     '\\',
     "''",
     "''",
     'hey',
     ',',
     'let',
     "'s",
     'pool',
     'our',
     'money',
     'together',
     'and',
     'make',
     'a',
     'really',
     'bad',
     'movie',
     '!',
     '\\',
     "''",
     "''",
     'or',
     'something',
     'like',
     'that',
     '.',
     'what',
     'ever',
     'they',
     'said',
     ',',
     'they',
     'still',
     'ended',
     'up',
     'making',
     'a',
     'really',
     'bad',
     'movie',
     '--',
     'dull',
     'story',
     ',',
     'bad',
     'script',
     ',',
     'lame',
     'acting',
     ',',
     'poor',
     'cinematography',
     ',',
     'bottom',
     'of',
     'the',
     'barrel',
     'stock',
     'music',
     ',',
     'etc',
     '.',
     'all',
     'corners',
     'were',
     'cut',
     ',',
     'except',
     'the',
     'one',
     'that',
     'would',
     'have',
     'prevented',
     'this',
     'film',
     "'s",
     'release',
     '.',
     'life',
     "'s",
     'like',
     'that',
     '.',
     "''"]




```python
db['review'] = db['review'].apply(lambda x: by_freq(x, 1)).apply(lambda x: by_len(x, 2)).apply(lambda x: by_stop(x, stopset))
#apply()를 쓸 때 받아오는 함수가 인자를 여러 개 받는다면 lambda를 통해 어떤 위치에 데이터베이스가 들어 가야 하는지 명시
db['review']
```




    0    [one, film, said, really, bad, movie, like, sa...
    1                                         [film, film]
    2    [new, york, joan, barnard, elvire, audrey, bar...
    3    [went, film, film, went, jump, send, n't, jump...
    4    [site, movie, bad, even, movie, made, movie, s...
    5    [ehle, northam, wonderful, wonderful, ehle, no...
    6    [role, movie, n't, author, book, author, autho...
    7    [plane, ceo, search, rescue, mission, ceo, har...
    8    [gritty, movie, sci-fi, good, suspense, movie,...
    9                                         [girl, girl]
    Name: review, dtype: object




```python
db['stem'] = db['review'].apply(by_pstem)
```


```python
db
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
      <th>review</th>
      <th>stem</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>[one, film, said, really, bad, movie, like, sa...</td>
      <td>[one, film, said, realli, bad, movi, like, sai...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>[film, film]</td>
      <td>[film, film]</td>
    </tr>
    <tr>
      <th>2</th>
      <td>[new, york, joan, barnard, elvire, audrey, bar...</td>
      <td>[new, york, joan, barnard, elvir, audrey, barn...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>[went, film, film, went, jump, send, n't, jump...</td>
      <td>[went, film, film, went, jump, send, n't, jump...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>[site, movie, bad, even, movie, made, movie, s...</td>
      <td>[site, movi, bad, even, movi, made, movi, spec...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>[ehle, northam, wonderful, wonderful, ehle, no...</td>
      <td>[ehl, northam, wonder, wonder, ehl, northam, l...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>[role, movie, n't, author, book, author, autho...</td>
      <td>[role, movi, n't, author, book, author, author...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>[plane, ceo, search, rescue, mission, ceo, har...</td>
      <td>[plane, ceo, search, rescu, mission, ceo, harl...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>[gritty, movie, sci-fi, good, suspense, movie,...</td>
      <td>[gritti, movi, sci-fi, good, suspens, movi, sc...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>[girl, girl]</td>
      <td>[girl, girl]</td>
    </tr>
  </tbody>
</table>
</div>



#### <a id='toc1_1_2_3_'></a>[문장 토큰화 sentence tokenization](#toc0_)
---


```python
text = "My email address is 'abcde@codeit.com'. Send it to Mr.Kim."
```


```python
toksent = sent_tokenize(text)
toksent
```




    ["My email address is 'abcde@codeit.com'.", 'Send it to Mr.Kim.']



##### <a id='toc1_1_2_3_1_'></a>[POS part of speech tagging](#toc0_)


```python
nltk.download('averaged_perceptron_tagger')
tagged = pos_tag(token)
tagged
```

    [nltk_data] Downloading package averaged_perceptron_tagger to
    [nltk_data]     C:\Users\moonlight\AppData\Roaming\nltk_data...
    [nltk_data]   Package averaged_perceptron_tagger is already up-to-
    [nltk_data]       date!
    




    [('the', 'DT'),
     ('for', 'IN'),
     ('this', 'DT'),
     ('movie', 'NN'),
     (',', ','),
     ('I', 'PRP'),
     ('not', 'RB'),
     ('I', 'PRP'),
     ('be', 'VB'),
     (',', ','),
     ('or', 'CC'),
     ('.', '.'),
     ('of', 'IN'),
     ('people', 'NNS'),
     ('who', 'WP'),
     ('a', 'DT'),
     ('about', 'IN'),
     ('the', 'DT'),
     ('military', 'JJ'),
     ('or', 'CC'),
     ('who', 'WP'),
     ('they', 'PRP'),
     ('they', 'PRP'),
     ('on', 'IN'),
     ('this', 'DT'),
     ('or', 'CC'),
     ('on', 'IN'),
     ('about', 'IN'),
     ('Abu-Gharib', 'NNP'),
     ('makes', 'VBZ'),
     ('about', 'IN'),
     ('the', 'DT'),
     ('of', 'IN'),
     ('in', 'IN'),
     ('the', 'DT'),
     ('.', '.'),
     ('the', 'DT'),
     ('I', 'PRP'),
     ('this', 'DT'),
     ('the', 'DT'),
     ('number', 'NN'),
     ('of', 'IN'),
     ('people', 'NNS'),
     ('in', 'IN'),
     ('the', 'DT'),
     ('US', 'NNP'),
     ('military', 'JJ'),
     ('million', 'CD'),
     ('on', 'IN'),
     ('with', 'IN'),
     ('in', 'IN'),
     ('the', 'DT'),
     ('and', 'CC'),
     ('for', 'IN'),
     ('a', 'DT'),
     ('total', 'NN'),
     ('of', 'IN'),
     ('million', 'CD'),
     ('.', '.'),
     ('The', 'DT'),
     ('number', 'NN'),
     ('of', 'IN'),
     ('people', 'NNS'),
     ('for', 'IN'),
     ('at', 'IN'),
     ('at', 'IN'),
     ('Abu-Gharib', 'NNP'),
     ('makes', 'VBZ'),
     ('the', 'DT'),
     ('total', 'JJ'),
     ('of', 'IN'),
     ('people', 'NNS'),
     ('of', 'IN'),
     ('the', 'DT'),
     ('total', 'JJ'),
     ('military', 'JJ'),
     ('.', '.'),
     ('you', 'PRP'),
     ('every', 'DT'),
     ('military', 'NN'),
     ('that', 'WDT'),
     ('in', 'IN'),
     ('to', 'TO'),
     ('Abu-Gharib', 'NNP'),
     (',', ','),
     ('you', 'PRP'),
     ('would', 'MD'),
     ('not', 'RB'),
     ('to', 'TO'),
     ('that', 'IN'),
     ('a', 'DT'),
     ('number', 'NN'),
     ('.', '.'),
     ('The', 'DT'),
     ('in', 'IN'),
     ('this', 'DT'),
     ('movie', 'NN'),
     ('would', 'MD'),
     ('to', 'TO'),
     ('.', '.'),
     ('I', 'PRP'),
     ('that', 'IN'),
     ('it', 'PRP'),
     ('to', 'TO'),
     ('be', 'VB'),
     (',', ','),
     ('in', 'IN'),
     (',', ','),
     ('the', 'DT'),
     ('and', 'CC'),
     ('are', 'VBP'),
     ('to', 'TO'),
     ('make', 'VB'),
     ('about', 'IN'),
     ('the', 'DT'),
     ('of', 'IN'),
     ('the', 'DT'),
     ('military', 'JJ'),
     ('an', 'DT'),
     ('to', 'TO'),
     ('.', '.'),
     (',', ','),
     ('the', 'DT'),
     ('US', 'NNP'),
     ('military', 'JJ'),
     ('at', 'IN'),
     ('there', 'EX'),
     ('are', 'VBP'),
     ('not', 'RB'),
     ('on', 'IN'),
     ('.', '.'),
     ('The', 'DT'),
     ('military', 'JJ'),
     ('the', 'DT'),
     ('for', 'IN'),
     ('and', 'CC'),
     ('.', '.'),
     ('the', 'DT'),
     (',', ','),
     ('the', 'DT'),
     (',', ','),
     ('the', 'DT'),
     ('US', 'NNP'),
     ('military', 'NN'),
     ('was', 'VBD'),
     ('the', 'DT'),
     ('on', 'IN'),
     ('the', 'DT'),
     ('.', '.'),
     ('the', 'DT'),
     ('of', 'IN'),
     ('the', 'DT'),
     ('the', 'DT'),
     (',', ','),
     ('it', 'PRP'),
     ('was', 'VBD'),
     ('military', 'JJ'),
     ('who', 'WP'),
     ('at', 'IN'),
     ('people', 'NNS'),
     (',', ','),
     ('the', 'DT'),
     ('people', 'NNS'),
     ('this', 'DT'),
     ('movie', 'NN'),
     (',', ','),
     ('and', 'CC'),
     ('make', 'VB'),
     ('it', 'PRP'),
     ('.', '.'),
     (',', ','),
     ('was', 'VBD'),
     ('.', '.'),
     ('days', 'NNS'),
     (',', ','),
     (',', ','),
     ('and', 'CC'),
     ('a', 'DT'),
     ('was', 'VBD'),
     ('and', 'CC'),
     ('.', '.'),
     ('and', 'CC'),
     ('days', 'NNS'),
     (',', ','),
     ('not', 'RB'),
     ('and', 'CC'),
     ('.', '.'),
     ('there', 'EX'),
     ('are', 'VBP'),
     ('people', 'NNS'),
     ('in', 'IN'),
     ('the', 'DT'),
     ('US', 'NNP'),
     ('military', 'JJ'),
     ('.', '.'),
     (',', ','),
     ('there', 'EX'),
     ('are', 'VBP'),
     ('in', 'IN'),
     ('every', 'DT'),
     ('of', 'IN'),
     (',', ','),
     ('every', 'DT'),
     ('.', '.'),
     ('to', 'TO'),
     ('people', 'NNS'),
     ('on', 'IN'),
     ('this', 'DT'),
     ('that', 'DT'),
     ('million', 'CD'),
     ('and', 'CC'),
     ('are', 'VBP'),
     (',', ','),
     ('with', 'IN'),
     ('on', 'IN'),
     ('of', 'IN'),
     ('or', 'CC'),
     ('an', 'DT'),
     ('to', 'TO'),
     ('the', 'DT'),
     ('that', 'IN'),
     ('they', 'PRP'),
     ('every', 'DT'),
     ('.', '.'),
     ('on', 'IN'),
     ('this', 'DT'),
     ('to', 'TO'),
     ('that', 'DT'),
     ('military', 'NN'),
     ('are', 'VBP'),
     ('in', 'IN'),
     ('it', 'PRP'),
     ('for', 'IN'),
     ('.', '.'),
     ('make', 'VB'),
     ('an', 'DT'),
     ('hour', 'NN'),
     ('a', 'DT'),
     ('hour', 'NN'),
     ('.', '.'),
     (',', ','),
     ('a', 'DT'),
     ('and', 'CC'),
     ('in', 'IN'),
     ('in', 'IN'),
     ('hour', 'NN'),
     ('days', 'NNS'),
     ('for', 'IN'),
     ('on', 'IN'),
     ('.', '.'),
     ('makes', 'VBZ'),
     ('the', 'DT'),
     ('minimum', 'NN'),
     ('.', '.'),
     ('for', 'IN'),
     ('.', '.'),
     ('I', 'PRP'),
     ('you', 'PRP'),
     (',', ','),
     ('make', 'VB'),
     ('with', 'IN'),
     ('the', 'DT'),
     ('you', 'PRP'),
     ('.', '.'),
     ('to', 'TO'),
     ('a', 'DT'),
     (',', ','),
     ('get', 'VB'),
     ('a', 'DT'),
     ('and', 'CC'),
     ('of', 'IN'),
     ('the', 'DT'),
     ('and', 'CC'),
     ('you', 'PRP'),
     ('are', 'VBP'),
     ('to', 'TO'),
     ('.', '.'),
     ('would', 'MD'),
     ('be', 'VB'),
     ('.', '.'),
     ('The', 'DT'),
     ('military', 'JJ'),
     ('people', 'NNS'),
     ('in', 'IN'),
     ('of', 'IN'),
     ('.', '.'),
     ('a', 'DT'),
     ('minimum', 'NN'),
     ('of', 'IN'),
     ('a', 'DT'),
     ('and', 'CC'),
     ('a', 'DT'),
     ('.', '.'),
     ('The', 'DT'),
     ('are', 'VBP'),
     ('to', 'TO'),
     ('get', 'VB'),
     ('a', 'DT'),
     ('minimum', 'NN'),
     ('of', 'IN'),
     ('and', 'CC'),
     ('the', 'DT'),
     ('are', 'VBP'),
     ('to', 'TO'),
     ('get', 'VB'),
     ('.', '.')]




```python
def tagger(token_sent):
    tagged = []
    for sentence in token_sent:
        tagged.extend(pos_tag(word_tokenize(sentence)))

    return tagged
```

##### <a id='toc1_1_2_3_2_'></a>[Penn Treebank POS tag](#toc0_)

![penntreebank](https://www.researchgate.net/profile/Mitchell-Marcus-2/publication/220017637/figure/tbl1/AS:393942622326789@1470934648152/The-Penn-Treebank-POS-tagset.png)

##### <a id='toc1_1_2_3_3_'></a>[word net](#toc0_)
![penntreebank](https://media.geeksforgeeks.org/wp-content/uploads/20190221232747/wordnet.jpg)

##### <a id='toc1_1_2_3_4_'></a>[표제어(사전적 어원) lemma 추출](#toc0_)
am, are, is >>> be


```python
def penn_to_wn(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    elif tag.startswith('V'):
        return wordnet.VERB
    else:
        return
```


```python
nltk.download('wordnet')
nltk.download('omw-1.4')
```

    [nltk_data] Downloading package wordnet to
    [nltk_data]     C:\Users\moonlight\AppData\Roaming\nltk_data...
    [nltk_data]   Package wordnet is already up-to-date!
    [nltk_data] Downloading package omw-1.4 to
    [nltk_data]     C:\Users\moonlight\AppData\Roaming\nltk_data...
    [nltk_data]   Package omw-1.4 is already up-to-date!
    




    True




```python
lemma = WordNetLemmatizer()
```


```python
lem = []
for word, tag in tagged:
    wntag = penn_to_wn(tag)
    if wntag in (wordnet.ADJ, wordnet.NOUN, wordnet.ADV, wordnet.VERB):
        lem.append(lemma.lemmatize(word, wntag))
    else:
        lem.append(word)
```


```python
lem
```




    ['the',
     'for',
     'this',
     'movie',
     ',',
     'I',
     'not',
     'I',
     'be',
     ',',
     'or',
     '.',
     'of',
     'people',
     'who',
     'a',
     'about',
     'the',
     'military',
     'or',
     'who',
     'they',
     'they',
     'on',
     'this',
     'or',
     'on',
     'about',
     'Abu-Gharib',
     'make',
     'about',
     'the',
     'of',
     'in',
     'the',
     '.',
     'the',
     'I',
     'this',
     'the',
     'number',
     'of',
     'people',
     'in',
     'the',
     'US',
     'military',
     'million',
     'on',
     'with',
     'in',
     'the',
     'and',
     'for',
     'a',
     'total',
     'of',
     'million',
     '.',
     'The',
     'number',
     'of',
     'people',
     'for',
     'at',
     'at',
     'Abu-Gharib',
     'make',
     'the',
     'total',
     'of',
     'people',
     'of',
     'the',
     'total',
     'military',
     '.',
     'you',
     'every',
     'military',
     'that',
     'in',
     'to',
     'Abu-Gharib',
     ',',
     'you',
     'would',
     'not',
     'to',
     'that',
     'a',
     'number',
     '.',
     'The',
     'in',
     'this',
     'movie',
     'would',
     'to',
     '.',
     'I',
     'that',
     'it',
     'to',
     'be',
     ',',
     'in',
     ',',
     'the',
     'and',
     'be',
     'to',
     'make',
     'about',
     'the',
     'of',
     'the',
     'military',
     'an',
     'to',
     '.',
     ',',
     'the',
     'US',
     'military',
     'at',
     'there',
     'be',
     'not',
     'on',
     '.',
     'The',
     'military',
     'the',
     'for',
     'and',
     '.',
     'the',
     ',',
     'the',
     ',',
     'the',
     'US',
     'military',
     'be',
     'the',
     'on',
     'the',
     '.',
     'the',
     'of',
     'the',
     'the',
     ',',
     'it',
     'be',
     'military',
     'who',
     'at',
     'people',
     ',',
     'the',
     'people',
     'this',
     'movie',
     ',',
     'and',
     'make',
     'it',
     '.',
     ',',
     'be',
     '.',
     'day',
     ',',
     ',',
     'and',
     'a',
     'be',
     'and',
     '.',
     'and',
     'day',
     ',',
     'not',
     'and',
     '.',
     'there',
     'be',
     'people',
     'in',
     'the',
     'US',
     'military',
     '.',
     ',',
     'there',
     'be',
     'in',
     'every',
     'of',
     ',',
     'every',
     '.',
     'to',
     'people',
     'on',
     'this',
     'that',
     'million',
     'and',
     'be',
     ',',
     'with',
     'on',
     'of',
     'or',
     'an',
     'to',
     'the',
     'that',
     'they',
     'every',
     '.',
     'on',
     'this',
     'to',
     'that',
     'military',
     'be',
     'in',
     'it',
     'for',
     '.',
     'make',
     'an',
     'hour',
     'a',
     'hour',
     '.',
     ',',
     'a',
     'and',
     'in',
     'in',
     'hour',
     'day',
     'for',
     'on',
     '.',
     'make',
     'the',
     'minimum',
     '.',
     'for',
     '.',
     'I',
     'you',
     ',',
     'make',
     'with',
     'the',
     'you',
     '.',
     'to',
     'a',
     ',',
     'get',
     'a',
     'and',
     'of',
     'the',
     'and',
     'you',
     'be',
     'to',
     '.',
     'would',
     'be',
     '.',
     'The',
     'military',
     'people',
     'in',
     'of',
     '.',
     'a',
     'minimum',
     'of',
     'a',
     'and',
     'a',
     '.',
     'The',
     'be',
     'to',
     'get',
     'a',
     'minimum',
     'of',
     'and',
     'the',
     'be',
     'to',
     'get',
     '.']




```python
def lemmatize(tagged):
    lem = []
    for word, tag in tagged:
        wntag = penn_to_wn(tag)
        if wntag in (wordnet.ADJ, wordnet.NOUN, wordnet.ADV, wordnet.VERB):
            lem.append(lemma.lemmatize(word, wntag))
        else:
            lem.append(word)
    return lem   
```


```python
dvd = pd.read_csv('imdb.tsv', delimiter='\\t')
```

    C:\Users\moonlight\AppData\Local\Temp\ipykernel_4524\1131901464.py:1: ParserWarning: Falling back to the 'python' engine because the 'c' engine does not support regex separators (separators > 1 char and different from '\s+' are interpreted as regex); you can avoid this warning by specifying engine='python'.
      dvd = pd.read_csv('imdb.tsv', delimiter='\\t')
    


```python
dvd['review'] = dvd['review'].str.lower()
dvd['review']
```




    0    "watching time chasers, it obvious that it was...
    1    i saw this film about 20 years ago and remembe...
    2    minor spoilers in new york, joan barnard (elvi...
    3    i went to see this film with a great deal of e...
    4    "yes, i agree with everyone on this site this ...
    5    "jennifer ehle was sparkling in \""pride and p...
    6    amy poehler is a terrific comedian on saturday...
    7    "a plane carrying employees of a large biotech...
    8    a well made, gritty science fiction movie, it ...
    9    "incredibly dumb and utterly predictable story...
    Name: review, dtype: object




```python
dvd['review'] = dvd['review'].apply(sent_tokenize)
dvd['review']
```




    0    ["watching time chasers, it obvious that it wa...
    1    [i saw this film about 20 years ago and rememb...
    2    [minor spoilers in new york, joan barnard (elv...
    3    [i went to see this film with a great deal of ...
    4    ["yes, i agree with everyone on this site this...
    5    ["jennifer ehle was sparkling in \""pride and ...
    6    [amy poehler is a terrific comedian on saturda...
    7    ["a plane carrying employees of a large biotec...
    8    [a well made, gritty science fiction movie, it...
    9    ["incredibly dumb and utterly predictable stor...
    Name: review, dtype: object




```python
dvd['review'][0]
```




    ['"watching time chasers, it obvious that it was made by a bunch of friends.',
     'maybe they were sitting around one day in film school and said, \\""hey, let\'s pool our money together and make a really bad movie!\\"" or something like that.',
     'what ever they said, they still ended up making a really bad movie--dull story, bad script, lame acting, poor cinematography, bottom of the barrel stock music, etc.',
     "all corners were cut, except the one that would have prevented this film's release.",
     'life\'s like that."']




```python
dvd['tagged'] = dvd['review'].apply(tagger)
dvd
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
      <th>review</th>
      <th>tagged</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>["watching time chasers, it obvious that it wa...</td>
      <td>[(``, ``), (watching, JJ), (time, NN), (chaser...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>[i saw this film about 20 years ago and rememb...</td>
      <td>[(i, NN), (saw, VBD), (this, DT), (film, NN), ...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>[minor spoilers in new york, joan barnard (elv...</td>
      <td>[(minor, JJ), (spoilers, NNS), (in, IN), (new,...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>[i went to see this film with a great deal of ...</td>
      <td>[(i, JJ), (went, VBD), (to, TO), (see, VB), (t...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>["yes, i agree with everyone on this site this...</td>
      <td>[(``, ``), (yes, RB), (,, ,), (i, JJ), (agree,...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>["jennifer ehle was sparkling in \""pride and ...</td>
      <td>[(``, ``), (jennifer, NN), (ehle, NN), (was, V...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>[amy poehler is a terrific comedian on saturda...</td>
      <td>[(amy, JJ), (poehler, NN), (is, VBZ), (a, DT),...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>["a plane carrying employees of a large biotec...</td>
      <td>[(``, ``), (a, DT), (plane, NN), (carrying, VB...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>[a well made, gritty science fiction movie, it...</td>
      <td>[(a, DT), (well, NN), (made, VBN), (,, ,), (gr...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>["incredibly dumb and utterly predictable stor...</td>
      <td>[(``, ``), (incredibly, RB), (dumb, JJ), (and,...</td>
    </tr>
  </tbody>
</table>
</div>




```python
dvd['lemma'] = dvd['tagged'].apply(lemmatize)
dvd
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
      <th>review</th>
      <th>tagged</th>
      <th>lemma</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>["watching time chasers, it obvious that it wa...</td>
      <td>[(``, ``), (watching, JJ), (time, NN), (chaser...</td>
      <td>[``, watching, time, chaser, ,, it, obvious, t...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>[i saw this film about 20 years ago and rememb...</td>
      <td>[(i, NN), (saw, VBD), (this, DT), (film, NN), ...</td>
      <td>[i, saw, this, film, about, 20, year, ago, and...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>[minor spoilers in new york, joan barnard (elv...</td>
      <td>[(minor, JJ), (spoilers, NNS), (in, IN), (new,...</td>
      <td>[minor, spoiler, in, new, york, ,, joan, barna...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>[i went to see this film with a great deal of ...</td>
      <td>[(i, JJ), (went, VBD), (to, TO), (see, VB), (t...</td>
      <td>[i, go, to, see, this, film, with, a, great, d...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>["yes, i agree with everyone on this site this...</td>
      <td>[(``, ``), (yes, RB), (,, ,), (i, JJ), (agree,...</td>
      <td>[``, yes, ,, i, agree, with, everyone, on, thi...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>["jennifer ehle was sparkling in \""pride and ...</td>
      <td>[(``, ``), (jennifer, NN), (ehle, NN), (was, V...</td>
      <td>[``, jennifer, ehle, be, sparkle, in, \, '', '...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>[amy poehler is a terrific comedian on saturda...</td>
      <td>[(amy, JJ), (poehler, NN), (is, VBZ), (a, DT),...</td>
      <td>[amy, poehler, be, a, terrific, comedian, on, ...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>["a plane carrying employees of a large biotec...</td>
      <td>[(``, ``), (a, DT), (plane, NN), (carrying, VB...</td>
      <td>[``, a, plane, carry, employee, of, a, large, ...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>[a well made, gritty science fiction movie, it...</td>
      <td>[(a, DT), (well, NN), (made, VBN), (,, ,), (gr...</td>
      <td>[a, well, make, ,, gritty, science, fiction, m...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>["incredibly dumb and utterly predictable stor...</td>
      <td>[(``, ``), (incredibly, RB), (dumb, JJ), (and,...</td>
      <td>[``, incredibly, dumb, and, utterly, predictab...</td>
    </tr>
  </tbody>
</table>
</div>




```python
len(dvd['lemma'][1])
```




    85




```python
dvd['by_freq'] = dvd['lemma'].apply(lambda x: by_freq(x, 1))
```


```python
dvd
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
      <th>review</th>
      <th>tagged</th>
      <th>lemma</th>
      <th>by_freq</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>["watching time chasers, it obvious that it wa...</td>
      <td>[(``, ``), (watching, JJ), (time, NN), (chaser...</td>
      <td>[``, watching, time, chaser, ,, it, obvious, t...</td>
      <td>[,, it, that, it, be, make, a, of, ., they, be...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>[i saw this film about 20 years ago and rememb...</td>
      <td>[(i, NN), (saw, VBD), (this, DT), (film, NN), ...</td>
      <td>[i, saw, this, film, about, 20, year, ago, and...</td>
      <td>[i, film, and, it, as, be, ., i, it, be, a, a,...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>[minor spoilers in new york, joan barnard (elv...</td>
      <td>[(minor, JJ), (spoilers, NNS), (in, IN), (new,...</td>
      <td>[minor, spoiler, in, new, york, ,, joan, barna...</td>
      <td>[in, new, york, ,, joan, barnard, (, elvire, a...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>[i went to see this film with a great deal of ...</td>
      <td>[(i, JJ), (went, VBD), (to, TO), (see, VB), (t...</td>
      <td>[i, go, to, see, this, film, with, a, great, d...</td>
      <td>[i, go, to, this, film, with, a, of, i, be, wi...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>["yes, i agree with everyone on this site this...</td>
      <td>[(``, ``), (yes, RB), (,, ,), (i, JJ), (agree,...</td>
      <td>[``, yes, ,, i, agree, with, everyone, on, thi...</td>
      <td>[,, i, with, on, this, site, this, movie, be, ...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>["jennifer ehle was sparkling in \""pride and ...</td>
      <td>[(``, ``), (jennifer, NN), (ehle, NN), (was, V...</td>
      <td>[``, jennifer, ehle, be, sparkle, in, \, '', '...</td>
      <td>[ehle, be, in, \, '', '', and, '', '', northam...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>[amy poehler is a terrific comedian on saturda...</td>
      <td>[(amy, JJ), (poehler, NN), (is, VBZ), (a, DT),...</td>
      <td>[amy, poehler, be, a, terrific, comedian, on, ...</td>
      <td>[be, a, on, ,, her, role, in, movie, do, n't, ...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>["a plane carrying employees of a large biotec...</td>
      <td>[(``, ``), (a, DT), (plane, NN), (carrying, VB...</td>
      <td>[``, a, plane, carry, employee, of, a, large, ...</td>
      <td>[a, plane, of, a, --, the, ceo, 's, --, go, do...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>[a well made, gritty science fiction movie, it...</td>
      <td>[(a, DT), (well, NN), (made, VBN), (,, ,), (gr...</td>
      <td>[a, well, make, ,, gritty, science, fiction, m...</td>
      <td>[a, ,, gritty, movie, ,, it, be, of, movie, ,,...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>["incredibly dumb and utterly predictable stor...</td>
      <td>[(``, ``), (incredibly, RB), (dumb, JJ), (and,...</td>
      <td>[``, incredibly, dumb, and, utterly, predictab...</td>
      <td>[and, a, girl, ,, by, ,, a, girl, ., they, ,, ...</td>
    </tr>
  </tbody>
</table>
</div>




```python
len(dvd['by_freq'][0])
```




    64




```python
dvd['by_len'] = dvd['by_freq'].apply(lambda x: by_len(x, 2))
dvd
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
      <th>review</th>
      <th>tagged</th>
      <th>lemma</th>
      <th>by_freq</th>
      <th>by_len</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>["watching time chasers, it obvious that it wa...</td>
      <td>[(``, ``), (watching, JJ), (time, NN), (chaser...</td>
      <td>[``, watching, time, chaser, ,, it, obvious, t...</td>
      <td>[,, it, that, it, be, make, a, of, ., they, be...</td>
      <td>[that, make, they, one, film, and, say, and, m...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>[i saw this film about 20 years ago and rememb...</td>
      <td>[(i, NN), (saw, VBD), (this, DT), (film, NN), ...</td>
      <td>[i, saw, this, film, about, 20, year, ago, and...</td>
      <td>[i, film, and, it, as, be, ., i, it, be, a, a,...</td>
      <td>[film, and, and, and, and, but, the, the, the,...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>[minor spoilers in new york, joan barnard (elv...</td>
      <td>[(minor, JJ), (spoilers, NNS), (in, IN), (new,...</td>
      <td>[minor, spoiler, in, new, york, ,, joan, barna...</td>
      <td>[in, new, york, ,, joan, barnard, (, elvire, a...</td>
      <td>[new, york, joan, barnard, elvire, audrey, tha...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>[i went to see this film with a great deal of ...</td>
      <td>[(i, JJ), (went, VBD), (to, TO), (see, VB), (t...</td>
      <td>[i, go, to, see, this, film, with, a, great, d...</td>
      <td>[i, go, to, this, film, with, a, of, i, be, wi...</td>
      <td>[this, film, with, with, the, for, but, this, ...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>["yes, i agree with everyone on this site this...</td>
      <td>[(``, ``), (yes, RB), (,, ,), (i, JJ), (agree,...</td>
      <td>[``, yes, ,, i, agree, with, everyone, on, thi...</td>
      <td>[,, i, with, on, this, site, this, movie, be, ...</td>
      <td>[with, this, site, this, movie, very, very, ba...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>["jennifer ehle was sparkling in \""pride and ...</td>
      <td>[(``, ``), (jennifer, NN), (ehle, NN), (was, V...</td>
      <td>[``, jennifer, ehle, be, sparkle, in, \, '', '...</td>
      <td>[ehle, be, in, \, '', '', and, '', '', northam...</td>
      <td>[ehle, and, northam, wonderful, the, with, thi...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>[amy poehler is a terrific comedian on saturda...</td>
      <td>[(amy, JJ), (poehler, NN), (is, VBZ), (a, DT),...</td>
      <td>[amy, poehler, be, a, terrific, comedian, on, ...</td>
      <td>[be, a, on, ,, her, role, in, movie, do, n't, ...</td>
      <td>[her, role, movie, n't, her, with, her, author...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>["a plane carrying employees of a large biotec...</td>
      <td>[(``, ``), (a, DT), (plane, NN), (carrying, VB...</td>
      <td>[``, a, plane, carry, employee, of, a, large, ...</td>
      <td>[a, plane, of, a, --, the, ceo, 's, --, go, do...</td>
      <td>[plane, the, ceo, down, the, when, the, search...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>[a well made, gritty science fiction movie, it...</td>
      <td>[(a, DT), (well, NN), (made, VBN), (,, ,), (gr...</td>
      <td>[a, well, make, ,, gritty, science, fiction, m...</td>
      <td>[a, ,, gritty, movie, ,, it, be, of, movie, ,,...</td>
      <td>[gritty, movie, movie, but, keep, the, for, th...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>["incredibly dumb and utterly predictable stor...</td>
      <td>[(``, ``), (incredibly, RB), (dumb, JJ), (and,...</td>
      <td>[``, incredibly, dumb, and, utterly, predictab...</td>
      <td>[and, a, girl, ,, by, ,, a, girl, ., they, ,, ...</td>
      <td>[and, girl, girl, they, and, all, the, the, al...</td>
    </tr>
  </tbody>
</table>
</div>




```python
len(dvd['by_len'][0])
```




    29




```python
dvd['by_stop'] = dvd['by_len'].apply(lambda x: by_stop(x, stopset))
dvd
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
      <th>review</th>
      <th>tagged</th>
      <th>lemma</th>
      <th>by_freq</th>
      <th>by_len</th>
      <th>by_stop</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>["watching time chasers, it obvious that it wa...</td>
      <td>[(``, ``), (watching, JJ), (time, NN), (chaser...</td>
      <td>[``, watching, time, chaser, ,, it, obvious, t...</td>
      <td>[,, it, that, it, be, make, a, of, ., they, be...</td>
      <td>[that, make, they, one, film, and, say, and, m...</td>
      <td>[make, one, film, say, make, really, bad, movi...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>[i saw this film about 20 years ago and rememb...</td>
      <td>[(i, NN), (saw, VBD), (this, DT), (film, NN), ...</td>
      <td>[i, saw, this, film, about, 20, year, ago, and...</td>
      <td>[i, film, and, it, as, be, ., i, it, be, a, a,...</td>
      <td>[film, and, and, and, and, but, the, the, the,...</td>
      <td>[film, film]</td>
    </tr>
    <tr>
      <th>2</th>
      <td>[minor spoilers in new york, joan barnard (elv...</td>
      <td>[(minor, JJ), (spoilers, NNS), (in, IN), (new,...</td>
      <td>[minor, spoiler, in, new, york, ,, joan, barna...</td>
      <td>[in, new, york, ,, joan, barnard, (, elvire, a...</td>
      <td>[new, york, joan, barnard, elvire, audrey, tha...</td>
      <td>[new, york, joan, barnard, elvire, audrey, bar...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>[i went to see this film with a great deal of ...</td>
      <td>[(i, JJ), (went, VBD), (to, TO), (see, VB), (t...</td>
      <td>[i, go, to, see, this, film, with, a, great, d...</td>
      <td>[i, go, to, this, film, with, a, of, i, be, wi...</td>
      <td>[this, film, with, with, the, for, but, this, ...</td>
      <td>[film, film, jump, send, n't, jump, radio, n't...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>["yes, i agree with everyone on this site this...</td>
      <td>[(``, ``), (yes, RB), (,, ,), (i, JJ), (agree,...</td>
      <td>[``, yes, ,, i, agree, with, everyone, on, thi...</td>
      <td>[,, i, with, on, this, site, this, movie, be, ...</td>
      <td>[with, this, site, this, movie, very, very, ba...</td>
      <td>[site, movie, bad, even, movie, movie, make, m...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>["jennifer ehle was sparkling in \""pride and ...</td>
      <td>[(``, ``), (jennifer, NN), (ehle, NN), (was, V...</td>
      <td>[``, jennifer, ehle, be, sparkle, in, \, '', '...</td>
      <td>[ehle, be, in, \, '', '', and, '', '', northam...</td>
      <td>[ehle, and, northam, wonderful, the, with, thi...</td>
      <td>[ehle, northam, wonderful, wonderful, ehle, no...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>[amy poehler is a terrific comedian on saturda...</td>
      <td>[(amy, JJ), (poehler, NN), (is, VBZ), (a, DT),...</td>
      <td>[amy, poehler, be, a, terrific, comedian, on, ...</td>
      <td>[be, a, on, ,, her, role, in, movie, do, n't, ...</td>
      <td>[her, role, movie, n't, her, with, her, author...</td>
      <td>[role, movie, n't, author, book, funny, author...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>["a plane carrying employees of a large biotec...</td>
      <td>[(``, ``), (a, DT), (plane, NN), (carrying, VB...</td>
      <td>[``, a, plane, carry, employee, of, a, large, ...</td>
      <td>[a, plane, of, a, --, the, ceo, 's, --, go, do...</td>
      <td>[plane, the, ceo, down, the, when, the, search...</td>
      <td>[plane, ceo, search, rescue, mission, call, ce...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>[a well made, gritty science fiction movie, it...</td>
      <td>[(a, DT), (well, NN), (made, VBN), (,, ,), (gr...</td>
      <td>[a, well, make, ,, gritty, science, fiction, m...</td>
      <td>[a, ,, gritty, movie, ,, it, be, of, movie, ,,...</td>
      <td>[gritty, movie, movie, but, keep, the, for, th...</td>
      <td>[gritty, movie, movie, keep, sci-fi, good, kee...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>["incredibly dumb and utterly predictable stor...</td>
      <td>[(``, ``), (incredibly, RB), (dumb, JJ), (and,...</td>
      <td>[``, incredibly, dumb, and, utterly, predictab...</td>
      <td>[and, a, girl, ,, by, ,, a, girl, ., they, ,, ...</td>
      <td>[and, girl, girl, they, and, all, the, the, al...</td>
      <td>[girl, girl]</td>
    </tr>
  </tbody>
</table>
</div>




```python
len(dvd['by_stop'][0])
```




    18




```python
dvd['cleaned_cor'] = dvd['by_stop'].apply(lambda x: ' '.join(x))
```


```python
dvd['cleaned_cor']
```




    0    make one film say make really bad movie like s...
    1                                            film film
    2    new york joan barnard elvire audrey barnard jo...
    3    film film jump send n't jump radio n't send re...
    4    site movie bad even movie movie make movie spe...
    5    ehle northam wonderful wonderful ehle northam ...
    6    role movie n't author book funny author author...
    7    plane ceo search rescue mission call ceo harla...
    8    gritty movie movie keep sci-fi good keep suspe...
    9                                            girl girl
    Name: cleaned_cor, dtype: object



#### <a id='toc1_1_2_4_'></a>[정수 인코딩 ineger encoding](#toc0_)
---

토큰화 된 단어에 정수를 맵핑하는 방법. 가장 일반적으로는 등장 빈도를 기준으로 정렬하여 인덱스 부여


```python
print(dvd['review'][4])
print(dvd['tagged'][4])
print(dvd['lemma'][4])
print(dvd['by_freq'][4])
print(dvd['by_len'][4])
print(dvd['by_stop'][4])
```

    ['"yes, i agree with everyone on this site this movie is very very bad.', 'to even call this a movie is an insult to all movies ever made.', "it's 40 minutes long.", 'someone compares this movie to an after school special.', 'b-i-n-g-o!', 'that describes is perfectly.', 'the packaging for this movie intentionally is misleading.', 'for example, the title of this movie should describe the movie.', 'rubberface???', 'that should be the first hint.', 'it was retitled with a new package of some goofy face jim probably made in his stand-up days.', 'i was hoping for more stand-up from jim.', 'if you like jim now as an actor.', 'you would love him in his stand up days.', 'still trying to locate the rodney dangerfield young comedians special from hbo that featured jim in his early career days.', "it isn't even mentioned on this site.", "i'd love to find anything jim did stand-up wise.", 'also jim carrey is a supporting actor in this movie.', 'the main character is very very annoying.', 'she is some girl lacking self confidence but yet wants to be a stand up comedian.', 'jim is there to say lines like \\""that\'s funny janet\\"" and \\""you really are talented\\"".', 'and honestly she is terrible really terrible.', 'and the movie is terrible.', 'beware of false advertising and a really bad movie."']
    [('``', '``'), ('yes', 'RB'), (',', ','), ('i', 'JJ'), ('agree', 'VBP'), ('with', 'IN'), ('everyone', 'NN'), ('on', 'IN'), ('this', 'DT'), ('site', 'NN'), ('this', 'DT'), ('movie', 'NN'), ('is', 'VBZ'), ('very', 'RB'), ('very', 'RB'), ('bad', 'JJ'), ('.', '.'), ('to', 'TO'), ('even', 'RB'), ('call', 'VB'), ('this', 'DT'), ('a', 'DT'), ('movie', 'NN'), ('is', 'VBZ'), ('an', 'DT'), ('insult', 'NN'), ('to', 'TO'), ('all', 'DT'), ('movies', 'NNS'), ('ever', 'RB'), ('made', 'VBD'), ('.', '.'), ('it', 'PRP'), ("'s", 'VBZ'), ('40', 'CD'), ('minutes', 'NNS'), ('long', 'RB'), ('.', '.'), ('someone', 'NN'), ('compares', 'VBZ'), ('this', 'DT'), ('movie', 'NN'), ('to', 'TO'), ('an', 'DT'), ('after', 'IN'), ('school', 'NN'), ('special', 'JJ'), ('.', '.'), ('b-i-n-g-o', 'NN'), ('!', '.'), ('that', 'DT'), ('describes', 'VBZ'), ('is', 'VBZ'), ('perfectly', 'RB'), ('.', '.'), ('the', 'DT'), ('packaging', 'NN'), ('for', 'IN'), ('this', 'DT'), ('movie', 'NN'), ('intentionally', 'RB'), ('is', 'VBZ'), ('misleading', 'VBG'), ('.', '.'), ('for', 'IN'), ('example', 'NN'), (',', ','), ('the', 'DT'), ('title', 'NN'), ('of', 'IN'), ('this', 'DT'), ('movie', 'NN'), ('should', 'MD'), ('describe', 'VB'), ('the', 'DT'), ('movie', 'NN'), ('.', '.'), ('rubberface', 'NN'), ('?', '.'), ('?', '.'), ('?', '.'), ('that', 'DT'), ('should', 'MD'), ('be', 'VB'), ('the', 'DT'), ('first', 'JJ'), ('hint', 'NN'), ('.', '.'), ('it', 'PRP'), ('was', 'VBD'), ('retitled', 'VBN'), ('with', 'IN'), ('a', 'DT'), ('new', 'JJ'), ('package', 'NN'), ('of', 'IN'), ('some', 'DT'), ('goofy', 'JJ'), ('face', 'NN'), ('jim', 'NN'), ('probably', 'RB'), ('made', 'VBD'), ('in', 'IN'), ('his', 'PRP$'), ('stand-up', 'JJ'), ('days', 'NNS'), ('.', '.'), ('i', 'NN'), ('was', 'VBD'), ('hoping', 'VBG'), ('for', 'IN'), ('more', 'JJR'), ('stand-up', 'NN'), ('from', 'IN'), ('jim', 'NN'), ('.', '.'), ('if', 'IN'), ('you', 'PRP'), ('like', 'VBP'), ('jim', 'RB'), ('now', 'RB'), ('as', 'IN'), ('an', 'DT'), ('actor', 'NN'), ('.', '.'), ('you', 'PRP'), ('would', 'MD'), ('love', 'VB'), ('him', 'PRP'), ('in', 'IN'), ('his', 'PRP$'), ('stand', 'NN'), ('up', 'RP'), ('days', 'NNS'), ('.', '.'), ('still', 'RB'), ('trying', 'VBG'), ('to', 'TO'), ('locate', 'VB'), ('the', 'DT'), ('rodney', 'NN'), ('dangerfield', 'NN'), ('young', 'JJ'), ('comedians', 'NNS'), ('special', 'JJ'), ('from', 'IN'), ('hbo', 'NN'), ('that', 'WDT'), ('featured', 'VBD'), ('jim', 'NN'), ('in', 'IN'), ('his', 'PRP$'), ('early', 'JJ'), ('career', 'NN'), ('days', 'NNS'), ('.', '.'), ('it', 'PRP'), ('is', 'VBZ'), ("n't", 'RB'), ('even', 'RB'), ('mentioned', 'VBN'), ('on', 'IN'), ('this', 'DT'), ('site', 'NN'), ('.', '.'), ('i', 'NN'), ("'d", 'MD'), ('love', 'VB'), ('to', 'TO'), ('find', 'VB'), ('anything', 'NN'), ('jim', 'NN'), ('did', 'VBD'), ('stand-up', 'JJ'), ('wise', 'NN'), ('.', '.'), ('also', 'RB'), ('jim', 'NN'), ('carrey', 'NN'), ('is', 'VBZ'), ('a', 'DT'), ('supporting', 'VBG'), ('actor', 'NN'), ('in', 'IN'), ('this', 'DT'), ('movie', 'NN'), ('.', '.'), ('the', 'DT'), ('main', 'JJ'), ('character', 'NN'), ('is', 'VBZ'), ('very', 'RB'), ('very', 'RB'), ('annoying', 'VBG'), ('.', '.'), ('she', 'PRP'), ('is', 'VBZ'), ('some', 'DT'), ('girl', 'JJ'), ('lacking', 'VBG'), ('self', 'JJ'), ('confidence', 'NN'), ('but', 'CC'), ('yet', 'RB'), ('wants', 'VBZ'), ('to', 'TO'), ('be', 'VB'), ('a', 'DT'), ('stand', 'NN'), ('up', 'RP'), ('comedian', 'NN'), ('.', '.'), ('jim', 'NN'), ('is', 'VBZ'), ('there', 'RB'), ('to', 'TO'), ('say', 'VB'), ('lines', 'NNS'), ('like', 'IN'), ('\\', 'NN'), ("''", "''"), ("''", "''"), ('that', 'WDT'), ("'s", 'VBZ'), ('funny', 'JJ'), ('janet\\', 'NN'), ("''", "''"), ("''", "''"), ('and', 'CC'), ('\\', 'VB'), ("''", "''"), ("''", "''"), ('you', 'PRP'), ('really', 'RB'), ('are', 'VBP'), ('talented\\', 'JJ'), ("''", "''"), ("''", "''"), ('.', '.'), ('and', 'CC'), ('honestly', 'RB'), ('she', 'PRP'), ('is', 'VBZ'), ('terrible', 'JJ'), ('really', 'RB'), ('terrible', 'JJ'), ('.', '.'), ('and', 'CC'), ('the', 'DT'), ('movie', 'NN'), ('is', 'VBZ'), ('terrible', 'JJ'), ('.', '.'), ('beware', 'NN'), ('of', 'IN'), ('false', 'JJ'), ('advertising', 'NN'), ('and', 'CC'), ('a', 'DT'), ('really', 'RB'), ('bad', 'JJ'), ('movie', 'NN'), ('.', '.'), ("''", "''")]
    ['``', 'yes', ',', 'i', 'agree', 'with', 'everyone', 'on', 'this', 'site', 'this', 'movie', 'be', 'very', 'very', 'bad', '.', 'to', 'even', 'call', 'this', 'a', 'movie', 'be', 'an', 'insult', 'to', 'all', 'movie', 'ever', 'make', '.', 'it', "'s", '40', 'minute', 'long', '.', 'someone', 'compare', 'this', 'movie', 'to', 'an', 'after', 'school', 'special', '.', 'b-i-n-g-o', '!', 'that', 'describe', 'be', 'perfectly', '.', 'the', 'packaging', 'for', 'this', 'movie', 'intentionally', 'be', 'mislead', '.', 'for', 'example', ',', 'the', 'title', 'of', 'this', 'movie', 'should', 'describe', 'the', 'movie', '.', 'rubberface', '?', '?', '?', 'that', 'should', 'be', 'the', 'first', 'hint', '.', 'it', 'be', 'retitled', 'with', 'a', 'new', 'package', 'of', 'some', 'goofy', 'face', 'jim', 'probably', 'make', 'in', 'his', 'stand-up', 'day', '.', 'i', 'be', 'hop', 'for', 'more', 'stand-up', 'from', 'jim', '.', 'if', 'you', 'like', 'jim', 'now', 'as', 'an', 'actor', '.', 'you', 'would', 'love', 'him', 'in', 'his', 'stand', 'up', 'day', '.', 'still', 'try', 'to', 'locate', 'the', 'rodney', 'dangerfield', 'young', 'comedian', 'special', 'from', 'hbo', 'that', 'feature', 'jim', 'in', 'his', 'early', 'career', 'day', '.', 'it', 'be', "n't", 'even', 'mention', 'on', 'this', 'site', '.', 'i', "'d", 'love', 'to', 'find', 'anything', 'jim', 'do', 'stand-up', 'wise', '.', 'also', 'jim', 'carrey', 'be', 'a', 'support', 'actor', 'in', 'this', 'movie', '.', 'the', 'main', 'character', 'be', 'very', 'very', 'annoy', '.', 'she', 'be', 'some', 'girl', 'lack', 'self', 'confidence', 'but', 'yet', 'want', 'to', 'be', 'a', 'stand', 'up', 'comedian', '.', 'jim', 'be', 'there', 'to', 'say', 'line', 'like', '\\', "''", "''", 'that', "'s", 'funny', 'janet\\', "''", "''", 'and', '\\', "''", "''", 'you', 'really', 'be', 'talented\\', "''", "''", '.', 'and', 'honestly', 'she', 'be', 'terrible', 'really', 'terrible', '.', 'and', 'the', 'movie', 'be', 'terrible', '.', 'beware', 'of', 'false', 'advertising', 'and', 'a', 'really', 'bad', 'movie', '.', "''"]
    [',', 'i', 'with', 'on', 'this', 'site', 'this', 'movie', 'be', 'very', 'very', 'bad', '.', 'to', 'even', 'this', 'a', 'movie', 'be', 'an', 'to', 'movie', 'make', '.', 'it', "'s", '.', 'this', 'movie', 'to', 'an', 'special', '.', 'that', 'describe', 'be', '.', 'the', 'for', 'this', 'movie', 'be', '.', 'for', ',', 'the', 'of', 'this', 'movie', 'should', 'describe', 'the', 'movie', '.', '?', '?', '?', 'that', 'should', 'be', 'the', '.', 'it', 'be', 'with', 'a', 'of', 'some', 'jim', 'make', 'in', 'his', 'stand-up', 'day', '.', 'i', 'be', 'for', 'stand-up', 'from', 'jim', '.', 'you', 'like', 'jim', 'an', 'actor', '.', 'you', 'love', 'in', 'his', 'stand', 'up', 'day', '.', 'to', 'the', 'comedian', 'special', 'from', 'that', 'jim', 'in', 'his', 'day', '.', 'it', 'be', 'even', 'on', 'this', 'site', '.', 'i', 'love', 'to', 'jim', 'stand-up', '.', 'jim', 'be', 'a', 'actor', 'in', 'this', 'movie', '.', 'the', 'be', 'very', 'very', '.', 'she', 'be', 'some', 'to', 'be', 'a', 'stand', 'up', 'comedian', '.', 'jim', 'be', 'to', 'like', '\\', "''", "''", 'that', "'s", "''", "''", 'and', '\\', "''", "''", 'you', 'really', 'be', "''", "''", '.', 'and', 'she', 'be', 'terrible', 'really', 'terrible', '.', 'and', 'the', 'movie', 'be', 'terrible', '.', 'of', 'and', 'a', 'really', 'bad', 'movie', '.', "''"]
    ['with', 'this', 'site', 'this', 'movie', 'very', 'very', 'bad', 'even', 'this', 'movie', 'movie', 'make', 'this', 'movie', 'special', 'that', 'describe', 'the', 'for', 'this', 'movie', 'for', 'the', 'this', 'movie', 'should', 'describe', 'the', 'movie', 'that', 'should', 'the', 'with', 'some', 'jim', 'make', 'his', 'stand-up', 'day', 'for', 'stand-up', 'from', 'jim', 'you', 'like', 'jim', 'actor', 'you', 'love', 'his', 'stand', 'day', 'the', 'comedian', 'special', 'from', 'that', 'jim', 'his', 'day', 'even', 'this', 'site', 'love', 'jim', 'stand-up', 'jim', 'actor', 'this', 'movie', 'the', 'very', 'very', 'she', 'some', 'stand', 'comedian', 'jim', 'like', 'that', 'and', 'you', 'really', 'and', 'she', 'terrible', 'really', 'terrible', 'and', 'the', 'movie', 'terrible', 'and', 'really', 'bad', 'movie']
    ['site', 'movie', 'bad', 'even', 'movie', 'movie', 'make', 'movie', 'special', 'describe', 'movie', 'movie', 'describe', 'movie', 'jim', 'make', 'stand-up', 'day', 'stand-up', 'jim', 'like', 'jim', 'actor', 'love', 'stand', 'day', 'comedian', 'special', 'jim', 'day', 'even', 'site', 'love', 'jim', 'stand-up', 'jim', 'actor', 'movie', 'stand', 'comedian', 'jim', 'like', 'really', 'terrible', 'really', 'terrible', 'movie', 'terrible', 'really', 'bad', 'movie']
    


```python
dvd[['by_stop']]
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
      <th>by_stop</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>[make, one, film, say, make, really, bad, movi...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>[film, film]</td>
    </tr>
    <tr>
      <th>2</th>
      <td>[new, york, joan, barnard, elvire, audrey, bar...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>[film, film, jump, send, n't, jump, radio, n't...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>[site, movie, bad, even, movie, movie, make, m...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>[ehle, northam, wonderful, wonderful, ehle, no...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>[role, movie, n't, author, book, funny, author...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>[plane, ceo, search, rescue, mission, call, ce...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>[gritty, movie, movie, keep, sci-fi, good, kee...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>[girl, girl]</td>
    </tr>
  </tbody>
</table>
</div>




```python
Counter(dvd['by_stop'][3])
```




    Counter({"n't": 5,
             'jump': 3,
             'radio': 3,
             'film': 2,
             'send': 2,
             'reporter': 2,
             'fear': 2})




```python
tkn = dvd['by_stop'][7]
vcb = Counter(tkn)
```


```python
vcb = vcb.most_common()
vcb
```




    [('scene', 10),
     ('reason', 8),
     ('film', 6),
     ('could', 6),
     ('quastel', 6),
     ('time', 6),
     ('monster', 5),
     ('try', 4),
     ('one', 4),
     ("'re", 4),
     ('dialogue', 4),
     ('idea', 4),
     ('search', 3),
     ('rescue', 3),
     ('call', 3),
     ('knowles', 3),
     ('henriksen', 3),
     ('easily', 3),
     ('bad', 3),
     ('see', 3),
     ('appear', 3),
     ('get', 3),
     ('character', 3),
     ('think', 3),
     ('good', 3),
     ('use', 3),
     ('whether', 3),
     ('need', 3),
     ("n't", 3),
     ('even', 3),
     ('though', 3),
     ('plane', 2),
     ('ceo', 2),
     ('mission', 2),
     ('harlan', 2),
     ('lance', 2),
     ('put', 2),
     ('wood', 2),
     ('two', 2),
     ('decent', 2),
     ('sasquatch', 2),
     ('edit', 2),
     ('want', 2),
     ('potential', 2),
     ('material', 2),
     ('relate', 2),
     ('crib', 2),
     ('exposition', 2),
     ('far', 2),
     ('costume', 2),
     ('would', 2),
     ('stereotype', 2),
     ('well', 2),
     ('effective', 2),
     ('make', 2),
     ('occur', 2),
     ('line', 2),
     ('back', 2),
     ('irrelevant', 2),
     ('comment', 2),
     ('cut', 2),
     ('random', 2),
     ('show', 2),
     ('important', 2),
     ('either', 2),
     ('never', 2),
     ('leave', 2),
     ('like', 2),
     ('love', 2)]




```python
indx = {}
i = 0
for (word, frq) in vcb:
    i += 1
    indx[word] = i
```


```python
indx
```




    {'scene': 1,
     'reason': 2,
     'film': 3,
     'could': 4,
     'quastel': 5,
     'time': 6,
     'monster': 7,
     'try': 8,
     'one': 9,
     "'re": 10,
     'dialogue': 11,
     'idea': 12,
     'search': 13,
     'rescue': 14,
     'call': 15,
     'knowles': 16,
     'henriksen': 17,
     'easily': 18,
     'bad': 19,
     'see': 20,
     'appear': 21,
     'get': 22,
     'character': 23,
     'think': 24,
     'good': 25,
     'use': 26,
     'whether': 27,
     'need': 28,
     "n't": 29,
     'even': 30,
     'though': 31,
     'plane': 32,
     'ceo': 33,
     'mission': 34,
     'harlan': 35,
     'lance': 36,
     'put': 37,
     'wood': 38,
     'two': 39,
     'decent': 40,
     'sasquatch': 41,
     'edit': 42,
     'want': 43,
     'potential': 44,
     'material': 45,
     'relate': 46,
     'crib': 47,
     'exposition': 48,
     'far': 49,
     'costume': 50,
     'would': 51,
     'stereotype': 52,
     'well': 53,
     'effective': 54,
     'make': 55,
     'occur': 56,
     'line': 57,
     'back': 58,
     'irrelevant': 59,
     'comment': 60,
     'cut': 61,
     'random': 62,
     'show': 63,
     'important': 64,
     'either': 65,
     'never': 66,
     'leave': 67,
     'like': 68,
     'love': 69}




```python
encoded_idx = []
for tok in tkn:
    idn = indx[tok]
    encoded_idx.append(idn)
```


```python
encoded_idx
```




    [32,
     33,
     13,
     14,
     34,
     15,
     33,
     35,
     16,
     36,
     17,
     37,
     13,
     14,
     34,
     16,
     13,
     8,
     14,
     38,
     3,
     9,
     36,
     17,
     9,
     39,
     4,
     18,
     40,
     3,
     39,
     10,
     5,
     3,
     15,
     41,
     19,
     42,
     20,
     5,
     21,
     8,
     6,
     43,
     8,
     44,
     45,
     46,
     32,
     8,
     47,
     45,
     46,
     7,
     47,
     48,
     11,
     44,
     49,
     7,
     50,
     22,
     20,
     23,
     38,
     4,
     5,
     51,
     52,
     6,
     7,
     42,
     53,
     1,
     40,
     11,
     4,
     18,
     54,
     41,
     55,
     2,
     5,
     24,
     25,
     12,
     11,
     1,
     56,
     6,
     20,
     57,
     1,
     57,
     1,
     58,
     58,
     2,
     24,
     25,
     12,
     26,
     26,
     11,
     27,
     28,
     12,
     6,
     59,
     60,
     27,
     59,
     60,
     56,
     9,
     6,
     2,
     29,
     27,
     1,
     61,
     62,
     1,
     10,
     63,
     21,
     62,
     64,
     65,
     66,
     21,
     10,
     49,
     1,
     2,
     67,
     1,
     3,
     65,
     28,
     48,
     22,
     28,
     61,
     64,
     7,
     4,
     18,
     63,
     2,
     23,
     67,
     30,
     31,
     2,
     1,
     30,
     31,
     66,
     2,
     23,
     15,
     35,
     16,
     68,
     10,
     52,
     2,
     5,
     26,
     7,
     1,
     30,
     31,
     50,
     29,
     19,
     51,
     54,
     37,
     19,
     4,
     22,
     12,
     43,
     68,
     3,
     25,
     17,
     69,
     69,
     3,
     9,
     4,
     29,
     6,
     24,
     53,
     5,
     55]




```python
tokens = sum(dvd['by_stop'], [])
tokens
```




    ['make',
     'one',
     'film',
     'say',
     'make',
     'really',
     'bad',
     'movie',
     'like',
     'say',
     'make',
     'really',
     'bad',
     'movie',
     'bad',
     'one',
     'film',
     'like',
     'film',
     'film',
     'new',
     'york',
     'joan',
     'barnard',
     'elvire',
     'audrey',
     'barnard',
     'john',
     'saxon',
     'italy',
     'etruscan',
     'tomb',
     'joan',
     'italy',
     'colleague',
     'italy',
     'maggot',
     'maggot',
     'joan',
     'drug',
     'drug',
     'tomb',
     'colleague',
     'story',
     'end',
     'new',
     'york',
     'joan',
     'colleague',
     'romantic',
     'end',
     'waste',
     'time',
     'watch',
     'story',
     'romantic',
     'end',
     'elvire',
     'audrey',
     'john',
     'saxon',
     'maggot',
     'watch',
     'etrusco',
     'watch',
     'waste',
     'time',
     'etrusco',
     'etruscan',
     'film',
     'film',
     'jump',
     'send',
     "n't",
     'jump',
     'radio',
     "n't",
     'send',
     'reporter',
     'fear',
     'jump',
     'fear',
     'radio',
     'reporter',
     "n't",
     'radio',
     "n't",
     "n't",
     'site',
     'movie',
     'bad',
     'even',
     'movie',
     'movie',
     'make',
     'movie',
     'special',
     'describe',
     'movie',
     'movie',
     'describe',
     'movie',
     'jim',
     'make',
     'stand-up',
     'day',
     'stand-up',
     'jim',
     'like',
     'jim',
     'actor',
     'love',
     'stand',
     'day',
     'comedian',
     'special',
     'jim',
     'day',
     'even',
     'site',
     'love',
     'jim',
     'stand-up',
     'jim',
     'actor',
     'movie',
     'stand',
     'comedian',
     'jim',
     'like',
     'really',
     'terrible',
     'really',
     'terrible',
     'movie',
     'terrible',
     'really',
     'bad',
     'movie',
     'ehle',
     'northam',
     'wonderful',
     'wonderful',
     'ehle',
     'northam',
     'lust',
     'lust',
     'ehle',
     'northam',
     'role',
     'movie',
     "n't",
     'author',
     'book',
     'funny',
     'author',
     'author',
     'role',
     "n't",
     'funny',
     'queen',
     'corn',
     'corn',
     'queen',
     'author',
     'book',
     'movie',
     "n't",
     'plane',
     'ceo',
     'search',
     'rescue',
     'mission',
     'call',
     'ceo',
     'harlan',
     'knowles',
     'lance',
     'henriksen',
     'put',
     'search',
     'rescue',
     'mission',
     'knowles',
     'search',
     'try',
     'rescue',
     'wood',
     'film',
     'one',
     'lance',
     'henriksen',
     'one',
     'two',
     'could',
     'easily',
     'decent',
     'film',
     'two',
     "'re",
     'quastel',
     'film',
     'call',
     'sasquatch',
     'bad',
     'edit',
     'see',
     'quastel',
     'appear',
     'try',
     'time',
     'want',
     'try',
     'potential',
     'material',
     'relate',
     'plane',
     'try',
     'crib',
     'material',
     'relate',
     'monster',
     'crib',
     'exposition',
     'dialogue',
     'potential',
     'far',
     'monster',
     'costume',
     'get',
     'see',
     'character',
     'wood',
     'could',
     'quastel',
     'would',
     'stereotype',
     'time',
     'monster',
     'edit',
     'well',
     'scene',
     'decent',
     'dialogue',
     'could',
     'easily',
     'effective',
     'sasquatch',
     'make',
     'reason',
     'quastel',
     'think',
     'good',
     'idea',
     'dialogue',
     'scene',
     'occur',
     'time',
     'see',
     'line',
     'scene',
     'line',
     'scene',
     'back',
     'back',
     'reason',
     'think',
     'good',
     'idea',
     'use',
     'use',
     'dialogue',
     'whether',
     'need',
     'idea',
     'time',
     'irrelevant',
     'comment',
     'whether',
     'irrelevant',
     'comment',
     'occur',
     'one',
     'time',
     'reason',
     "n't",
     'whether',
     'scene',
     'cut',
     'random',
     'scene',
     "'re",
     'show',
     'appear',
     'random',
     'important',
     'either',
     'never',
     'appear',
     "'re",
     'far',
     'scene',
     'reason',
     'leave',
     'scene',
     'film',
     'either',
     'need',
     'exposition',
     'get',
     'need',
     'cut',
     'important',
     'monster',
     'could',
     'easily',
     'show',
     'reason',
     'character',
     'leave',
     'even',
     'though',
     'reason',
     'scene',
     'even',
     'though',
     'never',
     'reason',
     'character',
     'call',
     'harlan',
     'knowles',
     'like',
     "'re",
     'stereotype',
     'reason',
     'quastel',
     'use',
     'monster',
     'scene',
     'even',
     'though',
     'costume',
     "n't",
     'bad',
     'would',
     'effective',
     'put',
     'bad',
     'could',
     'get',
     'idea',
     'want',
     'like',
     'film',
     'good',
     'henriksen',
     'love',
     'love',
     'film',
     'one',
     'could',
     "n't",
     'time',
     'think',
     'well',
     'quastel',
     'make',
     'gritty',
     'movie',
     'movie',
     'keep',
     'sci-fi',
     'good',
     'keep',
     'suspense',
     'look',
     'movie',
     'sci-fi',
     "'re",
     'look',
     "'re",
     'look',
     'good',
     'gritty',
     'sci-fi',
     'good',
     'suspense',
     'movie',
     'good',
     'girl',
     'girl']




```python
indx = {}
i = 0
vocab = Counter(tokens)
vocab = vocab.most_common()

for (word, frq) in vocab:
    i += 1
    indx[word] = i
```


```python
vocab = Counter(tokens)
vocab.most_common()
```




    [('movie', 18),
     ('film', 12),
     ("n't", 11),
     ('scene', 10),
     ('bad', 8),
     ('time', 8),
     ('reason', 8),
     ('make', 7),
     ('jim', 7),
     ('good', 7),
     ('one', 6),
     ('like', 6),
     ('could', 6),
     ("'re", 6),
     ('quastel', 6),
     ('really', 5),
     ('even', 5),
     ('monster', 5),
     ('joan', 4),
     ('love', 4),
     ('author', 4),
     ('try', 4),
     ('dialogue', 4),
     ('idea', 4),
     ('italy', 3),
     ('colleague', 3),
     ('maggot', 3),
     ('end', 3),
     ('watch', 3),
     ('jump', 3),
     ('radio', 3),
     ('stand-up', 3),
     ('day', 3),
     ('terrible', 3),
     ('ehle', 3),
     ('northam', 3),
     ('search', 3),
     ('rescue', 3),
     ('call', 3),
     ('knowles', 3),
     ('henriksen', 3),
     ('easily', 3),
     ('see', 3),
     ('appear', 3),
     ('get', 3),
     ('character', 3),
     ('think', 3),
     ('use', 3),
     ('whether', 3),
     ('need', 3),
     ('though', 3),
     ('sci-fi', 3),
     ('look', 3),
     ('say', 2),
     ('new', 2),
     ('york', 2),
     ('barnard', 2),
     ('elvire', 2),
     ('audrey', 2),
     ('john', 2),
     ('saxon', 2),
     ('etruscan', 2),
     ('tomb', 2),
     ('drug', 2),
     ('story', 2),
     ('romantic', 2),
     ('waste', 2),
     ('etrusco', 2),
     ('send', 2),
     ('reporter', 2),
     ('fear', 2),
     ('site', 2),
     ('special', 2),
     ('describe', 2),
     ('actor', 2),
     ('stand', 2),
     ('comedian', 2),
     ('wonderful', 2),
     ('lust', 2),
     ('role', 2),
     ('book', 2),
     ('funny', 2),
     ('queen', 2),
     ('corn', 2),
     ('plane', 2),
     ('ceo', 2),
     ('mission', 2),
     ('harlan', 2),
     ('lance', 2),
     ('put', 2),
     ('wood', 2),
     ('two', 2),
     ('decent', 2),
     ('sasquatch', 2),
     ('edit', 2),
     ('want', 2),
     ('potential', 2),
     ('material', 2),
     ('relate', 2),
     ('crib', 2),
     ('exposition', 2),
     ('far', 2),
     ('costume', 2),
     ('would', 2),
     ('stereotype', 2),
     ('well', 2),
     ('effective', 2),
     ('occur', 2),
     ('line', 2),
     ('back', 2),
     ('irrelevant', 2),
     ('comment', 2),
     ('cut', 2),
     ('random', 2),
     ('show', 2),
     ('important', 2),
     ('either', 2),
     ('never', 2),
     ('leave', 2),
     ('gritty', 2),
     ('keep', 2),
     ('suspense', 2),
     ('girl', 2)]




```python
indx
```




    {'movie': 1,
     'film': 2,
     "n't": 3,
     'scene': 4,
     'bad': 5,
     'time': 6,
     'reason': 7,
     'make': 8,
     'jim': 9,
     'good': 10,
     'one': 11,
     'like': 12,
     'could': 13,
     "'re": 14,
     'quastel': 15,
     'really': 16,
     'even': 17,
     'monster': 18,
     'joan': 19,
     'love': 20,
     'author': 21,
     'try': 22,
     'dialogue': 23,
     'idea': 24,
     'italy': 25,
     'colleague': 26,
     'maggot': 27,
     'end': 28,
     'watch': 29,
     'jump': 30,
     'radio': 31,
     'stand-up': 32,
     'day': 33,
     'terrible': 34,
     'ehle': 35,
     'northam': 36,
     'search': 37,
     'rescue': 38,
     'call': 39,
     'knowles': 40,
     'henriksen': 41,
     'easily': 42,
     'see': 43,
     'appear': 44,
     'get': 45,
     'character': 46,
     'think': 47,
     'use': 48,
     'whether': 49,
     'need': 50,
     'though': 51,
     'sci-fi': 52,
     'look': 53,
     'say': 54,
     'new': 55,
     'york': 56,
     'barnard': 57,
     'elvire': 58,
     'audrey': 59,
     'john': 60,
     'saxon': 61,
     'etruscan': 62,
     'tomb': 63,
     'drug': 64,
     'story': 65,
     'romantic': 66,
     'waste': 67,
     'etrusco': 68,
     'send': 69,
     'reporter': 70,
     'fear': 71,
     'site': 72,
     'special': 73,
     'describe': 74,
     'actor': 75,
     'stand': 76,
     'comedian': 77,
     'wonderful': 78,
     'lust': 79,
     'role': 80,
     'book': 81,
     'funny': 82,
     'queen': 83,
     'corn': 84,
     'plane': 85,
     'ceo': 86,
     'mission': 87,
     'harlan': 88,
     'lance': 89,
     'put': 90,
     'wood': 91,
     'two': 92,
     'decent': 93,
     'sasquatch': 94,
     'edit': 95,
     'want': 96,
     'potential': 97,
     'material': 98,
     'relate': 99,
     'crib': 100,
     'exposition': 101,
     'far': 102,
     'costume': 103,
     'would': 104,
     'stereotype': 105,
     'well': 106,
     'effective': 107,
     'occur': 108,
     'line': 109,
     'back': 110,
     'irrelevant': 111,
     'comment': 112,
     'cut': 113,
     'random': 114,
     'show': 115,
     'important': 116,
     'either': 117,
     'never': 118,
     'leave': 119,
     'gritty': 120,
     'keep': 121,
     'suspense': 122,
     'girl': 123}




```python
def idx_encoder(tokens, indx):
    encoded_idx = []
    for token in tokens:
        idx = indx[token]
        encoded_idx.append(idx)
    return encoded_idx
```


```python
dvd['integer_encoded'] = dvd['by_stop'].apply(lambda x: idx_encoder(x, indx))
```


```python
dvd['integer_encoded']
```




    0    [8, 11, 2, 54, 8, 16, 5, 1, 12, 54, 8, 16, 5, ...
    1                                               [2, 2]
    2    [55, 56, 19, 57, 58, 59, 57, 60, 61, 25, 62, 6...
    3    [2, 2, 30, 69, 3, 30, 31, 3, 69, 70, 71, 30, 7...
    4    [72, 1, 5, 17, 1, 1, 8, 1, 73, 74, 1, 1, 74, 1...
    5             [35, 36, 78, 78, 35, 36, 79, 79, 35, 36]
    6    [80, 1, 3, 21, 81, 82, 21, 21, 80, 3, 82, 83, ...
    7    [85, 86, 37, 38, 87, 39, 86, 88, 40, 89, 41, 9...
    8    [120, 1, 1, 121, 52, 10, 121, 122, 53, 1, 52, ...
    9                                           [123, 123]
    Name: integer_encoded, dtype: object



##### <a id='toc1_1_2_4_1_'></a>[Padding](#toc0_)
행렬로 만들기 위해 패딩을 넣기도 한다


```python
mxln = max(len(item) for item in dvd['integer_encoded'])
mxln
```




    200




```python
for row in dvd['integer_encoded']:
    while len(row) < mxln:
        row.append(0)
```


```python
dvd[['integer_encoded']]
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
      <th>integer_encoded</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>[8, 11, 2, 54, 8, 16, 5, 1, 12, 54, 8, 16, 5, ...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>[2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>[55, 56, 19, 57, 58, 59, 57, 60, 61, 25, 62, 6...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>[2, 2, 30, 69, 3, 30, 31, 3, 69, 70, 71, 30, 7...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>[72, 1, 5, 17, 1, 1, 8, 1, 73, 74, 1, 1, 74, 1...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>[35, 36, 78, 78, 35, 36, 79, 79, 35, 36, 0, 0,...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>[80, 1, 3, 21, 81, 82, 21, 21, 80, 3, 82, 83, ...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>[85, 86, 37, 38, 87, 39, 86, 88, 40, 89, 41, 9...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>[120, 1, 1, 121, 52, 10, 121, 122, 53, 1, 52, ...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>[123, 123, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,...</td>
    </tr>
  </tbody>
</table>
</div>



### <a id='toc1_1_3_'></a>[감성 분석 sentiment analysis](#toc0_)
---

1. 규칙 기반 : 감성 어휘 사전에 따라 긍정, 중립, 부정을 분류

![규칙](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5897&directory=5.1.1.png&name=5.1.1.png)

2. 머신 러닝 기반 : 긍정, 부정을 학습시킨 후 모델의 결과값으로 확인

![머신](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5897&directory=5.1.2.png&name=5.1.2.png)

- 규칙 기반을 다룬다

NLTK의 WordNet의 SentiWordNet

Natural Language Toolkit

NLTK is a leading platform for building Python programs to work with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning, wrappers for industrial-strength NLP libraries, and an active discussion forum.

WordNet® is a large lexical database of English. Nouns, verbs, adjectives and adverbs are grouped into sets of cognitive synonyms (synsets), each expressing a distinct concept. Synsets are interlinked by means of conceptual-semantic and lexical relations.

WordNet was first created in 1985, in English only, in the Cognitive Science Laboratory of Princeton University under the direction of psychology professor George Armitage Miller. It was later directed by Christiane Fellbaum. The project was initially funded by the U.S. Office of Naval Research, and later also by other U.S. government agencies including the DARPA, the National Science Foundation, the Disruptive Technology Office (formerly the Advanced Research and Development Activity) and REFLEX


```python
wordnet.synsets('lead')
```




    [Synset('lead.n.01'),
     Synset('lead.n.02'),
     Synset('lead.n.03'),
     Synset('lead.n.04'),
     Synset('lead.n.05'),
     Synset('lead.n.06'),
     Synset('lead.n.07'),
     Synset('star.n.04'),
     Synset('lead.n.09'),
     Synset('tip.n.03'),
     Synset('lead.n.11'),
     Synset('spark_advance.n.01'),
     Synset('leash.n.01'),
     Synset('lead.n.14'),
     Synset('lead.n.15'),
     Synset('jumper_cable.n.01'),
     Synset('lead.n.17'),
     Synset('lead.v.01'),
     Synset('leave.v.07'),
     Synset('lead.v.03'),
     Synset('lead.v.04'),
     Synset('lead.v.05'),
     Synset('run.v.03'),
     Synset('head.v.02'),
     Synset('lead.v.08'),
     Synset('contribute.v.03'),
     Synset('conduct.v.02'),
     Synset('go.v.25'),
     Synset('precede.v.04'),
     Synset('run.v.23'),
     Synset('moderate.v.01')]




```python
wordnet.synset('lead.n.02').definition()
```




    'a soft heavy toxic malleable metallic element; bluish white when freshly cut but tarnishes readily to dull grey'




```python
wordnet.synsets('lead', 'v')
```




    [Synset('lead.v.01'),
     Synset('leave.v.07'),
     Synset('lead.v.03'),
     Synset('lead.v.04'),
     Synset('lead.v.05'),
     Synset('run.v.03'),
     Synset('head.v.02'),
     Synset('lead.v.08'),
     Synset('contribute.v.03'),
     Synset('conduct.v.02'),
     Synset('go.v.25'),
     Synset('precede.v.04'),
     Synset('run.v.23'),
     Synset('moderate.v.01')]




```python
wordnet.synset('lead.v.05').definition()
```




    'cause to undertake a certain action'



#### <a id='toc1_1_3_1_'></a>[sentiwordnet은 감성 정보를 갖고 있다. wordnet의 단어 품사 순번 정보를 받아 올 수도 있다](#toc0_)


```python
nltk.download('sentiwordnet')
```

    [nltk_data] Downloading package sentiwordnet to
    [nltk_data]     C:\Users\moonlight\AppData\Roaming\nltk_data...
    [nltk_data]   Package sentiwordnet is already up-to-date!
    




    True




```python
print('wordnet: ', wordnet.synsets('happy'))
print('sentiwordent: ', list(swn.senti_synsets('happy')))
```

    wordnet:  [Synset('happy.a.01'), Synset('felicitous.s.02'), Synset('glad.s.02'), Synset('happy.s.04')]
    sentiwordent:  [SentiSynset('happy.a.01'), SentiSynset('felicitous.s.02'), SentiSynset('glad.s.02'), SentiSynset('happy.s.04')]
    

sentiwordnet에는 긍정, 부정, 객관성 지수가 부여돼있다
- pos_score()
- neg_score()
- obj_score()


```python
hppy = list(swn.senti_synsets('happy'))
```


```python
print(hppy[0].pos_score(),
hppy[0].neg_score(),
hppy[0].obj_score())
```

    0.875 0.0 0.125
    

모두 0 ~ 1 사이의 값을 갖는다


```python
# 따라서 pos - neg 한 값이 +1에 가까울수록 긍정 -1에 가까울수록 부정을 뜻한다
total_score = hppy[0].pos_score() - hppy[0].neg_score()
total_score
```




    0.875



품사 별 감성 값을 찾아본다


```python
wordnet.synsets('hard', 'r')
```




    [Synset('hard.r.01'),
     Synset('hard.r.02'),
     Synset('hard.r.03'),
     Synset('hard.r.04'),
     Synset('hard.r.05'),
     Synset('heavily.r.07'),
     Synset('hard.r.07'),
     Synset('hard.r.08'),
     Synset('hard.r.09'),
     Synset('hard.r.10')]




```python
# .name()는 단어, 품사, 순번을 반환한다
wordnet.synset('hard.r.02').name()
```




    'hard.r.02'




```python
adv = wordnet.synsets('hard', 'r')
adj = wordnet.synsets('hard', 'a')
```

swn.senti_synset()에 단어, 품사, 순번을 인자로 넣고 print()하면 감성 값을 알 수 있다


```python
print(swn.senti_synset(adv[0].name()))
print(swn.senti_synset(adj[0].name()))
```

    <hard.r.01: PosScore=0.125 NegScore=0.125>
    <difficult.a.01: PosScore=0.0 NegScore=0.75>
    


```python
swn.senti_synset(adv[0].name()).pos_score()
```




    0.125




```python
def get_total_senti_score(word, pos):
    sns = wordnet.synsets(word, pos)
    ssns = swn.senti_synset(sns[0].name())
    return ssns.pos_score() - ssns.neg_score()
```


```python
get_total_senti_score('teach', 'v')
```




    0.5




```python
dvd
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
      <th>review</th>
      <th>tagged</th>
      <th>lemma</th>
      <th>by_freq</th>
      <th>by_len</th>
      <th>by_stop</th>
      <th>cleaned_cor</th>
      <th>integer_encoded</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>["watching time chasers, it obvious that it wa...</td>
      <td>[(``, ``), (watching, JJ), (time, NN), (chaser...</td>
      <td>[``, watching, time, chaser, ,, it, obvious, t...</td>
      <td>[,, it, that, it, be, make, a, of, ., they, be...</td>
      <td>[that, make, they, one, film, and, say, and, m...</td>
      <td>[make, one, film, say, make, really, bad, movi...</td>
      <td>make one film say make really bad movie like s...</td>
      <td>[8, 11, 2, 54, 8, 16, 5, 1, 12, 54, 8, 16, 5, ...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>[i saw this film about 20 years ago and rememb...</td>
      <td>[(i, NN), (saw, VBD), (this, DT), (film, NN), ...</td>
      <td>[i, saw, this, film, about, 20, year, ago, and...</td>
      <td>[i, film, and, it, as, be, ., i, it, be, a, a,...</td>
      <td>[film, and, and, and, and, but, the, the, the,...</td>
      <td>[film, film]</td>
      <td>film film</td>
      <td>[2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>[minor spoilers in new york, joan barnard (elv...</td>
      <td>[(minor, JJ), (spoilers, NNS), (in, IN), (new,...</td>
      <td>[minor, spoiler, in, new, york, ,, joan, barna...</td>
      <td>[in, new, york, ,, joan, barnard, (, elvire, a...</td>
      <td>[new, york, joan, barnard, elvire, audrey, tha...</td>
      <td>[new, york, joan, barnard, elvire, audrey, bar...</td>
      <td>new york joan barnard elvire audrey barnard jo...</td>
      <td>[55, 56, 19, 57, 58, 59, 57, 60, 61, 25, 62, 6...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>[i went to see this film with a great deal of ...</td>
      <td>[(i, JJ), (went, VBD), (to, TO), (see, VB), (t...</td>
      <td>[i, go, to, see, this, film, with, a, great, d...</td>
      <td>[i, go, to, this, film, with, a, of, i, be, wi...</td>
      <td>[this, film, with, with, the, for, but, this, ...</td>
      <td>[film, film, jump, send, n't, jump, radio, n't...</td>
      <td>film film jump send n't jump radio n't send re...</td>
      <td>[2, 2, 30, 69, 3, 30, 31, 3, 69, 70, 71, 30, 7...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>["yes, i agree with everyone on this site this...</td>
      <td>[(``, ``), (yes, RB), (,, ,), (i, JJ), (agree,...</td>
      <td>[``, yes, ,, i, agree, with, everyone, on, thi...</td>
      <td>[,, i, with, on, this, site, this, movie, be, ...</td>
      <td>[with, this, site, this, movie, very, very, ba...</td>
      <td>[site, movie, bad, even, movie, movie, make, m...</td>
      <td>site movie bad even movie movie make movie spe...</td>
      <td>[72, 1, 5, 17, 1, 1, 8, 1, 73, 74, 1, 1, 74, 1...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>["jennifer ehle was sparkling in \""pride and ...</td>
      <td>[(``, ``), (jennifer, NN), (ehle, NN), (was, V...</td>
      <td>[``, jennifer, ehle, be, sparkle, in, \, '', '...</td>
      <td>[ehle, be, in, \, '', '', and, '', '', northam...</td>
      <td>[ehle, and, northam, wonderful, the, with, thi...</td>
      <td>[ehle, northam, wonderful, wonderful, ehle, no...</td>
      <td>ehle northam wonderful wonderful ehle northam ...</td>
      <td>[35, 36, 78, 78, 35, 36, 79, 79, 35, 36, 0, 0,...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>[amy poehler is a terrific comedian on saturda...</td>
      <td>[(amy, JJ), (poehler, NN), (is, VBZ), (a, DT),...</td>
      <td>[amy, poehler, be, a, terrific, comedian, on, ...</td>
      <td>[be, a, on, ,, her, role, in, movie, do, n't, ...</td>
      <td>[her, role, movie, n't, her, with, her, author...</td>
      <td>[role, movie, n't, author, book, funny, author...</td>
      <td>role movie n't author book funny author author...</td>
      <td>[80, 1, 3, 21, 81, 82, 21, 21, 80, 3, 82, 83, ...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>["a plane carrying employees of a large biotec...</td>
      <td>[(``, ``), (a, DT), (plane, NN), (carrying, VB...</td>
      <td>[``, a, plane, carry, employee, of, a, large, ...</td>
      <td>[a, plane, of, a, --, the, ceo, 's, --, go, do...</td>
      <td>[plane, the, ceo, down, the, when, the, search...</td>
      <td>[plane, ceo, search, rescue, mission, call, ce...</td>
      <td>plane ceo search rescue mission call ceo harla...</td>
      <td>[85, 86, 37, 38, 87, 39, 86, 88, 40, 89, 41, 9...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>[a well made, gritty science fiction movie, it...</td>
      <td>[(a, DT), (well, NN), (made, VBN), (,, ,), (gr...</td>
      <td>[a, well, make, ,, gritty, science, fiction, m...</td>
      <td>[a, ,, gritty, movie, ,, it, be, of, movie, ,,...</td>
      <td>[gritty, movie, movie, but, keep, the, for, th...</td>
      <td>[gritty, movie, movie, keep, sci-fi, good, kee...</td>
      <td>gritty movie movie keep sci-fi good keep suspe...</td>
      <td>[120, 1, 1, 121, 52, 10, 121, 122, 53, 1, 52, ...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>["incredibly dumb and utterly predictable stor...</td>
      <td>[(``, ``), (incredibly, RB), (dumb, JJ), (and,...</td>
      <td>[``, incredibly, dumb, and, utterly, predictab...</td>
      <td>[and, a, girl, ,, by, ,, a, girl, ., they, ,, ...</td>
      <td>[and, girl, girl, they, and, all, the, the, al...</td>
      <td>[girl, girl]</td>
      <td>girl girl</td>
      <td>[123, 123, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,...</td>
    </tr>
  </tbody>
</table>
</div>




```python
dvd['tagged'][0]
```




    [('``', '``'),
     ('watching', 'JJ'),
     ('time', 'NN'),
     ('chasers', 'NNS'),
     (',', ','),
     ('it', 'PRP'),
     ('obvious', 'VBZ'),
     ('that', 'IN'),
     ('it', 'PRP'),
     ('was', 'VBD'),
     ('made', 'VBN'),
     ('by', 'IN'),
     ('a', 'DT'),
     ('bunch', 'NN'),
     ('of', 'IN'),
     ('friends', 'NNS'),
     ('.', '.'),
     ('maybe', 'RB'),
     ('they', 'PRP'),
     ('were', 'VBD'),
     ('sitting', 'VBG'),
     ('around', 'IN'),
     ('one', 'CD'),
     ('day', 'NN'),
     ('in', 'IN'),
     ('film', 'NN'),
     ('school', 'NN'),
     ('and', 'CC'),
     ('said', 'VBD'),
     (',', ','),
     ('\\', 'FW'),
     ("''", "''"),
     ("''", "''"),
     ('hey', 'NN'),
     (',', ','),
     ('let', 'VB'),
     ("'s", 'POS'),
     ('pool', 'VB'),
     ('our', 'PRP$'),
     ('money', 'NN'),
     ('together', 'RB'),
     ('and', 'CC'),
     ('make', 'VB'),
     ('a', 'DT'),
     ('really', 'RB'),
     ('bad', 'JJ'),
     ('movie', 'NN'),
     ('!', '.'),
     ('\\', 'NN'),
     ("''", "''"),
     ("''", "''"),
     ('or', 'CC'),
     ('something', 'NN'),
     ('like', 'IN'),
     ('that', 'DT'),
     ('.', '.'),
     ('what', 'WP'),
     ('ever', 'RB'),
     ('they', 'PRP'),
     ('said', 'VBD'),
     (',', ','),
     ('they', 'PRP'),
     ('still', 'RB'),
     ('ended', 'VBD'),
     ('up', 'RP'),
     ('making', 'VBG'),
     ('a', 'DT'),
     ('really', 'RB'),
     ('bad', 'JJ'),
     ('movie', 'NN'),
     ('--', ':'),
     ('dull', 'JJ'),
     ('story', 'NN'),
     (',', ','),
     ('bad', 'JJ'),
     ('script', 'NN'),
     (',', ','),
     ('lame', 'NN'),
     ('acting', 'NN'),
     (',', ','),
     ('poor', 'JJ'),
     ('cinematography', 'NN'),
     (',', ','),
     ('bottom', 'NN'),
     ('of', 'IN'),
     ('the', 'DT'),
     ('barrel', 'NN'),
     ('stock', 'NN'),
     ('music', 'NN'),
     (',', ','),
     ('etc', 'FW'),
     ('.', '.'),
     ('all', 'DT'),
     ('corners', 'NNS'),
     ('were', 'VBD'),
     ('cut', 'VBN'),
     (',', ','),
     ('except', 'IN'),
     ('the', 'DT'),
     ('one', 'NN'),
     ('that', 'WDT'),
     ('would', 'MD'),
     ('have', 'VB'),
     ('prevented', 'VBN'),
     ('this', 'DT'),
     ('film', 'NN'),
     ("'s", 'POS'),
     ('release', 'NN'),
     ('.', '.'),
     ('life', 'NN'),
     ("'s", 'POS'),
     ('like', 'IN'),
     ('that', 'DT'),
     ('.', '.'),
     ("''", "''")]




```python
tagged_word = dvd['tagged'][0]
senti = 0

for word, tag in tagged_word:
    wntagged = penn_to_wn(tag)
    if wntagged not in (wordnet.NOUN, wordnet.ADV, wordnet.ADJ, wordnet.VERB):
        continue
    if not wordnet.synsets(word, wntagged):
        continue
    else:
        synsets = wordnet.synsets(word, wntagged)
    
    swn_synset = swn.senti_synset(synsets[0].name())
    senti += swn_synset.pos_score() - swn_synset.neg_score()
    
```


```python
senti
```




    -0.375




```python
def swn_polarity(tagged_words):
    senti = 0
    
    for word, tag in tagged_words:
        wntagged = penn_to_wn(tag)
        if wntagged not in (wordnet.NOUN, wordnet.ADV, wordnet.ADJ, wordnet.VERB):
            continue
        if not wordnet.synsets(word, wntagged):
            continue
        else:
            synsets = wordnet.synsets(word, wntagged)
    
        swn_synset = swn.senti_synset(synsets[0].name())
        senti += swn_synset.pos_score() - swn_synset.neg_score()
    return senti
```


```python
swn_polarity(dvd['tagged'][3])
```




    -0.5




```python
dvd['sentiment'] = dvd['tagged'].apply(swn_polarity)
```


```python
dvd['sentiment']
```




    0   -0.375
    1   -1.500
    2   -2.250
    3   -0.500
    4    3.000
    5    6.750
    6    0.750
    7    8.750
    8    4.500
    9   -1.125
    Name: sentiment, dtype: float64



#### <a id='toc1_1_3_2_'></a>[VADER valence aware dictionary and sentiment reasoner 감성 분석용 알고리즘](#toc0_)
- 축약형, 기호 등을 더 잘 추출해준다
- 감성 총점 계산기능이 내장


```python
nltk.download('vader_lexicon')
```

    [nltk_data] Downloading package vader_lexicon to
    [nltk_data]     C:\Users\moonlight\AppData\Roaming\nltk_data...
    




    True




```python
analyzer = SentimentIntensityAnalyzer()
```


```python
text1 = "This is a great movie!"
text2 = "This is a terrible movie!"
text3 = "This movie was just okay."
```


```python
analyzer.polarity_scores(text1)
```




    {'neg': 0.0, 'neu': 0.406, 'pos': 0.594, 'compound': 0.6588}




```python
analyzer.polarity_scores(text2)
```




    {'neg': 0.531, 'neu': 0.469, 'pos': 0.0, 'compound': -0.5255}




```python
analyzer.polarity_scores(text3)
```




    {'neg': 0.0, 'neu': 0.678, 'pos': 0.322, 'compound': 0.2263}




```python
def vader_score(text):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)['compound']
    return score
```


```python
dvd
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
      <th>review</th>
      <th>tagged</th>
      <th>lemma</th>
      <th>by_freq</th>
      <th>by_len</th>
      <th>by_stop</th>
      <th>cleaned_cor</th>
      <th>integer_encoded</th>
      <th>sentiment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>["watching time chasers, it obvious that it wa...</td>
      <td>[(``, ``), (watching, JJ), (time, NN), (chaser...</td>
      <td>[``, watching, time, chaser, ,, it, obvious, t...</td>
      <td>[,, it, that, it, be, make, a, of, ., they, be...</td>
      <td>[that, make, they, one, film, and, say, and, m...</td>
      <td>[make, one, film, say, make, really, bad, movi...</td>
      <td>make one film say make really bad movie like s...</td>
      <td>[8, 11, 2, 54, 8, 16, 5, 1, 12, 54, 8, 16, 5, ...</td>
      <td>-0.375</td>
    </tr>
    <tr>
      <th>1</th>
      <td>[i saw this film about 20 years ago and rememb...</td>
      <td>[(i, NN), (saw, VBD), (this, DT), (film, NN), ...</td>
      <td>[i, saw, this, film, about, 20, year, ago, and...</td>
      <td>[i, film, and, it, as, be, ., i, it, be, a, a,...</td>
      <td>[film, and, and, and, and, but, the, the, the,...</td>
      <td>[film, film]</td>
      <td>film film</td>
      <td>[2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ...</td>
      <td>-1.500</td>
    </tr>
    <tr>
      <th>2</th>
      <td>[minor spoilers in new york, joan barnard (elv...</td>
      <td>[(minor, JJ), (spoilers, NNS), (in, IN), (new,...</td>
      <td>[minor, spoiler, in, new, york, ,, joan, barna...</td>
      <td>[in, new, york, ,, joan, barnard, (, elvire, a...</td>
      <td>[new, york, joan, barnard, elvire, audrey, tha...</td>
      <td>[new, york, joan, barnard, elvire, audrey, bar...</td>
      <td>new york joan barnard elvire audrey barnard jo...</td>
      <td>[55, 56, 19, 57, 58, 59, 57, 60, 61, 25, 62, 6...</td>
      <td>-2.250</td>
    </tr>
    <tr>
      <th>3</th>
      <td>[i went to see this film with a great deal of ...</td>
      <td>[(i, JJ), (went, VBD), (to, TO), (see, VB), (t...</td>
      <td>[i, go, to, see, this, film, with, a, great, d...</td>
      <td>[i, go, to, this, film, with, a, of, i, be, wi...</td>
      <td>[this, film, with, with, the, for, but, this, ...</td>
      <td>[film, film, jump, send, n't, jump, radio, n't...</td>
      <td>film film jump send n't jump radio n't send re...</td>
      <td>[2, 2, 30, 69, 3, 30, 31, 3, 69, 70, 71, 30, 7...</td>
      <td>-0.500</td>
    </tr>
    <tr>
      <th>4</th>
      <td>["yes, i agree with everyone on this site this...</td>
      <td>[(``, ``), (yes, RB), (,, ,), (i, JJ), (agree,...</td>
      <td>[``, yes, ,, i, agree, with, everyone, on, thi...</td>
      <td>[,, i, with, on, this, site, this, movie, be, ...</td>
      <td>[with, this, site, this, movie, very, very, ba...</td>
      <td>[site, movie, bad, even, movie, movie, make, m...</td>
      <td>site movie bad even movie movie make movie spe...</td>
      <td>[72, 1, 5, 17, 1, 1, 8, 1, 73, 74, 1, 1, 74, 1...</td>
      <td>3.000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>["jennifer ehle was sparkling in \""pride and ...</td>
      <td>[(``, ``), (jennifer, NN), (ehle, NN), (was, V...</td>
      <td>[``, jennifer, ehle, be, sparkle, in, \, '', '...</td>
      <td>[ehle, be, in, \, '', '', and, '', '', northam...</td>
      <td>[ehle, and, northam, wonderful, the, with, thi...</td>
      <td>[ehle, northam, wonderful, wonderful, ehle, no...</td>
      <td>ehle northam wonderful wonderful ehle northam ...</td>
      <td>[35, 36, 78, 78, 35, 36, 79, 79, 35, 36, 0, 0,...</td>
      <td>6.750</td>
    </tr>
    <tr>
      <th>6</th>
      <td>[amy poehler is a terrific comedian on saturda...</td>
      <td>[(amy, JJ), (poehler, NN), (is, VBZ), (a, DT),...</td>
      <td>[amy, poehler, be, a, terrific, comedian, on, ...</td>
      <td>[be, a, on, ,, her, role, in, movie, do, n't, ...</td>
      <td>[her, role, movie, n't, her, with, her, author...</td>
      <td>[role, movie, n't, author, book, funny, author...</td>
      <td>role movie n't author book funny author author...</td>
      <td>[80, 1, 3, 21, 81, 82, 21, 21, 80, 3, 82, 83, ...</td>
      <td>0.750</td>
    </tr>
    <tr>
      <th>7</th>
      <td>["a plane carrying employees of a large biotec...</td>
      <td>[(``, ``), (a, DT), (plane, NN), (carrying, VB...</td>
      <td>[``, a, plane, carry, employee, of, a, large, ...</td>
      <td>[a, plane, of, a, --, the, ceo, 's, --, go, do...</td>
      <td>[plane, the, ceo, down, the, when, the, search...</td>
      <td>[plane, ceo, search, rescue, mission, call, ce...</td>
      <td>plane ceo search rescue mission call ceo harla...</td>
      <td>[85, 86, 37, 38, 87, 39, 86, 88, 40, 89, 41, 9...</td>
      <td>8.750</td>
    </tr>
    <tr>
      <th>8</th>
      <td>[a well made, gritty science fiction movie, it...</td>
      <td>[(a, DT), (well, NN), (made, VBN), (,, ,), (gr...</td>
      <td>[a, well, make, ,, gritty, science, fiction, m...</td>
      <td>[a, ,, gritty, movie, ,, it, be, of, movie, ,,...</td>
      <td>[gritty, movie, movie, but, keep, the, for, th...</td>
      <td>[gritty, movie, movie, keep, sci-fi, good, kee...</td>
      <td>gritty movie movie keep sci-fi good keep suspe...</td>
      <td>[120, 1, 1, 121, 52, 10, 121, 122, 53, 1, 52, ...</td>
      <td>4.500</td>
    </tr>
    <tr>
      <th>9</th>
      <td>["incredibly dumb and utterly predictable stor...</td>
      <td>[(``, ``), (incredibly, RB), (dumb, JJ), (and,...</td>
      <td>[``, incredibly, dumb, and, utterly, predictab...</td>
      <td>[and, a, girl, ,, by, ,, a, girl, ., they, ,, ...</td>
      <td>[and, girl, girl, they, and, all, the, the, al...</td>
      <td>[girl, girl]</td>
      <td>girl girl</td>
      <td>[123, 123, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,...</td>
      <td>-1.125</td>
    </tr>
  </tbody>
</table>
</div>




```python
# dvd['vader_score'] = dvd['review'].apply(vader_score)
dvd['review']
```




    0    ["watching time chasers, it obvious that it wa...
    1    [i saw this film about 20 years ago and rememb...
    2    [minor spoilers in new york, joan barnard (elv...
    3    [i went to see this film with a great deal of ...
    4    ["yes, i agree with everyone on this site this...
    5    ["jennifer ehle was sparkling in \""pride and ...
    6    [amy poehler is a terrific comedian on saturda...
    7    ["a plane carrying employees of a large biotec...
    8    [a well made, gritty science fiction movie, it...
    9    ["incredibly dumb and utterly predictable stor...
    Name: review, dtype: object




```python
rev = pd.read_csv('imdb.tsv', delimiter='\\t')
```

    C:\Users\moonlight\AppData\Local\Temp\ipykernel_4524\3882597684.py:1: ParserWarning: Falling back to the 'python' engine because the 'c' engine does not support regex separators (separators > 1 char and different from '\s+' are interpreted as regex); you can avoid this warning by specifying engine='python'.
      rev = pd.read_csv('imdb.tsv', delimiter='\\t')
    


```python
rev['vader_score'] = rev['review'].str.lower().apply(vader_score)
```


```python
rev
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
      <th>review</th>
      <th>vader_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>"Watching Time Chasers, it obvious that it was...</td>
      <td>-0.9095</td>
    </tr>
    <tr>
      <th>1</th>
      <td>I saw this film about 20 years ago and remembe...</td>
      <td>-0.9694</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Minor Spoilers In New York, Joan Barnard (Elvi...</td>
      <td>-0.2794</td>
    </tr>
    <tr>
      <th>3</th>
      <td>I went to see this film with a great deal of e...</td>
      <td>-0.9707</td>
    </tr>
    <tr>
      <th>4</th>
      <td>"Yes, I agree with everyone on this site this ...</td>
      <td>0.8049</td>
    </tr>
    <tr>
      <th>5</th>
      <td>"Jennifer Ehle was sparkling in \""Pride and P...</td>
      <td>0.9494</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Amy Poehler is a terrific comedian on Saturday...</td>
      <td>0.8473</td>
    </tr>
    <tr>
      <th>7</th>
      <td>"A plane carrying employees of a large biotech...</td>
      <td>0.9885</td>
    </tr>
    <tr>
      <th>8</th>
      <td>A well made, gritty science fiction movie, it ...</td>
      <td>0.9887</td>
    </tr>
    <tr>
      <th>9</th>
      <td>"Incredibly dumb and utterly predictable story...</td>
      <td>-0.7375</td>
    </tr>
  </tbody>
</table>
</div>




```python
dvd['vader_score'] = rev['vader_score']
dvd
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
      <th>review</th>
      <th>tagged</th>
      <th>lemma</th>
      <th>by_freq</th>
      <th>by_len</th>
      <th>by_stop</th>
      <th>cleaned_cor</th>
      <th>integer_encoded</th>
      <th>sentiment</th>
      <th>vader_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>["watching time chasers, it obvious that it wa...</td>
      <td>[(``, ``), (watching, JJ), (time, NN), (chaser...</td>
      <td>[``, watching, time, chaser, ,, it, obvious, t...</td>
      <td>[,, it, that, it, be, make, a, of, ., they, be...</td>
      <td>[that, make, they, one, film, and, say, and, m...</td>
      <td>[make, one, film, say, make, really, bad, movi...</td>
      <td>make one film say make really bad movie like s...</td>
      <td>[8, 11, 2, 54, 8, 16, 5, 1, 12, 54, 8, 16, 5, ...</td>
      <td>-0.375</td>
      <td>-0.9095</td>
    </tr>
    <tr>
      <th>1</th>
      <td>[i saw this film about 20 years ago and rememb...</td>
      <td>[(i, NN), (saw, VBD), (this, DT), (film, NN), ...</td>
      <td>[i, saw, this, film, about, 20, year, ago, and...</td>
      <td>[i, film, and, it, as, be, ., i, it, be, a, a,...</td>
      <td>[film, and, and, and, and, but, the, the, the,...</td>
      <td>[film, film]</td>
      <td>film film</td>
      <td>[2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ...</td>
      <td>-1.500</td>
      <td>-0.9694</td>
    </tr>
    <tr>
      <th>2</th>
      <td>[minor spoilers in new york, joan barnard (elv...</td>
      <td>[(minor, JJ), (spoilers, NNS), (in, IN), (new,...</td>
      <td>[minor, spoiler, in, new, york, ,, joan, barna...</td>
      <td>[in, new, york, ,, joan, barnard, (, elvire, a...</td>
      <td>[new, york, joan, barnard, elvire, audrey, tha...</td>
      <td>[new, york, joan, barnard, elvire, audrey, bar...</td>
      <td>new york joan barnard elvire audrey barnard jo...</td>
      <td>[55, 56, 19, 57, 58, 59, 57, 60, 61, 25, 62, 6...</td>
      <td>-2.250</td>
      <td>-0.2794</td>
    </tr>
    <tr>
      <th>3</th>
      <td>[i went to see this film with a great deal of ...</td>
      <td>[(i, JJ), (went, VBD), (to, TO), (see, VB), (t...</td>
      <td>[i, go, to, see, this, film, with, a, great, d...</td>
      <td>[i, go, to, this, film, with, a, of, i, be, wi...</td>
      <td>[this, film, with, with, the, for, but, this, ...</td>
      <td>[film, film, jump, send, n't, jump, radio, n't...</td>
      <td>film film jump send n't jump radio n't send re...</td>
      <td>[2, 2, 30, 69, 3, 30, 31, 3, 69, 70, 71, 30, 7...</td>
      <td>-0.500</td>
      <td>-0.9707</td>
    </tr>
    <tr>
      <th>4</th>
      <td>["yes, i agree with everyone on this site this...</td>
      <td>[(``, ``), (yes, RB), (,, ,), (i, JJ), (agree,...</td>
      <td>[``, yes, ,, i, agree, with, everyone, on, thi...</td>
      <td>[,, i, with, on, this, site, this, movie, be, ...</td>
      <td>[with, this, site, this, movie, very, very, ba...</td>
      <td>[site, movie, bad, even, movie, movie, make, m...</td>
      <td>site movie bad even movie movie make movie spe...</td>
      <td>[72, 1, 5, 17, 1, 1, 8, 1, 73, 74, 1, 1, 74, 1...</td>
      <td>3.000</td>
      <td>0.8049</td>
    </tr>
    <tr>
      <th>5</th>
      <td>["jennifer ehle was sparkling in \""pride and ...</td>
      <td>[(``, ``), (jennifer, NN), (ehle, NN), (was, V...</td>
      <td>[``, jennifer, ehle, be, sparkle, in, \, '', '...</td>
      <td>[ehle, be, in, \, '', '', and, '', '', northam...</td>
      <td>[ehle, and, northam, wonderful, the, with, thi...</td>
      <td>[ehle, northam, wonderful, wonderful, ehle, no...</td>
      <td>ehle northam wonderful wonderful ehle northam ...</td>
      <td>[35, 36, 78, 78, 35, 36, 79, 79, 35, 36, 0, 0,...</td>
      <td>6.750</td>
      <td>0.9494</td>
    </tr>
    <tr>
      <th>6</th>
      <td>[amy poehler is a terrific comedian on saturda...</td>
      <td>[(amy, JJ), (poehler, NN), (is, VBZ), (a, DT),...</td>
      <td>[amy, poehler, be, a, terrific, comedian, on, ...</td>
      <td>[be, a, on, ,, her, role, in, movie, do, n't, ...</td>
      <td>[her, role, movie, n't, her, with, her, author...</td>
      <td>[role, movie, n't, author, book, funny, author...</td>
      <td>role movie n't author book funny author author...</td>
      <td>[80, 1, 3, 21, 81, 82, 21, 21, 80, 3, 82, 83, ...</td>
      <td>0.750</td>
      <td>0.8473</td>
    </tr>
    <tr>
      <th>7</th>
      <td>["a plane carrying employees of a large biotec...</td>
      <td>[(``, ``), (a, DT), (plane, NN), (carrying, VB...</td>
      <td>[``, a, plane, carry, employee, of, a, large, ...</td>
      <td>[a, plane, of, a, --, the, ceo, 's, --, go, do...</td>
      <td>[plane, the, ceo, down, the, when, the, search...</td>
      <td>[plane, ceo, search, rescue, mission, call, ce...</td>
      <td>plane ceo search rescue mission call ceo harla...</td>
      <td>[85, 86, 37, 38, 87, 39, 86, 88, 40, 89, 41, 9...</td>
      <td>8.750</td>
      <td>0.9885</td>
    </tr>
    <tr>
      <th>8</th>
      <td>[a well made, gritty science fiction movie, it...</td>
      <td>[(a, DT), (well, NN), (made, VBN), (,, ,), (gr...</td>
      <td>[a, well, make, ,, gritty, science, fiction, m...</td>
      <td>[a, ,, gritty, movie, ,, it, be, of, movie, ,,...</td>
      <td>[gritty, movie, movie, but, keep, the, for, th...</td>
      <td>[gritty, movie, movie, keep, sci-fi, good, kee...</td>
      <td>gritty movie movie keep sci-fi good keep suspe...</td>
      <td>[120, 1, 1, 121, 52, 10, 121, 122, 53, 1, 52, ...</td>
      <td>4.500</td>
      <td>0.9887</td>
    </tr>
    <tr>
      <th>9</th>
      <td>["incredibly dumb and utterly predictable stor...</td>
      <td>[(``, ``), (incredibly, RB), (dumb, JJ), (and,...</td>
      <td>[``, incredibly, dumb, and, utterly, predictab...</td>
      <td>[and, a, girl, ,, by, ,, a, girl, ., they, ,, ...</td>
      <td>[and, girl, girl, they, and, all, the, the, al...</td>
      <td>[girl, girl]</td>
      <td>girl girl</td>
      <td>[123, 123, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,...</td>
      <td>-1.125</td>
      <td>-0.7375</td>
    </tr>
  </tbody>
</table>
</div>




```python
dvd[['review', 'sentiment', 'vader_score']]
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
      <th>review</th>
      <th>sentiment</th>
      <th>vader_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>["watching time chasers, it obvious that it wa...</td>
      <td>-0.375</td>
      <td>-0.9095</td>
    </tr>
    <tr>
      <th>1</th>
      <td>[i saw this film about 20 years ago and rememb...</td>
      <td>-1.500</td>
      <td>-0.9694</td>
    </tr>
    <tr>
      <th>2</th>
      <td>[minor spoilers in new york, joan barnard (elv...</td>
      <td>-2.250</td>
      <td>-0.2794</td>
    </tr>
    <tr>
      <th>3</th>
      <td>[i went to see this film with a great deal of ...</td>
      <td>-0.500</td>
      <td>-0.9707</td>
    </tr>
    <tr>
      <th>4</th>
      <td>["yes, i agree with everyone on this site this...</td>
      <td>3.000</td>
      <td>0.8049</td>
    </tr>
    <tr>
      <th>5</th>
      <td>["jennifer ehle was sparkling in \""pride and ...</td>
      <td>6.750</td>
      <td>0.9494</td>
    </tr>
    <tr>
      <th>6</th>
      <td>[amy poehler is a terrific comedian on saturda...</td>
      <td>0.750</td>
      <td>0.8473</td>
    </tr>
    <tr>
      <th>7</th>
      <td>["a plane carrying employees of a large biotec...</td>
      <td>8.750</td>
      <td>0.9885</td>
    </tr>
    <tr>
      <th>8</th>
      <td>[a well made, gritty science fiction movie, it...</td>
      <td>4.500</td>
      <td>0.9887</td>
    </tr>
    <tr>
      <th>9</th>
      <td>["incredibly dumb and utterly predictable stor...</td>
      <td>-1.125</td>
      <td>-0.7375</td>
    </tr>
  </tbody>
</table>
</div>



vader는 compound 값을 0 ~ 1로 표준화해서 보여주므로 비교가 더 쉽다

## <a id='toc1_2_'></a>[국어](#toc0_)

- 국어 데이터 분석 시 영어와 달리 추가로 해야 할 작업이 있다
  - 띄어쓰기 교정

## <a id='toc1_3_'></a>[수료증](https://www.codeit.kr/certificates/n3xxh-lq8ru-kF5Ru-d5PLR) [&#8593;](#toc0_)
