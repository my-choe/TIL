# 📝 35 Dictionary Comprehesions(Dictionary 표현식)

## 1. Dictionary 표현식
* Dictionary 표현식 또한 리스트 표현식과 다르지 않습니다.
* '나라:수도' 형식의 Dictionary변수를 '수도:나라'로 변경하겠습니다.
* {key표현식 : value표현식 for item in iterable} 이 기본 형식입니다.
```python
>>> country_capital = {'대한민국':'서울',
...                     '영국' :'런던',
...                     '미국' :'워싱턴',
...                     '일본' :'도쿄'}
>>> capital_country = {capital: country for country, capital in country_capital.items()}
>>> capital_country
{'서울': '대한민국', '런던': '영국', '워싱턴': '미국', '도쿄': '일본'}
```
<br/>

* dictionary는 키가 중복되면 마지막이 표시되는 것에 유의해야합니다.
```python
>>> country = ['Sweden', 'Saudi', 'USA', 'Korea', 'Swiss']
>>> { w[0] : w for w in country}
{'S': 'Swiss', 'U': 'USA', 'K': 'Korea'}
```
<br/>

* dictionary 표현식으로 간단하게 파일 목록과 파일 사이즈를 뽑아 보겠습니다.
* os패키지는 파일경로를 위해 glob패키지는 파일 목록을 가져올때 사용됩니다.
* pprint는 Dictionary 타입을 예쁘게(?) 정렬해서 보여줍니다.
```python
>>> import os
>>> import glob
>>> from pprint import pprint as pp
>>> file_info = {os.path.realpath(p) : os.stat(p).st_size for p in glob.glob('*.*')}
>>> pp(file_info)
{'/Users/Blidkaga/Documents/CodeLab/Python_Basic/a.log': 68,
 '/Users/Blidkaga/Documents/CodeLab/Python_Basic/a.txt': 0,
 '/Users/Blidkaga/Documents/CodeLab/Python_Basic/b.log': 0,
 '/Users/Blidkaga/Documents/CodeLab/Python_Basic/b.txt': 0,
 '/Users/Blidkaga/Documents/CodeLab/Python_Basic/c.log': 68,
 '/Users/Blidkaga/Documents/CodeLab/Python_Basic/err.log': 13,
 '/Users/Blidkaga/Documents/CodeLab/Python_Basic/exceptional.py': 566,
 '/Users/Blidkaga/Documents/CodeLab/Python_Basic/words.py': 910}
>>> 
```


<br/><br/><br/>
## 2. Dictionary 표현식 if 필터링
* 리스트와 동일합니다.
* `{key표현식 : value표현식 for item in iterable if 조건(item)}` 이 기본 형식입니다.
* 위쪽 예제 `file_info`변수를 활용하여, 확장자가 'log'인 파일만 파일명을 키로 사이즈를 값으로 입력하겠습니다.
* os.path.split : 전체 경로에서 경로와 파일명을 나누어 주는 메소드
* os.path.splitext: 전체경로+파일명과 확장자를 나누어주는 메소드
```python
>>> {os.path.split(key)[-1] : value for key, value in file_info.items() if os.path.splitext(key)[-1]=='.log'}
{'b.log': 0, 'err.log': 13, 'c.log': 68, 'a.log': 68}
```


<br/><br/><br/>
> 참고 : [wikidocs(파이썬 - 기본을 갈고 닦자!)](https://wikidocs.net/16067)
