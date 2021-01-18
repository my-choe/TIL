# 📝 14 tuple(튜플)
## 1. tuple(튜플)
* tuple(튜플)은 불변한 순서가 있는 객체의 집합입니다.
* list형과 비슷하지만 한 번 생성되면 값을 변경할 수 없습니다.
<br/>

* REPL에서 확인해봅니다.
* list와 마찬가지로 다양한 타입이 함께 포함될 수 있습니다.
```python
>>> t = (1, "korea", 3.5, 1)
>>> t
(1, 'korea', 3.5, 1)
>>> type(t)
<class 'tuple'>
```
<br/>

* 순서가 있기때문에 인덱스로 접근 가능합니다.
```python
>>> t[0]
1
>>> t[1]
'korea'
```
<br/>

* len내장함수로 길이를 구할 수 있습니다.
```python
>>> len(t)
4
```
<br/>

* list와 마찬가지로 for loop을 돌 수 있습니다.
```python
>>> for i in t:
...     print(i)
... 
1
korea
3.5
1
```
<br/>

* `+` 연산으로 tuple(튜플)을 추가할 수 있습니다.
```python
>>> t = t + (3 ,5)
>>> t
(1, 'korea', 3.5, 1, 3, 5)
```
<br/>

* `*` 연산으로 tuple(튜플)을 반복할 수 있습니다.
```python
>>> t * 2
(1, 'korea', 3.5, 1, 3, 5, 1, 'korea', 3.5, 1, 3, 5)
```
<br/>

* tuple(튜플) 속에 tuple이 포함될 수 있습니다.
```python
>>> a = ((1 ,2) , (3,4), (5,9))
>>> a[2]
(5, 9)
>>> a[2][1]
9
```
<br/>

* tuple(튜플)이 하나의 원소만 존재하는 경우는 tuple(튜플)이 되지않습니다.
* but 회피하는 방법이 있습니다. 한개의 원소 뒤에 콤마를 찍어주면 tuple이 유지됩니다.
```python
>>> h = (350)
>>> type(h)
<class 'int'>
>>> h = (350,)
>>> type(h)
<class 'tuple'>
>>> len(h)
1
```
<br/>

* 위에 예제들 속에서 tuple(튜플)은 '( )'를 입력했습니다만, 괄호가 필수 조건은 아닙니다.
```python
>>> p = 1, 3, 2, 5, 7
>>> type(p)
<class 'tuple'>
```
<br/>

* tuple(튜플)을 이용하여 함수에서 여러 값을 한꺼번에 리턴시킬 수 있습니다.
```python
>>> def minmax(items):
...     return min(items), max(items)
...  
>>> minmax([7,5,2,1,11,15,55])
(1, 55)
```
<br/>

* tuple(튜플)을 이용하여 변수를 한꺼번에 할당할 수 있습니다.(자바스크립트 ES6 해체할당과 비슷합니다.)
```python
>>> lower, upper = minmax([7,5,2,1,11,15,55])
>>> lower
1
>>> upper
55
```
<br/>

* tuple(튜플)속에 tuple(튜플)을 이용해 이러한 할당도 가능합니다.
```python
>>> (a, (b,(c, d))) = (4,(3,(2,1)))
>>> a
4
>>> b
3
>>> c
2
>>> d
1
```
<br/>

* 보통 다른언어에서 두 변수의 값을 서로 바꾸려면, 새로운 변수가 하나 필요하지만 파이썬에서는 튜플의 해체할당기능을 통해 바로 바꿔줄 수 있습니다.
```python
>>> a = '감자'
>>> b = '고구마'
>>> a, b  = b, a
>>> a
'고구마'
>>> b
'감자'
```
<br/>

* tuple(튜플)변환 - `tuple(iterable한객체)`로 tuple(튜플)로 변형할 수 있습니다.
```python
>>> len(t)
4
```
<br/>

* in 절로 포함되어 있는지 체크할 수 있습니다.
```python
>>> 'a' in ('a', 'b', 'c')
True
>>> 5 in ('a','b','c')
False
>>> 5 not in ('a','b','c')
True
```
<br/>


<br/><br/><br/>
> 참고 : [wikidocs(파이썬 - 기본을 갈고 닦자!)](https://wikidocs.net/16042)
