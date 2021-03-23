## 💻 04. 필수개념과 명령어
### 🔎 RPM(Redhat Package Manager)
* RPM  : windows의 setup.exe와 비슷한 설치 파일로 확장명은 `*.rpm`이며 이를 `패키지(Package)`라고 부름
![image](https://user-images.githubusercontent.com/54934681/112099969-b9739c80-8be7-11eb-80f2-dafa2be5c5b8.png)

* 패키지이름-버전-릴리즈번호.CentOS버전.아키텍처.rpm
    * 패키지이름 : gzip → 패키지(프로그램 이름)
    * 버전1.9 : 대개 3자리 수로 구성. 주버전, 부버전, 패치버전
    * 릴리즈번호4 : 문제점을 개선할 때마다 붙여지는 번호
    * CentOS 버전: el8 → CentOS에서 배포할 경우에 붙여짐. el(enterprise linux)
    * 아키텍쳐 : x86_64 → 64비트  /  i386~686 : 32비트 CPU  / src : 소스  / noarch : 모든 CPU
* RPM 단점
  * 의존성 문제 : A패키지를 설치하려면 B패키지가 설치되어 있어야 하는 경우 RPM으로는 해결이 까다로움<br/>
  (→ 이를 해결하기 위해 DNF(YUM) 등장)
<br/>

### 🔎 RPM 명령어 옵션
* 설치 : rpm -Uvh 패키지파일이름.rpm
  * U : 패키지 설치/업그레이드
  * v : 설치 과정 확인
  * h : 설치진행과정을 "#" 마크로 화면에 출력
  * `-rpm -lvh`도 있지만 lvh는 기존 설치되어 있으면 오류 발생.<br/>U의 경우 기존 설치 되어 있으면 넘어가고, 최신버전이라면 업그레이드 진행
  * 설치 시 `Uvh 패키지파일.rpm`의 경우 패키지 파일이 현재 폴더 또는 지정경로에 있어야 함(삭제는 home에서도 가능)

* 삭제 : `rpm -e 패키지 이름`
* 이미 설치된 패키지 질의
  * `rpm -qa 패키지 이름` : 패키지 설치 여부 확인
  * `rpm -qf 파일절대경로` : 파일이 어느 패키지에 포함된 것인지 확인
* 아직 설치되지 않은 rpm 파일에 대한 질의
  * `rpm -qlp 패키지파일이름.rpm` : 패키지 파일에 어떤 파일들이 포함되었는지 확인
  * `rpm -qip 패키지파일이름.rpm` : 패키지 파일의 상세 정보
<br/>

### 🔎 DNF(Dandified)
* `rpm` 명령의 패키지 의존성 문제를 완전하게 해결
* 인터넷을 통해 필요한 파일을 저장소(Repository)에서 자동으로 모두 다운로드해서 설치하는 방식
* CentOS 7은 YUM, CentOS 8은 YUM이 개선된 DNF 명령 사용
* 실제 rpm패키지가 없어도 centos8 서버`(/etc/yum.repos.d/)`에 있는 파일을 다운로드 하는 것이므로<br/>의존성이 필요한 파일까지 모두 다운로드 함
* `dnf install rpm파일이름.rpm` 에서 rpm생략하고 파일이름만 써도 가능(다만 현재 폴더 안에 있어야 함)
![image](https://user-images.githubusercontent.com/54934681/112100423-7108ae80-8be8-11eb-97dc-2269d2bbe245.png)

* DNF 기본적인 사용법
  * 기본설치 : `dnf install 패키지 이름`
     * 저장소의 URL은 `/etc/yum,repos.d/디렉터리`
     * "-y"는 사용자의 확인을 모두 "yes"로 간주하고 설치를 진행한다는 옵션
  * RPM 파일 설치 : `dnf install rpm파일이름.rpm`
  * 업데이트 가능한 목록 보기 : `dnf check-update`
  * 업데이트 : `dnf update 패키지이름`
  * 삭제 : `dnf remove 패키지이름`
  * 정보확인 : `dnf info 패키지이름`

* DNF 고급 사용법
  * 패키지 그룹 설치 : `dnf groupinstall "패키지 그룹이름"`
    * 패키지 그룹을 설치하려면 그룹 이름 먼저 알아야 함(`dnf grouplist` 또는 `dnf grouplist hidden`)
  * 패키지 리스트 확인 : `dnf list 패키지 이름`
  * 특정파일이 속한 패키지 이름 확인 : `dnf provides 파일이름`
  * GPG 키 검사 생략 : `dnf install --nogpgceheck rpm파일이름.rpm` (CentOS8에서 인증되지 않은 패키지를 강제 설치할 때 사용)
  * 기존 저장소 목록 지우기 : `dnf clean all`
<br/>
