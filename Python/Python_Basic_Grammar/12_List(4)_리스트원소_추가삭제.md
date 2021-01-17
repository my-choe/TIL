# 📝 12 List(4) - 리스트 원소 추가, 삭제
## 1. list 원소 추가
* append : 원소 마지막에 추가
```python
>>> a = [1, 2, 3, 4, 5]
>>> a.append(6)
>>> a
[1, 2, 3, 4, 5, 6]
```
<br/>

* insert : `리스트.index(입력할index, 값)`
```python
>>> a = [1, 2, 3]
>>> a.insert(1, 5)
>>> a
[1, 5, 2, 3]
```
<br/>

* `+` 연산자로 더하기
```python
>>> m = [2, 5, 7]
>>> n = [3, 5, 9]
>>> k = m + n
>>> k
[2, 5, 7, 3, 5, 9]
>>> k +=[11, 13]
>>> k
[2, 5, 7, 3, 5, 9, 11, 13]
```
<br/>

* extend메소드 : `리스트.extend(추가할리스트)`
```python
>>> a = [1,2,3]
>>> a.extend([4,5,6])
>>> a
[1, 2, 3, 4, 5, 6]
```


<br/><br/><br/>
## 2. list 원소 삭제
* del 키워드를 통한 삭제
```python
>>> a = [1, 2, 3, 4, 5, 6, 7]
>>> del a[1]
>>> a
[1, 3, 4, 5, 6, 7]
```
<br/>

* list의 remove메소드에 의한 삭제
* `list.remove(찾을아이템)`
* 찾을 아이템이 없으면 ValueError 발생
```python
>>> a = [1, 2, 3, 4, 5, 6, 7]
>>> a.remove(3)
>>> a
[1, 2, 4, 5, 6, 7]
>>> a.remove(9)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
```
<br/>

* del키워드와 리스트의 index메소드와 혼합하여 사용하면 remove효과가 남
```python
>>> a = [1, 2, 3, 4, 5, 6, 7]
>>> del a[a.index(3)]
>>> a
[1, 2, 4, 5, 6, 7]
```

<br/><br/><br/>
> 참고 : [wikidocs(파이썬 - 기본을 갈고 닦자!)](https://wikidocs.net/16040)
