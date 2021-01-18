# 📝 20 module import와 실행
## 1. module(모듈)에 function 적용
* [18. module(모듈)](https://github.com/my-choe/TIL/blob/main/Python/Python_Basic_Grammar/18_module(%EB%AA%A8%EB%93%88).md)에서 작성된 파일에 function을 적용합니다.
```python
from urllib.request import urlopen


def fetch_words():
  with urlopen('https://suwoni-codelab.com/assets/story.txt') as story:
      story_words = []
      for line in story:
          line_words = line.decode('utf-8').split()
          for word in line_words:
              story_words.append(word)

  for word in story_words:
      print(word)
```



<br/><br/><br/>
## 2. module(모듈) import와 실행
* 다시한번 REPL을 실행합니다. 실행되어 있는 상태라면, REPL을 종료하고 다시 실행합니다.
* 다시 `words.py`를 import 해봅니다.
* [18. module(모듈)](https://github.com/my-choe/TIL/blob/main/Python/Python_Basic_Grammar/18_module(%EB%AA%A8%EB%93%88).md)에서는 import하면 바로 코드가 실행됬지만, 이번에는 함수로 감쌌기 때문에 코드가 바로 실행되지 않습니다.
```python
>>> import words
```
<br/>

* 아래의 코드로 실행해봅니다.
```python
>>> words.fetch_words()
나는
Python을
공부하고
있습니다.
Python은
간편하고,
다재다능합니다.
다재다능한
Python으로
여러가지
앱
그리고
자동화
툴,
데이터
처리등을
이용해보고
싶습니다.
```
<br/>

* 모듈 전체 import가 아니라 함수만 import할 수 있습니다.
```python
from words import fetch_words
```
<br/>

* 이번에는 모듈이름을 빼고 import할때 함수명칭대로 실행합니다.
```python
>>> fetch_words()
나는
Python을
공부하고
있습니다.
Python은
간편하고,
다재다능합니다.
다재다능한
Python으로
여러가지
앱
그리고
자동화
툴,
데이터
처리등을
이용해보고
싶습니다.
```
<br/>

* 모듈을 import할때 별칭을 줄 수 있습니다.
```python
>>> from words import fetch_words as fwords
>>> fwords()
나는
Python을
공부하고
있습니다.
Python은
간편하고,
다재다능합니다.
다재다능한
Python으로
여러가지
앱
그리고
자동화
툴,
데이터
처리등을
이용해보고
싶습니다.
```


<br/><br/><br/>
## 3. `__name__`
* 파이썬 실행환경에서는 더블 언더스코어로 구분되어지는 특별한 속성이나 메소드가 존재합니다. 그 중 하나가 `__name__` 입니다.
* `__name__` : 콘솔창에서 script로 실행되는 것인지 아니면 import되는 것인지 구분이 가능하게 해줍니다.
* `words.py` 파일에 아래의 코드를 맨 아래쪽에 추가합니다.
```python
... 생략
print(__name__)
```
<br/>

* 다시 REPL을 종료하고 재실행합니다.
* words.py 모듈을 다시 import하면 `words` 라는 것이 print되는 것을 확인할 수 있습니다.
```python
>>> import words
words
```
<br/>


* 그 상태에서 다시 한번 import를 수행하면 `words`라는 단어가 나오지 않습니다.
* 모듈을 한번 import 하면 계속 메모리에 기억하고 있기때문에 다시 수행하지 않습니다.
```python
>>> import words
```
<br/>


* REPL을 종료한 후 터미널창에서 script로써 words.py를 바로 실행해보겠습니다.
* `__main__` 이 출력되는 것을 확인할 수 있습니다.
```python
$ python words.py 
__main__
```
<br/>


* 이를 이용하여 script로써 실행할 때는 함수를 실행하는 코드작성을 추가할 수 있습니다.
* `words.py` 파일아래쪽에 `print(__name__)` 코드를 제거하고 다음 내용을 추가합니다.
```python
... 생략 (print(__name__)제거)
if __name__ == '__main__':
    fetch_words()
```
* 추가 후 터미널 창에서 `python words.py` 를 실행하면 결과가 수행되고, REPL에서 import 할 경우 함수가 수행되지 않음을 확인할 수 있습니다.


<br/><br/><br/>
> 참고 : [wikidocs(파이썬 - 기본을 갈고 닦자!)](https://wikidocs.net/16048)
