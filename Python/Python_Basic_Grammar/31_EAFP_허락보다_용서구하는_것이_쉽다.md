# 📝 31 EAFP - 허락보다 용서구하는 것이 쉽다.

## 1. EAFP VS LBYL
* EAFP - 'It's **E**asier to **A**sk **F**orgiveness than **P**ermission' 의 줄임말 입니다. 허락보다 용서구하는 것이 쉽다.
* LBYL - '**L**ook **B**efore **Y**ou **L**eap'의 줄임말입니다. 도약하기전에 봐라. 라는 뜻입니다.
* LBYL 스타일은 어떤 것을 실행하기전에 에러가 날만한 요소들을 조건절로 검사를 하고 수행하는 스타일입니다.
* EAFP 스타일은 예외처리를 활용하여 검사를 수행하지 않고 일단 실행하고 예외처리를 진행하는 스타일입니다.
* 파이썬은 EAFP 스타일을 권장합니다.
* [PEP-0463](https://www.python.org/dev/peps/pep-0463/) (이문서가 맞는지 모르겠으나.. 검색해본 바로는...)
* EAFP는 Python에서 표준이며, 철학은 예외에 의해 가능합니다.
* 대신 오류 코드를 사용하는 예외가 없으면 오류 처리를 논리의 기본 흐름에 직접 포함시켜야합니다.
* 예외로 인해 메인 플로우가 중단되므로 예외적 인 경우가 아닌 로컬로 처리 할 수 있습니다.
* EAFP와 결합 된 예외는 오류 코드 예외를 쉽게 무시할 수 없기 때문에 우수합니다.
* 기본적으로 예외는 큰 효과가 있지만 오류 코드는 기본적으로 무음이므로 예외 EAFP- 기본 스타일은 문제를 자동으로 무시하기 어렵게 만듭니다.
<br/>

* LBYL 코딩 스타일
```python
if key in dic:
    process(dic[key])
else:
    process(None)
# As an expression:
process(dic[key] if key in dic else None)
```
<br/>

* EAFP 코딩 스타일
```python
try:
    process(dic[key])
except KeyError:
    process(None)
# As an expression:
process(dic[key] except KeyError: None)
```


<br/><br/><br/>
> 참고 : [wikidocs(파이썬 - 기본을 갈고 닦자!)](https://wikidocs.net/16062)
