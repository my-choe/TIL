# 웹 프레임워크 Django(python) 개념 정리

### 1. MVC, MTV
* **M**odel : 안전하게 데이터 저장
* **V**iew : 데이터를 적절하게 유저에게 보여줌
* **C**ontrol, **T**emplate(Django) : 사용자의 입력과 이벤트에 반응하여 Model과 View 업데이트
* 참고: http://www.essenceandartifact.com/2012/12/the-essence-of-mvc.html


### 2. Django 개념
![image](https://user-images.githubusercontent.com/54934681/107361911-6e139c00-6b1b-11eb-83df-2ef1b2a713ce.png)

1. Web Browser에서 유저가 다양한 액션을 발생시킨다.
2. 액션은 장고 서버로 들어와 URL Dispatcher가 요청을 분석한다.
3. 분석한 URL에 적합한 View로 보내준다.
4. View는 사용자 요청을 받아 어느 database에 접근해서 어떤 데이터를 가공해야 할지 알려준다.
5. Model에서 실제적인 Database와 Connection을 하고 데이터를 가져온다.
6. Database에서 Model로, Model이 다시 View에 실질적인 데이터를 보내준다.
7. View가 실제적으로 보여줄 데이터들을 Template에 적용시킨다.
8. Template이 HTML나 Javascript등 다양한 형태의 User Interface를 만들어 웹브라우저로 넘겨준다.
<br/>
➡ 이런 복잡한 과정을 거치는 이유는 특정 영역을 분리하여 효율적 개발하는 것이 목표이기 때문

<br/><br/><br/>
![image](https://user-images.githubusercontent.com/54934681/107362908-bf705b00-6b1c-11eb-8d17-d963da40766b.png)
* WSGI : 웹서버와 장고를 적절하게 결합시켜주는 역할(Gateway)
* URL RESOLUTION : 웹서버로부터 신호가 들어오게 되면 정규표현식으로 구성된 urls.py 파이썬 코드에서 받게되며 정규표현식에 맞게 특정 view로 보내준다.
* VIEW : 실질적으로 파이썬 코드를 작성할 부분. 모델로 신호를 보내기도, 모델이 보낸 데이터를 가공할수도 있다.
* MODEL : 데이터베이스로부터 어떤 데이터를 가지고 올 때 변수를 다룰 수 있다.
* TEMPLATE : View가 가공한 데이터를 사용자에게 보여주기 위해 UI작업을 할 수 있다. HTML파일 안에 로직 삽입 가능.


### 3. Project와 App
* Project 생성
    * 하나의 웹 사이트
    * $ django-admin startproject tutorial
    * ![image](https://user-images.githubusercontent.com/54934681/107364509-e039b000-6b1e-11eb-982c-0d04e67d0dab.png)
  <br/>
  
* App 생성
    * 프로젝트 내부에 다수의 app 생성
    * 다른 프로젝트의 하위 app으로 활용 가능(재사용)
    * $ ./manage.py startapp community
    * ![image](https://user-images.githubusercontent.com/54934681/107364577-f9daf780-6b1e-11eb-98d2-000ac54cc8b3.png)


### 4. settings.py
* 프로젝트 환경 설정 파일
    * DEBUG : 디버그 모드 설정
    * INSTALLED_APPS : pip로 설치한 앱(3rd party app) 또는 본인이 만든 app 추가
    * MIDDELWARE_CLASSES : request와 response 사이의 주요 기능 레이어(인증, 보안 등)
    * TEMPLATES : Django template 관련 설정, 실제 뷰(html, 변수). template파일과 관련된 변수들을 조종하는 context, template을 검색하기 위한 다양한 기능, 폴더 위치를 다루는 설정파일
    * DATABASE : 데이터베이스 엔진 연결 설정
    * STATIC_URL : 정적파일의 URL(CSS, javascript, image, etc.)


### 5. manage.py
* 프로젝트 관리 명령어 모음
* 주요 명령어
    * startapp : 앱 생성
    * runserver : 서버 실행
    * createsuperuser : 관리자 생성
    * makemigration app : app의 모델 변경 사항 체크
    * migrate : 변경사항을 DB에 반영
    * shell : 쉘을 통해 데이터 확인
    * collectstatic : static 파일을 한 곳에 모음
    * ex) ./manage.py runserver 0.0.0.0:8080



<br/><br/><br/>

> 참고 : [인프런 - Django 초보가이드 : 웹 프레임워크 Django(python) 개념 정리](https://www.inflearn.com/course/django-%EC%B4%88%EB%B3%B4-%EA%B0%80%EC%9D%B4%EB%93%9C-%EC%8B%A4%EC%8A%B5%EC%9D%84-%ED%86%B5%ED%95%B4-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-%EC%9E%A5%EA%B3%A0-%EC%9E%85%EB%AC%B8/lecture/2603?tab=note)
