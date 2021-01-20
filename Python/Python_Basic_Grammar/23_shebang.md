# 📝 23 shebang
## 1. hebang 이란?
* harp(#) + bang(!) 합성어
* Unix계열 OS(리눅스, Mac)에서 스크립트(bash, python등등) 코드 최상단에서 해당 파일을 해석해줄 인터프리터의 절대경로를 지정합니다.
```python
#!인터프리터절대경로
```
<br/>

* 프로그램의 경로는 시스템에따라 달라질 수 있습니다.
* 일반적으로 사용할 수 있는 방법이 `/usr/bin/env`파일을 이용하는 방법입니다. `#!/usr/bin/env + 언어` 식으로 입력하는 방법이 있습니다.
```python
#!/usr/bin/env bash
#!/usr/bin/env python
#!/usr/bin/env perl
#!/usr/bin/env php
```

<br/><br/><br/>
## 2. shebang 작성
* [20 module import와 실행](https://github.com/my-choe/TIL/blob/main/Python/Python_Basic_Grammar/20_module_import%EC%99%80_%EC%8B%A4%ED%96%89.md)에서 작성했던 파일로 shebang을 작성하고 실행해보겠습니다.
* 인터프리터 절대경로로 입력하는 방법입니다.
* 터미널창에 아래의 명령어를 입력하면 python실행경로가 나옵니다.
```python
$ which python
```
<br/>

* words.py 파일 최상단에 아래와 같이 입력하고 저장합니다. 아래의 경로는 저의 시스템 경로입니다.
```python
#!/Users/Blidkaga/.pyenv/shims/python
```
<br/>

* 파일은 저장했지만 한가지가 더 필요합니다. 유닉스 계열환경에서는 실행하도록 권한을 부여해야합니다.
```python
chmod +x words.py  
```
<br/>

* 실행해봅니다. python명령어 없이도 바로 실행되었습니다.
```python
./words.py https://suwoni-codelab.com/assets/story.txt
```
<br/>

* 자신의 시스템에서만 사용한다면 이렇게 사용해도 무방합니다.
* 여러사람이 한 파일을 공유할경우 `env`를 이용하여 작성하는 것이 좋습니다.
* `words.py`파일에서 `env` 경로로 작성하고 python을 추가해서 작성해줍니다.
```python
#!/usr/bin/env python
```
* 다시 위쪽예제와 똑같이 실행하면 정상적으로 실행됩니다.

<br/><br/><br/>
> 참고 : [wikidocs(파이썬 - 기본을 갈고 닦자!)](https://wikidocs.net/16051)
