**Table of contents**<a id='toc0_'></a>    
- [Objective Oriented Programming 객체 지향 프로그래밍](#toc1_)    
  - [절차지향 프로그래밍](#toc1_1_)    
  - [객체지향 프로그래밍](#toc1_2_)    
    - [class](#toc1_2_1_)    
    - [instance](#toc1_2_2_)    
    - [object](#toc1_2_3_)    
    - [method](#toc1_2_4_)    
      - [self](#toc1_2_4_1_)    
      - [call method](#toc1_2_4_2_)    
    - [namespace, MRO, LEGB](#toc1_2_5_)    
      - [constructor __init __](#toc1_2_5_1_)    
      - [__str __](#toc1_2_5_2_)    
    - [class method](#toc1_2_6_)    
      - [cls](#toc1_2_6_1_)    
    - [static method](#toc1_2_7_)    
  - [first class function 일급함수 tbd](#toc1_3_)    
  - [magic method](#toc1_4_)    
  - [수료증](#toc1_5_)    

<!-- vscode-jupyter-toc-config
	numbering=false
	anchor=true
	flat=false
	minLevel=1
	maxLevel=6
	/vscode-jupyter-toc-config -->
<!-- THIS CELL WILL BE REPLACED ON TOC UPDATE. DO NOT WRITE YOUR TEXT IN THIS CELL -->

# <a id='toc1_'></a>[Objective Oriented Programming 객체 지향 프로그래밍](#toc0_)
---

## <a id='toc1_1_'></a>[절차지향 프로그래밍](#toc0_)
---
컴퓨터는 주어진 코드를 순차적으로 실행하는 것이 기본이다  
그러므로 컴퓨터가 위에서부터 아래로 순차적으로 실행하게 끔 코드를 작성하는 방법을 절차 지향 프로그래밍이라고 한다

그러나 이러한 방식은 코드의 재사용성이 떨어지고 유지보수가 어렵다는 단점이 있다  

## <a id='toc1_2_'></a>[객체지향 프로그래밍](#toc0_)
---
따라서 경우에 따라 객체 지향 프로그래밍을 사용한다  
객체 지향 프로그래밍은 먼저 속성과 동작을 갖는 객체를 정의하고 이 객체들을 조립해서 프로그램을 만드는 방식이다  
Object-oriented programming (OOP) is a method of structuring a program by bundling related properties and behaviors into individual objects.

참고로 파이썬은 객체 지향 언어이고 파이썬의 모든 게 객체라고 할 수 있다  
예를 들면 모든 자료형은 결국 어떤 클래스의 객체이다

어떤 종류의 값을 가질 수 있고 어떤 종류의 동작을 할 수 있는지 미리 정의해두면  
나중에 수없이 많은 작업을 수행해야 할지라도 간단하게 처리할 수 있다  
이렇게 객체와 객체 간 상호작용을 설계하는 작업을 modeling이라고 한다  
속성attribute과 행동method을 바탕으로 객체object를 묶어내고 객체 간 상호작용을 설계한다

절차 지향 프로그래밍이 하나의 춤을 처음부터 끝까지 가르쳐 놓고 그것만 추게 하는 방법이라면  
객체 지향 프로그래밍은 먼저 춤의 부분 부분을 나눠서 동작별로 가르쳐 놓고 추게 하는 방법이다  
이렇게 구분해서 가르쳐 놓으면 나중에 동작을 변형하거나 동작들을 다른 순서로 결합해서 다양한 춤을 추게 할 수 있다

### <a id='toc1_2_1_'></a>[class](#toc0_)
---
이 때 속성attribute과 동작method을 정의하는 틀을 클래스Class 라고 한다


```python
class TwoStep:
    distance = 10
    
    def step_side(person, direction):
        person.direction = direction
        
```

### <a id='toc1_2_2_'></a>[instance](#toc0_)
---
정의 해둔 클래스를 변수에 담아 만든 객체를 인스턴스Instance 라고 한다  
인스턴스는 클래스에 정의된 속성과 동작을 그대로 물려받으면서도 속성을 또 별도로 부여할 수 있다


```python
left_two_step = TwoStep()
left_two_step.step_side('left')
print(left_two_step.direction)
```

    left
    

### <a id='toc1_2_3_'></a>[object](#toc0_)
---
객체Object는 클래스로 만들어내는 대상이다  
인스턴스는 개별 객체를 가리킨다  
객체와 인스턴스라는 말은 구분 없이 사용한다

### <a id='toc1_2_4_'></a>[method](#toc0_)
---
step_side()처럼 클래스 내부에 정의된 함수를 메서드Method 라고 한다

#### <a id='toc1_2_4_1_'></a>[self](#toc0_)
---
위에서 본 바, 매서드의 첫번째 매개변수(person)를 지정해주지 않아도 오류가 뜨지 않는다  
그 이유는 파이썬에서는 메서드의 첫번째 매개변수를 self로 인식하기 때문이다  
self란 인스턴스 자기 자신을 의미한다

그러므로 매서드의 첫번째 매개변수는 self라고 불러주는 것이 관례이다


```python
class TwoStep:
    distance = 10
    
    def step_side(self, direction):
        self.direction = direction
        
    def selfie(self):
        print('selfie')
        
    def no_self():
        print('no self')
        
```

#### <a id='toc1_2_4_2_'></a>[call method](#toc0_)
---
매서드를 호출 할 때 클래스 이름으로 부를 수도 있고 인스턴스 이름으로 부를 수도 있다


```python
left_two_step = TwoStep()
left_two_step.selfie()
TwoStep.selfie(left_two_step)
```

    selfie
    selfie
    

self가 없는 매서드는 클래스 이름으로 호출할 수 있지만 self가 있으면 인스턴스가 꼭 필요하다  
오히려 인스턴스가 매서드를 호출하면 self가 인수로 들어가므로 인스턴스는 self 없는 매서드를 부를 수 없다  
만약 불러오게 하고 싶다면 나중에 소개하는 클래스매소드class method로 정의해야 한다


```python
TwoStep.no_self()
```

    no self
    

### <a id='toc1_2_5_'></a>[namespace, MRO, LEGB](#toc0_)
---

객체는 변수나 매서드를 자기가 정의된 범위에서 찾는다  
이 범위를 네임스페이스Namespace 라고 한다  

> an abstract container or environment created to hold a logical grouping of unique identifiers or symbols

만약 어떤 reference를 불렀을 때 객체가 자기 네임스페이스에서 찾지 못하면 자기가 속한 클래스의 네임스페이스에서 찾고  
클래스의 네임스페이스에서도 찾지 못하면 부모 클래스의 네임스페이스에서 찾는다  
이렇게 찾아가는 순서를 메서드 탐색 순서Method Resolution Order, MRO 라고 한다

변수를 찾을 때도 LEGB 규칙을 따른다  
즉, 먼저 자기 네임스페이스에서 찾고(local), 그 다음엔 부모 클래스의 네임스페이스(enclosing)에서 찾는다  
그리고도 없으면 외부(global)에서 찾고 마지막으로 내장(built-in)에서 찾는다

#### <a id='toc1_2_5_1_'></a>[constructor __init __](#toc0_)
---
객체가 생성되자 마자 자동으로 호출되는 매서드를 생성자Constructor 라고 한다  
생성자는 __init__이라는 이름을 가진다


```python
class Doggy:
    species = 'doggy dogg'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('new doggy')        
        
    def info(self):
        return f'{self.name} is {self.age} years old'
    
    
    def bark(self, msg):
        return f'{self.name} says {msg}'
    
    
    def __del__(self):
        print('doggy bye bye')


matt = Doggy('matt', 2)
#__init__이 있으면
#객체 = 클래스("속성")으로 한줄로 표현할 수 있다
#그렇지 않았을 땐 객체 = 클래스()로 객체를 만들어준 후 객체.매소드("속성")로 부여해야 했다
##예를 들면 matt = Doggy() 를 만들고 그 다음 matt.name = 'matt', matt.age = 2를 따로 썼어야 한다
#두줄씩 써야 했던 걸 한줄로 쓸 수 있게 됐다
print(matt.info())
print(matt.bark('I\'m the goodest boy'))
del matt
```

    new doggy
    matt is 2 years old
    matt says I'm the goodest boy
    doggy bye bye
    


```python
class User:
    # 인스턴스 변수 설정
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

        self.following_list = []    # 이 유저가 팔로우하는 유저 리스트
        self.followers_list = []    # 이 유저를 팔로우하는 유저 리스트

    # 팔로우
    def follow(self, another_user):
        # 여기에 코드를 작성하세요
        self.following_list.append(another_user)
        another_user.followers_list.append(self)
        ## 매소드에서 셀프가 아니라 다른 인스턴스를 써도 되는 구나!?

    # 내가 몇 명을 팔로우하는지 리턴
    def num_following(self):
        # 여기에 코드를 작성하세요
        return len(self.following_list)

    # 나를 몇 명이 팔로우하는지 리턴
    def num_followers(self):
        # 여기에 코드를 작성하세요
        return len(self.followers_list)

# 유저들 생성
user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
user3 = User("Taeho", "taeho@codeit.kr", "123abc")
user4 = User("Lisa", "lisa@codeit.kr", "abc123")

# 유저마다 서로 관심 있는 유저를 팔로우
user1.follow(user2)
user1.follow(user3)
user2.follow(user1)
user2.follow(user3)
user2.follow(user4)
user4.follow(user1)

# 유저 이름, 자신의 팔로워 수, 자신이 팔로우하는 사람 수를 출력합니다
print(user1.name, user1.num_followers(), user1.num_following())
print(user2.name, user2.num_followers(), user2.num_following())
print(user3.name, user3.num_followers(), user3.num_following())
print(user4.name, user4.num_followers(), user4.num_following())
```

    Young 2 2
    Yoonsoo 1 3
    Taeho 2 0
    Lisa 1 1
    

#### <a id='toc1_2_5_2_'></a>[__str __](#toc0_)
---
언더스코어 _가 두 개 연달아 있는 걸 더블 언더스코어 줄여서 던더라고 한다

던더 에스티알__str__은 객체를 문자열로 표현할 때 사용하는 매서드이다  
던더 에스티알__str__을 갖고 있는 객체를 print() 함수의 인자로 넣으면 __str__의 리턴값이 출력된다

### <a id='toc1_2_6_'></a>[class method](#toc0_)
---

위에서 살펴 본 바와 같이 클래스 내에 정의된 함수, 즉 매소드는 자동으로 인스턴스 스스로를 첫번째 인자로 받고 우리는 이 첫번째 인자를 self라고 부른다.

그러나 클래스 내의 모든 매소드가 다 인스턴스를 인자로 필요하지 않는다. 뿐만 아니라 클래스 자체를 인자로 받을 필요가 있는 경우도 있다. 이럴 때 사용하는 것이 클래스 매소드이다.  
클래스 매소드는 decorator를 통해 정의하며 이 때 사용하는 데코레이터가 @classmethod이다  
(데코레이터는 함수를 꾸며주는 함수라고 생각하면 되는 데 데코레이터에 대한 설명과 이를 이해하기 위한 일급함수, 클로져 등에 대한 설명은 뒤에 이어서 진행하도록 한다)


```python
class Emp:
    
    num_of_emp = 0
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@email.com'
        
        Emp.num_of_emp += 1
        
    def fullname(self):
        return f'{self.first} {self.last}'
    
    def apply_rasie(self):
        self.pay = int(self.pay * Emp.raise_amt)
        
    @classmethod
    def set_raise_amt(cls, amt):
        cls.raise_amt = amt
        
    @classmethod
    def from_string(cls, case):
        first, last, pay = case.split('-')
        new_emp = cls(first, last, pay)
        return new_emp
    
    @staticmethod
    def is_workday(day):
        if day.weekday() in [5, 6]:
            return False
        return True
        
        
sarah = Emp('Sarah', 'Jones', 1000000)
john = Emp('John', 'Baptist', 1100000)

print(john.fullname())
print(sarah.email)
print(Emp.num_of_emp)

case_1 = 'Jesus-Christ-1000000'


jesus = Emp.from_string(case_1)
print(jesus.email)

import datetime
new_date = datetime.date.today()
print(Emp.is_workday(new_date))
```

    John Baptist
    SarahJones@email.com
    2
    JesusChrist@email.com
    True
    

#### <a id='toc1_2_6_1_'></a>[cls](#toc0_)
---

위 예제에서 볼 수 있듯이 클래스 매소드는 첫번째 인자로 cls를 받는다. cls는 클래스 자체를 의미한다. 매소드가 self를 쓰는 것과 같은 역할이다  
클래스 매소드도 인스턴스에서 호출 할 수 있다. 그러나 인스턴스에서 호출하더라도 첫번째 인자로 클래스가 자동으로 들어가므로 cls를 명시적으로 쓰지 않아도 된다.

클래스 매소드는 주로 클래스 변수를 다루거나 매소드 간에 공통적으로 해야하는 작업이 있을 때 사용한다.

### <a id='toc1_2_7_'></a>[static method](#toc0_)
---

스태틱 매소드는 클래스와 인스턴스의 객체를 사용하지 않는 매소드이다. 사실상 외부 함수랑 동일한데 클래스 내에 정의되어 있을 뿐이다.  
클래스나 인스턴스의 정보를 사용하진 않지만, 클래스가 수행하는 기능에 속한다고 판단 될 때 한곳에 몰아넣기 위해, 즉 기능을 일관되게 정리하고자 할 때 사용한다.  
데코레이터는 @staticmethod이며 위의 예제에서 같이 볼 수 있다

## <a id='toc1_3_'></a>[first class function 일급함수 tbd](#toc0_)

위에 설명한 데코레이터 decorator를 이해하기 위해서는 일급함수에 대한 이해가 필요하다

tbd 클로져

## <a id='toc1_4_'></a>[magic method](#toc0_)

매직 매소드란 클래스 안에 정의할 수 있는 built-in method  
매직 매소드는 __로 시작해서 __로 끝나는 이름을 가진다 여기서 _를 underscore라고 부르는데 이게 두 번 연달아 있으니 double underscore라고 부르고 이를 줄여서 dunder 던더라고 부른다  
그러므로 __init __은 던더이닛이라 부른다

매직 매소드를 이용하면 새로 만든 클래스 객체에도 파이썬의 내장 기능을 이용할 수 있다  
https://towardsdatascience.com/introducing-pythons-magic-methods-f443ed913703

## <a id='toc1_5_'></a>[수료증](https://www.codeit.kr/certificates/yNkdP-owvEs-YN619-PqEm6) [&#8593;](#toc0_)

클래스101 조대표&유대표 Python 101: 매일 30분, 40일 동안! LV. 1 파이썬 기초 프로젝트  
인프런 우리를 위한 프로그래밍 : 파이썬 중급 (Inflearn Original)
