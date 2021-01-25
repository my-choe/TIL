# 📝 39 class 정리 - 클래스 기본적인 사용
## 1. 클래스 개요
* 클래스는 객체의 구조와 행동을 정의합니다.
* 객체의 클래스는 초기화를 통해 제어합니다.
* 클래스는 복잡한 문제를 다루기 쉽도록 만듭니다.
<br/><br/>

## 2. 클래스 정의
* 클래스를 작성하기 위해서는 **class** 키워드 사용하여 새로운 클래스를 작성합니다.
* Python의 대부분 네이밍컨벤션이 단어와 단어사이에 `_` 를 넣는 다면 **클래스의 네이밍컨벤션은 CamelCase**를 사용합니다.
```python
class CustomClass:
    def __init__(self, param):
        .......
```
<br/>

### 2-1 클래스 생성 연습
* 연습은 에디터를 통해서 이루어집니다. 에디터에서 `airtravel.py` 파일을 생성합니다.
* 클래스 생성은 아래와 같이 `class` 키워드 및 클래스의 이름을 입력하여 생성.
```python
class Flight:
    pass
```
<br/>

* 생성한 클래스는 REPL에서 아래와 같이 import할 수 있습니다.
```python
>>> from airtravel import Flight
>>> Flight
<class 'airtravel.Flight'>
```
<br/>

* 클래스 객체 생성 및 변수에 할당
```python
# 새로운 객체를 생성하기, java나 C# 등의 다른 언어와 다르게 new 키워드가 없다.
>>> f = Flight()
>>> type(f)
<class 'airtravel.Flight'>
```
<br/>

* 클래스 메소드 작성
* 메소드란 클래스 내의 함수
```python
# 메소드 작성하기
class Flight:
    def number(self):
        return 'SN060'
```
<br/>

* 인스턴스 메소드의 접근
* 인스턴스 메소드란 객체에서 호출되어질수 있는 함수
```python
# 인스턴스의 메소드 사용
>>> from airtravel import Flight
>>> f = Flight()
>>> f.number()
'SN060'
```
<br/>

* 파이썬 메서드의 첫번째 파라미터명은 관례적으로 self라는 이름을 사용합니다.
* 호출 시 호출한 객체 자신이 전달되기 때문에 self라는 이름을 사용하게 된 것
* 이를 이용하여 클래스에서 바로 메소드로 접근하면서 위에서 할당한 Flight의 객체 f를 파라미터로 전달함으로써 똑같은 결과값 얻습니다.
```python
# 클래스의 내부에 self 파라미터가 포함되는데 이를 이용한 접근법
>>> Flight.number(f) # f는 Flight객체
'SN060'
```
<br/>

### 2-2 생성자와 초기화자
* 위 예제에서 연습했듯 파이썬에서 객체를 생성할때 아래와 같이 생성자를 사용합니다.
```python
f = Flight() # 생성자(constructor)
```
<br/>

* 생성자로 객체생성을 호출받으면 먼저 `__new__` 를 호출하여 객체를 생성할당하고, `__new__` 메소드가 `__init__`메소드를 호출하여 객체에서 사용할 초기값들을 초기화하게됩니다.
* 간혹 여러 자료들을 보면.. `__init__` 메소드를 생성자로 소개하는 경우가 있는데, 그렇지 않습니다.
* 자료 https://stackoverflow.com/questions/6578487/init-as-a-constructor
* 일반적으로 파이썬에서 클래스를 만들 시 `__init__` 메소드만 오버라이딩하여 객체초기화에만 이용합니다.
* 2-1 예제를 조금 수정해보겠습니다.
```python
class Flight:

    def __init__(self):
        print('init')
        super().__init__()

    def __new__(cls):
        print('new')
        return super().__new__(cls)

    def number(self):
        return 'SN060'
```
<br/>

* 다시 REPL에서 객체를 생성해보겠습니다.
* 먼저 `__new__`가 클래스 자체를 받으며 할당하게되고, `__init__`가 self를 받으며 객체의 내부에서 사용할 속성을 초기화 합니다.
```python
>>> from airtravel import Flight
>>> f = Flight()
new
init
```
<br/>

* 객체의 속성을 초기화 해봅니다. `Flight`클래스를 수정해봅니다. `__new__` 메소드는 자동으로 실행되므로 제거합니다.
* `__init__` 메소드에 코드를 수정합니다.
* 아래의 코드에서 `self._number` 로 할당했는데 변수명의 `_` 의 의미는 다음과 같습니다.
* 내부적으로 사용되는 변수
* 파이썬기본 키워드와 충돌을 피하기 위한 변수
* `_` 관련 네이밍컨벤션에 관련한 자료
      * https://spoqa.github.io/2012/08/03/about-python-coding-convention.html
      * https://www.python.org/dev/peps/pep-0008/#naming-conventions
```python
class Flight:
    def __init__(self, number):
        self._number = number

    def number(self):
        return self._number
```
<br/>

* 다시 REPL에서 확인 합니다.
```python
 >>> from airtravel import Flight
 >>> f = Flight(5)
 >>> f.number()
 5
 >>> f._number
 5
```
* Python은 기본적으로 다른언어에 있는 접근제어자(public, private, protected)가 없음
* 기본적으로 모두 Public
<br/>

### 2-3 초기화자(`__init__`)에 객체의 불변성을 확립하자(유효성검증을 수행)
* 일반적으로 초기화자(`__init__`) 에서 객체의 불변성을 확립하는 것이 좋습니다.
* 객체 생성시 들어올 값에 대해서 `__init__`에서 Validation을 수행합니다.
* 비행기 번호는 앞에 두글자는 영문이어야하며 대문자입니다. 그리고 뒤에 세번째 글자부터 마지막까지는 양의 정수여야합니다.
* Flight클래스를 다음과 같이 변경해봅니다.
* 객체를 생성시 규칙에 맞지 않는 값이 들어오면 ValueError를 발생시킵니다.
```python
class Flight:

    def __init__(self, number):
        if not number[:2].isalpha():
            raise ValueError("첫 두글자가 알파벳이 아닙니다.")
        if not number[:2].isupper():
            raise ValueError("첫 두글자가 대문자가 아닙니다.")
        if not number[2:].isdigit():
            raise ValueError("세번째 글자 이상이 양의 숫자가 아닙니다.")
        self._number = number

    ...생략
```
```python
>>> from airtravel import Flight
>>> f= Flight("abc")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/Blidkaga/Documents/CodeLab/Python_Basic/airtravel.py", line 11, in __init__
    raise ValueError("첫 두글자가 대문자가 아닙니다.")
ValueError: 첫 두글자가 대문자가 아닙니다.
>>> f= Flight("AB0")
>>> f= Flight("AB001")
```
<br/>

### 2-4 비공개 속성
* 위의 예처럼 `_` 언더바 한개는 내부적으로만 사용되는 변수다라고 알리지만, 사실 값을 얻어올수도 있고 할당도 가능합니다. 사람들이 코딩컨벤션으로 파이썬을 쓰는 사람들이면 내부적인 변수구나 하고 알고 있을 뿐..
```python
>>> f= Flight("AB001")
>>> f._number
'AB001'
>>> f._number = 'abc'
>>> f.number()
'abc'
```
<br/>

* 원천적인 접근을 막으려면 `__` 더블 언더바를 사용하면 막을 수 있습니다.
* 코드를 다시 변경해보겠습니다. `_name` 변수를 `__name`으로 변경하였습니다.
```python
class Flight:

    def __init__(self, number):
        if not number[:2].isalpha():
            raise ValueError("첫 두글자가 알파벳이 아닙니다.")
        if not number[:2].isupper():
            raise ValueError("첫 두글자가 대문자가 아닙니다.")
        if not number[2:].isdigit():
            raise ValueError("세번째 글자 이상이 양의 숫자가 아닙니다.")
        self.__number = number

    def number(self):
        return self.__number
```
<br/>

* 결과를 확인해봅니다.
* `number()`인스턴스 메소드를 통해서 내부에서는 접근 가능한 모습을 보이나, 객체 `f`의 속성으로 접근 시 에러가 발생합니다.
```python
>>> from airtravel import Flight
>>> f= Flight("AB001")
>>> f.number() 
'AB001'
>>> f.__number
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Flight' object has no attribute '__number'
```

<br/><br/>
## 3. 주의! 파이썬은 메소드 오버로딩이 없다.
* 메소드 오버로딩이란? : 하나의 클래스 내부에서 메소드 명칭은 똑같고, 인자를 다르게하는 형태를 허용합니다.
* Java코드는 아래와 같은 코드를 허용합니다.
```python
class Adder{  
    static int add(int a,int b)
    {
        return a+b;
    }  
    static int add(int a,int b,int c)
    {
        return a+b+c;
    }  
}  
```
<br/>

* **파이썬은 메소드 오버로딩이 없습니다.**
* 아래와 같은 코드가 있다면 첫번째 show는 무시되고, 두번째 show만 유지됩니다.
```python
class Korea:

    def __init__(self, name,population, captial):
        self.name = name
        self.population = population
        self.capital = captial

    def show(self):
        print(
            """
            국가의 이름은 {} 입니다.
            국가의 인구는 {} 입니다.
            국가의 수도는 {} 입니다.
            """.format(self.name, self.population, self.capital)
        )

    def show(self, abc):
        print('abc :', abc)
```
<br/>

* 결과
```python
>>> from inheritance import *
>>> a = Korea('대한민국',50000000, '서울')
>>> a.show()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: show() missing 1 required positional argument: 'abc'
```



<br/><br/><br/>
> 참고 : [wikidocs(파이썬 - 기본을 갈고 닦자!)](https://wikidocs.net/16071)
