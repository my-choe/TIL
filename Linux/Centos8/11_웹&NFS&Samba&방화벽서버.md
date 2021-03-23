## 💻 11. 웹 & NFS & Samba 서버
### 🔎 웹 서버
* **APM**
  * 리눅스를 가장 많이 활용하는 분야 중 하나가 바로 웹(Web) 서버
  * 가장 안정적이고 유명한 Apache 웹 서버
  * APM = Apache 웹 서버 + 프로그래밍 언어 PHP + 데이터베이스 MariaDB(이전 MySQL)
  * 리눅스 환경에서 사용될 경우 LAPM(Linux, Apache, PHP, MariaDB)라고도 부름
  * APM이라는 소프트웨어는 존재하지 않으며 이 3가지가 서로 잘 연동되어 운영되도록 만든 환경을 일컬음
<br/>

* **클라우드 서비스**
  * 네이버의 N드라이브, 구글 드라이브, Microsoft OneDrive 등의 서비스를 말함
  * 기존의 웹하드 기능까지 포함
  * 클라우드 서비스 개념도(한 명 기준)
<br/>



### 🔎 NFS 서버
  * Linux (Unix) 컴퓨터끼리 저장공간을 공유할 수 있도록 해주는 시스템이 NFS(Network File System)
  * ▼ NFS 서버 구현의 개요도<br/>
![image](https://user-images.githubusercontent.com/54934681/112108183-31938f80-8bf3-11eb-88f7-ad51bac1d907.png)
  * 클라이언트는 /myShare 내의 폴더에 옮기지만 실은 192.168.111.100 의 /share 폴더에 들어감
<br/>


### 🔎 Samba 서버
* 예전에는 Windows 와 Linux/Unix 사이에 프린터나 폴더등의 자원을 공유하기가 어려웠음
* Samba 서버는 Windows와 Linux/Unix 사이에서 자원을 공유하기 위해 개발됨
* Linux에서 Windows의 자원을 사용하는 방법과 Windows에서 Linux의 자원을 사용하는 방법으로 나뉨
* NFS와 비슷하지만 NFS는 리눅스간의 공유이고 Samba는 windows와 Linux간의 공유
* ▼ 윈도우의 프린터와 공유폴더를 linux에서 사용하기<br/>
![image](https://user-images.githubusercontent.com/54934681/112108342-6acbff80-8bf3-11eb-8cbc-ee7d1670d134.png)
* 윈도우에서는 samba 서버라는 개념이 없음. 그냥 폴더만 공유해놓으면 됨.
<br/>


### 🔎 방화벽 서버
* **방화벽이란?**
  * 외부에 공개된 네트워크와 내부의 사설 네트워크 사이에 자리잡고<br/>
    외부와 내부에 전달되는 트래픽을 '정책(Policy)'에 의해서 허용/거부하는 역할을 하는 컴퓨터나 장치를 말함
  * 내부 사용자는 외부 인터넷을 이용하면서, 외부에서는 내부로 침입할 수 없게 하는 방법 중<br/>
    가장 보편적으로 사용하는 방법이 사설IP (Private IP)라고 흔히 불리는 nonroutable IP 주소를 이용하는 것
  * 사설 IP 주소의 범위는 10.0.0.0 ~ 10.255.255.255   /   172.16.0.0 ~ 172.31.255.255    /   192.168.0.0 ~ 192.168.255.255
  * 사설 IP주소의 컴퓨터가 외부 인터넷으로 접속할 수 있게 해주는 방법을 IP 마스커레이딩(Masquerading)이라고 함

* ▼ 보편적인 회사 네트워크 구성<br/>
![image](https://user-images.githubusercontent.com/54934681/112108572-ba123000-8bf3-11eb-9728-9ca819d3e67f.png)
<br/>
