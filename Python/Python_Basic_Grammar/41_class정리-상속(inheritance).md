# 📝 41 class 정리 - 상속(inheritance)
## 1. 상속(inheritance) 이란?
* 클래스에서 상속이란, 물려주는 클래스(Parent Class, Super class)의 내용(속성과 메소드)을 물려받는 클래스(Child class, sub class)가 가지게 되는 것입니다.
* 예를 들면 국가라는 클래스가 있고, 그것을 상속받은 한국, 일본, 중국, 미국 등의 클래스를 만들 수 있으며, 국가라는 클래스의 기본적인 속성으로 인구라는 속성을 만들었다면, 상속 받은 한국, 일본, 중국 등등의 클래스에서 부모 클래스의 속성과 메소드를 사용할 수 있음을 말합니다.
* 기본적인 사용방법은 아래와 같습니다.
* 자식클래스를 선언할때 소괄호로 부모클래스를 포함시킵니다.
* 그러면 자식클래스에서는 부모클래스의 속성과 메소드는 기재하지 않아도 포함이 됩니다.
```python
class 부모클래스:
    ...내용...

class 자식클래스(부모클래스):
    ...내용...
```
<br/><br/>

## 2. 상속 사용해보기
* 상속을 표현해보기위헤 에디터에서 `inheritance.py` 파일을 하나 만듭니다.
* 아래와 같이 코드를 작성해봅니다.
```python
class Country:
    """Super Class"""

    name = '국가명'
    population = '인구'
    capital = '수도'

    def show(self):
        print('국가 클래스의 메소드입니다.')


class Korea(Country):
    """Sub Class"""

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print('국가 이름은 : ', self.name)
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

* REPL에서 한번 실행해보겠습니다.
* 상속받은 서브 클래스에서는 상속해준 슈퍼 클래스의 속성과 메소드를 모두 사용할 수 있음을 확인할 수 있습니다.
```python
>>> from inheritance import *
>>> a = Korea('대한민국')
>>> a.show()
국가 클래스의 메소드입니다.
>>> a.show_name()
국가 이름은 :  대한민국
>>> a.capital
'수도'
>>> a.name
'대한민국'
```
<br/><br/>


## 3. 메소드 오버라이딩 (Method overriding)
### 3-1 일반적인 메소드 오버라이딩
* 메소드 오버라이딩은 부모 클래스의 메소드를 자식 클래스에서 재정의 하는 것입니다.
* 코드로 한번 보겠습니다. Korea 클래스에서 부모의 show 메소드를 재정의 합니다.
```python
class Korea(Country):
    """Sub Class"""

    def __init__(self, name,population, capital):
        self.name = name
        self.population = population
        self.capital = capital

    def show(self):
        print(
            """
            국가의 이름은 {} 입니다.
            국가의 인구는 {} 입니다.
            국가의 수도는 {} 입니다.
            """.format(self.name, self.population, self.capital)
        )
    ... 생략
```
<br/>

* 결과를 보겠습니다.
* 부모 클래스의 `show()`메소드는 무시되고 자식클래스의 `show()`메소드가 수행됩니다.
```python
>>> from inheritance import *
>>> a = Korea('대한민국', 50000000, '서울')
>>> a.show()

            국가의 이름은 대한민국 입니다.
            국가의 인구는 50000000 입니다.
            국가의 수도는 서울 입니다.

>>> 
```
<br/>

### 3-2 부모 메소드 호출하기
* 부모클래스의 메소드도 수행하고, 자식클래스의 메소드의 내용도 함께 출력하기를 원할 수 있습니다.
* 그럴때는 `super()` 라는 키워드를 사용하면 자식클래스 내에서 코드에서도 부모클래스를 호출할 수 있습니다.
```python
 class Korea(Country):

    ... 생략

    def show(self):
        super().show()
        print(
            """
            국가의 이름은 {} 입니다.
            국가의 인구는 {} 입니다.
            국가의 수도는 {} 입니다.
            """.format(self.name, self.population, self.capital)
        )

    ... 생략
```
<br/><br/>
 
* 결과를 확인해봅니다.
* 부모클래스의 'show()' 또한 실행이 되었음을 확인할 수 있습니다.
```python
>>> from inheritance import *
>>> a = Korea('대한민국', 50000000, '서울')
>>> a.show()
국가 클래스의 메소드입니다.

            국가의 이름은 대한민국 입니다.
            국가의 인구는 50000000 입니다.
            국가의 수도는 서울 입니다.

>>> 
```
<br/><br/>


## 4. 다중상속
* C# 또는 Java는 다중상속이 불가능한 언어입니다.
* 파이썬은 C++과 같이 다중상속이 가능합니다.
* 작성 형식은 아래와 같습니다.
```python
    class 부모클래스1:
        ...내용...

    class 부모클래스2:
        ...내용...

    class 자식클래스(부모클래스1, 부모클래스2):
        ...내용...
```
<br/>

* 예제 코드 입니다.
* 아래와 같이 2개의 클래스를 상속하였습니다. 상속 개수에는 제한이 없습니다.
```python
class Country:
    """Super Class"""
...생략


class Province:
    Province_list = []


class Korea(Country,Province ):
    """Sub Class"""
... 생략
```
<br/><br/>


## 기타. mro() 메소드
* `mro()` - 클래스를 작성하면 상속 관계를 확인할 수 있는 메소드
* Korea클래스에 `mro()` 메소드를 실행하면 Korea클래스 다음 Country 다음 object가 나옵니다.
* 모든 클래스는 object클래스의 상속입니다. 기본적으로 파이썬 3부터 object가 생략되어 코드가 작성됩니다.
```python
>>> Korea.mro()
[<class 'inheritance.Korea'>, <class 'inheritance.Country'>, <class 'object'>]
```



<br/><br/><br/>
> 참고 : [wikidocs(파이썬 - 기본을 갈고 닦자!)](https://wikidocs.net/16073)
