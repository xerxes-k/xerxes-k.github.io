---
layout: single
title:  "encapsulation"
---

# encapsulation

It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. To prevent accidental change, an object’s variable can only be changed by an object’s method. Those types of variables are known as private variables.

클래스 내부 정보를 외부에서 직접 접근하지 못하게 막는( 척을 한)다  
주민번호처럼 민감한 정보가 노출되는 경우를 차단한다

언더바 두 개를 앞에만 붙여서 만든다


```python
class Example():
    """example"""
    def __examplify(self, name):
        self.__name = name
#이렇게 하면 외부에서 instance.__name을 불러도 못 부르고
#instance.__examplify('name')을 해도 못 부른다
#특수 매소드는 이름 뒤에도 언더바 두 개가 있어서 불린다

ex = Example()
ex.__examplify('dav')
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    Cell In[13], line 10
          5 #이렇게 하면 외부에서 instance.__name을 불러도 못 부르고
          6 #instance.__examplify('name')을 해도 못 부른다
          7 #특수 매소드는 이름 뒤에도 언더바 두 개가 있어서 불린다
          9 ex = Example()
    ---> 10 ex.__examplify('dav')
    

    AttributeError: 'Example' object has no attribute '__examplify'


---

그래도 주민번호를 활용해야 할 때가 있다  
그렇게 속성에 접근할 필요가 있을 땐 설정, 접근 매소드를 따로 정의한다

즉 객체의 속성과 그것을 사용하는 매소드를 하나로 묶는 것이다


```python
class Example():
    """example"""
    def __examplify(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if type(name) is str:
            self.__name = name
        else:
            print('need string')

ex2 = Example()
ex2.set_name('mary')
ex2.get_name()
```




    'mary'



- 값을 읽는 매소드 → getter
- 값을 쓰는 메소드 → setter
- 던더 이닛__init__에서 초기값 설정할 때도 setter를 써서 하면 인자가 적절한 값인지도 확인할 수 있다


```python
class Example():
    """example"""
    def __init__(self, name):
        self.set_name(name)
        ###### 여기다가 self.__name = self.set_name(name) 이렇게 쓰고 한참 고민했다
        # 변수에다가 매소드를 집어넣고 있었다

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if type(name) is str:
            self.__name = name
        else:
            print('need string')

ex3 = Example('vitamin')
print(ex3._Example__name)
```

    vitamin
    

---

그러나 사실 이는 눈 가리고 아웅일 뿐이다 __methodname을 _ClassName__methodname으로 바꿔치기 해서 __metohdname()으로 부르지 못하게 만 할 뿐이다  
이렇게 이름을 비틀어서 못 가져오게 하는 걸 name mangling이라고 한다


```python
ex._Example__examplify('dav')
ex._Example__name
```




    'dav'



이렇게 방법만 알면 다 불러낼 수 있다 따라서 진정한 encapsulation은 아니다  
이는 파이썬의 특성으로 자바는 확실한 캡슐화가 가능하다  

언더바 두 개를 붙여서 접근을 막는 법도 있지만 개발자들 간의 표식으로 언더바 하나만 _써서 
- _변수 
- _매소드는  


직접 호출하지 않기로 서로 약속한다

그 와중에 getter와 setter는 @decorator를 이용해 따로 만들 수 있다


```python
@property
def age(self):
    return self._age

@age.setter
def age(self, value):
    self._age = value

# instance.age
#이렇게 여기에 리턴되고
# instance.age = 10
#이렇게 하면 세팅된다

# 변수 이름은 _age이다. age는 매소드 이름이다.

class Test:
    def __init__(self, name) -> None:
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, n):
        self._name = n
        
t = Test('what')
print(t.name)
t.name = 'why'
print(t.name)
```

    what
    why
    

getter, setter를 만들어줌으로써 변수를 직접 호출하지 않아도 마치 직접 호출하는 것 마냥 쓸 수 있다  
추상화를 곁들이 셈이다
