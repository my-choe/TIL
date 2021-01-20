# 📝 25 함수 인자(Arguments)
## 1. default value(기본값)
* 파이썬 함수에서는 인자의 기본값을 설정할 수 있습니다.
* 형식은 아래와 같습니다. b에 기본값이 할당된 형식입니다.
```python
def function(a, b=value):
    ...내부코드
```
<br/>

* REPL을 통해 예제코드를 작성해봅니다.
* 저를 정의하는 함수를 만들었습니다.
* 인자를 입력하면 그에 맞게 출력됩니다.
* 하지만 두번째 실행에서 nick 입력하지 않으니 기본값이 출력되었습니다.
```python
>>> def define_suwoni(msg, nick='천재'):
...     print("""
... 수워니는 어떤사람? 
...     - {msg}
... 수워니의 별명은?
...     - {nick}
... """.format(msg=msg,nick=nick))
... 
>>> define_suwoni('키큰사람', '바보')

수워니는 어떤사람? 
  - 키큰사람
수워니의 별명은?
  - 바보

>>> define_suwoni('잠이 많은 사람')

수워니는 어떤사람?  
  - 잠이 많은 사람
수워니의 별명은?
  - 천재
```
<br/>

## default value 주의 사항
* **default value는 함수가 실행될 때가 아닌, 정의된 함수가 처음 평가될 때입니다.**
* 실행을 여러번해도 결과값은 변하지 않습니다.
```python
>>> import time
>>> time.ctime()
'Mon Mar  5 14:57:24 2018'
>>> time.ctime()
'Mon Mar  5 14:57:27 2018'
>>> def show_time(now=time.ctime()):
...     print(now)
... 
>>> show_time()
Mon Mar  5 14:57:52 2018
>>> show_time()
Mon Mar  5 14:57:52 2018
>>> show_time()
Mon Mar  5 14:57:52 2018
```
<br/>

* **default value를 mutable한 객체로 했을때 주의가 필요합니다.**
* 적당한 변수를 만들어 대입했을때는 문제가 없어 보이지만, default value를 여러번 사용하게 될 경우 예상치 않은 결과가 나올 수 있습니다.
```python
>>> def add_book(book_list=[]):
...     book_list.append('파이썬 베이직')
...     return book_list
... 
>>> book_list=['Hello, Python', 'Head First Python']
>>> add_book(book_list)
['Hello, Python', 'Head First Python', '파이썬 베이직']
>>> add_book()
['파이썬 베이직']
>>> add_book()
['파이썬 베이직', '파이썬 베이직']
>>> add_book()
['파이썬 베이직', '파이썬 베이직', '파이썬 베이직']
```
<br/>


* 해결책은 default value를 None으로 주고, None인 경우에만 값을 할당합니다.
```python
>>> def add_book(book_list=None):
...     if book_list is None:
...             book_list =[]
...     book_list.append('파이썬 베이직')
...     return book_list
... 
>>> add_book()
['파이썬 베이직']
>>> add_book()
['파이썬 베이직']
```


<br/><br/><br/>
## 2. postional argument(위치 인자)
* 흔히 보는 일반적인 인자입니다.
* 함수에서 정의한 위치대로 대입하는 것입니다.
```python
>>> define_suwoni('키큰사람', '바보')

    수워니는 어떤사람? 
      - 키큰사람
    수워니의 별명은?
      - 바보
```



<br/><br/><br/>
## 3. keyword argument(키워드 인자)
* 파이썬은 keyword argument(키워드 인자)를 지원합니다.
* 위 예제에서 `def define_suwoni(msg, nick='천재'):` 순서로 정의했지만, 아래와 같이 키워드 인자를 사용하면 순서를 무시하고 입력할 수 있습니다.
```python
>>> define_suwoni(nick='바보', msg = '잠이 많은 사람')

수워니는 어떤사람? 
  - 잠이 많은 사람
수워니의 별명은?
  - 바보
```
<br/>

* 위치 인자와 키워드 인자를 혼합해서 사용할 수 있습니다.
* 혼합해서 사용하는 경우 위치 인자 뒤에 키워드 인자가 와야합니다.
```python
>>> def abc(a, b, c):
...     return b, a, c
... 
>>> abc(1, 2, 3)
(2, 1, 3)
>>> abc(1, 2, c=3)
(2, 1, 3)
>>> abc(1, c=3, b=2)
(2, 1, 3)
>>> abc(1, b=2, 3)
  File "<stdin>", line 1
SyntaxError: positional argument follows keyword argument
```

<br/><br/><br/>
## 4. 위치 인자 언패킹
* 리스트나 튜플과 같이 index가 존재하는 객체를 `*`표시를 붙여 인자로서 함수에 입력하면 함수의 정의된 위치에 맡게 입력이 됩니다.
위 3번의 두번째 예제함수를 한번더 이용합니다.
```python
>>> def abc(a, b, c):
...     return b, a, c
... 
>>> p = [5, 7, 9]
>>> abc(*p)
(7, 5, 9)
```
<br/>

* 함수의 인자 수와 입력하는 객체의 수가 다르면 에러가 발생합니다.
```python
>>> z = [5,9]
>>> abc(*z)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: abc() missing 1 required positional argument: 'c'
>>> zz = [5, 9, 7, 11]
>>> abc(*zz)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: abc() takes 3 positional arguments but 4 were given
```
<br/>

* 변수대신 바로 입력할 수 있습니다.
```python
>>> abc(*(1,5,9))
(5, 1, 9)
```
<br/>

* 입력할 때 뿐만아니라, 정의할 때도 사용할 수 있습니다.
```python
>>> def abc(*args):
...     return args[1], args[0], args[2]
... 
>>> abc(*(1,5,9))
(5, 1, 9)
```
<br/>

* 정의할때 위치인자 언패킹을 사용하면, 인자를 받는 수에 제한이 없어집니다.
```python
>>> abc(*(1,5,9,11))
(5, 1, 9)
>>> abc(*(1,5,9,11,33,55,77))
(5, 1, 9)
```
<br/>

* 함수를 정의할때, 고정 인자와 위치인자 언패킹을 함께 사용할 수 있습니다.
```python
>>> def abc(a, *args):
...     return args[0], a, args[1]
... 
>>> abc(*(1,5,9))
(5, 1, 9)
```
<br/>

* 위치인자 언패킹할 인자는 반드시 뒤쪽에 위치해야합니다. 아니면 함수 사용 시 에러가 발생합니다.
```python
>>> def abc(*args, c):
...     return args[1], args[0],c
... 
>>> abc(*(1, 5, 9))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: abc() missing 1 required keyword-only argument: 'c'
>>> abc(*(1,5),9)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: abc() missing 1 required keyword-only argument: 'c'
```



<br/><br/><br/>
## 5. 키워드 인자 언패킹
* 키워드인자 언패킹은 키와 값이 있는 dictionary타입의 변수에 ** 표시를 해서 대입합니다.
```python
>> def air_line(departure, arrival, flighttime):
...     print('출발지는 : ', departure)
...     print('도착지는 : ', arrival)
...     print('비행시간은 :', flighttime)
... 
>>> myflight = {'departure':'서울', 'arrival':'LA', 'flighttime':'10시간'}
>>> air_line(**myflight)
출발지는 :  서울
도착지는 :  LA
비행시간은 : 10시간
```
<br/>

* 변수가 아닌 인자에 바로 값을 입력하고 언패킹 표시를 해줄 수 있습니다.
```python
>>> air_line(**{'departure':'서울', 'arrival':'LA', 'flighttime':'10시간'})
출발지는 :  서울
도착지는 :  LA
비행시간은 : 10시간
```
<br/>

* 함수정의할 때 키워드 인자 언패킹을 이용할 수 있습니다.
```python
>>> def air_line(**kwargs):
...     print('출발지는 : ', kwargs['departure'])
...     print('도착지는 : ', kwargs['arrival'])
...     print('비행시간은 : ', kwargs['flighttime'])
... 
>>> air_line(**{'departure':'서울', 'arrival':'프라하', 'flighttime':'15시간'})
출발지는 :  서울
도착지는 :  프라하
비행시간은 :  15시간
```
<br/>

* 함수를 정의할때, 고정 인자와 키워드 인자 언패킹을 함께 사용할 수 있습니다.
* 함께 쓸 경우 키워드 인자 언패킹을 뒤쪽에 사용해야 합니다.
```python
>>> def air_line(departure, **kwargs):
...     print('출발지는 : ', departure)
...     print('도착지는 : ', kwargs['arrival'])
...     print('비행시간은 : ', kwargs['flighttime'])
... 
>>> air_line(**{'departure':'인천', 'arrival':'멜버른', 'flighttime':'11시간'})
출발지는 :  인천
도착지는 :  멜버른
비행시간은 :  11시간
```


<br/><br/><br/>
> 참고 : [wikidocs(파이썬 - 기본을 갈고 닦자!)](https://wikidocs.net/16053)
