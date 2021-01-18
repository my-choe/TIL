# 📝 17 for in 반복문, Range, enumerate
## 1. for in 반복문
* 여타 다른 언어에서는 일반적인 for문, foreach문, for of문등 여러가지 방식을 한꺼번에 지원하는 경우가 많습니다.
* Python에서는 for in문 한가지 방식의 for 문만 제공합니다.
<br/>

* REPL 에서 확인해보겠습니다.
* for in 문 형식 입니다.
* iterable은 사전적의미와 똑같이 반복가능한 객체를 말합니다.
```python
for item in iterable:
  ... 반복할 구문...
```
<br/>

* terable 객체를 판별하기 위해서는 아래의 방법이 있습니다.
* collections.Iterable에 속한 instance인지 확인하면 됩니다.
* isinstance 함수는 첫번째 파라미터가 두번째 파라미터 클래스의 instance이면 True를 반환합니다.
```python
>>> import collections

# iterable 한 타입
>>> var_list = [1, 3, 5, 7]
>>> isinstance(var_list, collections.Iterable)
True
>>> var_dict = {"a": 1, "b":1}
>>> isinstance(var_dict, collections.Iterable)
True
>>> var_set = {1, 3}
>>> isinstance(var_set, collections.Iterable)
True
>>> var_str = "abc"
>>> isinstance(var_str, collections.Iterable)
True
>>> var_bytes = b'abcdef'
>>> isinstance(var_bytes, collections.Iterable)
True
>>> var_tuple = (1, 3, 5, 7)
>>> isinstance(var_tuple, collections.Iterable)
True
>>> var_range = range(0,5)
>>> isinstance(var_range, collections.Iterable)
True

# iterable하지 않은 타입
>>> var_int = 932
>>> isinstance(var_int, collections.Iterable)
False
>>> var_float = 10.2
>>> isinstance(var_float, collections.Iterable)
False
>>> var_none = None
>>> isinstance(var_none, collections.Iterable)
False
```
<br/>

* 앞서 다룬 타입 중 list, dictionary, set, string, tuple, bytes가 iterable한 타입입니다.
* range도 iterable 합니다. 이번 포스트 아래쪽에서 다루겠습니다.
* for문을 동작시켜봅니다.
```python
>>> for i in var_list:
...     print(i)
... 
1
3
5
7
>>> for i in var_dict:
...     print(i)
... 
a
b
>>> for i in var_set:
...     print(i)
... 
1
3
>>> for i in var_str:
...     print(i)
... 
a
b
c
>>> for i in var_bytes:
...     print(i)
... 
97
98
99
100
101
102
>>> for i in var_tuple:
...     print(i)
... 
1
3
5
7
>>> for i in var_range:
...     print(i)
... 
0
1
2
3
4
```
* dictionary의 for문을 다시 보면 key값만 출력됩니다.


<br/><br/><br/>
## 2. range
* 위쪽 for문의 range 결과 값이 0, 1, 2, 3, 4 순서대로 결과 값이 출력되었습니다.
* range는 `range(시작숫자, 종료숫자, step)`의 형태로 리스트 슬라이싱과 유사합니다.
* range의 결과는 시작숫자부터 종료숫자 바로 앞 숫자까지 컬렉션을 만듭니다.
* 시작숫자와 step은 생략가능합니다.
```python
>>> range(5)
range(0, 5)
>>> for i in range(5):
...     print(i)
... 
0
1
2
3
4
```
<br/>

* range는 값을 확인하기 위해서 다른 순서 있는 컬렉션으로 변환해야합니다.
```python
>>> range(5,10)
range(5, 10)
>>> list(range(5,10))
[5, 6, 7, 8, 9]
>>> tuple(range(5,10))
(5, 6, 7, 8, 9)
```
<br/>

* step을 사용해봅니다.
```python
>>> list(range(10,20,2))
[10, 12, 14, 16, 18]
>>> list(range(10,20,3))
[10, 13, 16, 19]
```
<br/>

* **파이썬에서 권장하지 않는 패턴입니다.**
```python
>>> s = [1, 3, 5]
>>> for i in range(len(s)):
...     print(s[i])
... 
1
3
5
```
<br/>

* **파이썬에서 권장하는 패턴**
```python
>>> for v in s:
...     print(v)
... 
1
3
5
```




<br/><br/><br/>
## 3. enumerate
* 반복문 사용 시 몇 번째 반복문인지 확인이 필요할 수 있습니다. 이때 사용합니다.
* 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환합니다.
```python
>>> t = [1, 5, 7, 33, 39, 52]
>>> for p in enumerate(t):
...     print(p)
... 
(0, 1)
(1, 5)
(2, 7)
(3, 33)
(4, 39)
(5, 52)
```
<br/>

* tuple형태 반환을 이용하여 아래처럼 활용할 수 있습니다.
```python
>>> for i, v in enumerate(t):
...     print("index : {}, value: {}".format(i,v))
... 
index : 0, value: 1
index : 1, value: 5
index : 2, value: 7
index : 3, value: 33
index : 4, value: 39
index : 5, value: 52
```


<br/><br/><br/>
> 참고 : [wikidocs(파이썬 - 기본을 갈고 닦자!)](https://wikidocs.net/16045)
