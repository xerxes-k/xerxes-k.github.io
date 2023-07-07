**Table of contents**<a id='toc0_'></a>    
- [4 pillars of OOP 객체지향 프로그래밍의 4기둥](#toc1_)    
  - [abstraction](#toc1_1_)    
  - [encapsulation](#toc1_2_)    
    - [setter, getter](#toc1_2_1_)    
    - [__methodname()](#toc1_2_2_)    
  - [inheritance 상속](#toc1_3_)    
      - [instance inheritance](#toc1_3_1_1_)    
      - [override](#toc1_3_1_2_)    
    - [실습: 계좌 개설](#toc1_3_2_)    
      - [multi inheritance 다중 상속: 여러 부모 클래스를 상속받는 것](#toc1_3_2_1_)    

<!-- vscode-jupyter-toc-config
	numbering=false
	anchor=true
	flat=false
	minLevel=1
	maxLevel=6
	/vscode-jupyter-toc-config -->
<!-- THIS CELL WILL BE REPLACED ON TOC UPDATE. DO NOT WRITE YOUR TEXT IN THIS CELL -->

# <a id='toc1_'></a>[4 pillars of OOP 객체지향 프로그래밍의 4기둥](#toc0_)

## <a id='toc1_1_'></a>[abstraction](#toc0_)

![pilars](https://nulls.co.kr/media/post-body/2021/10/07/image.png)

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

## <a id='toc1_2_'></a>[encapsulation](#toc0_)
---

It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. To prevent accidental change, an object’s variable can only be changed by an object’s method. Those types of variables are known as private variables.

클래스 내부 정보를 외부에서 직접 접근하지 못하게 막는(척을 한)다  
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


### <a id='toc1_2_1_'></a>[setter, getter](#toc0_)
---

그래도 주민번호를 활용해야 할 때가 있다  
그렇게 속성에 접근할 필요가 있을 땐 설정setter, 접근getter 매소드를 따로 정의한다

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
    

### <a id='toc1_2_2_'></a>[__methodname()](#toc0_)
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

## <a id='toc1_3_'></a>[inheritance 상속](#toc0_)
---

코드 중복을 피하기 위해 사용  
클래스 별로 공통되는 부분을 뽑아서 부모 클래스로 만들고,  
부모 클래스를 상속받아 자식 클래스를 만들어서 사용

```python
class 클래스(부모 클래스):  
```
형태로 사용할 수 있다


```python
class Employee:
    """직원 클래스"""
    raise_percentage = 1.03
    company_name = "코드잇 버거"

    
    def __init__(self, name, wage):
        """인스턴스 변수 설정"""
        self.name = name
        self.wage = wage


    def raise_pay(self):
        """직원 시급을 인상하는 메소드"""
        self.wage *= Employee.raise_percentage


    def __str__(self):
        """직원 정보를 문자열로 리턴하는 메소드"""
        return Employee.company_name + " 직원: " + self.name


class Cashier(Employee):
    pass


class Manager(Employee):
    pass
```

- 어떤 클래스를 상속하고 있는지 확인하는 방법  
  - ```help(ClassName)```에서 *method resolution order*를 읽거나  
  - ```ClassName.mro()```로 mro를 따로 출력해 볼 수 있다  
  - ```issubclass(자식 클래스, 부모 클래스)```로 확인할 수 있다


메소드는 mro에 나오는 순서대로 호출된다


```python
print(help(Cashier))
```

    Help on class Cashier in module __main__:
    
    class Cashier(Employee)
     |  Cashier(name, wage)
     |  
     |  Method resolution order:
     |      Cashier
     |      Employee
     |      builtins.object
     |  
     |  Methods inherited from Employee:
     |  
     |  __init__(self, name, wage)
     |      인스턴스 변수 설정
     |  
     |  __str__(self)
     |      직원 정보를 문자열로 리턴하는 메소드
     |  
     |  raise_pay(self)
     |      직원 시급을 인상하는 메소드
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from Employee:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from Employee:
     |  
     |  company_name = '코드잇 버거'
     |  
     |  raise_percentage = 1.03
    
    None
    


```python
print(Cashier.mro())
```

    [<class '__main__.Cashier'>, <class '__main__.Employee'>, <class 'object'>]
    


```python
print(issubclass(Cashier, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Cashier, object))
print(issubclass(Manager, list))
```

    True
    True
    True
    False
    

#### <a id='toc1_3_1_1_'></a>[instance inheritance](#toc0_)
---
자식 클래스의 인스턴스는 부모 클래스의 인스턴스이기도 하다  
인스턴스인지 여부를 확인하는 방법은  
isinstance(인스턴스, 클래스)를 사용하면 된다


```python
young = Cashier("강영훈", 8700)
print(young)
print(isinstance(young, Cashier))
print(isinstance(young, Manager))
print(isinstance(young, Employee))
```

    코드잇 버거 직원: 강영훈
    True
    False
    True
    

#### <a id='toc1_3_1_2_'></a>[override](#toc0_)
---
override: 부모 클래스의 메소드를 자식 클래스에서 재정의하는 것  
부모 클래스에 존재하는 같은 이름의 매소드를 자식 클래스에서 필요에 맞게 재정의할 수 있다

이 때, 부모 클래스의 매소드를 일부만 수정하고 싶다면  
super().메소드()를 사용하면 된다  
super()는 부모 클래스를 지칭한다  
다만 super().메소드()에 self를 넣어서 사용하면 안된다


```python
class Cashier(Employee):
    def __init__(self, name, wage):
        # super().__init__(self, name, wage) 여기서 self를 쓰지 않는다
        super().__init__(name, wage)
```

부모 클래스의 변수를 override하고 싶다면 그냥 같은 이름의 변수를 정의하면 된다


```python
class DeliveryMan(Employee):
    """배달원 클래스"""

    def __init__(self, name, wage, on_standby):
        """인스턴스 변수 설정"""
        super().__init__(name, wage)
        self.on_standby = on_standby

    def raise_pay(self):
        """시급을 인상한다"""
        self.wage *= self.raise_percentage

    def deliver(self, address):
        """배달원이 대기 중이면 주어진 주소로 배달을 보내고 아니면 메시지를 출력한다"""
        if self.on_standby:
            print(address + "로 배달 나갑니다!")
            self.on_standby = False
        else:
            print("이미 배달하러 나갔습니다!")

    def back(self):
        """배달원 복귀를 처리한다"""
        self.on_standby = True

    def __str__(self):
        return self.company_name + " 배달원: " + self.name
    

taeho = DeliveryMan("성태호", 7000, True)

taeho.raise_pay()
print(taeho.wage)

taeho.deliver("서울시 코드잇로 51 최고 건물 401호")
taeho.deliver("서울시 코드잇로 51 최고 건물 402호")

taeho.back()
taeho.deliver("서울시 코드잇로 51 최고 건물 402호") 

print(taeho)

print(DeliveryMan.mro())
```

    7210.0
    서울시 코드잇로 51 최고 건물 401호로 배달 나갑니다!
    이미 배달하러 나갔습니다!
    서울시 코드잇로 51 최고 건물 402호로 배달 나갑니다!
    코드잇 버거 배달원: 성태호
    [<class '__main__.DeliveryMan'>, <class '__main__.Employee'>, <class 'object'>]
    

### <a id='toc1_3_2_'></a>[실습: 계좌 개설](#toc0_)


```python
class CheckingAccount:
    """자유 입출금 계좌 클래스"""
    def __init__(self, name, balance, max_spending):
        """모든 인스턴스 변수의 초기값을 설정한다"""
        self.name = name
        self.balance = balance
        self.max_spending = max_spending

    def withdraw(self, amount):
        """돈을 출금한다"""
        self.balance -= amount

    def deposit(self, amount):
        """돈을 입금한다"""
        self.balance += amount

    def use_check_card(self, amount):
        """한 회 사용 한도 초과 이하인 금액을 체크 카드 결제 시 예치금을 줄인다"""
        if amount <= self.max_spending:
            self.balance -= amount
        else:
            print("{}님의 체크 카드는 한 회 {} 초과 사용 불가능합니다".format(self.name, self.max_spending))

    def __str__(self):
        """자유 입출금 계좌의 정보를 문자열로 리턴한다."""
        return "{}님의 계좌 예치금은 {}원입니다".format(self.name, self.balance)
```


```python
class SavingsAccount:
    """저축 계좌 클래스"""
    def __init__(self, name, balance, interest_rate):
        """모든 인스턴스 변수의 초기값을 설정한다"""
        self.name = name
        self.balance = balance
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        """돈을 출금한다"""
        self.balance -= amount

    def deposit(self, amount):
        """돈을 입금한다"""
        self.balance += amount

    def add_interest(self):
        """이자를 더한다"""
        self.balance *= (1+self.interest_rate)

    def __str__(self):
        """저축 계좌의 정보를 문자열로 리턴한다."""
        return "{}님의 계좌 예치금은 {}원입니다".format(self.name, self.balance)
```


```python
class BankAccount:
    # 여기에 코드를 작성하세요
    def __init__(self, name, balance):
        """모든 인스턴스 변수의 초기값을 설정한다"""
        self.name = name
        self.balance = balance    

    def withdraw(self, amount):
        """돈을 출금한다"""
        self.balance -= amount

    def deposit(self, amount):
        """돈을 입금한다"""
        self.balance += amount
    
    def __str__(self):
        """계좌의 정보를 문자열로 리턴한다."""
        return "{}님의 계좌 예치금은 {}원입니다".format(self.name, self.balance)

class CheckingAccount(BankAccount):
    # 여기에 코드를 작성하세요
    def __init__(self, name, balance, max_spending):
        """모든 인스턴스 변수의 초기값을 설정한다"""
        super().__init__(name, balance)
        self.max_spending = max_spending
        
    def use_check_card(self, amount):
        """한 회 사용 한도 초과 이하인 금액을 체크 카드 결제 시 예치금을 줄인다"""
        if amount <= self.max_spending:
            self.balance -= amount
        else:
            print("{}님의 체크 카드는 한 회 {} 초과 사용 불가능합니다".format(self.name, self.max_spending))

    

class SavingsAccount(BankAccount):
    # 여기에 코드를 작성하세요
    def __init__(self, name, balance, interest_rate):
        """모든 인스턴스 변수의 초기값을 설정한다"""
        super().__init__(name, balance)
        self.interest_rate = interest_rate
        
    def add_interest(self):
        """이자를 더한다"""
        self.balance *= (1+self.interest_rate)

bank_account_1 = CheckingAccount("성태호", 100000, 10000)
bank_account_2 = SavingsAccount("강영훈", 20000, 0.05)

bank_account_1.withdraw(1000)
bank_account_1.deposit(1000)
bank_account_1.use_check_card(2000)

bank_account_2.withdraw(1000)
bank_account_2.deposit(1000)
bank_account_2.add_interest()

print(bank_account_1)
print(bank_account_2)

print(CheckingAccount.mro())
print(SavingsAccount.mro())
```

    성태호님의 계좌 예치금은 98000원입니다
    강영훈님의 계좌 예치금은 21000.0원입니다
    [<class '__main__.CheckingAccount'>, <class '__main__.BankAccount'>, <class 'object'>]
    [<class '__main__.SavingsAccount'>, <class '__main__.BankAccount'>, <class 'object'>]
    

#### <a id='toc1_3_2_1_'></a>[multi inheritance 다중 상속: 여러 부모 클래스를 상속받는 것](#toc0_)

```클래스 클래스이름(부모클래스1, 부모클래스2, ...):``` 형식으로 받으면 된다

다만 ```super()```로 부모 클래스를 부를 때 어떤 부모 클래스를 지칭하는지 알 수 없다  
따라서 ```부모클래스이름.메소드()```로 호출해야 한다

부모 클래스 안에 동일한 이름의 메소드가 있다면 mro에 나오는 순서대로 호출된다  
**다중상속은 이런 단점 때문에 아예 자식 클래스에서 오버라이드 하기도 한다**

## 4. 다형성 polymorphism
---

하나의 변수가 여러 타입, 인스턴스를 가리킬 수 있는 것  

여러 클래스 안에 같은 이름의 매소드를 정의한다  
그리고 각각의 인스턴스를 생성한 다음 동일하게 이름 지은 매소드를 호출하면 인스턴스 마다 다른 동작을 하게 된다  
이 때 매소드의 이름은 같은데 다른 동작을 가리키는 게 다형성 덕분이다

다형성을 이용하면 같은 이름으로 다른 동작을 하는 매소드들을 한번에 통제할 수 있다  
예를 들어 부모 클래스를 만들고 거기에 매소드 이름을 먼저 정의한 뒤  
개별 클래스 마다 이름만 상속 받고 동작을 오버라이드 해놓으면  
실제 동작을 실행시킬 클래스, 함수에서 부모 클래스의 인스턴스인지 여부 isinstance()를 통해  
동작 여부를 통제할 수 있다

그러나 자식 클래스에서 오버라이드를 안 하면 오류가 난다  
자식 클래스에서 매소드를 오버라이드 하도록 강제하려면

### 추상 클래스
---
```python
from abc import ABC, abstractmethod 
```
위와 같이 추상 클래스를 import 한 뒤 (abc는 abstract base class의 약자)  
```python
class 클래스명(ABC):
```  
위와 같이 추상 클래스를 정의한다  
**추상 클래스는 ABC를 부모 클래스로 상속 받는 거라 할 수 있다**


그러면 추상 클래스를 상속받는 자식 클래스에서는 반드시 추상 클래스의 추상 매소드를 오버라이드 해야 한다
- 추상 클래스에는 하나 이상의 추상 매소드가 필요한데 추상 매소드는 @abstractmethod 데코레이터를 붙여야 한다  
- 추상 매소드는 매소드의 몸통을 가지지 않는다
- 추상 클래스는 인스턴스를 생성할 수 없다

추상 클래스를 상속 받는 자식 클래스는 추상 클래스의 추상 매소드를 반드시 오버라이드 해야 한다  
만약 오버라이드 하지 않으면 그 자체가 추상 클래스가 되고 인스턴스를 만들 수 없다

추상 클래스로 정의해두면 자식 클래스는 항상 추상 클래스의 추상 매소드를 오버라이드 해야 하므로  
자식 클래스는 언제나 특정 매소드를 갖고 있다고 기대해도 된다

추상 매소드는 가독성을 높이기 위해 type hinting을 해주는 게 좋다


```python
from math import sqrt
from abc import ABC, abstractmethod

class Shape(ABC):
    """도형 클래스"""
    @abstractmethod
    def area(self) -> float:
        """도형의 넓이를 리턴한다: 자식 클래스가 오버라이딩할 것"""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """도형의 둘레를 리턴한다: 자식 클래스가 오버라이딩할 것"""
        pass
    
    
class Paint:
    """그림판 프로그램 클래스"""
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        """도형 인스턴스만 그림판에 추가한다"""
        if isinstance(shape, Shape):
            self.shapes.append(shape)
        else:
            print("도형 클래스가 아닌 인스턴스는 추가할 수 없습니다!")

    def total_area_of_shapes(self):
        """그림판에 있는 모든 도형의 넓이의 합을 구한다"""
        return sum([shape.area() for shape in self.shapes])

    def total_perimeter_of_shapes(self):
        """그림판에 있는 모든 도형의 둘레의 합을 구한다"""
        return sum([shape.perimeter() for shape in self.shapes])

    
class RightTriangle(Shape):
    # 여기에 코드를 작성하세요
    def __init__(self, base, height) -> None:
        self.base = base
        self.height = height
    
    def area(self) -> float:
        return self.base * self.height / 2
    
    def perimeter(self) -> float:
        return self.base + self.height + sqrt((self.base**2 + self.height**2))
    
    
    

# 여기에 코드를 작성하세요
right_triangle_1 = RightTriangle(3, 4)
right_triangle_2 = RightTriangle(5, 12)
right_triangle_3 = RightTriangle(6, 8)

paint_program = Paint()

paint_program.add_shape(right_triangle_1)
paint_program.add_shape(right_triangle_2)
paint_program.add_shape(right_triangle_3)

print(paint_program.total_area_of_shapes())
print(paint_program.total_perimeter_of_shapes())


```

    60.0
    66.0
    

추상 메소드 내에 공통적으로 사용할 동작을 정의해두고  
자식 클래스에서 오버라이드 할 때 ```super().메소드명()```으로 불러오면  
오버라이드 함과 동시에 공통 동작도 실행된다

자식 클래스에서 특정 변수를 갖도록 강제하려면 추상 매소드를 정의할 때  
getter, setter를 추상 매소드로 정의하는 방법이 있다


```python
class Shape(ABC):
    """도형 클래스"""
    @abstractmethod
    def area(self) -> float:
        """도형의 넓이를 리턴한다: 자식 클래스가 오버라이딩할 것"""
        print("도형 넓이 계산 중!")

    @abstractmethod
    def perimeter(self) -> float:
        """도형의 둘레를 리턴한다: 자식 클래스가 오버라이딩할 것"""
        pass

    def __str__(self):
        return "추상 클래스라고 해서 모든 메소드가 추상 메소드일 필요는 없습니다!"

    @property
    @abstractmethod
    def x(self):
        """도형의 x 좌표 getter 메소드"""
        pass

    @property
    @abstractmethod
    def y(self):
        """도형의 y 좌표 getter 메소드"""
        pass
```


```python
class EquilateralTriangle(Shape):
    """정삼각형 클래스"""
    def __init__(self, x, y, side):
        self._x = x
        self._y = y
        self.side = side    

    def area(self):
        """정삼각형의 넓이를 리턴한다"""
        super().area() # --------------- 부모 클래스에서 가져옴
        return sqrt(3) * self.side * self.side / 4

    def perimeter(self):
        """정삼각형의 둘레를 리턴한다"""
        return 3 * self.side

    @property
    def x(self):
        """_x getter 메소드"""
        return self._x

    @x.setter
    def x(self, value):
        """_x setter 메소드"""
        self._x = value

    @property
    def y(self):
        """_y getter 메소드"""
        return self._y

    @y.setter
    def y(self, value):
        """_y setter 메소드"""
        self._y = value

equilateral_triangle = EquilateralTriangle(5, 6, 4) # 에러가 나지 않는다
equilateral_triangle.x = 10
print(equilateral_triangle.x) # 출력: 10

equilateral_triangle.y = 5
print(equilateral_triangle.y) # 출력: 5

equilateral_triangle.area()
```

    10
    5
    도형 넓이 계산 중!
    


    6.928203230275509


#### 추상 클래스의 다중상속
---
일반 클래스에서 다중 상속은 주의해야 하나, 추상 클래스는 흔히 다중 상속을 사용한다  
추상 매소드는 어차피 오버라이드 해야 하므로 추상 매소드가 겹치는 건 문제가 되지 않는다  
다만 추상 클래스라 할지라도 일반 매소드가 겹치면 마찬가지로 mro에 따라 매소가 실행되므로 주의해야 한다

#### 클래스 뿐만 아니라 함수, 매소드도 다형성을 가진다
---

함수에 옵셔널 파라미터를 정의하면 같은 함수가 여러 동작을 할 수 있다  

옵셔널 파라미터는 함수 정의에서 기본값을 정해주는 파라미터를 말하며 일반 파라미터를 정의한 후에 정의해줘야 한다  
```python
def 함수(파라미터1, 파라미터2=기본값):
```

실습 예제


```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    # 여기에 코드를 작성하세요
    @abstractmethod
    def start(self):
        pass
    
    def stop(self):
        self.speed = 0
        
    @property
    @abstractmethod
    def speed(self):
        pass
    
    @speed.setter
    def speed(self):
        pass

print(Vehicle.mro())        
print(dir(Vehicle))
```

    [<class '__main__.Vehicle'>, <class 'abc.ABC'>, <class 'object'>]
    ['__abstractmethods__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__weakref__', '_abc_impl', 'speed', 'start', 'stop']
    


```python
class Bicycle(Vehicle):
    max_speed = 15 # 자전거의 최대 속도
    
    def __init__(self, speed):
        self._speed = speed

    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, new_value):
        self._speed = new_value if 0 <= new_value <= Bicycle.max_speed else 0

    def start(self):
        # 여기에 코드를 작성하세요
        print('자전거 페달 돌리기 시작합니다.')        
        self.speed = self.max_speed / 3
        
    def __str__(self):
        # 여기에 코드를 작성하세요
        return f'이 자전거는 현재 {self.speed}km/h로 주행 중입니다.'
        
class NormalCar(Vehicle):
    
    def __init__(self, speed, max_speed):
        self._speed = speed
        self.max_speed = max_speed        
        
    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, new_value):
        self._speed = new_value if 0 <= new_value <= self.max_speed else 0
    
    def start(self):
        # 여기에 코드를 작성하세요
        print('일반 자동차 시동겁니다.')
        self.speed = self.max_speed / 2

    def __str__(self):
        # 여기에 코드를 작성하세요
        return f'이 일반 자동차는 현재 {self.speed}km/h로 주행 중입니다.'
    
    
class SportsCar(Vehicle):
    
    def __init__(self, speed, max_speed):
        self._speed = speed
        self.max_speed = max_speed
        
    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, new_value):
        self._speed = new_value if 0 <= new_value <= self.max_speed else 0
               
    def start(self):
        # 여기에 코드를 작성하세요
        print('스포츠카 시동겁니다.')   
        self.speed = self.max_speed     
             
    def __str__(self):
        # 여기에 코드를 작성하세요
        return f'이 스포츠카는 현재 {self.speed}km/h로 주행 중입니다.'
        

# 자전거 인스턴스
bicycle = Bicycle(0)        
    
# 일반 자동차 인스턴스
car = NormalCar(0, 100)

# 스포츠카 인스턴스
sports_car = SportsCar(0, 200)

# 정의한 인스턴스들을 모두 주행 시작시킨다
bicycle.start()
car.start()
sports_car.start()

# 자전거의 속도를 출력한다
print(bicycle)

# 자전거만 주행을 멈춰준다
bicycle.stop()

# 결괏값을 출력한다
print(bicycle)
print(car)
print(sports_car)
```

    자전거 페달 돌리기 시작합니다.
    일반 자동차 시동겁니다.
    스포츠카 시동겁니다.
    이 자전거는 현재 5.0km/h로 주행 중입니다.
    이 자전거는 현재 0km/h로 주행 중입니다.
    이 일반 자동차는 현재 50.0km/h로 주행 중입니다.
    이 스포츠카는 현재 200km/h로 주행 중입니다.
    


```python
class DrivingSimulator:
    def __init__(self):
        """교통 수단 인스턴스들을 담을 리스트를 변수로 갖는다"""
        self.vehicle = []

    def add_vehicle(self, new_vehicle):
        """교통 수단 인스턴스들만 시뮬레이터에 추가될 수 있게 한다"""
        if isinstance(new_vehicle, Vehicle):
            self.vehicle.append(new_vehicle)
        else:
            print(f'{new_vehicle}은 교통 수단이 아니기 때문에 추가할 수 없습니다.')            

    def start_all_vehicles(self):
        """모든 교통 수단을 주행 시작시킨다"""
        print('모든 교통 수단을 주행 시작시킵니다!')
        print()
        for v in self.vehicle:
            v.start()

    def stop_all_vehicles(self):
        """모든 교통 수단을 주행 정지시킨다"""
        print('모든 교통 수단을 주행 정지시킵니다!')
        print()
        for v in self.vehicle:
            v.stop()

    def __str__(self):
        """갖고 있는 교통 수단들의 현재 속도를 문자열로 리턴한다"""
        info = ''
        for v in self.vehicle:
            info += str(v) + '\n'
            
        return info
        
        


# 자전거 인스턴스
bicycle = Bicycle(0)

# 일반 자동차 인스턴스들
car_1 = NormalCar(0, 100)
car_2 = NormalCar(0, 120)

# 스포츠카 인스턴스들
sports_car_1 = SportsCar(0, 200)
sports_car_2 = SportsCar(0, 190)


# 주행 시뮬레이터 인스턴스
driving_simulator = DrivingSimulator()

# 교통 수단 인스턴스들을 주행 시뮬레이터에 추가한다
driving_simulator.add_vehicle(bicycle)
driving_simulator.add_vehicle(car_1)
driving_simulator.add_vehicle(car_2)
driving_simulator.add_vehicle(sports_car_1)
driving_simulator.add_vehicle(sports_car_2)
driving_simulator.add_vehicle(1)

# 시뮬레이터 내 모든 인스턴스들을 주행 시작시킨다
driving_simulator.start_all_vehicles()
print(driving_simulator)

# 시뮬레이터 내 모든 인스턴스들을 주행 정지시킨다
driving_simulator.stop_all_vehicles()
print(driving_simulator)
```

    1은 교통 수단이 아니기 때문에 추가할 수 없습니다.
    모든 교통 수단을 주행 시작시킵니다!
    
    자전거 페달 돌리기 시작합니다.
    일반 자동차 시동겁니다.
    일반 자동차 시동겁니다.
    스포츠카 시동겁니다.
    스포츠카 시동겁니다.
    이 자전거는 현재 5.0km/h로 주행 중입니다.
    이 일반 자동차는 현재 50.0km/h로 주행 중입니다.
    이 일반 자동차는 현재 60.0km/h로 주행 중입니다.
    이 스포츠카는 현재 200km/h로 주행 중입니다.
    이 스포츠카는 현재 190km/h로 주행 중입니다.
    
    모든 교통 수단을 주행 정지시킵니다!
    
    이 자전거는 현재 0km/h로 주행 중입니다.
    이 일반 자동차는 현재 0km/h로 주행 중입니다.
    이 일반 자동차는 현재 0km/h로 주행 중입니다.
    이 스포츠카는 현재 0km/h로 주행 중입니다.
    이 스포츠카는 현재 0km/h로 주행 중입니다.
    
    

지금까지 예제는 LBYL Look Before You Leap 방식으로 작성됐다  
즉, 실행 전에 미리 조건을 확인하고 실행하는 방식으로 예제에서는 ```if와 isinstance()```를 이용해 추상 클래스를 상속 받은 클래스의 객체인지를 확인하고 실행하도록 하였다

이와 달리 EAFP Easier to Ask for Forgiveness than Permission 방식은 실행 후에 예외를 처리하는 방식이다

EAFP는 try except 구문을 사용한다

## [수료증](https://www.codeit.kr/certificates/E6jXF-LtxuJ-S59X4-76ObE)
