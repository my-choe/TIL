# 📝 22 Docstring(문서화)
* 파이썬을 접하면서, 여러가지로 멋지다라고 생각했던 것 중에 하나
* docstring을 작성하면, 프로그래밍의 속성으로 접근할수 있음.

## 1. docstring 이란
* docstring은 모듈, 함수, 클래스 또는 메소드 정의의 첫 번째 명령문으로 발생하는 문자열 리터럴
* 이러한 docstring은 해당 객체의 **doc** 특수 속성으로 변환됨
* Docstring convention - https://www.python.org/dev/peps/pep-0257/


<br/><br/><br/>
## 2. docstring 작성
* Module 첫번째 줄, 함수 선언 후 내부 바로 아랫줄 또는 클래스 선언 후 내부 바로 아랫줄에 큰따옴표 3개나 작은 따옴표 3개로 작성하면됩니다.
 ```python
 class CustomClass:
"""
클래스의 문서화 내용을 입력합니다.    
"""

    def custom_function(param):
        '''
        함수의 문서화 내용을 입력합니다.
        '''
        ... 코드  ...

 ```
<br/>

* Python(파이썬) 기본 - [20. module import와 실행](https://github.com/my-choe/TIL/blob/main/Python/Python_Basic_Grammar/20_module_import%EC%99%80_%EC%8B%A4%ED%96%89.md)에서 작성했던 예제파일에 docstring을 추가해보겠습니다.
```python
... 생략
def fetch_words(url):
    """
    url주소에서 파일을 가져와 단어 리스트를 반환합니다.
    :param url: 불러올 url
    :return:
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words
... 생략
```
<br/>

* REPL을 실행하고, `words.py`에서 `fetch_words` 함수를 import합니다.
* `help`함수에서 `fetch_words` 함수의 docstring 내용을 확인할 수 있습니다.
```python
>>> from words import fetch_words
>>> help(fetch_words)
```
<br/>

* `fetch_words` 함수 속성으로 `__doc__` 속성이 추가됩니다.
```python
>>> from words import fetch_words
>>> fetch_words.__doc__
'\n    url주소에서 파일을 가져와 단어 리스트를 반환합니다.\n    :param url: 불러올 url\n    :return:\n    '
```
<br/>

* 이번에는 Module최상단과 나머지 함수 모두 docstring을 다음과 같이 작성해봅니다.
```python
"""
    URL로부터 파일을 가져와 단어를 print 함.
Usage:

    python words.py <URL>
"""

from urllib.request import urlopen

import sys


def fetch_words(url):
    """
    url주소에서 파일을 가져와 단어 리스트를 반환합니다.
    :param url: 불러올 url
    :return:
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """
    items를 print
    :param items: 
    :return: 
    """
    for item in items:
        print(item)


def main(url):
    '''
    url을 받아 단어를 print 함
    :param url: url
    :return:
    '''
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])
```
<br/>

* 다시 REPL을 재실행하고, 모듈 전체를 import 합니다.
* module의 docstring은 물론 내부 모든 함수의 docstring을 확인할 수 있습니다.
```python
>>> import words
>>> help(words)
```

<br/><br/><br/>
> 참고 : [wikidocs(파이썬 - 기본을 갈고 닦자!)](https://wikidocs.net/16050)
