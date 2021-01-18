# 📝 15 Dictionary(딕셔너리)
## 1. dictionary(딕셔너리)
* 딕셔너리 타입은 immutable한 키(key)와 mutable한 값(value)으로 맵핑되어 있는 순서가 없는 집합입니다.
<br/>

* REPL에서 확인합니다.
* 일반적인 딕셔너리 타입의 모습입니다. 중괄호로 되어 있고 키와 값이 있습니다.
```python
>>> {"a" : 1, "b":2}
{'a': 1, 'b': 2}
```
<br/>

* 키로는 immutable한 값은 사용할 수 있지만, mutable한 객체는 사용할 수 없습니다.
```python
# immutable 예
>>> a = {1: 5, 2: 3}   # int 사용
>>> a
{1: 5, 2: 3}
>>> a = {(1,5): 5, (3,3): 3} # tuple사용
>>> a
{(1, 5): 5, (3, 3): 3}
>>> a = { 3.6: 5, "abc": 3} # float 사용
>>> a
{3.6: 5, 'abc': 3}
>>> a = { True: 5, "abc": 3} # bool 사용
>>> a
{True: 5, 'abc': 3}

# mutable 예
>>> a = { {1, 3}: 5, {3,5}: 3}     #set 사용 에러
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'set'
>>> a = {[1,3]: 5, [3,5]: 3}     #list 사용 에러
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>> a = { {"a":1}: 5, "abc": 3}     #dict 사용 에러
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'dict'
```
<br/>

* 값은 중복될 수 있지만, 키가 중복되면 마지막 값으로 덮어씌워집니다.
```python
>>> {"a" : 1, "a":2}
{'a': 2}
```
<br/>

* 순서가 없기 때문에 인덱스로는 접근할수 없고, 키로 접근 할 수 있습니다.
```python
>>> d = {'abc' : 1, 'def' : 2}
>>> d[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 0
>>> d['abc']
1
```
<br/>

* mutable 한 객체이므로 키로 접근하여 값을 변경할 수 있습니다.
```python
>>> d['abc'] = 5
>>> d
{'abc': 5, 'def': 2}
```
<br/>

* `*` 연산으로 tuple(튜플)을 반복할 수 있습니다.
```python
>>> t * 2
(1, 'korea', 3.5, 1, 3, 5, 1, 'korea', 3.5, 1, 3, 5)
```
<br/>

* 새로운 키와 값을 아래와 같이 추가할 수 있습니다.
```python
>>> d['ghi'] = 999
>>> d
{'abc': 5, 'def': 2, 'ghi': 999}
```


<br/><br/><br/>
## 2. dictionary(딕셔너리) 선언
* 딕셔너리 선언할때는 빈 중괄호를 사용합니다.(set 중괄호를 이용하지만 빈중괄호로 선언하면 type이 dict가 됩니다.)
* 딕셔너리로 명시적으로 선언할 수도 있습니다.
```python
>>> e = {}
>>> type(e)
<class 'dict'>
>>> f = dict()
>>> type(f)
<class 'dict'>
```
<br/>

* dict constructor를 통해서 아래와 같이 바로 키와 값을 할당하며 선언할 수 있습니다.
```python
>>> newdict = dict( alice = 5, bob = 20, tony= 15, suzy = 30)
>>> newdict
{'alice': 5, 'bob': 20, 'tony': 15, 'suzy': 30}
```



<br/><br/><br/>
## 3. dictionary(딕셔너리) 변환
* 리스트 속에 리스트나 튜플, 튜플속에 리스트나 튜플의 값을 키와 value를 나란히 입력하면, 아래와 같이 dict로 변형할 수 있습니다.
```python
>>> name_and_ages = [['alice', 5], ['Bob', 13]]
>>> dict(name_and_ages)
{'alice': 5, 'Bob': 13}
>>> name_and_ages = [('alice', 5), ('Bob', 13)]
>>> dict(name_and_ages)
{'alice': 5, 'Bob': 13}
>>> name_and_ages = (('alice', 5), ('Bob', 13))
>>> dict(name_and_ages)
{'alice': 5, 'Bob': 13}
>>> name_and_ages = (['alice', 5], ['Bob', 13])
>>> dict(name_and_ages)
{'alice': 5, 'Bob': 13}
```



<br/><br/><br/>
## 3. dictionary(딕셔너리) 변환
* 얕은 복사(shallow copy) 1
```python
>>> a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> b =a.copy()
>>> b['alice'].append(5)
>>> b
{'alice': [1, 2, 3, 5], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> a
{'alice': [1, 2, 3, 5], 'bob': 20, 'tony': 15, 'suzy': 30}
```
<br/>

* 위에 예제들 속에서 tuple(튜플)은 '( )'를 입력했습니다만, 괄호가 필수 조건은 아닙니다.
```python
>>> p = 1, 3, 2, 5, 7
>>> type(p)
<class 'tuple'>
```
<br/>

* 얕은 복사(shallow copy) 2
```python
>>> a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> b = dict(a)
>>> a
{'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> b
{'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> id(a)
4334645680
>>> id(b)
4334648920
```
<br/>

* 깊은 복사(deep copy)
```python
>>> import copy
>>> a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> b = copy.deepcopy(a)
>>> b['alice'].append(5)
>>> b
{'alice': [1, 2, 3, 5], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> a
{'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
```



<br/><br/><br/>
## 5. dictionary update(딕셔너리 수)
* 단일 수정은 키로 접근하여 값을 할당하면 됩니다.
```python
>>> a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> a['alice'] = 5
>>> a
{'alice': 5, 'bob': 20, 'tony': 15, 'suzy': 30}
```
<br/>

* 여러값 수정은 update 메소드를 사용합니다. 키가 없는 값이면 추가됩니다.
```python
>>> a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> a.update({'bob':99, 'tony':99, 'kim': 30})
>>> a
{'alice': [1, 2, 3], 'bob': 99, 'tony': 99, 'suzy': 30, 'kim': 30}
```



<br/><br/><br/>
## 6. dictionary(딕셔너리) for문
* for문을 통해 딕셔너리를 for문을 돌리면 key값이 할당됩니다.
* **순서는 임의적이다.같은 순서를 보장할 수 없다.**
```python
>>> a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> for key in a:
...     print(key)
... 
alice
bob
tony
suzy
```
<br/>

* value값으로 for문을 반복하기 위해서는 `values()`를 사용해야합니다.
```python
>>> for val in a.values():
...     print(val)
... 
[1, 2, 3]
20
15
30
```
<br/>

* key와 value를 한꺼번에 for문을 반복하려면 `items()`를 사용합니다.
```python
>>> for key, val in a.items():
...     print("key = {key}, value={value}".format(key=key,value=val))
... 
key = alice, value=[1, 2, 3]
key = bob, value=20
key = tony, value=15
key = suzy, value=30
```



<br/><br/><br/>
## 7. dictionary(딕셔너리) 의 in
* dictionary의 in은 키에 한해서 동작합니다.
```python
>>> 'alice' in a
True
>>> 'teacher' in a
False
>>> 'teacher' not in a
True
```


<br/><br/><br/>
## 8. dictionary(딕셔너리)의 요소 삭제
* list와 마찬가지로 del키워드를 사용합니다.
```python
>>> a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> del a['alice']
>>> a
{'bob': 20, 'tony': 15, 'suzy': 30}
```



<br/><br/><br/>
## 9.dictionary(딕셔너리)를 읽기 쉽게 표현해주는 pprint
* pprint모듈로 dictionary를 찍어보자
```python
>>> from pprint import pprint as pp
>>> a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30,"dodo": [1,3,5,7], "mario": "pitch"}
>>> print(a)
{'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30, 'dodo': [1, 3, 5, 7], 'mario': 'pitch'}
>>> pp(a)
{'alice': [1, 2, 3],
 'bob': 20,
 'dodo': [1, 3, 5, 7],
 'mario': 'pitch',
 'suzy': 30,
 'tony': 15}
```



<br/><br/><br/>
> 참고 : [wikidocs(파이썬 - 기본을 갈고 닦자!)](https://wikidocs.net/16043)
