---
layout: single
title:  "variable and binding "
---


# 변수variable 와 할당binding
---

변수는 값을 담아놓은 메모리 주소다  
변수에 값을 담는 행위를 할당한다고 한다

id() 함수는 변수의 메모리 주소를 알려준다


```python
#할당
number = 1
print(id(name))
```

    2710481561776
    

같은 값이라고 해도 다른 변수에 담으면 다른 주소를 갖는다  
**같은 값(동일인물)을 가리키는 것이 아니라 값(이름)이 같은 것(동명이인)이다**


```python
num_1 = 777
print(id(num_1))
num_2 = num_1
print(id(num_2))
num_3 = 777
print(id(num_3))

print(id(num_1) == id(num_2))
print(id(num_1) == id(num_3))
```

    2710503017552
    2710503017552
    2710502896240
    True
    False
    


```python
name_1 = "홍길동"
print(id(name_1))
name_2 = name_1
print(id(name_2))
name_3 = "홍길동"
print(id(name_3))

print(id(name_1) == id(name_2))
print(id(name_1) == id(name_3))
```

    2710503481456
    2710503481456
    2710503483952
    True
    False
    
