# Virtualenv

## 0. Python 설치
* [https://www.python.org/downloads/](https://www.python.org/downloads/) 설치 완료 후 환경변수 등록
<br /><br />



## 1. virtualenv란?
### ✔ virtualenv 정의
  * 파이썬에서 제공하는 가상환경 관리 패키지 'virtualenv'는 가상환경 기능을 통해 **프로젝트마다 패키지를 따로 관리**할 수 있음

### ✔ virtualenv 필요성
  * 한 컴퓨터에서 여러 개의 프로젝트 관리 시 라이브러리 버전이 각자 다르다면?<br />
    → 프로젝트마다 환경을 분리하지 않고 라이브러리 사용 시 충돌 발생 가능성 있음<br />
    → 프로젝트별 각각 다른 환경을 만들어 패키지를 따로 관리할 필요성이 높아짐<br />
  
  * 라이브러리가 특정 프로젝트에서만 사용되는 경우, 해당 라이브러리만 포함시켜 배포할 수 있음<br />
    → 가상환경에서 라이브러리를 추가하면 추가된 라이브러리는 그 가상환경에서만 사용됨
    
  * 필요한 라이브러리가 있을 때 바로바로 다른 폴더에 설치하여 쓸 수 있고, <br />
  개인 폴더에 설치하는 것이기 때문에 관리 권한이 필요하지 않음
  
  * 각 프로젝트마다 가상환경을 만들어두면 추후 프로젝트 배포 시 환경 전체를 압축하여 배포 가능<br />
    (Check! 프로젝트를 받는 사람은 같은 버전의 파이썬이 설치되어 있어야 함)
    
    
    
<br /><br />
## 2. virtualenv설치(Windows10 기준)
### ✔ 설치에 앞서
  * **pip**(Package Installer for Python)
    * 라이브러리 설치 프로그램인 pip는 PyPI(Python Package Index) 저장소로부터 파이썬 패키지를 받아 설치하는 **패키지 관리도구**
    * Ruby에서의 RubyGems, PHP의 Packagist, Perl의 CPAN, Node.js의 NPM과 비슷함

  * pip와 virtualenv는 일반적으로 **Global**(전역)에 설치되어야하는 유일한 패키지
  * pip는 python 설치 시 **환경변수**(path)를 올바르게 설정하였다면 cmd에서 `pip` 입력 시 실행됨
  * pip 버전이 낮다는 메시지 표출 시 업그레이드 진행
    ```console
    python -m pip install --upgrade pip
    ```
    
### ✔ virtualenv 설치
* ⚙ **python2.x**
```console
pip install virtualenv
```


* ⚙ **python3.x**
```console
pip3 install virtualenv
```


* ⚙ **가상환경생성 명령어 도움말**
```console
mkvirtualenv --help
```
* virtualenv는 pip의 복사본을 수반하고 있기에 사실상 필요한 것은 virtualenv뿐
* 만일 오류가 난다면 기존 파이썬 설치 폴더에서 DLLs 폴더를 새로 생성한 가상환경 폴더로 복사<br />
  → DLLs 폴더가 없을 때 오류가 생기는 경우 있음
  
  
  
<br /><br />
## 3. virtualenv를 이용한 가상환경 만들기
* 파이썬 버전에 따라 아래 명령어 실행 시 아무 패키지도 포함되지 않은 빈 가상환경이 생성됨
* ⚙ **python2.x 가상환경 생성 명령어**
```console
virtualenv env_name
```

* ⚙ **python3.x 가상환경 생성 명령어**
```console
virtualenv -p python3 env_name
```

* ⚙ **추가 명령어**
  * 기본 파이썬에 설치되어 있는 `site-packages`를 모두 가져오기 위해서는 아래 명령어 실행(독립된 파이썬 환경 생성)
```console
virtualenv -system-site-packages -p python3 env_name
```

* 💥  **가상환경 생성 시 주의점**
  * `site-packages`를 설치하기 위한 명령어의 경우 `pip install`로 설치하는 모든 패키지들은 기본 파이썬에도 반영되므로 주의필요
  * 위의 명령어들을 통해 가상환경을 만들게 되면, 가상환경을 담은 디렉토리가 **현재 내가 터미널상에 위치하고 있는 디렉토리 내부에 생성됨**.
  (즉, 현재 내가 `/home/mychoe`에 위치해 있었다면, 가상환경이 담긴 디렉토리 경로는 `/home/mychoe/env_name`이 된다.)
  
  
  
  
<br /><br />
## 4. 가상환경 실행/종료
* ⚙ **가상환경 실행 명령어**
```console
(Linux) source /home/mychoe/env_name/bin/active
(Windows) call /home/mychoe/env_name/Scripts/active
```
→ 해당 명령어 실행 후 다음부터는 쉘 명령창 앞부분에 `(env_name)`이 따라다니는데 이는 `/home/mychoe/env_name` 가상환경 안에 있음을 뜻함<br/>
→ 이 상태에서는 콘솔에서 python이나 pip를 호출하더라도, 기존 python과 pip가 아닌 실행된 가상환경의 python과 pip가 호출됨<br/>
→ 따라서 가상환경에서 라이브러리 설치 및 스크립트 실행 시, 그 환경에만 영향 있음

* ⚙ **가상환경 종료 명령어**
```console
(Linux) source /home/mychoe/env_name/bin/deactive
(Windows) call /home/mychoe/env_name/Scripts/deactive
```
→ 해당 명령어 실행 후 쉘 명령창 앞부분의 `(env_name)`이 사라짐




<br /><br />
## 5. 패키지 설치(예시)
* **설치할 가상환경을 active한 후 pip를 이용해 필요한 패키지 설치**
```console
pip install Django
pip install pyinstaller
```

* **패키지 삭제(예시)**
```console
pip uninstall Django
pip uninstall pyinstaller
```




<br /><br />
## 6. 가상환경 설치 패키지 확인
* **가상환경 별 설치된 패키지를 쉽게 확인하기 위함**
```console
pip freeze  (패키지 목록 확인 가능)
pip freeze > requirements.txt    (패키지목록을 텍스트 파일로도 저장 가능)
```
→ 위의 명령어 수행 시 패키지 목록이 모두 `requirements.txt` 파일에 저장되며, 이를 새로운 패키지 설치에 이용할 수도 있음
```console
pip install -r requirements.txt
```



<br /><br />
## 7. 이클립스 PyDev 환경에서 가상환경 사용하기
1. 이클립스 실행 후 `Help` > `Eclipse Marketplace` > `PyDev` 검색 > install<br/><br/>
2. `Windows` > `Preferences` > `PyDev` > `Interpreters` > `Python Interpreter` > `Browse for python/pypy exe`<br/>
![image01](https://user-images.githubusercontent.com/54934681/103770222-fe684800-5068-11eb-9dd2-41e59289e884.png)
<br/>인터프리터명 입력 > 실행할 파이썬.exe 선택 > `OK` > `Apply and Close`<br/><br/>
3. `New` > `PyDev Project` > 앞서 생성한 Interpreter 선택<br/>
![image02](https://user-images.githubusercontent.com/54934681/103770523-7d5d8080-5069-11eb-887b-245ef44b626c.png)

