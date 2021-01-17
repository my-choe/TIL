# 📝 11 List(3) - 리스트 반복 & 리스트 관련 메소드
## 1. list Repetition(리스트 반복)
* `*` 연산자로 리스트를 반복 시킬 수 있습니다.
```python
>>> a = [5,3]
>>> b = a * 3
>>> a
[5, 3]
>>> b
[5, 3, 5, 3, 5, 3]
```
<br/>

* 리스트 반복에서도 얕은복사 문제가 있습니다.
* 관련 포스팅 : https://suwoni-codelab.com/python%20%EA%B8%B0%EB%B3%B8/2018/03/02/Python-Basic-copy/
* a변수의 첫번째 원소에만 값을 추가했는데 3개의 원소 모두 추가됩니다.
* **리스트 반복 시에도 얕은 복사됨을 인지하고 있어야 합니다.**
```python
>>> a = [[2,5]] * 3
>>> a
[[2, 5], [2, 5], [2, 5]]
>>> a[0].append(7)
>>> a
[[2, 5, 7], [2, 5, 7], [2, 5, 7]
```

<br/><br/><br/>
## 2. list 관련 메소드 및 연산
* index(item) : 리스트안에서 해당 item의 index번호를 리턴, 없는 경우 ValueError
```python
>>> a = ['서울','인천', '대전','제주도']
>>> a.index('인천')
1
>>> a.index('부산')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: '부산' is not in list
```
<br/>

* count(item) : 매칭되는 갯수를 리턴해줌
```python
>>> a = [1, 5, 5, 3, 7, 0, 1, 2]
>>> a.count(5)
2
>>> a.count(13)
0
```
<br/>

* in절로 list안에 포함되어 있는지 확인할수 있습니다.
```python
>>> 35 in [1, 35,90,100]
True
>>> 11 in [1, 3, 5,10]
False
>>> 11 not in [1, 3, 5,10]
True
```

<br/><br/><br/>
> 참고 : [wikidocs(파이썬 - 기본을 갈고 닦자!)](https://wikidocs.net/16039)
