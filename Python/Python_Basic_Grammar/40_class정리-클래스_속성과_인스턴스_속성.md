# 📝 40 class 정리 - 클래스 속성과 인스턴스 속성
## 1. 클래스 속성과 인스턴스 속성의 차이
* 앞서 포스팅 [39. class 정리](https://github.com/my-choe/TIL/blob/main/Python/Python_Basic_Grammar/39_class%EC%A0%95%EB%A6%AC-%ED%81%B4%EB%9E%98%EC%8A%A4_%EA%B8%B0%EB%B3%B8%EC%A0%81%EC%9D%B8_%EC%82%AC%EC%9A%A9.md)에서 다루었던 초기화자(`__init__`)에서 `self.속성'에 할당 했던 변수들은 모두 인스턴스 속성에 해당합니다.
* 클래스 속성은 아래와 같이 `self.속성`에 할당하는 것이 아니라 class안에서 바로 할당합니다.
```python
class CustomClass:
    속성명 = 값

    def custom_method():
        pass
    ...
```
<br/><br/>

## 2. 클래스 속성
* 클래스 속성에 접근하는 메소드를 작성해보겠습니다.
* 에디터에서 작성합니다.
```python
class Flight:
    class_attr = []

    def add_class_attr(self, number):
        Flight.class_attr.append(number)
```
* REPL에서 확인해봅니다.
* 객체를 2개를 만들고, 클래스 속성에 값을 추가하는 인스턴스 메소드를 사용합니다.
* 클래스 속성에서의 직접접근 `클래스명.클래스속성`, 객체에서의 `객체변수명.클래스속성` 모두 똑같이 값을 공유합니다.
```python
>>> from airtravel import Flight
>>> f = Flight()
>>> g = Flight()
>>> f.add_class_attr(5)
>>> Flight.class_attr
[5]
>>> f.class_attr
[5]
>>> g.class_attr
[5]
>>> g.add_class_attr(7)
>>> Flight.class_attr
[5, 7]
>>> g.class_attr
[5, 7]
>>> f.class_attr
[5, 7]
```
<br/>

* 똑같은 클래스 속성과 인스턴스 속성을 선언하고 값이 어떻게 변하는지 살펴보겠습니다.
* 초기화자(`__init__`)와 메소드를 하나 추가합니다.
```python
class Flight:
    class_attr = []

    def __init__(self):
        self.class_attr = []

    def add_instance_attr(self, number):
        self.class_attr.append(number)

    def add_class_attr(self, number):
        Flight.class_attr.append(number)
```
<br/>

* REPL에서 결과값을 확인합니다.
* 인스턴스와 클래스 에 모두 같은 속성이 있으면 아래와 같이 인스턴스 속성을 먼저 찾는 것을 알 수 있습니다.
* 속성과 메소드 이름 찾는 순은 인스턴스, 클래스 순입니다.
```python
>>> from airtravel import Flight
>>> f = Flight()
>>> g = Flight()
>>> f.add_instance_attr(5)
>>> Flight.class_attr
[]
>>> f.class_attr
[5]
>>> g.class_attr
[]
```
* **클래스 속성은 여러 객체가 공유한다는 것을 유의해야합니다.**

<br/><br/>
## 3. 비공개 클래스 속성
* 비공개 클래스 속성은 인스턴스의 비공개 속성과 동일합니다. 언더바 두개(`__`)로 속성명이 시작하면 비공개 속성이됩니다.
* 코드로 확인해봅니다. 아래와 같이 `__private_attr = 5` 코드를 추가합니다.
```python
class Flight:
    __private_attr = 5
    ...생략
```
<br/>

* REPL에서 확인해보겠습니다.
```python
>>> from airtravel import Flight
>>> Flight.__private_attr
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: type object 'Flight' has no attribute '__private_attr'
```



<br/><br/><br/>
> 참고 : [wikidocs(파이썬 - 기본을 갈고 닦자!)](https://wikidocs.net/16072)
