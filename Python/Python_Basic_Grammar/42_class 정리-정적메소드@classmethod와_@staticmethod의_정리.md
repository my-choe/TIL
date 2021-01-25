# 📝 42 class 정리 - 정적메소드 @classmethod와 @staticmethod의 정리
## 1. 정적메소드(@classmethod와 @staticmethod)
* 정적메소드라 함은 클래스에서 직접 접근할 수 있는 메소드입니다.
* 파이썬에서는 클래스에서 직접 접근할 수 있는 메소드가 두가지가 있습니다.staticmethod와 classmethod 입니다.
* **하지만 파이썬에서는 다른언어와는 다르게 정적메소드임에도 불구하고 인스턴스에서도 접근이 가능합니다. 이 차이에 유의해야합니다.**
* 에디터에서 `static_method.py`파일을 작성합니다.
* 인스턴스 메소드는 첫번째 인자로 객체 자신 `self`자신을 입력합니다.
* classmethod는 첫번째 인자로 클래스를 입력합니다.
* staticmethod는 특별히 추가되는 인자가 없습니다.
```python
class CustomClass:

    # instance method
    def add_instance_method(self, a,b):
        return a + b

    # classmethod
    @classmethod
    def add_class_method(cls, a, b):
        return a + b

    # staticmethod
    @staticmethod
    def add_static_method(a, b):
        return a + b
```
<br/>

* REPL을 통해 접근해봅니다.
* 먼저 인스턴스 메소드를 클래스에서 바로 접근해봅니다.
* 일반적으로 인스턴스 메소드안에서 인스턴스 변수를 접근할경우 아래처럼 사용하면 안되고, 첫번째 인자에 객체를 할당해야합니다.
```python
>>> from static_method import CustomClass
>>> CustomClass.add_instance_method(None, 3, 5)
8
```
<br/>

* classmethod를 접근해봅니다.
* 첫번째 인자가 클래스지만 생략하고 접근해야합니다.
```python
>>> CustomClass.add_class_method(CustomClass, 3, 5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: add_class_method() takes 3 positional arguments but 4 were given
>>> CustomClass.add_class_method(3, 5)
8
```
<br/>

* staticmethod를 접근해봅니다.
```python
>>> CustomClass.add_static_method(3, 5)
8  
```
<br/>

* **classmethod도 staticmethod도 객체에서 접근이 됩니다.유의해야합니다.**
```python
>>> a = CustomClass()
>>> a.add_class_method(3, 5)
8
>>> a.add_static_method(3, 5)
8
```
<br/><br/>

## 2. @classmethod와 @staticmethod 의 차이
* classmethod와 static메소드의 차이는 상속에서 두드러지게 차이가 납니다.
*  만들어봅니다. `language.py`를 작성합니다.
```python
class Language:
    default_language = "English"

    def __init__(self):
        self.show = '나의 언어는' + self.default_language

    @classmethod
    def class_my_language(cls):
        return cls()

    @staticmethod
    def static_my_language():
        return Language()

    def print_language(self):
        print(self.show)


class KoreanLanguage(Language):
    default_language = "한국어"
```
<br/>

* REPL에서 결과값을 확인합니다.
* staticmethod에서는 부모클래스의 클래스속성 값을 가져오지만, classmethod에서는 cls인자를 활용하여 cls의 클래스속성을 가져오는 것을 알 수 있습니다.
```python
>>> from language import *
>>> a = KoreanLanguage.static_my_language()
>>> b = KoreanLanguage.class_my_language()
>>> a.print_language()
나의 언어는English
>>> b.print_language()
나의 언어는한국어
```



<br/><br/><br/>
> 참고 : [wikidocs(파이썬 - 기본을 갈고 닦자!)](https://wikidocs.net/16074)
