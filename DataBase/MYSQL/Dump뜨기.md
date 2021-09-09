## Dump뜨기 (Federate 사용하지 않는 경우 2,3번 skip)

### 1. cmd 실행
* 관리자 권한으로 cmd 실행
```cmd
> mysqldump --routines --triggers db명 -uroot -p비밀번호 > 210909_db명_dump.sql
```

<br/>

### 2. mysql  federated 엔진 켜기
* federated 가 yes인지 확인
```cmd
> show engines; 
```

* federated자체가 없으면 플러그인 설치
```cmd
> install plugin federated soname 'ha_federated.dll'
```

* 플러그인 설치 후 /etc/my.cnf 파일에 federated 추가
```cmd
[mysqld]
federated
```


<br/>

### 3. 페더레이트 정보 수정
* dump 된 파일 열어서 기존 페더레이트 연결 되어 있으면 내용 수정
* 파일이 너무 커서 열리지 않을 경우 PilotEdit Lite 설치하여 열어보기

<br/>

### 4. User 생성
* 유저 목록 확인
``` cmd
> use mysql;
> select user, host from user;
```
* 유저 생성
```cmd
> create user 'yeonkoung'@'%' identified by 'bread18'
```


<br/>

### 5. Datebase 생성
* 데이터베이스 목록 확인
``` cmd
> show databases;
```
* 데이터 베이스 생성
```cmd
create database oneandonly default character set utf8;
```


<br/>

### 6. Datebase 권한부여
* 권한 부여
``` cmd
> grant all privileges on oneandonly.* to yeonkoung@'%' identified by 'bread18';
```
* 변경된 권한 내용 메모리에 반영
```cmd
> flush privileges;
```


<br/>

### 7. Dump 파일 Import
* sql 파일 경로에 cmd 창 켜서 import 실시
``` cmd
> mysql -uroot -p비밀번호 oneandonly < ./210909_db명_dump.sql
```
