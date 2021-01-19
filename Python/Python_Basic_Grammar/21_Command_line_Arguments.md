# 📝 21 Command line Arguments
## 1. Command line Arguments
* 이전 포스트에서 module을 리팩토링 후 파이썬 스크립트 실행 시 Arguments(인자)를 줄 수 있도록합니다.
* 일단 [20. module import와 실행](https://github.com/my-choe/TIL/blob/main/Python/Python_Basic_Grammar/20_module_import%EC%99%80_%EC%8B%A4%ED%96%89.md) 마지막 코드입니다.
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


if __name__ == '__main__':
    fetch_words()
 ```
<br/>

* 첫번째로 위 코드를 아래와 같이 고쳐봅니다.
* 단어를 print하는 부분을 print_words로 분리하였습니다.
* fetch_words함수의 결과를 return하였습니다.
* 맨 아래의 실행하는 부분을 수정하였습니다.
```python
from urllib.request import urlopen


def fetch_words():
   with urlopen('https://suwoni-codelab.com/assets/story.txt') as story:
       story_words = []
       for line in story:
           line_words = line.decode('utf-8').split()
           for word in line_words:
               story_words.append(word)
   return story_words


def print_words(story_words):
   for word in story_words:
       print(word)


if __name__ == '__main__':
   words = fetch_words()
   print_words(words)
```
<br/>

* 다시 두번째로 맨 아래의 실행부분을 main() 함수로 묶겠습니다.
```python
from urllib.request import urlopen


def fetch_words():
    with urlopen('https://suwoni-codelab.com/assets/story.txt') as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_words(story_words):
    for word in story_words:
        print(word)


def main():
    words = fetch_words()
    print_words(words)


if __name__ == '__main__':
    main()
```
<br/>

* 위 내용을 저장하고, REPL을 실행해봅니다.
* 위 파일에서 3개의 함수로 분리하였습니다.
* import 할 때도 여러개의 함수를 한 번에 imort해보겠습니다.
```python
>>> from words import (fetch_words, print_words)
>>> print_words(fetch_words())
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

* 한번에 모든 함수를 import 하기위해서는 `*` 표시를 사용합니다.
* REPL에서 가볍게 사용할때 만 권장하고, 프로그램 작성시에는 `*`을 사용하는 것을 피해야합니다. 
* 쓰지 않는 많은 모듈을 불러오는 것은 자칫 네임스페이스 충돌등 여러 문제를 야기할 수 있습니다.
```python
>>> from words import *
```
<br/>

* 함수를 3개로 분리함으로써 다른 용도로 함수를 활용할 수 있습니다.
```python
>>> print_words(['가나다', '다라마'])
가나다
다라마
>>> print_words("가나다라마바사")
가
나
다
라
마
바
사
```
<br/>

* print_words함수가 이렇듯 원래의 목적과 다른 용도로도 사용할 수 있으므로, 함수명칭을 좀 더 일반적인 명칭으로 변경하고 파라미터명칭도 변경하겠습니다.
```python
...생략
def print_items(items):
    for item in items:
        print(item)


def main():
    words = fetch_words()
    print_items(words)
... 생략
```
<br/>

* 하드코딩으로 입력된 url을 python script로 실행 시 인자로 받아서 처리하겠습니다.
* python sciprt실행시 인자를 받기 위해서는 `sys`모듈을 import해야합니다.
* 파일 상단에 아래 코드를 추가합니다.
```python
import sys
...생략
```
<br/>

* 그리고 `fetch_words`함수와 `main`함수 그리고 마지막 실행구문을 아래와 같이 수정해줍니다.
* `fetch_words`함수에서 파라미터에 url을 추가하고, 하드코딩된 url부분을 파라미터 url로 변경하였습니다.
* main함수에서는 `sys.argv[1]`을 통해서 script실행 시 인자를 받습니다.
* `sys.argv[0]`은 모듈의 파일명이 넘어옵니다.
```python
... 생략
def fetch_words(url):
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words
... 생략
def main(url):
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])
```
<br/>

* 아래와 같이 파이썬 스크립트를 콘솔창에서 실행해봅니다.
```python
$ python words.py https://suwoni-codelab.com/assets/story.txt
```
<br/>

* 최종 코드입니다.
```python
from urllib.request import urlopen

import sys


def fetch_words(url):
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    for item in items:
        print(item)


def main(url):
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])
```



<br/><br/><br/>
> 참고 : [wikidocs(파이썬 - 기본을 갈고 닦자!)](https://wikidocs.net/16049)
