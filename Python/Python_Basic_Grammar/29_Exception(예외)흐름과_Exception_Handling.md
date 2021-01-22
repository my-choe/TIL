# 📝 29 Exception(예외) 흐름과 Exception Handling

## 1. Exception Handling(예외 처리)란
* Exception 이란? : 정상적인 프로그램 흐름을 중단시키는 에러를 말합니다.
* Exception Handling이란? : 정상적인 프로그램 흐름을 중단하고 주변의 컨텍스트 또는 코드 블록에서 계속하기위한 메커니즘


<br/><br/><br/>
## 2. Exception 발생 확인
* 임의로 Exception이 발생되는 것을 확인하겠습니다.
* 해당 코드를 계속 수정하면서 진행할 것이기에 REPL이 아닌 에디터를 사용합니다.
* 에디터에서 특정위치에 exceptional.py 를 만든 후 아래의 코드를 입력합니다.
```python
"""Exception을 설명하는 모듈"""


def convert(s):
    """int로 변환"""
    a = int(s)
    return a
```
<br/>

* 코드 작성 후 REPL을 사용합니다.
* "55"는 잘 변환 되지만, "test"는 ValueError이 발생하였습니다.
* 예외는 호출스택 안에서 상위 수준으로 전파 됩니다.
* int() 예외 발생 -> convert 내부 -> Module -> REPL
```python
>>> from exceptional import convert
>>> convert("55")
55
>>> convert("test")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/Blidkaga/Documents/CodeLab/Python_Basic/exceptional.py", line 6, in convert
    a = int(s)
ValueError: invalid literal for int() with base 10: 'test'
```


<br/><br/><br/>
## 3. Exception Handling(예외 처리)
### 3-1. except 블록
* 위 `exceptional.py`를 예외 처리 해보겠습니다.
* 아래와 같이 코드를 수정합니다
```python
# Exception을 설명하는 모듈

def convert(s):
    """int로 변환"""
    try:
        a = int(s)
    except ValueError:
        a = -1
    return a
```
<br/>

* REPL을 재실행한 후 다시 테스트를 해봅니다.
* Value Error가 발생하여 -1이 출력이 되었습니다. 코드가 중단되지 않았습니다.
```python
>>> from exceptional import convert
>>> convert("test")
-1
```
<br/>

* 다시 코드를 수정합니다.
```python
def convert(s):
    """int로 변환"""
    try:
        a = int(s)
        print('성공')
    except ValueError:
        print('실패')
        a = -1
    return a
```
<br/>

* 다시 REPL을 실행하여 테스트 해봅니다.
* try 마지막 라인 `print('성공')` 은 실행되지 않았습니다.
* 에러가 발생하면 그 다음 코드는 건너뛰고 except 블록이 실행됩니다.
```python
>>> from exceptional import convert
>>> convert("test")
실패
-1
```
<br/>

* 이번에는 `[1,2,3]` 을 convert함수 파라미터로 입력해보겠습니다.
* 이번에는 TypeError이 발생하였습니다.
* 위쪽 코드에서 ValueError만 except블록에서 처리했기때문입니다.
```python
>>> from exceptional import convert
>>> convert("test")
-1
```
<br/>

* TypeError도 처리하겠습니다.
* except 블럭을 하나 더 추가하였습니다.
```python
def convert(s):
    """int로 변환"""
    try:
        a = int(s)
        print('성공')
    except ValueError:
        print('실패 : ValueError')
        a = -1
    except TypeError:
        print('실패 : TypeError')
        a = -1
    return a
```
<br/>

* REPL 재실행 후 다시 테스트 합니다.
* 실패 메세지가 나왔지만, 프로그램이 에러에 의해 중단되지는 않았습니다.
```python
>>> from exceptional import convert
>>> convert([1, 2, 3])
실패 : TypeError
-1
```
<br/>

* except 블럭을 하나로 합치겠습니다.
```python
"""Exception을 설명하는 모듈"""


def convert(s):
    """int로 변환"""
    try:
        a = int(s)
        print('성공')
    except (ValueError, TypeError):
        print('실패')
        a = -1
    return a
```
<br/>

* REPL 재실행 후 테스트 해봅니다.
```python
>>> from exceptional import convert
>>> convert("test")
실패
-1
>>> convert([1, 2, 3])
실패
-1
```
<br/><br/>


### 3-2. exception 정보얻기
* except 블록에서는 단순히 예외처리 뿐만 아니라 예외에 관한 정보를 얻을 수 있습니다.
* 코드를 다음과 같이 수정합니다.
```python
import sys


def convert(s):
    """int로 변환"""
    try:
        a = int(s)
        print('성공')
    except (ValueError, TypeError) as e:
        print('에러정보 : ', e)
        a = -1
    return a
```
<br/>

* print옵션을 통해 stderr 표준오류스트림을 통해 출력할 수 있습니다.
* 리눅스 등 유닉스계열 OS는 일반적으로 print 되는 로그를 `>` 를 통해 파일로 저장할 수 있습니다.
* exceptional.py를 다음과 같이 수정해봅니다.
```python
"""Exception을 설명하는 모듈"""

def convert(s):
    """int로 변환"""
    try:
        a = int(s)
        print('성공')
    except (ValueError, TypeError) as e:
        print('에러정보 : ', e)
        a = -1
    return a


convert(sys.argv[1])
```
<br/>

* 그리고 터미널 화면에서 아래와 같이 입력해봅니다.
* a.log라는 파일에 저장됩니다. vi 명령어로 결과를 볼 수 있습니다.
* 이때 사용되는 것이 기본으로 사용되는 stdout 스트림입니다.
```python
$ python exceptional.py '가나다' > a.log
$ vi a.log
```
<br/>

* 이것을 print 키워드 파라미터로 표준 error 출력으로 변경해봅니다.
```python
import sys


def convert(s):
    """int로 변환"""
    try:
        a = int(s)
        print('성공')
    except (ValueError, TypeError) as e:
        print('에러정보 : ', e, file=sys.stderr)
        a = -1
    return a
```
<br/>

* 이제 표준출력에서 표준error 출력으로 변경되었습니다.
* 아까와 똑같이 꺽쇠만 하면, 파일에 아무내용이 기록되지 않습니다. 출력이 바뀌었기때문입니다.
* `2>` 표준에러출력을 받아 파일로 기록합니다.
* https://stackoverflow.com/questions/15344547/how-to-see-stderr-output-in-linux
```python
$ python exceptional.py '가나다' 2> c.log 
$ vi b.log
```
* 다시 아래와 같이 실행해봅니다.
<br/><br/>



### 3-3. raise로 Exception발생시키기
* 상황에 따라서는 호출 하는 함수에 정보를 넘겨주기 위해 일부러 Exception을 발생시켜야할 때도 있습니다.
* exceptional.py 파일에 함수를 하나 추가합니다.
```python
from math import log

def string_log(s):
    v = convert(s)
    return log(v)
```
<br/>

* `raise` 키워드로 Exception을 발생시킬 수 있습니다.
* convert함수를 다음과 같이 변경합니다.
* 그리고 모듈 최하단 `convert(sys.argv[1])` 라인을 제거합니다.
```python
def convert(s):
    """int로 변환"""
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print('에러정보 : ', e, file=sys.stderr)
        raise
```
<br/>

* REPL에서 확인해봅니다.
* `string_log` 함수를 실행하고, convert에서 발생된 에러정보가 나타납니다.
```python
>>> from exceptional import string_log
>>> string_log("25")
3.2188758248682006
>>> string_log("test")
에러정보 :  invalid literal for int() with base 10: 'test'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/Blidkaga/Documents/CodeLab/Python_Basic/exceptional.py", line 18, in string_log
    v = convert(s)
  File "/Users/Blidkaga/Documents/CodeLab/Python_Basic/exceptional.py", line 9, in convert
    return int(s)
ValueError: invalid literal for int() with base 10: 'test'
>>> string_log([1,3,5,7])
에러정보 :  int() argument must be a string, a bytes-like object or a number, not 'list'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/Blidkaga/Documents/CodeLab/Python_Basic/exceptional.py", line 18, in string_log
    v = convert(s)
  File "/Users/Blidkaga/Documents/CodeLab/Python_Basic/exceptional.py", line 9, in convert
    return int(s)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
```
<br/>

* raise로 특정 에러를 발생시킬 수 있습니다.
* raise 발생시키고자하는에러(에러메세지) 형식으로 입력합니다.
```python
def convert(s):
    """int로 변환"""
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print('에러정보 : ', e, file=sys.stderr)
        raise ValueError("Argument에 잘못된 값이 전달되었습니다.")
```
<br/>

* REPL에서 확인합니다.
* TypeError가 발생하던 상황이었는데 ValueError와 직접입력한 에러메세지가 전달되었습니다.
```python
>>> string_log([1,2,3])
에러정보 :  int() argument must be a string, a bytes-like object or a number, not 'list'
Traceback (most recent call last):
  File "/Users/Blidkaga/Documents/CodeLab/Python_Basic/exceptional.py", line 9, in convert
    return int(s)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/Blidkaga/Documents/CodeLab/Python_Basic/exceptional.py", line 18, in string_log
    v = convert(s)
  File "/Users/Blidkaga/Documents/CodeLab/Python_Basic/exceptional.py", line 12, in convert
    raise ValueError("Argument에 잘못된 값이 전달되었습니다.")
ValueError: Argument에 잘못된 값이 전달되었습니다.
```


<br/><br/>
### 3-4. finally block
* finally블록은 예외처리 구문에서 예외가 발생하던 하지 않던 무조건적으로 처리하는 블록입니다.
* convert함수를 변경해보겠습니다.
```python
def convert(s):
    """int로 변환"""
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print('에러정보 : ', e, file=sys.stderr)
        raise ValueError("Argument에 잘못된 값이 전달되었습니다.")
    finally:
        print('여기는 에러가 발생할 때도, 안 할때도 무조건 실행됩니다.')
```
<br/>

* REPL에서 확인해보겠습니다.
* 정상 실행 시에도, 에러 발생 시에도 finally 블록에 구문은 실행됩니다.
```python
>>> from exceptional import string_log
##### 정상 실행 시
>>> string_log(1) 
여기는 에러가 발생할 때도, 안 할때도 무조건 실행됩니다. 
0.0


##### 에러 발생 시
>>> string_log('aa')
에러정보 :  invalid literal for int() with base 10: 'aa'
여기는 에러가 발생할 때도, 안 할때도 무조건 실행됩니다.
Traceback (most recent call last):
  File "/Users/Blidkaga/Documents/CodeLab/Python_Basic/exceptional.py", line 9, in convert
    return int(s)
ValueError: invalid literal for int() with base 10: 'aa'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/Blidkaga/Documents/CodeLab/Python_Basic/exceptional.py", line 20, in string_log
    v = convert(s)
  File "/Users/Blidkaga/Documents/CodeLab/Python_Basic/exceptional.py", line 12, in convert
    raise ValueError("Argument에 잘못된 값이 전달되었습니다.")
ValueError: Argument에 잘못된 값이 전달되었습니다.
```
<br/><br/>


### 3-5. else 블록
* 예외처리구문에 else블록이 있습니다.
* except 블록과 반대입니다. 예외가 없으면 실행되는 블록입니다.
* C#, Java, Javascript에서는 볼 수 없었던 구문입니다.
* convert 함수를 수정하여 한번 확인해보겠습니다. try 안에 return구문이 있던 것 을 변경하였습니다.
```python
def convert(s):
    """int로 변환"""
    try:
        a = int(s)
    except (ValueError, TypeError) as e:
        print('에러정보 : ', e, file=sys.stderr)
        raise ValueError("Argument에 잘못된 값이 전달되었습니다.")
    else :
        print('에러가 발생하지 않았어요!!')
    finally:
        print('여기는 에러가 발생할 때도, 안 할때도 무조건 실행됩니다.')
    return a
```
<br/>

* 결과 '에러가 발생하지 않았어요!!' 구문은 정말로 에러가 발생하지 않았을 때만 수행되었습니다.
```python
>>> from exceptional import string_log
>>> string_log(1)
에러가 발생하지 않았어요!!
여기는 에러가 발생할 때도, 안 할때도 무조건 실행됩니다.
0.0
>>> string_log("test")
에러정보 :  invalid literal for int() with base 10: 'test'
여기는 에러가 발생할 때도, 안 할때도 무조건 실행됩니다.
Traceback (most recent call last):
  File "/Users/Blidkaga/Documents/CodeLab/Python_Basic/exceptional.py", line 9, in convert
    a = int(s)
ValueError: invalid literal for int() with base 10: 'test'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/Blidkaga/Documents/CodeLab/Python_Basic/exceptional.py", line 23, in string_log
    v = convert(s)
  File "/Users/Blidkaga/Documents/CodeLab/Python_Basic/exceptional.py", line 12, in convert
    raise ValueError("Argument에 잘못된 값이 전달되었습니다.")
ValueError: Argument에 잘못된 값이 전달되었습니다.    
```
<br/>

* 그리고 터미널 화면에서 아래와 같이 입력해봅니다.
* a.log라는 파일에 저장됩니다. vi 명령어로 결과를 볼 수 있습니다.
* 이때 사용되는 것이 기본으로 사용되는 stdout 스트림입니다.
```python
$ python exceptional.py '가나다' > a.log
$ vi a.log
```



<br/><br/><br/>
> 참고 : [wikidocs(파이썬 - 기본을 갈고 닦자!)](https://wikidocs.net/16060)
