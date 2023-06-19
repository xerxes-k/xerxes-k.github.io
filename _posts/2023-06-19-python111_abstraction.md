---
layout: single
title:  "abstraction"
---

# abstraction

![pilars](https://nulls.co.kr/media/post-body/2021/10/07/image.png)

추상화란 객체지향 프로그래밍의 네 기둥 중 하나이다

기본적으로 정보나 과정을 이름으로 저장하는 행위를 말한다  
정보나 과정을 이름으로 저장하고 이름으로 불러옴으로 인해서 사용자는 정보자 과정에 직접 관여할 필요 없이 간단하게 이름으로 조작할 수 있다  

실천하는 방법은 여러가지가 있지만 예를 들면
- 이름 잘 짓기
- 문서화 하기
- type hinting


```python
class User:
    """User 클래스: SNS의 유저를 나타내는 클래스"""
    ############## 이렇게 클래스나 매소드나 변수를 정의할 때 따옴표 세 개로 감싸면서 설명을 해줄 수 있다
    #이렇게 적어준 설명은 파이썬 내장 함수로 불러올 수 있다
    count = 0
    # count how many insatances are created

    def __init__(self, name, email, pw):
        """__init__ 메소드: 이름, 이메일, 비밀번호를 인스턴스 변수로 갖고, 인스턴스가 생성될 때마다 클래스 변수 count를 1씩 증가시킨다."""
        self.name = name
        self.email = email
        self.pw = pw

        User.count += 1

    def say_hello(self):
        """say_hello 메소드: 유저의 이름을 포함한 인사 메시지를 출력한다."""
        print("안녕하세요! 저는 {}입니다!".format(self.name))

    def __str__(self):
        """__str__ 메소드: 유저 정보를 정의된 문자열 형태로 리턴한다."""
        return "사용자: {}, 이메일: {}, 비밀번호: ******".format(self.name, self.email)

    @classmethod
    def number_of_users(cls):
        """number_of_users 메소드: 총 유저 수를 출력하는 클래스 메소드"""
        print("총 유저 수는: {}입니다".format(cls.count))

help(User)
```

    Help on class User in module __main__:
    
    class User(builtins.object)
     |  User(name, email, pw)
     |  
     |  User 클래스: SNS의 유저를 나타내는 클래스
     |  
     |  Methods defined here:
     |  
     |  __init__(self, name, email, pw)
     |      __init__ 메소드: 이름, 이메일, 비밀번호를 인스턴스 변수로 갖고, 인스턴스가 생성될 때마다 클래스 변수 count를 1씩 증가시킨다.
     |  
     |  __str__(self)
     |      __str__ 메소드: 유저 정보를 정의된 문자열 형태로 리턴한다.
     |  
     |  say_hello(self)
     |      say_hello 메소드: 유저의 이름을 포함한 인사 메시지를 출력한다.
     |  
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |  
     |  number_of_users() from builtins.type
     |      number_of_users 메소드: 총 유저 수를 출력하는 클래스 메소드
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  count = 0
    
    

파이썬은 dynamic typing language 이기 때문에 변수가 어떤 자료형인지 굳이 지정하지 않아도 된다  
그러나 가독성을 높이고 추상화를 위해서 타입 힌트를 줄 수 있다  
타입 힌트는 그래도 개발자 간의 흔적 표시일 뿐 전혀 강제성이 없다  
힌트에 어긋나는 자료형이 오면 밑줄이 그어질 수 있으나 실행은 잘만 된다


```python
def greeting(name: str) -> str:
    """gets a string as its parameter. returns string"""
    return 'Hello ' + name
help(greeting)
greeting('carrot')
```

    Help on function greeting in module __main__:
    
    greeting(name: str) -> str
        gets a string as its parameter. returns string
    
    




    'Hello carrot'




```python
# This is how you declare the type of a variable
age: int = 1

# You don't need to initialize a variable to annotate it
a: int  # Ok (no value at runtime until assigned)

# Doing so can be useful in conditional branches
child: bool
if age < 18:
    child = True
else:
    child = False
```
