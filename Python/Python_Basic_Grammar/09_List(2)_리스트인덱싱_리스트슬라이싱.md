# 📝 List(2) - 리스트인덱싱 & 리스트슬라이싱
## 1. list indexing(리스트 인덱싱)
* 파이썬에서 리스트 인덱싱은 `-`(음수 인덱싱) 값도 허용합니다.
* `-` 값은 역순으로도 인덱싱됩니다.
* 다른 언어에서면 마지막열을 찾기위해 리스트의 길이를 구해서 찾아야 하지만, 파이썬은 -1만으로도 손쉽게 찾을 수 있습니다.
```python
>>> s = 'show how to index into sequences'.split()
>>> s
['show', 'how', 'to', 'index', 'into', 'sequences']
>>> s[0]
'show'
>>> s[5]
'sequences'
>>> s[-1]
'sequences'
>>> s[-2]
'into'
>>> s[-6]
'show'
```


<br/><br/><br/>
## 2. list slicing(리스트 슬라이싱)
* 파이썬에서는 리스트를 자르는 특별한 문법을 제공합니다.
* 사용법은 `리스트변수[시작인덱스:종료인덱스:step]` 입니다.
* 종료인덱스의 원소는 포함되지 않고 바로 앞 원소까지만 포함됩니다. step은 생략됩니다.
```python
>>> s[1:4]
['how', 'to', 'index']
```
<br/>

* 음수 인덱싱도 슬라이싱에 사용할 수 있습니다.
```python
>>> s[1:-1]
['how', 'to', 'index', 'into']
```
<br/>

* 시작인덱스부터 끝까지 포함시키려면 아래와 같이 입력합니다.
* `리스트변수[시작인덱스:]`
```python
>>> s[3:]
['index', 'into', 'sequences']
```
<br/>

* 반대로 처음부터 특정인덱스까지 가져오기 위해서는 아래와 같이입력합니다.
* `리스트변수[:종료인덱스]`
```python
>>> s[:3]
['show', 'how', 'to']
```
<br/>

* 위 두 예제를 합치면 처음 리스트 변수와 같습니다.
```python
>>> s[:3] + s[3:] == s
True
```
<br/>

* 모든 값을 복사하여 새로운 list를 만들기 위해서는 아래와같이 입력합니다.
* `리스트변수[:]`
```python
>>> [1, 3, 5] + [ 2, 7]
[1, 3, 5, 2, 7]
```
<br/>

* 문자열을 리스트로 변형해봅니다.
```python
>>> full_slice = s[:]
>>> full_slice
['show', 'how', 'to', 'index', 'into', 'sequences']
```
<br/>

* 슬라이스를 통해 새롭게 만든 변수와 값은 같지만, 같은 변수는 아닙니다.
```python
>>> full_slice == s
True
>>> full_slice is s
False
>>> 
```
<br/>

* 리스트를 복사하는 방법에는 두가지 방법이 더 있습니다.
```python
>>> u = s.copy()
>>> v = list(s)
>>> u
['show', 'how', 'to', 'index', 'into', 'sequences']
>>> v
['show', 'how', 'to', 'index', 'into', 'sequences']
```
<br/>

* step을 사용해봅니다.
```python
>>> s = 'show how to index into sequences'.split()
>>> s
['show', 'how', 'to', 'index', 'into', 'sequences']
>>> s[::2]
['show', 'to', 'into']
>>> 
```
<br/>

* step을 활용하여 리스트를 reverse할 수 있습니다.
```python
>>> s = 'show how to index into sequences'.split()
>>> s
['show', 'how', 'to', 'index', 'into', 'sequences']
>>> s[::-1]
['sequences', 'into', 'index', 'to', 'how', 'show']
>>> 
```




<br/><br/><br/>
> 참고 : [wikidocs(파이썬 - 기본을 갈고 닦자!)](https://wikidocs.net/16037)
