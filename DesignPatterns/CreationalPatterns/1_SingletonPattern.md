# 🛠 Singleton Pattern(싱글톤 패턴)
### ✔ 싱글톤 패턴이란?
* **단 하나의 인스턴스**를 생성해 사용하는 디자인 패턴
* 애플리케이션이 시작될 때 어떤 클래스가 **최초 한 번만 메모리를 할당**하고(Static) 그 메모리에 인스턴스를 만들어 사용하는 디자인 패턴
* 생성자가 여러 차례 호출되더라도 실제 생성되는 객체는 하나 → 최초 생성 이후 호출된 생성자는 **최초 생성 객체 반환**
* 자바에서는 **생성자**를 private으로 선언하여 **생성불가**하게 하고 getInstance()로 받아서 쓰기도 함

<br/><br/>
### ✔ 싱글톤 패턴을 쓰는 이유
* 고정된 메모리 영역을 얻어 한 번의 new로 인스턴스를 사용하기 때문에 **메모리 낭비 방지**
* 싱글톤으로 만들어진 클래스의 인스턴스는 전역 인스턴스 → 다른 클래스에서 인스턴스들이 **데이터를 공유**하기 쉬움<br/>
*(DBCP처럼 공통된 객체를 여러 개 생성해서 사용해야 하는 상황에서 주로 사용)*
* 오직 하나의 클래스 인스턴스를 보장하여야 하고, 잘 정의된 접근점(Access Point)으로 **모든 사용자가 접근**해야할 때 사용
* 유일한 인스턴스가 서브클래싱으로 확장되어야 하며, 사용자는 코드 수정없이 서브클래스의 인스턴스를 사용할 수 있어야 할 때 사용
* 두 번째 이용시부터는 **객체 로딩 시간**이 현저하게 줄어들어 성능이 좋아지는 장점이 있음

<br/><br/>
### ✔ 싱글톤 패턴 단점
* 싱글톤 인스턴스가 너무 많은 일을 하거나 많은 데이터를 공유시킬 경우, 인스턴스들 간 결합도 높아짐 → **개방-폐쇄 원칙**을 위배하게 됨
* **멀티스레드 환경**에서 **동기화 처리**를 하지 않으면 두 개의 인스턴스가 생성되는 경우 발생할 수 있음
> **개방-폐쇄 원칙(OCP, Open-Close Principle)**<br/>
> '소프트웨어 개체(클래스, 모듈, 함수 등등)는 확장에 대해 열려있어야 하고, 수정에 대해서는 닫혀 있어야 한다'는 프로그래밍 원칙

<br/><br/>
### ✔ 싱글톤 패턴 예제

```java
package CreationalPattern.singleton;

public class Speaker {
  private static Speaker speaker; // 외부에서 호출할 수 없도록 private 선언
  private int volume;
  
  private Speaker() {
    volumn = 5;
  }
  
  public static Speaker getInstance() {
  // getInstance() 메소드를 사용하여 스피커 인스턴스가 이미 생성되어있는지 확인
  // 생성되어 있지 않은 상황이라면 생성자를 호출해 인스턴스를 생성하고
  // 생성되어 있다면 정적 변수 speaker 변수를 참조하는 인스턴스를 반환
    if (speaker == null) {
      speaker = new Speaker();
    }
    return speaker;
  }
  
  public int getVolume(){
    return volume;
  }
  
  public void setVolume(int volume) {
    this.volume = volume;
  }
}
```

<br/><br/>
🔻 클라이언트 사용
```java
package CreationalPatterns.singleton;

public class RunSpeaker {
  
  public static void main(String[] args) {
    Speaker speaker1 = speaker.getInstace();
    Speaker speaker2 = speaker.getInstace();
    Speaker speaker3 = speaker.getInstace();
    
    System.out.println(speaker1);
    System.out.println(speaker2);
    System.out.println(speaker3);
    
    System.out.println(speaker1.getVolume());
    System.out.println(speaker2.getVolume());
    System.out.println(speaker3.getVolume());
    
    speaker1.setVolume(10);
    System.out.println(speaker1.getVolume());
    System.out.println(speaker2.getVolume());
    System.out.println(speaker3.getVolume());
    
    speaker2.setVolume(20);
    System.out.println(speaker1.getVolume());
    System.out.println(speaker2.getVolume());
    System.out.println(speaker3.getVolume());
  }
}
```


<br/><br/>
🔻 콘솔 결과창
```console
CreationalPattern.singleton.Speaker@6108b2d7
CreationalPattern.singleton.Speaker@6108b2d7
CreationalPattern.singleton.Speaker@6108b2d7
5
5
5
10
10
10
20
20
20
```

```
한 객체의 음량을 조절해도 모두 변경됨 → 모두 같은 객체임을 확인할 수 있음
다만 다중 스레드의 경우 동시에 volume 변수 값 갱신 시, 문제 발생 가능성 있음

// 해결방법
- 정적 변수에 인스턴스를 만들어 바로 초기화 한다.
  private static Speaker speaker = new Speaker();
  
- 또는 인스턴스를 만드는 메서드를 synchronized를 사용하여 동기화 한다.
  public synchronized static Speaker getInstance();
  public synchronized void setVolume(int volume);
```

