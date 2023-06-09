---
layout: single
title:  "SOLID principles "
---

**Table of contents**<a id='toc0_'></a>    
- [SOLID principles](#toc1_)    
  - [정의](#toc1_1_)    
  - [Single Responsibility Principle](#toc1_2_)    
  - [Open/Closed Principle](#toc1_3_)    
  - [Liskov Substitution Principle](#toc1_4_)    
  - [Interface Segregation Principle](#toc1_5_)    
  - [Dependency Inversion Principle](#toc1_6_)    
  - [수료증](#toc1_7_)    

<!-- vscode-jupyter-toc-config
	numbering=false
	anchor=true
	flat=false
	minLevel=1
	maxLevel=6
	/vscode-jupyter-toc-config -->
<!-- THIS CELL WILL BE REPLACED ON TOC UPDATE. DO NOT WRITE YOUR TEXT IN THIS CELL -->

# <a id='toc1_'></a>[SOLID principles](#toc0_)
---

OOP is a programming paradigm that relies on the concept of classes and objects. It is used to structure a software program into simple, reusable pieces of code blueprints (usually called classes), which are used to create individual instances of objects. There are many object-oriented programming languages including JavaScript, C++, Java, and Python.

therefore, designing class and object is the core of OOP.

객체 지향 프로그래밍에선 클래스와 오브젝트를 디자인 하는 게 핵심이다  
아래는 널리 알려진 OOP의 5가지 원칙이다  

## <a id='toc1_1_'></a>[정의](#toc0_)
---
SOLID stands for the five principles of object-oriented programming and design. These five principles are:  
1. Single Responsibility Principle
2. Open/Closed Principle
3. Liskov Substitution Principle
4. Interface Segregation Principle
5. Dependency Inversion Principle

introduced by Robert C. Martin (Uncle Bob) in his 2000 paper Design Principles and Design Patterns, although the SOLID acronym itself was introduced later by Michael Feathers.

프로그램 크기가 클수록 SOLID 원칙으로 개발하면 코드 복잡성을 줄이고 유지보수가 용이해진다  
그러나 작고 간단한 프로그램에는 오히려 번거로운 작업이 될 수 있다

**원칙들이 적용됐을 때 얻게 되는 장점이 무엇이고 그러기 위해 해야 하는 건 무엇인지 알아야 취사선택 할 수 있다**

## <a id='toc1_2_'></a>[Single Responsibility Principle](#toc0_)
---

A class should have one and only one reason to change, meaning that a class should have only one job.

클래스는 단 하나의 책임만을 가져야 하고 그러므로 클래스 내의 모든 기능은 하나의 책임을 수행하는 데 집중되어야 한다. 책임이란 우리 말로는 '역할'이라고 할 수 있다.

나중에 기능 하나 수정 할 때 이 클래스 하나만 신경 쓰면 되게 끔 한다  
같은 이유로 수정 할 코드들이 한군데에 묶여 있을수록 좋다


```python
class Ship:
    """배 클래스"""
    def __init__(self, fuel, fuel_per_hour, supplies, num_crew):
        """연료량, 시간당 연료 소비량, 물자량, 선원 수를 인스턴스 변수로 갖는다"""
        self.fuel = fuel
        self.fuel_per_hour = fuel_per_hour
        self.supplies = supplies
        self.num_crew = num_crew

    def report_fuel(self):
        """연료량 보고 메소드"""
        print("현재 연료는 {}l 남아 있습니다".format(self.fuel))

    def load_fuel(self, amount):
        """연료 충전 메소드"""
        self.fuel += amount

    def report_supplies(self):
        """물자량 보고 메소드"""
        print("현재 물자는 {}명분이 남아 있습니다".format(self.supplies))

    def load_supplies(self, amount):
        """물자 보급 메소드"""
        self.supplies += amount

    def distribute_supplies_to_crew(self):
        """물자 배분 메소드"""
        if self.supplies >= self.num_crew:
            self.supplies -= self.num_crew
            return True
        print("물자가 부족하기 때문에 배분할 수 없습니다")
        return False

    def report_crew(self):
        """선원 수 보고 메소드"""
        print("현재 선원 {}명이 있습니다".format(self.num_crew))

    def load_crew(self, number):
        """선원 승선 메소드"""
        self.num_crew += number

    def run_engine_for_hours(self, hours):
        """엔진 작동 메소드"""
        if self.fuel > self.fuel_per_hour * hours:
            self.fuel -= self.fuel_per_hour * hours
            print("엔진을 {}시간 동안 돌립니다!".format(hours))
        else:
            print("연료가 부족하기 때문에 엔진 작동을 시작할 수 없습니다")
```


```python
class Ship:
    """배 클래스"""
    def __init__(self, fuel, fuel_per_hour, supplies, num_crew):
        self.fuel_tank = FuelTank(fuel)
        self.crew_manager = CrewManager(num_crew)
        self.supply_hold = SupplyHold(supplies, self.crew_manager)
        self.engine = Engine(self.fuel_tank, fuel_per_hour)


class FuelTank:
    """연료 탱크 클래스"""
    def __init__(self, fuel):
        """연료 탱크에 저장된 연료량을 인스턴스 변수로 갖는다"""
        self.fuel = fuel

    def load_fuel(self, amount):
        """연료 충전 메소드"""
        self.fuel += amount

    def use_fuel(self, amount):
        """연료 사용 메소드"""
        if self.fuel - amount >= 0:
            self.fuel -= amount
            return True
        print("연료가 부족합니다!")
        return False

    def report_fuel(self):
        """연료량 보고 메소드"""
        print("현재 연료는 {}l 남아 있습니다".format(self.fuel))


class Engine:
    """엔진 클래스"""
    def __init__(self, fuel_tank, fuel_per_hour):
        """연료 탱크 인스턴스와 시간당 연료 소비량을 인스턴스 변수로 갖는다"""
        self.fuel_tank = fuel_tank
        self.fuel_per_hour = fuel_per_hour

    def run_for_hours(self, hours):
        """엔진 작동 메소드, 연료 탱크 인스턴스를 사용한다"""
        if self.fuel_tank.use_fuel(self.fuel_per_hour * hours):
            print("엔진을 {}시간 동안 돌립니다!".format(hours))
            return True
        print("연료가 부족하기 때문에 엔진 작동을 시작할 수 없습니다")
        return False


class CrewManager:
    """선원 관리 클래스"""
    def __init__(self, num_crew):
        """승선한 선원 수를 인스턴스 변수로 갖는다"""
        self.num_crew = num_crew

    def load_crew(self, number):
        """선원 승선 메소드"""
        self.num_crew += number

    def report_crew(self):
        """선원 수 보고 메소드"""
        print("현재 선원 {}명이 있습니다".format(self.num_crew))


class SupplyHold:
    """물자 창고 클래스"""
    def __init__(self, supplies, crew_manager):
        """물자량과 선원 관리 인스턴스를 인스턴스 변수로 갖는다"""
        self.supplies = supplies
        self.crew_manager = crew_manager

    def load_supplies(self, amount):
        """물자 충전 메소드"""
        self.supplies += amount

    def distribute_supplies_to_crew(self):
        """물자 배분 메소드, 각 선원들에게 동일한 양의 물자를 배분한다"""
        if self.supplies >= self.crew_manager.num_crew:
            self.supplies -= self.crew_manager.num_crew
            return True
        print("물자가 부족하기 때문에 배분할 수 없습니다")
        return False

    def report_supplies(self):
        """물자량 보고 메소드"""
        print("현재 물자는 {}명분이 남아 있습니다".format(self.supplies))
```


```python
class Student:
    def __init__(self, name, id, major):
        self.name = name
        self.id = id
        self.major = major
        self.grades = []

    def change_student_info(self, new_name, new_id, new_major):
        """학생 기본 정보 수정 메소드"""
        self.name = new_name
        self.id = new_id
        self.major = new_major

    def add_grade(self, grade):
        """학점 추가 메소드"""
        if 0 <= grade <= 4.3:
            self.grades.append(grade)
        else:
            print("수업 학점은 0과 4.3 사이여야 합니다!")

    def get_average_gpa(self):
        """평균 학점 계산 메소드"""
        return sum(self.grades) / len(self.grades)

    def print_report_card(self):
        """학생 성적표 출력 메소드"""
        print("코드잇 대학 성적표\n\n학생 이름:{}\n학생 번호:{}\n소속 학과:{}\n평균 학점:{}"\
        .format(self.name, self.id, self.major, self.get_average_gpa()))
        

## 학생 인스턴스 정의
younghoon = Student("강영훈", 20120034, "통계학과")
younghoon.change_student_info("강영훈", 20130024, "컴퓨터 공학과")

## 학생 성적 추가
younghoon.add_grade(3.0)
younghoon.add_grade(3.33)
younghoon.add_grade(3.67)
younghoon.add_grade(4.3)

## 학생 성적표 
younghoon.print_report_card()
```

    코드잇 대학 성적표
    
    학생 이름:강영훈
    학생 번호:20130024
    소속 학과:컴퓨터 공학과
    평균 학점:3.575
    


```python
class Student:
    def __init__(self, name, id, major):
        self.info = Info(name, id, major)
        self.grade = Grade(self.info)

class Info:
    def __init__(self, name, id, major):
        self.name = name
        self.id = id
        self.major = major        

    def change_student_info(self, new_name, new_id, new_major):
        """학생 기본 정보 수정 메소드"""
        self.name = new_name
        self.id = new_id
        self.major = new_major
        
class Grade:
    def __init__(self, info):
        self.grades = []
        self.info = info
    
    def add_grade(self, grade):
        """학점 추가 메소드"""
        if 0 <= grade <= 4.3:
            self.grades.append(grade)
        else:
            print("수업 학점은 0과 4.3 사이여야 합니다!")

    def get_average_gpa(self):
        """평균 학점 계산 메소드"""
        return sum(self.grades) / len(self.grades)

    def print_report_card(self):
        """학생 성적표 출력 메소드"""
        print("코드잇 대학 성적표\n\n학생 이름:{}\n학생 번호:{}\n소속 학과:{}\n평균 학점:{}"\
        .format(self.info.name, self.info.id, self.info.major, self.get_average_gpa()))
```

- 사령부 클래스를 만들 때 기능 단위 클래스로부터 인스턴스를 파견 받아와야 한다  
    - student 안의 속성들은 타 클래스의 인스턴스로 생성
- 기능 단위 클래스 간에 정보를 공유해야 할 때는 사령부 단위에서 연결해주면 된다
    - Grade 클래스에게 필요한 name 등의 정보를 사령부 인스턴스 self.info로 수취


```python
## 학생 인스턴스 정의
younghoon = Student("강영훈", 20120034, "통계학과")
younghoon.info.change_student_info("강영훈", 20130024, "컴퓨터 공학과")

## 학생 성적 추가
younghoon.grade.add_grade(3.0)
younghoon.grade.add_grade(3.33)
younghoon.grade.add_grade(3.67)
younghoon.grade.add_grade(4.3)

## 학생 성적표 
younghoon.grade.print_report_card()
```

    코드잇 대학 성적표
    
    학생 이름:강영훈
    학생 번호:20130024
    소속 학과:컴퓨터 공학과
    평균 학점:3.575
    

## <a id='toc1_3_'></a>[Open/Closed Principle](#toc0_)
---

opend to extend, closed to modify  
다른 클래스를 수정하지 않아도 기능을 확장할 수 있어야 한다

다형성을 이용해 같은 이름의 매소드를 지정하고 추상화 클래스, 매소드를 상속 받게 하면  
다른 클래스를 수정하지 않아도 기능을 확장할 수 있다


```python
class MessageNotificationManager:
    """메시지 알림 관리 클래스"""
    def __init__(self):
        self.message_notifications = []

    def add_new_message(self, new_message):
        """새로 온 메시지 추가"""
        self.message_notifications.append(new_message)

    def display_message_notifications(self):
        """모든 새 메시지 확인"""
        print("새로 온 메시지들:")

        for message in self.message_notifications:
            print(message.read_message() + "\n")
```


```python
from abc import ABC, abstractclassmethod

class Message(ABC):
    """message abstraction"""
    @abstractclassmethod
    def read_message(self):
        """process messages to display"""
        pass
```


```python
class KakaoTalkMessage(Message):
    """카카오톡 메시지 클래스"""
    notification_message_max_len = 10

    def __init__(self, sent_by, time, content):
        self.sent_by = sent_by
        self.time = time
        self.content = content

    def read_message(self):
        """메시지의 정보와 내용을 리턴함"""
        message_str = "{}\n{}\n".format(self.time, self.sent_by)
        message_str += self.content if len(self.content) <= KakaoTalkMessage.notification_message_max_len else self.content[:KakaoTalkMessage.notification_message_max_len] + "..."

        return message_str
```


```python
class FacebookMessage:
    """페이스북 메시지 클래스"""
    notification_message_max_len = 15

    def __init__(self, sent_by, location, time, content):
        self.sent_by = sent_by
        self.location = location
        self.time = time
        self.content = content

    def read_message(self):
       """메시지의 정보와 내용을 리턴함"""
       res_str = "{}\n{}\n{}\n".format(self.time, self.sent_by, self.location)
       res_str += self.content if len(self.content) <= FacebookMessage.notification_message_max_len else self.content[:FacebookMessage.notification_message_max_len] + "..."
       return res_str
```


```python
class TextMessage:
    """문자 메시지 클래스"""
    notification_message_max_len = 12

    def __init__(self, sent_by, time, content):
        self.sent_by = sent_by
        self.time = time
        self.content = content

    def read_message(self):
        """메시지의 정보와 내용을 리턴함"""
        noti_string = "{}, {}\n".format(self.sent_by, self.time)
        noti_string += self.content if len(self.content) <= TextMessage.notification_message_max_len else self.content[:TextMessage.notification_message_max_len] + "..."
        return noti_string
```


```python
# 메시지 알림 관리 인스턴스 생성
message_notification_manager = MessageNotificationManager()

# 카카오톡 메시지 3개 생성
kakao_talk_message_1 = KakaoTalkMessage("고대위", "2019년 7월 1일 오후 11시 30분", "나 오늘 놀러 못갈 거 같애 미안!")
kakao_talk_message_2 = KakaoTalkMessage("고대위", "2019년 7월 1일 오후 11시 35분", "아니다 갈게 너네 어디서 놀고 있어?")
kakao_talk_message_3 = KakaoTalkMessage("이영훈", "2019년 7월 2일 오전 12시 30분", "나도 놀러 갈게 나 지금 출발")

# 메시지 알림 관리 인스턴스에 메시지 추가
message_notification_manager.add_new_message(kakao_talk_message_1)
message_notification_manager.add_new_message(kakao_talk_message_2)
message_notification_manager.add_new_message(kakao_talk_message_3)

# 메시지 알림 관리 인스턴스에 있는 모든 메시지 출력
message_notification_manager.display_message_notifications()
```

    새로 온 메시지들:
    2019년 7월 1일 오후 11시 30분
    고대위
    나 오늘 놀러 못갈...
    
    2019년 7월 1일 오후 11시 35분
    고대위
    아니다 갈게 너네 ...
    
    2019년 7월 2일 오전 12시 30분
    이영훈
    나도 놀러 갈게 나...
    
    


```python
# 메시지 알림 관리 인스턴스 생성
message_notification_manager = MessageNotificationManager()

# 서로 다른 종류의 메시지 3개 생성
kakao_talk_message = KakaoTalkMessage("고대위", "2019년 7월 1일 오후 11시 30분", "나 오늘 놀러 못갈 거 같아, 미안!")
facebook_message = FacebookMessage("고대위", "서울시 성북구", "2019년 7월 1일 오후 11시 35분", "아니다, 갈게! 너네 어디서 놀고 있어?")
text_message = TextMessage("이영훈", "2019년 7월 2일 오전 12시 30분", "나도 놀러 갈게, 나 지금 출발")

# 메시지 알림 관리 인스턴스에 3개의 메시지를 추가
message_notification_manager.add_new_message(kakao_talk_message)
message_notification_manager.add_new_message(facebook_message)
message_notification_manager.add_new_message(text_message)

# 메시지 알림 관리 인스턴스에 있는 모든 메시지 출력
message_notification_manager.display_message_notifications()         
```

    새로 온 메시지들:
    2019년 7월 1일 오후 11시 30분
    고대위
    나 오늘 놀러 못갈...
    
    2019년 7월 1일 오후 11시 35분
    고대위
    서울시 성북구
    아니다, 갈게! 너네 어디서...
    
    이영훈, 2019년 7월 2일 오전 12시 30분
    나도 놀러 갈게, 나 ...
    
    

## <a id='toc1_4_'></a>[Liskov Substitution Principle](#toc0_)
---

부모 클래스 인스턴스를 사용할 위치에 자식 클래스 인스턴스를 사용해도 의도대로 동작해야 한다  
자식 클래스는 부모 클래스의 행동범위를 지켜줘야 한다

자식 클래스는 기본적으로 부모 클래스의 인스턴스이기도 하므로 치환이 가능하다  
그러나 치환이 불가능한 경우는 부모 클래스에서 정의한 내용을 어겼을 때인데  
1. 변수의 타입을 바꾸는 경우
2. 매소드 파라미터 타입이나 개수를 바꾸는 경우
3. 매소드 리턴 타입이나 개수를 바꾸는 경우  
등이 이에 해당한다  
또한 그 외에도 부모 클래스의 의도를 벗어나게 오버라이딩 하는 경우도 해당한다

만약 자식 클래스가 부모 클래스의 행동범위를 지킬 수 없다면  
상속을 해야 하는지 다시 고민해봐야 한다


```python
class Employee:
    """직원 클래스"""
    company_name = "코드잇 버거"
    raise_percentage = 1.03

    def __init__(self, name, wage):
        self.name = name
        self._wage = wage

    def raise_pay(self):
        """직원 시급을 인상하는 메소드"""
        self._wage *= self.raise_percentage

    @property
    def wage(self):
        return self._wage

    def __str__(self):
        """직원 정보를 문자열로 리턴하는 메소드"""
        return Employee.company_name + " 직원: " + self.name


class Cashier(Employee):
    """리스코프 치환 원칙을 지키지 않는 계산대 직원 클래스"""
    burger_price = 4000

    def __init__(self, name, wage, number_sold=0):
        super().__init__(name, wage)
        self.number_sold = number_sold

    def raise_pay(self, raise_amount):
        """직원 시급을 인상하는 메소드"""
        self.wage += self.raise_amount

    @property
    def wage(self):
        return "시급 정보를 알려줄 수 없습니다"

```

여기서 Cashier 클래스는 Employee 클래스를 상속 받으면서도 wage를 문자열로 반환하거나 raise_pay 매소드에 raise_amount 파라미터를 추가로 받는 등 헛짓거리를 해서 LSP를 어겼다

부모 클래스를 상속 하는 의미가 없어질 만큼 수정이 발생하면 부모 클래스를 상속 받은 걸로 생각하는 다른 사람이 작업할 때 에러가 발생하거나 코드 수정에 어려움을 겪게 된다

## <a id='toc1_5_'></a>[Interface Segregation Principle](#toc0_)
---

추상 클래스에서 추상 매소드만 있는 걸 인터페이스라고 할 수 있다

추상 매소드를 상속 받은 클래스는 추상 매소드를 반드시 구현해야 하는데  
자식 클래스에서는 쓰지도 않을 매소드를 추상 매소드로 만들어서 강제하지 말라는 거다

이럴 땐 인터페이스를 분리해서 추상 매소드를 적절히 나눠주면 된다  
이렇게 너무 많은 추상 매소드를 갖는 인터페이스를 분리하는 것을 interface segregation principle이라고 한다  
참고로 그렇게 많은 추상 매소드를 갖는 인터페이스를 fat interface라고 한다


```python
from abc import ABC, abstractmethod


class IMessage(ABC):
    @property
    @abstractmethod
    def content(self):
        """추상 getter 메소드"""
        pass

    @abstractmethod
    def edit_content(self, new_content: str) -> None:
        """작성한 메시지를 수정하는 메소드"""
        pass

    @abstractmethod
    def send(self, destination: str) -> bool:
        """작성한 메시지를 전송하는 메소드"""
        pass
```

만약 메세지를 보내지는 않고 저장만 하는 기능도 있다면


```python
class Itext(ABC):
    @property
    @abstractmethod
    def content(self):
        """추상 getter 메소드"""
        pass

    @abstractmethod
    def edit_content(self, new_content: str) -> None:
        """작성한 메시지를 수정하는 메소드"""
        pass
    
class Msend(ABC):
    @abstractmethod
    def send(self, destination: str) -> bool:
        """작성한 메시지를 전송하는 메소드"""
        pass
```

실습 예제


```python
from abc import ABC, abstractmethod

class IPrinter(ABC):
    @abstractmethod
    def print_file(self, file:str) -> bool:
        """문서 출력 메소드"""
        pass
    
class Iscanner(ABC):
    @abstractmethod
    def scan(self, content:str) -> bool:
        """문서 스캔 메소드"""
        pass
    
    
class SamsungPrinter(IPrinter, Iscanner):
    def __init__(self, has_ink, has_paper, is_connected):
        self.has_ink = has_ink
        self.has_paper = has_paper
        self.is_connected = is_connected

    def print_file(self, file):
        """문서 출력 메소드"""
        if self.has_ink and self.has_paper and self.is_connected:
            print("문서 {}을/를 출력 중입니다!".format(file))
            return True
        return False

    def scan(self, content):
        """문서 스캔 메소드"""
        if self.is_connected:
            print("{}을/를 이미지 파일로 저장합니다.".format(content))
            return True
        return False 
    
    
class LGPrinter(IPrinter):
    def __init__(self, has_ink, has_paper, is_connected):
        self.has_ink = has_ink
        self.has_paper = has_paper
        self.is_connected = is_connected

    def print_file(self, file):
        """문서 출력 메소드"""
        if self.has_ink and self.has_paper and self.is_connected:
            print("문서 {}을/를 출력합니다.".format(file))
            return True
        return False

    # def scan(self, content):
    #     """LG 프린터는 스캔 기능이 없기 때문에 False 리턴"""
    #     print("이 프린터는 문서를 스캔하는 기능이 없습니다.")
    #     return False 
    

samsung_printer = SamsungPrinter(True, True, True)
lg_printer = LGPrinter(True, True, True)

samsung_printer.print_file("4월 보고서.docx")
lg_printer.print_file("4월 보고서.docx")

samsung_printer.scan("스캔 테스트 문서")
# lg_printer.scan("스캔 테스트 문서")    

print(SamsungPrinter.mro())
print(LGPrinter.mro())
    
    
    
```

    문서 4월 보고서.docx을/를 출력 중입니다!
    문서 4월 보고서.docx을/를 출력합니다.
    스캔 테스트 문서을/를 이미지 파일로 저장합니다.
    [<class '__main__.SamsungPrinter'>, <class '__main__.IPrinter'>, <class '__main__.Iscanner'>, <class 'abc.ABC'>, <class 'object'>]
    [<class '__main__.LGPrinter'>, <class '__main__.IPrinter'>, <class 'abc.ABC'>, <class 'object'>]
    

## <a id='toc1_6_'></a>[Dependency Inversion Principle](#toc0_)
---

상위 모듈은 하위 모듈에 의존하면 안 된다  
상위 모듈과 하위 모듈 모두 추상화에 의존해야 한다  
it means that the high level module must not depend on the low level module, but they should depend on abstractions.

어떤 클래스에서 다른 클래스의 매소드를 직접 호출해와서 사용하면 나중에 그 매소드가 수정될 때 의존하는 클래스에서도 수정이 발생한다 이러면 번거롭다  
이런 번거로운 케이스를 만들지 말자는 거다  
그 해결책으로 추상화를 써서 레이어를 하나 깔아준다

의존관계 역전 원칙은 사실상 개방폐쇄 원칙과 대동소이하다


```python
from abc import ABC, abstractclassmethod

class Exporter(ABC):
    @abstractclassmethod
    def export(self, name, docu):
        pass

class Document:
    def __init__(self, name, content):
        self._name = name
        self._content = content

    @property
    def content(self):
        """문서의 내용을 리턴한다"""
        return self._content

    def __str__(self):
        """문서의 정보를 문자열로 리턴한다"""
        return "문서 이름: {}\n문서 내용:\n{}".format(self._name, self._content)


class CSVExporter(Exporter):
    """문서를 csv 형식으로 변환하는 클래스"""
    def export(self, new_name, document):
        """문서를 변환한 후 주어진 이름으로 리턴한다"""
        print("\nCSV 파일로 변환 중~")

        new_content = document.content.replace("|", ",")
        exported_document = Document(new_name, new_content)

        print("변환 완료!\n")

        return exported_document


class HTMLExporter(Exporter):
    """문서를 HTML 형식으로 변환하는 클래스"""
    def export(self, new_name, document):
        """문서를 변환한 후 주어진 이름으로 리턴한다"""
        print("\nHTML 문서 변환 중~")

        new_content = """
<!DOCTYPE html>
<html>
<head>
<title>Title of the document</title>
</head>

<body>
{}
</body>

</html>
        """.format(document.content)
        exported_document = Document(new_name, new_content)

        print("변환 완료!\n")

        return exported_document

    
class ExportController:
    """문서를 특정 파일 형식으로 변환하는 클래스"""
    def __init__(self):
        self.exporter = None

    def set_exporter(self, exporter: Exporter):
        """변환하고 싶은 파일 타입에 맞는 변환기를 설정한다"""
        self.exporter = exporter

    def run_export(self, new_name, document):
        """파일을 변환해서 리턴한다"""
        if self.exporter == None:
            print("변환기를 정해주세요")
            return document

        return self.exporter.export(new_name, document)


# 변환기 컨트롤러 인스턴스 정의
export_handler = ExportController()

# csv 변환기 인스턴스, html 변환기 인스턴스 정의
csv_exporter = CSVExporter()
html_exporter = HTMLExporter()

# 변환할 문서 인스턴스 정의
document = Document(
        "직원정보.txt",
        """
이름|이메일
강영훈|younghoon@codeit.kr
이윤수|yoonsoo@codeit.kr
손동욱|dongwook@codeit.kr"""
        )

# 기존 문서 출력
print(document)

# 변환기를 csv 변환기로 설정
export_handler.set_exporter(csv_exporter)

# 주어진 문서를 csv 문서로 변환
exported_document = export_handler.run_export("직원정보.csv", document)
# 변환된 문서 출력
print(exported_document)

export_handler.set_exporter(html_exporter)
exported_document = export_handler.run_export("직원정보.html", document)
print(exported_document)

print(CSVExporter.mro())
print(HTMLExporter.mro())
```

    문서 이름: 직원정보.txt
    문서 내용:
    
    이름|이메일
    강영훈|younghoon@codeit.kr
    이윤수|yoonsoo@codeit.kr
    손동욱|dongwook@codeit.kr
    
    CSV 파일로 변환 중~
    변환 완료!
    
    문서 이름: 직원정보.csv
    문서 내용:
    
    이름,이메일
    강영훈,younghoon@codeit.kr
    이윤수,yoonsoo@codeit.kr
    손동욱,dongwook@codeit.kr
    
    HTML 문서 변환 중~
    변환 완료!
    
    문서 이름: 직원정보.html
    문서 내용:
    
    <!DOCTYPE html>
    <html>
    <head>
    <title>Title of the document</title>
    </head>
    
    <body>
    
    이름|이메일
    강영훈|younghoon@codeit.kr
    이윤수|yoonsoo@codeit.kr
    손동욱|dongwook@codeit.kr
    </body>
    
    </html>
            
    [<class '__main__.CSVExporter'>, <class '__main__.Exporter'>, <class 'abc.ABC'>, <class 'object'>]
    [<class '__main__.HTMLExporter'>, <class '__main__.Exporter'>, <class 'abc.ABC'>, <class 'object'>]
    

## <a id='toc1_7_'></a>[수료증](https://www.codeit.kr/certificates/3Wz2v-j589m-eXxm6-bUlos) [&#8593;](#toc0_)
