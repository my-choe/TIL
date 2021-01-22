# 📝 33 List Comprehesions(리스트 표현식)

## 1. 리스트 표현식 for 문
* 다른 언어에서 잘 볼수 없었던 파이썬만의 독특하고 편리한 문법입니다.
* List 또는 set, dictionary 안에서 for문과 if문을 사용하여 컬렉션 내부의 원소들을 구성시킬 수 있습니다.
<br/>

* REPL에서 확인해봅니다.
* words는 문장을 split하여 만든 단어 리스트 입니다.
* 단어 리스트를 새로운 리스트의 for문을 돌아 길이를 구해 다른 리스트를 생성하였습니다.
* `[item for item in iterable]` 이 기본 형식입니다.
```python
>>> words = "나는 파이썬을 공부하고 있습니다. 파이썬은 무척 심플하고 명료합니다.".split()
>>> words
['나는', '파이썬을', '공부하고', '있습니다.', '파이썬은', '무척', '심플하고', '명료합니다.']
>>> [len(word) for word in words]
[2, 4, 4, 5, 4, 2, 4, 6]
```
<br/>

* 리스트 표현식을 사용하지 않으면 아래와 같은 코드로 작성되어져야합니다.
* 아래의 코드가 위에 예 처럼 한줄로 간편하게 표현됩니다.
```python
>>> length = []
>>> for word in words:
...     length.append(len(word))
... 
>>> length
[2, 4, 4, 5, 4, 2, 4, 6]
```

<br/><br/><br/>
## 2. 리스트 표현식 if 문에 의한 필터링
* 리스트 표현식을 단순히 for 문만이 아닌 if문을 더해서 이루어질 원소를 필터링 할 수 있습니다.
* `[item for item in iterable if 조건(item)]` 이 기본 형식입니다.
```python
>>> [len(word) for word in words if len(word) > 3]
[4, 4, 5, 4, 4, 6]
```


<br/><br/><br/>
> 참고 : [wikidocs(파이썬 - 기본을 갈고 닦자!)](https://wikidocs.net/16064)
