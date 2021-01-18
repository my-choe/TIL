# 📝 19 function(함수)
## 1. function(함수)란?
* 함수란 프로그래밍 코드를 작성하다보면 반복되는 코드를 줄여주기 위해 특정 코드를 함수안에 정의하고, 그 코드를 함수명칭을 호출함으로써 코드를 실행하게 해줍니다.
* 함수의 구조는 아래와 같습니다.
* return은 생략될 수 있습니다. return이 수행되면 함수가 종료됩니다.
```python
def 함수명(파라미터):
    실행될 코드
    return 결과 값
```



<br/><br/><br/>
## 2. 간단한 function(함수) 작성
* REPL을 활용하여 간단한 함수를 작성해봅니다.
* squre라는 명칭의 함수를 정의했습니다.
* x라는 파라미터(인수)를 받아 x * x 값을 반환하였습니다.
* 5를 파라미터로 squre함수를 호출하였습니다.
```python
>>> def square(x):
...     return x * x
... 
>>> square(5)
25
```
<br/>

* return을 생략한 함수입니다.
```python
>> def eat_dinner():
...     print("저녁 잘 먹었습니다.")
... 
>>> eat_dinner()
저녁 잘 먹었습니다.
```
<br/>

* return을 결과값을 반환하지 않고, 함수의 종료목적으로만 사용할 수 있습니다.
```python
>>> def even_or_odd(n):
...     if n % 2 == 0:
...             print("even")
...             return
...     print("odd")
... 
>>> even_or_odd(3)
odd
>>> even_or_odd(4)
even
```


<br/><br/><br/>
> 참고 : [wikidocs(파이썬 - 기본을 갈고 닦자!)](https://wikidocs.net/16047)
