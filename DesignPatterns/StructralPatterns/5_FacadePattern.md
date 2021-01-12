# 🛠 Facade Pattern(파사드 패턴)
### ✔ 파사드 패턴이란?
* Facade는 "건물의 정면"을 의미하는 단어로 어떤 소프트웨어의 커다란 코드 부분에 대해 **간략화된 인터페이스를 제공해주는 디자인 패턴**
* 작업 수행의 복잡성은 숨기고 사용자들에게는 간단한 인터페이스로 제공하는 패턴.<br/>
(전자레인지를 이용해 음식을 데울 때 마이크로파 발생 원리, 타이머 원리 등을 이해할 필요 없이 음식을 넣고 돌리기만 하면 됨.)
* 주의사항 : Facade 클래스가 클라이언트에게 제공하는 인터페이스는 변경되지 않아야 함.<br/>
    * 이와같이 하기 위해서는 Facade를 추상클래스로 정의하고 그 하위에 상속관계를 대입시킴
    * 이렇게 할 경우 Client는 서브 시스템이 어떤 방식으로 이루어지든 동일한 방식으로 서브시스템을 활용할 수 있음

<br/><br/>
### ✔ 파사드 패턴을 쓰는 이유
* Facade를 통해서만 접근이 가능하기 때문에 사용자와 서브시스템 간의 결합도를 줄여줌
* 클라이언트 입장에서 서브시스템을 사용해야 할 때 다뤄야 할 객체의 수를 줄여줌

<br/><br/>
### ✔ 파사드 패턴 단점
* 사용자에게 내부 서브 시스템까지 숨길 수는 없기 때문에 사용자가 서브 시스템 내부 클래스를 직접 사용하는 것을 막을 수 없음<br/>
(private로 은닉할 수 없으니 Namespace를 선언하는 것이 대안)

<br/><br/>
### ✔ 파사드 패턴 예제 구조
![캡처3](https://user-images.githubusercontent.com/54934681/104277840-f25a0b80-54ea-11eb-9b61-e4f8bc0495a3.PNG)

<br/><br/>
### ✔ 파사드 패턴 예제
영화관에서 영화를 상영하는 시스템이 있다고 생각해보자.<br/>
영화를 상영하기 위해 필요한 절차는 아래와 같다.<br/>
```
(1) 조명을 영화관 모드로 변경
(2) 스크린을 내림
(3) 프로젝터를 킴
(4) 프로젝터를 영화관 모드로 변경
(5) DVD Player를 킴
(6) DVD Player에서 영화를 시작
```
 
위의 모든 과정을 수행하기 위해서는 조명, 프로젝터, 스크린, DVD Player 객체를 알고 있어야 한다.<br/>
클라이언트가 이 모든 객체를 알고 있으면 결합도가 상당히 높고 복잡해진다.<br/>
퍼사드 패턴을 이용하여 클라이언트는 퍼사드 객체 하나만으로 영화를 상영할 수 있게 구현해본다.<br/>

<br/><br/>
🔻 SubSystem(영화를 상영하는데 필요한 객체들, 조명, 스크린, 프로젝터, DVD 플레이어로 구성된다.)
```java
package StructuralPattern.Facade;

public class Light {
	public void on() {
		System.out.println("조명을 켭니다");
	}
	
	public void movieMode() {
        System.out.println("조명을 영화관 모드로 변경합니다.");
    }
}
```
```java
package StructuralPattern.Facade;

public class Screen {
	 public void down() {
        System.out.println("스크린을 내립니다.");
    }

    public void up() {
        System.out.println("스크린을 올립니다.");
    }
}
```
```java
package StructuralPattern.Facade;

public class Projector {
	public void on() {
        System.out.println("Projector를 켭니다.");
    }


    public void off() {
        System.out.println("Projector를 종료합니다.");
    }

    public void movieMode() {
        System.out.println("Projector를 영화관모드로 설정합니다.");
    }
}
```
```java
package StructuralPattern.Facade;

public class DvdPlayer {
	public void on() {
        System.out.println("DvdPlayer를 킵니다.");
    }

    public void play(String movieName) {
        System.out.println("'" + movieName + "'을(를) 상영합니다.");
    }

    public void off() {
        System.out.println("DvcPlayer를 끕니다.");
    }
}
```

<br/><br/>
🔻 Facade
* 파사드는 영화 상영에 필요한 모든 장치들을 가지고 있다.
* `watchMovie`가 호출되었을 때 해당 영화를 상영하는데 필요한 모든 동작을 수행한다.
* `endMovie`가 호출되었을 때 영화를 종료하는데 필요한 모든 동작을 수행한다.
```java
package StructuralPattern.Facade;

public class HomeTheaterFacade {
	Light light;
	Projector projector;
	Screen screen;
	DvdPlayer dvdPlayer;
	
	public HomeTheaterFacade(Light light, Projector projector, Screen screen, DvdPlayer dvdPlayer) {
		this.light = light;
		this.projector = projector;
		this.screen = screen;
		this.dvdPlayer = dvdPlayer;
	}
	
	public void watchMovie(String movieName) {
		System.out.println("===============WATCH MOIVE===============");
		light.movieMode();
		screen.down();
		projector.on();
		projector.movieMode();
		dvdPlayer.on();
		dvdPlayer.play(movieName);
	}
	
	public void endMovie() {
		System.out.println("================END MOIVE================");
		light.on();
		screen.up();
		projector.off();
		dvdPlayer.off();
	}
	
}
```



<br/><br/>
🔻 Main클래스
```java
package StructuralPattern.Facade;

public class FacadeMain {

	public static void main(String[] args) {
		HomeTheaterFacade homeTF = new HomeTheaterFacade(new Light(), 
								   new Projector(), new Screen(), new DvdPlayer());
		
		homeTF.watchMovie("Begin Again");
		homeTF.endMovie();
	}
}
```
`클라이언트에서는 HomeTheatherFacade만 알고있으면 영화를 상영하고 끌 수 있다.`<br/>
`(퍼사드 패턴을 통해 구현과 서브시스템을 분리하여 클라이언트는 퍼사드 객체 하나만 참조하므로 결합도가 낮아졌다.)`


<br/><br/>
🔻 콘솔 결과창
```console
===============WATCH MOIVE===============
조명을 영화관 모드로 변경합니다.
스크린을 내립니다.
Projector를 켭니다.
Projector를 영화관모드로 설정합니다.
DvdPlayer를 킵니다.
'Begin Again'을(를) 상영합니다.
================END MOIVE================
조명을 켭니다
스크린을 올립니다.
Projector를 종료합니다.
DvcPlayer를 끕니다.
```
