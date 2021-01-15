# 📝 07_Bytes
* bytes는 유니코드가 아닌 문자열을 사용하는 것과 유사함.
* bytes는 원시 이진 데이터로 사용되어지거나 1바이트 문자로 고정을 위해 사용되어집니다.
* bytes HTTP 응답과 같은 파일과 네트워크 리소스는 바이트 스트림으로 전송되기 때문에 이해하는 것이 중요합니다.
* 반면에 우리는 유니 코드 문자열의 편의성을 선호합니다. 그렇기에 상호변환을 하는 경우가 많습니다.
<br/>

## 1. bytes 사용
* 사용방법은 문자열 앞에 `b`를 입력합니다.
REPL을 사용해보겠습니다.
```python
>>> b = b'abcde'
>>> b
b'abcde'
>>> print(b)
b'abcde'
>>> type(b)
<class 'bytes'>
```
<br/>

* bytes는 split을 하여도 내부 원소는 bytes형태가 됩니다.
```python
>>> s = b'abc def ghi'
>>> s.split()
[b'abc', b'def', b'ghi']
```


<br/><br/><br/>
## 2. str to bytes, bytes to str
* 문자열을 encode하면 byte형이 되고 byte형을 decode하면 문자열이 됩니다.
```python
>>> s = 'Vi er så glad for å høre og lære om Python!'
>>> b = s.encode('utf-8')
>>> b
b'Vi er s\xc3\xa5 glad for \xc3\xa5 h\xc3\xb8re og l\xc3\xa6re om Python!'
>>> b.decode('utf-8')
'Vi er så glad for å høre og lære om Python!'
```




<br/><br/><br/>
> 참고 : [wikidocs(파이썬 - 기본을 갈고 닦자!)](https://wikidocs.net/16035)
