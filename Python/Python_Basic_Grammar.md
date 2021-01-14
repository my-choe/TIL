# 🛠 Python Basic Grammer 파이썬 기초문법
## ✔ 입력과 출력
### 🌠출력하기
* `print()` : 괄호 안에 값을 넣으면 해당 값을 출력해주는 함수
```python
print('hello world') # hello world
print(1, 2, 3)  # 1 2 3
print(1 + 2)  # 3
```
### 🌠입력하기
* `input()` : 사용자에게 값을 입력 받아 컴퓨터가 사용할 수 있게 하는 함수
```python
input('이름을 입력하세요: ')   # 콘솔에 커서가 생기며 입력 받음
age = input('당신의 나이는? : ')  # 나이를 입력받아 age변수에 넣음. 콘솔에 age 입력 시 → 사용자가 입력한 값 표출
```

<br/><br/>
## ✔ 변수와 이름
### 🌠변수와 이름
* 변수 네이밍 규칙
    * `글자, 밑줄문자 가능` : my_int = 1
    * `대,소문자 구분` : python = 1, PYTHON = 2
    * `한글 가능` : 파이썬 = 20  
    * `특수문자 가능` : ☆ = 7  // 유니코드 사용하기 때문에 가능(한글도 마찬가지)
    * `변수명은 숫자로 시작할 수 없음`
    * `띄어쓰기 불가`
```python
my_int = 614
print(my_int)  # 614
my_int + 3   # 617
```


<br/><br/>
## ✔ 프로그램의 기본재료
* `type()` : 변수의 타입을 알 수 있는 함수
```python
my_int = 1
type(my_int)  # <class 'int'>
```
### 🌠숫자형, 문자형, 불린
* 숫자형(Numeric)
    * 정수형
    * 실수형
* 문자형(String)
    * 큰 따옴표 ("")
    * 작은 따옴표 ('')
    * 둘을 섞어쓸 수 없고 짝을 맞춰 써야 함
* 불린(Boolean)
    * 참(True)
    * 거짓(False)
    
    
### 🌠리스트, 튜플, 딕셔너리  ==> `컨테이너(여러 개 값을 저장하는 자료형)`
* 리스트(List)
    * 값을 나열할 수 있음. 값 변경 가능
    * `my_list = []`
    * `my_list = [1,2 3]`
 * 튜플(Tuple)
    * List와 비슷하나 값 변경 불가능
 * 딕셔너리(Dictionary)
    * 키-값 형태
    * `{key1 : val1, ...}`
    
 
### 🌠자료형 변환하기
* `int()` , `str()`, `flaot()` 등 자료의 형태를 변환하는 함수
```python
my_int = 1
type(my_int)  # <class 'int'>
type(str(my_int))  // <class 'str'>
my_str = "coding"
list(coding) # ['c', 'o', 'd', 'i', 'n', 'g']
```

<br/><br/>
## ✔ 주석
### 🌠주석
* #을 사용함
```python
print(2 + 3)  # 계산 결과 출력
```


<br/><br/>
## ✔ 문자열
### 🌠문자열
* 문자열 예시
```python
my_str = "바닐라라떼"
print(my_str) # 바닐라라떼
type(my_str) # <class 'str'>
```


* 큰(또는 작은) 따옴표 세 개 :  여러 줄을 하나의 변수에 저장
```python
my_str = """콜드브루라떼
아메리카노
카페라떼
"""
# 콜드브루라떼\n아메리카노\n카페라떼
```

### 🌠포맷팅
* 포맷팅 : %(퍼센트 연산자)를 사용하여 문자열을 좀 더 잘 표현하는 함수
* %S: 문자열 / %d: 정수형 / %f: 실수형 등
```python
my_str = "My name is %s' % 'MY-CHOE' # My name is MY-CHOE
```

### 🌠format()
* 좀 더 파이썬스러운 포맷팅
```python
"My name is %s' % 'MY-CHOE' # My name is MY-CHOE
"My name is {}".format("myc") # My name is myc
'{} X {} = {}'.format(2, 3, 2*3)  # 2 x 3 = 6
'{1} X {0} = {2}'.format(2, 3, 2*3)  # 3 x 2 = 6  << {}순서가 바뀜
```


### 🌠인덱싱
* index : 주소, 위치
```python
my_song = "개인주의"
# [0] : 개
# [1] : 인
# [2] : 주
# [3] : 의
my_song[3]   # 의
# [-1] : 의
# [-2] : 주
# [-3] : 인
# [-4] : 개
my_sone[-2]   # 주
```
* 마이너스 주소 : 뒤에서부터 시작. -1부터 시작


### 🌠슬라이싱
* 인덱싱과는 다르게 여러 개 뽑아오는 것
```python
my_str = "python"
# my_str[0] : p
# my_str[1] : y
# my_str[2] : t
# my_str[3] : h
# my_str[4] : o
# my_str[5] : n
my_str[1:4] # yth
my_str[:3] # pyt (처음부터 3까지)
my_str[2:] # thon (2부터 끝까지)

```


### 🌠메서드
* `string.split()` :   문자열을 기준에 따라 잘라주는 함수. String만 사용 가능
```python
my_str = "오늘의 할 일"
my_str.split()  # ['오늘의', '할', '일']  (공백 기준으로 잘라줌)
```


### 🌠독스트링(Docstring)
* 문자열을 쓸 때 큰(작은) 따옴표를 세 개씩 쓰는 것 자체를 주석으로 쓸 수 있도록 하는 함수
```python
# 이것은 주석입니다
""" 이것도 주석입니다"""  # 함수 설명할 때 주로 사용
```

### 🌠end, 이스케이프 코드
* end
      * `print('', end="")` : 출력 끝을 지정할 수 있는 함수
``` python
print('파이썬', end="/") # 파이썬/
print("안녕", end='하세요') # 안녕하세요
```

* Escape code
      * 특정 기능을 수행하는 문자의 조합
      * `\n` : 엔터
      * `\t' : 탭 기능
      * ` ; ` : 한 줄이 끝났다는 것을 알려주는 의미(여러 개의 명령어가 아닌 이상 권장하지 않음)
``` python
print("안녕\n하세요') 
# 안녕
# 하세요

print("미운", end='\t'); print("오리", end='\t') # 미운   오리
```



<br/><br/>
## ✔ 리스트
### 🌠리스트
### 🌠값 추가하기
### 🌠인덱싱, 슬라이싱
### 🌠메서드



<br/><br/>
## ✔ 튜플
### 🌠튜플
### 🌠패킹, 언패킹



<br/><br/>
## ✔ for
### 🌠for
### 🌠range()
### 🌠for x 2
### 🌠컴프리헨션



<br/><br/>
## ✔ 연산자
### 🌠할당
### 🌠산술
### 🌠%로 홀짝 구분하기
### 🌠문자열 연산자
### 🌠비교
### 🌠논리
### 🌠멤버쉽



<br/><br/>
## ✔ 조건문
### 🌠if
### 🌠else, elif



<br/><br/>
## ✔ while
### 🌠while
### 🌠continue, break



<br/><br/>
## ✔ 딕셔너리
### 🌠딕셔너리
### 🌠메서드



<br/><br/>
## ✔ 함수
### 🌠함수
### 🌠함수를 사용하는 이유
### 🌠여러 개 돌려주기



<br/><br/>
## ✔ 모듈
### 🌠모듈
### 🌠랜덤



<br/><br/>
## ✔ 객체
### 🌠객체


<br/><br/>
## ✔ 코딩스타일
### 🌠코딩스타일