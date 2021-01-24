# 📝 38 itertools 모듈과 iterable에 유용한 내장함수
## 1. itertools
* itertools 모듈에는 반복 가능한 데이터 스트림을 처리하는 데 유용한 많은 함수와 제네레이터가 포함되어 있습니다
* REPL을 통해 확인합니다.
* 예제를 위해 소수(1과 자기자신만 나눌 수 있는 수)를 구하는 함수를 작성합니다.
```python
>>> def is_prime(x):
...     if x > 1:
...             for i in range(2, x):
...                     if x % i == 0:
...                             return False
...     else:
...             return False
...     return True
... 
>>> is_prime(5)
True
>>> is_prime(8)
False    
```
<br/>

* itertools 모듈의 `count()`와 `islice()` 함수를 사용합니다.
* count : `count(시작, [step])` 의 함수로 시작 숫자부터 step만큼(없으면 1) 씩 무한히 증가하 제네레이터입니다.
* islice : `islice(iterable객체, [시작], 정지[,step])`의 함수로, iterable한 객체를 특정 범위로 슬라이싱하고 iterator로 반환됩니다.
* 다음은 0 부터 999까지의 수 중에 소수인 수를 반환하는 iterator를 만듭니다.
```python
>>> from itertools import islice, count
>>> thousand_primes = islice((x for x in count() if is_prime(x)),1000)
>>> next(thousand_primes)
2
>>> next(thousand_primes)
3
>>> next(thousand_primes)
5
```
<br/>

* chain : `chain(*iterable)`은 iterable한 객체들을 인수로 받아 하나의 iterator로 반환
```python
>>> from itertools import chain
>>> country = ['대한민국','스웨덴', '미국']
>>> capital = ['서울','스톡홀름','워싱턴']
>>> c = chain(country, capital)
>>> next(c)
'대한민국'
>>> next(c)
'스웨덴'
>>> next(c)
'미국'
>>> next(c)
'서울'
>>> next(c)
'스톡홀름'
>>> next(c)
'워싱턴'
```

<br/><br/>
## 2. iterable에 유용한 내장함수
* all : `all(iterable)`은 iterable한 객체를 인수로 받으며, 인수의 원소가 모두 참이면 True, 거짓이 하나라도 있 으면 False를 리턴
```python
>>> all([1, 2, 3])
True
>>> all([0, 1, 2, 3])
False
```
<br/>

* any : `any(iterable)`은 iterable한 객체를 인수로 받으며, 인수의 원소 중 하나라도 참이면 True, 모두 거짓일때만 False를 리턴, all의 반대
```python
>>> a = zip([1,2,3], (4,5,6))
>>> next(a)
(1, 4)
>>> next(a)
(2, 5)
>>> next(a)
(3, 6)
```
<br/>

* zip : `zip(*iterable)`은 iterable한 객체를 인수로 받으며 동일한 개수로 이루어진 자료형을 묶어서 iterator로 반환.
```python
>>> h = test_generator()
>>> i = test_generator()
>>> h == i
False
>>> h is i
False
>>> next(h)
1
>>> next(i)
1
>>> next(h)
2
>>> next(i)
2
>>> next(i)
3
>>> next(h)
3
```
<br/>

* zip은 두개의 iterable객체를 묶어 for문을 한꺼번에 반복시킬때 유용합니다.
```python
>>> country = ['대한민국','스웨덴', '미국']
>>> capital = ['서울','스톡홀름','워싱턴']
>>> for coun, cap in zip(country, capital):
...     print('국가명 : {}, 수도:{}'.format(coun,cap))
... 
국가명 : 대한민국, 수도:서울
국가명 : 스웨덴, 수도:스톡홀름
국가명 : 미국, 수도:워싱턴
```


<br/><br/><br/>
> 참고 : [wikidocs(파이썬 - 기본을 갈고 닦자!)](https://wikidocs.net/16070)
