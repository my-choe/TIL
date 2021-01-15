# 📝 06_String

## 1. 문자열(str)
* String은 글자의 Unicode 코드로 이루어진 불변한 순서있는 집합입니다.
* "" (쌍따옴표), ''(작은따옴표) 모두 사용가능합니다. 자바스크립트와 같습니다.
* "' 와같이 혼용할 수 없습니다.
* REPL 에서 확인합니다.
```python
>>> "쌍따옴표 문자열"
'쌍따옴표 문자열'
>>> '작은따옴표 문자열'
'작은따옴표 문자열'
>>> "혼용하면 에러발생'
File "<stdin>", line 1
  "혼용하면 에러발생'
             ^
SyntaxError: EOL while scanning string literal
```
<br/>

* 큰따옴표 안에 작은따옴표는 들어갈 수 있고, 반대로 큰따옴표 안에 작은따옴표 들어갈 수 있습니다.
```python
>>> "It's a good thing"
"It's a good thing"
>>> '"Yes",he said,"I agree!"'
'"Yes",he said,"I agree!"'
```
<br/>

* 문자열을 나란히 두개 입력하면 문자열이 합쳐집니다.
* **이로 인해 list에서 문자열을 입력할 때 실수할 여지가 있습니다. 콤마가 없으면 에러나지 않고 문자열이 합쳐집니다.**
```python
>>> "abc" "def"
'abcdef'
>>> "abc"     "def"
'abcdef'
>>> ["abc"
... "def",
... "ghi"]
['abcdef', 'ghi']
```

<br/><br/><br/>
## 2. 멀티라인 입력
* 여러열 문자를 입력할때는 """ 큰따옴표 3개나, ''' 작은따옴표 3개를 입력합니다.
* \n 으로 표시되는 부분이 newline문자로 열을 바꿔주는 문자입니다.
* 시스템상에서 기본 newline문자는 Mac과 Linux `\n` 이지만, Windows에서는 `\r\n` 입니다.
* 하지만 Windows에서도 newline문자로 `\n`이 찍히며, REPL에서도 정상적으로 라인이 바뀝니다.
```python
>>> """ 이것은
... 멀티라인
... 입력입니다."""
' 이것은\n멀티라인\n입력입니다.'
>>> ''' 이것도
... 멀티라인
... 입력입니다.'''
' 이것도\n멀티라인\n입력입니다.'
```

<br/><br/><br/>
## 3. 이스케이프 문자
* 이스케이프 문자란 직접 입력할 수 없는 일부 문자를 문자열에 포함시킬 수 있는 특수 문자를 지칭합니다.
* `\` 역슬래시가 파이썬의 이스케이프 문자
![capture](https://user-images.githubusercontent.com/54934681/104737309-6a446200-5787-11eb-8dff-4f742308917d.jpg)

* 예제
```python
>>> a = "이스케이프 문자 \n 라인이 바뀜 \\ 쌍따옴표를 또 쓰기 \"\" "
>>> print(a)
이스케이프 문자 
라인이 바뀜 \ 쌍따옴표를 또 쓰기 "" 
```

<br/><br/><br/>
## 3. 이스케이프 문자
* 이스케이프 문자란 직접 입력할 수 없는 일부 문자를 문자열에 포함시킬 수 있는 특수 문자를 지칭합니다.
* `\` 역슬래시가 파이썬의 이스케이프 문자
![capture](https://user-images.githubusercontent.com/54934681/104737309-6a446200-5787-11eb-8dff-4f742308917d.jpg)

* 예제
```python
>>> a = "이스케이프 문자 \n 라인이 바뀜 \\ 쌍따옴표를 또 쓰기 \"\" "
>>> print(a)
이스케이프 문자 
라인이 바뀜 \ 쌍따옴표를 또 쓰기 "" 
```
<br/>

* 이스케이프 문자를 통해 유니코드 문자열을 입력할 수 있습니다.
```python
>>> 'Vi er s\u00e5 glad for \u00e5 h\u00f8re og l\u00e6re om Python!'
'Vi er så glad for å høre og lære om Python!'
```
<br/>

* 유니코드 문자열을 16진수로 바로 입력할 수 있습니다.
```python
>>> '\xe5'
'å'
```
<br/>

* 반대로 이스케이프 문자를 막는 raw문자열을 문자열 앞에 `r` 을 붙여 만들 수 있습니다.
```python
>>> a = r"이스케이프 문자 \n 라인이 바뀜 \\ 쌍따옴표를 또 쓰기 \"\" "
>>> print(a)
이스케이프 문자 \n 라인이 바뀜 \\ 쌍따옴표를 또 쓰기 \"\" 
```




<br/><br/><br/>
## 4. 변환
* int, float -> str 변환
```python
>>> str(396)
'396'
>>> str(5.52)
'5.52'
>>> str(6.02e10)
'60200000000.0'
>>> str(6.02e20)
'6.02e+20'
```



<br/><br/><br/>
## 5. 컬렉션 접근
* String도 List와 같은 Collection 처럼 접근할 수 있습니다.
* `[문자열인덱스 숫자]` 형식으로 접근됩니다.
```python
>> s = 'abcdef'
>>> s[3]
'd' 
```





<br/><br/><br/>
## 6. String 여러가지 메소드
* 문자열을 다양하게 변환하며 활용하게 됩니다.
* 문자열을 type함수를 실행해보면 아래와같이 나옵니다.
```python
>>> type("문자열")
<class 'str'>
```
<br/>

* help 함수로 str에서 다양하게 활용할 수있는 메소드들 리스트를 볼수 있습니다.
* q 버튼으로 빠져나올 수 있습니다.
```python
help(str)
```
<br/>

* 몇가지만 살펴보겠습니다.
* join : 문자열을 합치는데 사용합니다. 구분자가 앞에서 사용되어집니다.
```python
>>> ','.join(['a','b','cde'])
'a,b,cde'
```
<br/>

* split : join과 반대입니다. 문자열을 구분자로 나누어 리스트로 반환합니다.
```python
>>> 'a,b,cde'.split(',')
['a', 'b', 'cde']
```
<br/>

* partition : 구분자로 나누어 tuple형으로 반환합니다.
```python
>>> departure, _, arrival = "Seattle-Seoul".partition('-')
>>> departure
'Seattle'
>>> _
'-'
>>> arrival
'Seoul'
```
<br/>

* format : 문자를 다양한 형태로 포맷팅하는데 사용합니다.
* 인덱스 형으로 format을 사용하는 예제입니다.
```python
>>> "Name: {}, Age:{}".format("철수", 13)
'Name: 철수, Age: 13'
>>> "Name: {0}, Age: {1}".format("영희", 15)
'Name: 영희, Age: 15'
>>> "Name: {0}, Age: {1}: {0}의 나이가 {1}".format("민호", 17)
'Name: 민호, Age: 17: 민호의 나이가 17'
```
<br/>

* 키워드 형으로 format을 사용하는 예제입니다.
```python
>>> "Name: {name}, Age: {age}: {name}의 나이가 {age}".format(age=19, name='재석')
'Name: 재석, Age: 19: 재석의 나이가 19'
```
<br/>

* 리스트를 넘기고 index로 접근하는 format예제입니다.
```python
>>> pos = [12.5, 35, 90]
>>> "A의 좌표는 x = {p[0]}, y = {p[1]}, z={p[2]}".format(p=pos)
'A의 좌표는 x = 12.5, y = 35, z = 90'
```
<br/>

* module을 넘겨 활용하는 format 예제입니다.
```python
>>> import math
>>> '수학에서의 파이= {m.pi}'.format(m=math)
'수학에서 파이= 3.141592653589793'
```
<br/>

* format을 통해 넘겨받은 데이터를 변형할수도 있습니다.
* 소수점 3자리에서 끊었습니다.
* [변형의 예는 좀 더 많습니다.](https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3)
```python
>>> '수학에서 파이= {m.pi:.3f}'.format(m=math)
'수학에서 파이= 3.142'
```
<br/>

* capitalize: 첫 글자 대문자 나머지 문자 소문자로 변환합니다.
* a가 바뀌지는 않습니다.
```python
>>> a = "abcDef"
>>> a.capitalize()
'Abcdef'
>>> a
'abcDef'
```
<br/>

* strip : 좌우 공백을 제거 합니다.
```python
>>> s = "  abc   "
>>> s.strip()
'abc'
>>> s
'  abc   '
```
<br/>

* len : Str함수는 아니며, 일반 내장함수입니다. 문자열 길이 또는 컬렉션형의 길이를 나타냅니다.
```python
>>> len("abcd12345abcdefg")
16
```



<br/><br/><br/>
> 참고 : [wikidocs(파이썬 - 기본을 갈고 닦자!)](https://wikidocs.net/16034)
