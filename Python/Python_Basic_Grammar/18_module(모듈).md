# 📝 18 module(모듈)
## 1. Module(모듈) 이란?
* 다른 언어에서 Module이란 명확하지 않고 약간은 추상적인 개념인것 같습니다. 기능적으로 나뉘어지는 프로그램, 라이브러리와 비슷하기도 하고...
* 파이썬에서의 모듈은 보다 명확합니다. 파이썬코드로 이루어진 파일입니다. 함수나 변수, 클래스등의 코드가 들어가 있습니다.
* 이렇게 파일로 이루어진 모듈은 다른 파이썬 파일 그리고 다른 실행환경에서 import하여 사용할 수 있습니다.
* 이전 포스트에서는 REPL만으로 실행했지만, 이제는 editor가 필요합니다.
* 추천 에디터 : [PyCharm](https://www.jetbrains.com/pycharm/download/), [Visual Studio Code](https://code.visualstudio.com/) 등이 있습니다.

<br/><br/><br/>
## 2. 간단한 Module(모듈) 작성
* 에디터에서 아래의 코드를 입력하고, 원하는 위치에 저장합니다. 저는 `words.py` 저장하였습니다.
```python
from urllib.request import urlopen

with urlopen('http://blogattach.naver.net/ca5fd665752b2ef2dd3a506a5db3c1b01343b85ee2/20180618_274_blogfile/topspin1278_1529278974170_Fa2424_txt/story.txt') as story:
  story_words = []
  for line in story:
      line_words = line.decode('utf-8').split()
      for word in line_words:
          story_words.append(word)

for word in story_words:
  print(word)
 ```
<br/>

* 터미널 또는 명령어프롬프트로 파일이 저장된 위치로 들어간 후 아래의 명령어를 입력합니다.

```python
$ python words.py
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

* 이번에는 REPL로 진입해보겠습니다. python 명령어만 입력합니다.
* REPL진입 후 words.py 모듈을 아래와 같이 import 합니다.
* import할때 확장자는 빼고 파일명만 적습니다.
* import 하자마자 코드가 바로 샐힝될 것입니다.
```python
>>> import words
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
* 이렇게 import 하자마자 바로 실행이 필요한 경우도 있겠지만, 필요할 때 부품으로 사용하기에는 부적절합니다.
* 그래서 function, class등을 이용합니다. 다음 포스팅에서 다루겠습니다.



<br/><br/><br/>
> 참고 : [wikidocs(파이썬 - 기본을 갈고 닦자!)](https://wikidocs.net/16046)
