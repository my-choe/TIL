# 📝 27 변수 scope
* **Java & C#, Javascript, Python 변수 스코프가 조금씩 차이가 있음. 주의요망**

## 1. javascript와 Python 차이
* 코드로써 차이를 확인하겠습니다.
* Javascript ES 6 let 키워드를 사용한 코드 입니다.
* if 바깥에서도 a 변수 불가능
* C#이나 Java의 변수 scope와 유사합니다.
```python
function abc(){
  if(true){
    let a = 5
    }
  console.log(a)
}
abc()

VM3146:5 Uncaught ReferenceError: a is not defined
    at abc (<anonymous>:5:14)
    at <anonymous>:1:1
```
<br/>

* Javascript ES 5 var 키워드를 사용한 코드 입니다.
* if 바깥에서도 a 변수 접근 가능
```python
function abc(){
  if(true){
    var a = 5
    }
  console.log(a)
}
abc()
5 //결과
console.log(a)
VM482:1 Uncaught ReferenceError: a is not defined
    at <anonymous>:1:13
```
<br/>

* Javascript ES 5 var와 let 모두 사용하지 않고 그냥 선언한경우
* if 바깥 뿐만아니라 함수 실행 후에는 함수 바깥에서도 접근 가능
```python
function abc(){
  if(true){
    a = 5
    }
  console.log(a)
}
console.log(a)
Uncaught ReferenceError: a is not defined
    at <anonymous>:1:1

abc()
5 //결과

console.log(a) // 함수 실행 후 외부에서도 a 접근 가능, 전역 window에 a가 할당되었기 때문
5
```
<br/>

* 이 사례만 본다면, 파이썬은 Javascript var 키워드의 스코프와 가장 유사합니다.
* 같은 로직의 함수의 파이썬 변수를 보겠습니다.
* if 바깥에서는 접근 가능, 함수 밖에서는 불가능 입니다.
```python
>>> def abc():
...     if True:
...             a = 5
...     print(a)
... 
>>> abc()
5
>>> a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
```

```python
>>> def test():
...     a= [1, 3, 5]
...     for i in a:
...             print("i:",i)
...     print(i)
... 
>>> test()
i: 1
i: 3
i: 5
5  
```

<br/><br/><br/>
## 2. LEGB Rule
* 파이썬 변수 scope 룰을 LEGB 룰이라고 불리기도 합니다.
* 변수가 값을 찾을 때, Local -> Enclosed -> Global -> Built-in
* local - 가장 가까운 함수안 범위 입니다.
* Enclosed - 파이썬은 함수 안에 함수가 정의 될수 있는데, 가장 가까운 함수가 아닌 두번째 이상의 함수 가까운 함수범위입니다.
* Global - 함수 바깥의 변수 또는 import된 module
* Built-in - 파이썬안에 내장되어 있는 함수 또는 속성들입니다.
```python
>>> a = 5    # Global
>>> b = 10   # Global
>>> def outer():
...     a = 10  # outer함수의 local이며, inner함수의 Enclosed
...     def inner():
...             c=30 # inner 함수의 local
...             print(a, b, c)
...     inner()
...     a = 22  # outer함수의 local이며, inner함수의 Enclosed
...     inner()
... 
>>> outer()
10 10 30  
22 10 30
```


<br/><br/><br/>
## 3. locals()와 globals()
* 로컬변수를 확인하는 `locals()`
* 글로벌변수를 확인하는 `globals()`
```python
>>> glob = 1
>>> def foo():
...     loc = 5
...     print('loc in foo():' , 'loc' in locals())
... 
>>> foo()
loc in foo(): True
>>> print('loc in global:', 'loc' in globals()) 
loc in global: False
>>> print('glob in global:', 'foo' in globals())
glob in global: True
```
<br/>

* `globals()`로 import 모듈도 global 변수 임을 확인
```python
>>> 'math' in globals()
False
>>> import math
>>> 'math' in globals()
True
>>> from math import factorial
>>> 'factorial' in globals()
True
```


<br/><br/><br/>
## 4. global 키워드
* global 변수를 사용함으로써 실수할 수 있는 예
* `set_count(5)`를 실행함으로써 global변수를 바꿀 수 있을 듯 보이지만..local에서 새롭게 변수를 할당하게 됩니다. 그러므로 `show_count()`는 계속 0입니다.
```python
>>> count = 0
>>> def show_count():
...     print("count = ", count)
... 
>>> def set_count(c):
...     count = c
... 
>>> show_count()
count =  0
>>> set_count(5)
>>> show_count()
count =  0
```
<br/>

* 위 해결책으로 global 키워드를 사용합니다.
* global 키워드는 함수 내부에서 로컬변수가 아닌 글로벌 변수를 사용하게 해줍니다.
```python
>>> count = 0
>>> def show_count():
...     print("count = ", count)
... 
>>> def set_count(c):
...     global count
...     count = c
... 
>>> set_count(5)
>>> show_count()
count =  5
```

<br/><br/><br/>
> 참고 : [wikidocs(파이썬 - 기본을 갈고 닦자!)](https://wikidocs.net/16055)
