---
layout: single
title:  "함수 function"
---

# 함수 function

A function is a block of organized, reusable code that is used to perform a single, related action. Functions provide better modularity and a high degree of code reusing.

함수를 호출하면 메모리에 올라가서 실행되고, 실행이 끝나면 메모리에서 사라진다  
매개변수 parameter로 입력한 값이 인자 argument로 할당되어 함수 내부에서 사용된다  
return으로 명시한 반환값이 지정한 호출부로 할당되고  
호출부에 할당하지 않은 객체는 메모리에서 사라진다

매개변수 parameter를 받을 때 *args, **kwargs를 쓰면 무제한으로 받을 수 있다  
args는 인자를 인덱스와 쌍으로 tuple로 저장하고  
kwargs는 키, 값 쌍으로 인자를 받아서 dictionary로 저장한다


```python
def args_func(*args):
    for i, v in enumerate(args):
        print(i, v)
        
def kwargs_func(**kwargs):
    for v in kwargs.keys():
        print(v, kwargs[v])
        
args_func('kim', 'lee', 'park', 'choi')
print('-'*30)
kwargs_func(name='kim', age=30, address='seoul')
```

    0 kim
    1 lee
    2 park
    3 choi
    ------------------------------
    name kim
    age 30
    address seoul
    

### lambda 익명함수

익명함수는 가독성이 떨어져서 협업 시 지양하지만, 간단한 함수를 만들 때는 유용하다  
람다는 즉시 실행하고 메모리를 초기화하므로 메모리 관리에 유리하다는 주장이 있다


```python
def mul_func(x,y):
    return x * y
print(mul_func(10, 50))

multi = lambda x, y : x * y
print(multi(7, 8))
```

    500
    56
    

tbd 중첩함수, input, exception, built in, external, module, package etc


