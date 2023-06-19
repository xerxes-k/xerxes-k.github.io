---
layout: single
title:  "다형성 polymorphism"
---

# 다형성 polymorphism

하나의 변수가 여러 타입, 인스턴스를 가리킬 수 있는 것  

여러 클래스의 안에 같은 이름으로 매소드를 정의한다  
그리고 각각의 인스턴스를 생성한 다음 동일하게 이름 지은 매소드를 호출하면 인스턴스 마다 다른 동작을 하게 된다  
이 때 매소드의 이름은 같은데 다른 동작을 가리키는 게 다형성 덕분이다

다형성을 이용하면 같은 이름으로 다른 동작을 하는 매소드들을 한번에 통제할 수 있다  
예를 들어 부모 클래스를 만들고 거기에 매소드 이름을 먼저 정의한 뒤  
개별 클래스 마다 이름만 상속 받고 동작을 오버라이드 해놓으면  
실제 동작을 실행시킬 클래스, 함수에서 부모 클래스의 인스턴스인지 여부 isinstance()를 통해  
동작 여부를 통제할 수 있다

그러나 자식 클래스에서 오버라이드를 안 하면 오류가 난다  
자식 클래스에서 매소드를 오버라이드 하도록 강제하려면

## 추상 클래스
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
자식 클래스에서 오버라이드 할 때 super().메소드명()으로 불러오면  
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



---

일반 클래스에서 다중 상속은 주의해야 하나, 추상 클래스는 흔히 다중 상속을 사용한다  
추상 매소드는 어차피 오버라이드 해야 하므로 추상 매소드가 겹치는 건 문제가 되지 않는다  
다만 추상 클래스라 할지라도 일반 매소드가 겹치면 마찬가지로 mro에 따라 매소가 실행되므로 주의해야 한다

---

### 클래스 뿐만 아니라 함수, 매소드도 다형성을 가진다

함수에 옵셔널 파라미터를 정의하면 같은 함수가 여러 동작을 할 수 있다  

옵셔널 파라미터는 함수 정의에서 기본값을 정해주는 파라미터를 말하며 일반 파라미터를 정의한 후에 정의해줘야 한다  
```python
def 함수(파라미터1, 파라미터2=기본값):
```

---

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
    
    

---

지금까지 예제는 LBYL Look Before You Leap 방식으로 작성됐다  
즉, 실행 전에 미리 조건을 확인하고 실행하는 방식으로 예제에서는 if와 isinstance()를 이용해 추상 클래스를 상속 받은 클래스의 객체인지를 확인하고 실행하도록 하였다

이와 달리 EAFP Easier to Ask for Forgiveness than Permission 방식은 실행 후에 예외를 처리하는 방식이다

EAFP는 try except 구문을 사용한다
