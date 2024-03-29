# 📝 26 Python(파이썬)의 타입 시스템
## 1. 파이썬 타입 시스템은?
* 정적타입 언어 : 자료형을 컴파일 타임에 결정하는 언어
* 동적타입 언어 : 자료형을 런타임(실행 시점)에 결정하는 언어
* 약타입 언어 : 자료형이 맞지 않을 시에 암묵적으로 타입을 변환하는 언어
* 강타입 언어 : 자료형이 맞지 않을 시에 에러 발생, 암묵적 변환을 지원하지 않음

파이썬은 동적타입이면서, 강타입 언어 입니다.

<br/><br/><br/>
## 2. 타입 시스템 확인
* 동적타입을 확인해봅니다.
* 런타임에 자료형을 결정해 + 방식을 변경합니다.
```python
>>> def add(a,b):
...     return a + b
... 
>>> add(5,10)
15
>>> add(3.3, 5.9)
9.2
>>> add("인천","공항")
'인천공항'
>>> add([1,3,5],[7,9])
[1, 3, 5, 7, 9]
```
<br/>

* 강타입 언어를 확인해봅니다.
* 약타입 언어인 자바스크립트에서는 "1"+1 = "11" 입니다.
* 파이썬은 형이 맞지 않기때문에 에러가 발생합니다.
```python
>>> add("1",1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in add
TypeError: must be str, not int

<br/><br/><br/>
> 참고 : [wikidocs(파이썬 - 기본을 갈고 닦자!)](https://wikidocs.net/16054)
