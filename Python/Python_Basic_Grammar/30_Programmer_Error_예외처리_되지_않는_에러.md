# 📝 30 Programmer Error - 예외처리 되지 않는 에러

## 1. 예외처리 되지 않는 에러
* [29  Exception(예외) 흐름과 Exception Handling](https://github.com/my-choe/TIL/blob/main/Python/Python_Basic_Grammar/29_Exception(%EC%98%88%EC%99%B8)%ED%9D%90%EB%A6%84%EA%B3%BC_Exception_Handling.md) `exceptional.py` 파일을 그대로 이용하겠습니다.

### 1-1. IndentationError
* IndentationError : 파이썬 들여쓰기 규칙이 잘못되었을 때 나타나는 오류
* 의도적으로 a = int(s) 부분의 들여쓰기를 한 더 수행하였습니다.
```python
def convert(s):
    """int로 변환"""
    try:
            a = int(s)
        print('성공')
    except (ValueError, TypeError, IndentationError):
        print('실패')
        a = -1
    return a
```
<br/>

* REPL에서 결과값 확인해봅니다.
* import과정에서 에러가 발생하며, except블록에 캐치되지 않습니다.
```python
>>> from exceptional import convert
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/Blidkaga/Documents/CodeLab/Python_Basic/exceptional.py", line 8
    print('성공')
               ^
IndentationError: unindent does not match any outer indentation level
```
<br/>

* 간혹 except 블록에 아무런 동작을 안하기를 원할 수 있습니다.
```python
def convert(s):
    """int로 변환"""
    try:
        a = int(s)
        print('성공')
    except (ValueError, TypeError, IndentationError):
    return a
```
<br/>

* REPL에서 결과 값을 확인해봅니다.
* 동일한 IndentationError가 발생합니다.
```python
>>> from exceptional import convert
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/Blidkaga/Documents/CodeLab/Python_Basic/exceptional.py", line 10
    return a
         ^
IndentationError: expected an indented block
```
<br/>

* 특정 블록에 아무코드를 입력하고 싶지 않을 때는 pass 라는 키워드를 사용합니다.
```python
def convert(s):
    """int로 변환"""
    try:
        a = int(s)
        print('성공')
    except (ValueError, TypeError, IndentationError):
        pass
    return a
```
<br/><br/>

### 1-2. SyntaxError
* SyntaxError : 구문 오류, 잘못된 기호를 입력하였을때 발생합니다.
* 의도적으로 작은 따옴표, 큰따옴표를 함께 혼용하였습니다.
```python
ef convert(s):
    """int로 변환"""
    try:
        a = int(s)
        print('성공")
    except (ValueError, TypeError, SyntaxError):
        print('실패')
        a = -1
    return a
```
<br/>

* REPL에서 결과값을 확인해봅니다.
* 역시나 import 단계에서 에러가 발생합니다.
```python
>>> from exceptional import convert
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/Blidkaga/Documents/CodeLab/Python_Basic/exceptional.py", line 8
    print('성공")
               ^
SyntaxError: EOL while scanning string literal
```


<br/><br/><br/>
> 참고 : [wikidocs(파이썬 - 기본을 갈고 닦자!)](https://wikidocs.net/16061)
