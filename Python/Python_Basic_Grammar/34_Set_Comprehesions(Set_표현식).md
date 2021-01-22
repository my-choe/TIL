# 📝 34 Set Comprehesions(Set 표현식)

## 1. Set 표현식
* Set 표현식 또한 리스트 표현식과 다르지 않습니다.
* [리스트 표현식 예제](https://github.com/my-choe/TIL/blob/main/Python/Python_Basic_Grammar/33_List_Comprehesions(%EB%A6%AC%EC%8A%A4%ED%8A%B8_%ED%91%9C%ED%98%84%EC%8B%9D).md)를 Set으로 똑같이 구현하겠습니다.
<br/>

* words는 문장을 split하여 만든 단어 리스트 입니다.
* 단어 리스트를 새로운 리스트의 for문을 돌아 길이를 구해 새로운 Set을 생성하였습니다.
* 리스트와 다른점이 있다면, **Set이기 때문에 중복된 값은 제거됩니다.**
* `{item for item in iterable}` 이 기본 형식입니다.
```python
>>> words = "나는 파이썬을 공부하고 있습니다. 파이썬은 무척 심플하고 명료합니다.".split()
>>> {len(word) for word in words}
{2, 4, 5, 6}
```


<br/><br/><br/>
## 2. Set 표현식 if 필터링
* 리스트와 동일합니다.
* `{item for item in iterable if 조건(item)}` 이 기본 형식입니다.
```python
>>> {len(word) for word in words if len(word)> 3}
{4, 5, 6}
```


<br/><br/><br/>
> 참고 : [wikidocs(파이썬 - 기본을 갈고 닦자!)](https://wikidocs.net/16066)
