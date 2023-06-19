---
layout: single
title:  "inheritance 상속"
---

# inheritance 상속

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

---

- 어떤 클래스를 상속하고 있는지 확인하는 방법  
  - help(ClassName)에서 *method resolution order*를 읽거나  
  - ClassName.mro()로 mro를 따로 출력해 볼 수 있다  
  - issubclass(자식 클래스, 부모 클래스)로 확인할 수 있다


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
    

---

### 실습: 계좌 개설


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
    

---

### 다중 상속: 여러 부모 클래스를 상속받는 것

클래스 클래스이름(부모클래스1, 부모클래스2, ...): 형식으로 받으면 된다

다만 super()로 부모 클래스를 부를 때 어떤 부모 클래스를 지칭하는지 알 수 없다  
따라서 부모클래스이름.메소드()로 호출해야 한다

부모 클래스 안에 동일한 이름의 메소드가 있다면 mro에 나오는 순서대로 호출된다  
**다중상속은 이런 단점 때문에 아예 자식 클래스에서 오버라이드 하기도 한다**
