## 💻 02. CentOS Linux
### 🔎 리눅스의 개요
* 리눅스 : 상용 유닉스의 무료 버전
* 1991년 '리누스 토르발스'가 버전 0.01을 최초 작성
* 1992년 0.02을 공개하면서 시작 됨
* 리누스 토르발스는 커널(Kernel)만 개발함
<br/>

### 🔎 배포판의 구성
![image](https://user-images.githubusercontent.com/54934681/112097373-3a7c6500-8be3-11eb-9801-b197f290b0ee.png)
* CentOS 리눅스도 많은 배포판 중 한가지임
* 하드웨어를 감싸고 있는 커널이 엄격한 의미의 리눅스
* 다양한 응용프로그램을 합쳐서 만들어진 것이 배포판
<br/>

### 🔎 커널 
* 커널 버전의 의미 (예: 5.3.2)
  * 5는 주 버전 (Major Version)
  * 3은 부 버전 (Minor Version)
  * 2는 패치 버전(Patch Version) 
* 배포판에 포함된 기본 커널을 사용자가 직접 최신 커널로 업그레이드 할 수 있음 (커널 업그레이드)
  * https://www.kernel.org에서 최신버전 무료 다운로드
  * CentOS 8은 커널 4.18을 포함함
<br/>

### 🔎 CentOS 8 설치 하드웨어 요구사항
* CPU : 64bit CPU
* 하드디스크 여유 공간 : 20GB 이상의 여유공간 권장(추가 설치에 따라 달라질 수 있음)
* 메모리 : 권장 4GB( 최소 2GB)
* VMware를 사용할 경우 더 높은 사양이 요구 됨
<br/>

### 🔎 CentOS 설치
* 예시: Server컴퓨터
1. CentOS8(1905) 다운 & 체크프로그램 다운(https://cafe.naver.com/thisislinux/5796)
2. 체크프로그램 SHA-256만 체크하고 CentOS8 확인 후 카페에 있는 SHA256코드를 Hash에 입력, Verify로 확인 (매치 시 정상적 파일!)
3. VMWare player 오픈 → Server 선택 → Edit virtual machine settings → CD/DVD(SATA) 의 Auto detect를 Use ISO Image file 
<br/> → ↑위에서 다운로드한 파일로 변경 (변경 시 위쪽에 있는 device status의 Connect at power on 체크 되어있는지 꼭 확인! 체크가 되어있어야 부팅하면서 ISO파일 인식) → 부팅!
4. 한국어로 선택 → 계속 진행 → 시간 및 날짜 한국 설정 → 네트워크 호스트 → 이더넷 켬
    <br/>  → 소프트웨어 선택 → 서버GUI를 워크스테이션으로 변경
    <br/>  (Why? gui는 깔리지만 나중에 추가 설치해야 할 것이 많기 때문에 그냥 워크스테이션으로)
    <br/>  → 설치 목적지(중요!) : 로컬 표준디스크 선택 > 저장소구성 : Custom 선택 > 완료 > 새로운 LVM: 표준 파티션 선택 
    <br/>  →  + 눌러서 마운트 지점 : swap,원하는 능력:4G (80기가 중에서 4기가를 임시메모리 공간으로 사용한다) 추가 →
    <br/>  →  한번 더 + 누르고 마운트지점: /, 원하는 능력 : 비워놓기(80기가에서 4기가 뺀 나머지 다)
    <br/>  (윈도우 c드라이브랑 비슷한 개념의 루트(슬래시)파티션 추가) 
    <br/>  →  완료및 변경사항 적용( 파티션을 두가지로 나눈 것임) → 설치시작!
    <br/>  → 설치하면서 root 암호 설정(임의설정) → 완료 2번 누름 → 사용자 생성(이름 암호 모두 centos로 함) → 설치 완료 후 재부팅
5. 라이센스 클릭 → 동의 → 설정완료 → 사용자 로그인(root로 로그인 하려면 목록에 없습니까? 클릭 → 사용자 이름 : root , 비밀번호 입력 → 로그인 → gnome 설정( 1. 한국어 → 2.한국어(Hangul) → 위치서비스 기본값 → 온라인계정 건너뛰기 → 시작!

* 리눅스에서는 이더넷 랜카드의 이름을  ens160으로 부름
* root : 리눅스에서의 관리자
<br/>

### 🔎 네트워크 설정
* Server 컴퓨터 192.168.111.100번으로 설정
1. cd /etc/sysconfig/network-scripts/

2. gedit ifcfg-ens160

3. bootproto수정 및 나머지 추가<br/>
 ```cmd
BOOTPROTO = "none"
IPADDR="192.168.111.100"
NETMASK="255.255.255.0"
GATEWAY="192.168.111.2"
DNS1="192.168.111.2"
```

4. 수정 후 재부팅 
```cmd
nmcli connection down ens160 
nmcli connection up ens160 > reboot
```

5. 수정반영여부 확인 
```cmd
ifconfig ens160
```
<br/>

### 🔎 스냅샷(PRO)
* 스냅샷 찍기
  * VMWare Workstation PRO 실행
  * Open a Virtual Machine
  * Server 생성한 폴더의 Server.vmx 파일 열기
  * 상단 메뉴 VM > snap shot > SnapShot Manager > 처음이면 You Are Here 선택 후 > Take Snapshot 선택 > 이름 설정 > 완료
* 스냅샷 복구하기
  * VMWare Workstation PRO 실행
  * 상단 메뉴 VM > snap shot > SnapShot Manager > 복구시점 이름 선택 후 Go to
<br/>
