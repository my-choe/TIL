## 💻 05. 필수개념과 명령어
### 🔎 파일 압축과 묶기
* Windows 압축과 다른 점
  * 윈도우
    * 압축과 동시에 묶어줌
    * 압축하면 기존 파일이 남아 있음
  * 리눅스
    * 압축과 묶기를 각각 실행해야 함
    * 기존파일 자체를 압축함

* 파일 압축
  * 압축파일 확장명 : xz, bz2, gz, zip, Z 등
  * xz > bzip2 > gzip 순으로 파일 압축률 높음 (xz가 제일 최신)
  * 파일 압축 : xz 파일명  / bzip 파일명  / gzip 파일명
  * 압축 해제 : xz -d 파일명.xz  /  bzip -d 파일명.bz2  /  gzip -d 파일명.gz
  * 사용 예
    * 파일압축 : `xz` my2
    * 여러파일 압축 : `tar` cvfJ file.tar.xz file1 file2 file3 file4
    * 압축 해제 : `tar` xvfJ my2.tar.xz 

* 파일 묶기
  * 리눅스(유닉스)에서는 '파일 압축'과 '파일 묶기'는 원칙적으로 별개 프로그램으로 수행
  * 파일 묶기의 명령어는 `tar`이며, 묶인 파일의 확장명도 `tar`

* 파일 묶기 명령(tar)
  * `tar` : 확장명 tar로 묶음 파일을 만들어 주거나 묶음을 풀어줌
    * 동작 : c(묶기), x(풀기), t(경로확인)
    * 옵션 : f(파일), v(과정보이기), J(tar+xz), z(tar+gzip), j(tar+bzip2)
  * 사용 예
    * `tar` cvf my.tar /etc/sysconfig/    ( /etc/sysconfig 폴더가 my라는 tar묶음파일로 만들어짐)
    * `tar` cvfJ my2.tar.xz /etc/sysconfig  (/etc/sysconfig 폴더를 tar폴더로 묶어서 xz로 압축하기)
<br/>

### 🔎 파일 위치 검색
* `기본파일찾기 : find [경로] [옵션] [조건] [action]`
* [옵션] : -name,    -user(소유자),    -newer(전,후),    -perm(허가권),    -size(크기)
* [action] : -print(디폴트),   -exec(외부명령실행)
* `which 실행파일이름` : PATH에 설정된 디렉터리만 검색
* `whereis 실행파일이름` : 실행파일, 소스, man페이지 파일까지 검색
* `locate 파일이름` : 파일 목록 데이터베이스에서 검색

* 사용 예
  * `find /etc -name "*.conf"`  (/etc 폴더에서 파일 이름 중 .conf 가 들어가는 것)
  * `find /bin -size +10k -size -100k`  (사이즈가 10~100 사이 파일)
  * `find /home -name "*.swap" -exec rm {} \;`  (이름에 .swap이 들어가는 파일을 rm삭제)
<br/>

### 🔎 CRON과 AT
* `cron`
  * 주기적으로 반복되는 일을 자동실행될 수 있도록 설정
  * 관련된 데몬(서비스)은 "crond",  "관련파일은 "/etc/crontab"
 ![image](https://user-images.githubusercontent.com/54934681/112101390-e759e080-8be9-11eb-8781-4e4d13295c72.png)
* 사용 예
  * `01  3  15  *  *  root  run-parts  /etc/cron.monthly` <br/>
  *  (1분마다  / 새벽3시 / 매달 15일 / 모든 달 / 모든 요일 사용자권한 /  명령어  / 실행할 파일이 있는 폴더)


* `at` : cron은 주기적 반복 작업을 예약하는 것이지만, at은 일회성 작업 예약
* 사용 예
  * `at  4:00am  tomorrow`  (내일 새벽 4시)
  * `at 11:00pm January 30` (1월 30일 오후 11시)
  * `at now + 1 hours` (1시간 후)
  * 프롬프트에 예약 명령어 입력 후 [Enter]
    * `reboot`  리부트(예시)
  * 작성 후 [ctrl] + [d] 누르면 저장
  * 예약 목록 보기 : `at -l`
  * 예약 지우기 : `atrm  작업번호`
<br/>
