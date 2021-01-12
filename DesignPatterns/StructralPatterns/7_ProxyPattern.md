# 🛠 Proxy Pattern(프록시 패턴)
### ✔ 프록시 패턴이란?
* 실제 기능을 수행하는 객체(Real Object) 대신 **가상의 객체(Proxy Object)를 사용해 로직의 흐름을 제어**하는 패턴
* 대개 2가지 경우에 사용
    * 첫째, 바빠서 그 일을 할 수 없는 본인 객체 대신 대리인 객체가 어느 정도 그 일을 처리해 줄 필요가 있을 경우
    * 둘째, 다른 객체에 접근하기 위해 본인 객체는 은닉하고 대리인 객체를 두고자 하는 경우
* 프록시 패턴은 한정된 자원을 가지고 서비스 요청이 폭주하는 시간에도 **안정되고 빠르게 유지**하기 위한 웹툰 서비스 등에 이용하며, **4가지 유형**으로 구분할 수 있음
* 프록시 유형
  * `가상 프록시(Virtual Proxy)`: 예제에 해당하는 프록시, 인스턴스가 필요한 시점에만 생성 및 초기화하는 프록시
  * `원격 프록시(Remote Proxy)`: 네트워크가 연결된 상황에서 원격으로 로컬 객체를 원격 객체처럼 사용
  * `보호 프록시(Access Proxy)`: RealSubject 기능에 대해 액세스 제한을 설정하는 프록시
  * `캐싱 프록시(Caching Proxy)`: 지연이 많이 되는 작업을 임시로 저장, 여러 클라이언트에게 공유하는 프록시
  * 기타: 방화벽 프록시, 스마트 레퍼런스 프록시, 동기화 프록시, 복잡도 숨김 프록시 등
  
  
<br/><br/>
### ✔ 프록시 패턴을 쓰는 이유
* 원래 하려던 기능을 수행하며 그외의 부가적인 작업(로깅, 인증, 네트워크 통신 등)을 수행하기에 좋음
* 비용이 많이 드는 연산(DB 쿼리, 대용량 텍스트 파일 등)을 실제로 필요한 시점에 수행할 수 있음
* 사용자 입장에서는 프록시 객체나 실제 객체나 **사용법은 유사**하므로 사용성이 좋음
* 기본 객체에 대한 **수정 없이**, 클라이언트에서의 사용과 기본 객체 사이에 일련의 로직을 프록시 객체를 통해 넣을 수 있음
* 프록시는 기본 객체와 요청 사이에 있기 때문에, 일종의 **방패(보안)의 역할**도 함

<br/><br/>
### ✔ 프록시 패턴 단점
* 프록시 객체가 중간에 껴있기 때문에, 간혹 응답이 느려질 수 있음. (캐싱이 안되어있는 초기 사용의 경우)

<br/><br/>
### ✔ 프록시 패턴 예제 구조
![캡처6](https://user-images.githubusercontent.com/54934681/104280054-add06f00-54ee-11eb-8b08-3bfa1e5f82ae.PNG)
* `Subject(PrintableSubject)`: Proxy와 RealSubject가 구현해야하는 인터페이스. 두 객체를 동일하게 다루기 위해 존재
* `Proxy(PrintProxy)`: RealSubject와 Client 요청 사이에 존재하는 객체. Subject를 구현함으로써 클라이언트 RealSubject 사용하는 것과 별 차이가 없어야 함.
* `RealSubject(PrintRealSubject)`: 실질적으로 요청에 대해 주된 기능을 수행하는 객체. Proxy객체는 내부적으로 이 객체를 로직에 맞게 사용함(위임)

<br/><br/>
### ✔ 프록시 패턴 예제
🔻 인터페이스(Proxy와 RealSubject 역할의 인터페이스 정의)
```java
package StructuralPattern.Proxy;

public interface PrintableSubject {
	void setPrintName(String name);
	String getPrinterName();
	void print(String string);
}
```


<br/><br/>
🔻 인터페이스
```java
package StructuralPattern.Proxy;

public class PrinterRealSubject implements PrintableSubject {
	private String name;
	
	public PrinterRealSubject(String name) {
		this.name = name;
		heavyJob("PrinterRealSubject[" + name + "] 인스턴스 생성중..");
	}
	
	private void heavyJob(String string) {
		System.out.println(string);
		try {
			Thread.sleep(3000);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		System.out.println("생성 완료...");
	}

	@Override
	public void setPrintName(String name) {
		this.name = name;
		
	}

	@Override
	public String getPrinterName() {
		return name;
	}

	@Override
	public void print(String string) {
		System.out.println(string);
	}
	
}
```
`인터페이스를 구현하기 위해 setPrinterName(), getPrinterName(), Print()를 재정의해주고, 객체의 인스턴스 생성 비용을 무겁게 하기 위해 heavyJob()이라는 메소드를 통해 3초를 지연시켰다.`

<br/><br/>
🔻 Proxy 클래스
```java
package StructuralPattern.Proxy;

public class PrinterProxy implements PrintableSubject{
	private String name;
	private PrinterRealSubject real;
	
	public PrinterProxy(String name) {
		this.name = name;
	}

	@Override
	public synchronized void setPrintName(String name) {
		if(real != null) {
			real.setPrintName(name);
		}
		this.name = name;
	}

	@Override
	public String getPrinterName() {
		return name;
	}

	@Override
	public synchronized void print(String string) {
		realize();
		real.print(string);
	}
	
	private synchronized void realize() {
		if(real == null) {
			real = new PrinterRealSubject(name);
		}
	}
	
}
```
`대리인으로서 처리가 가능한 부분은 객체가 맡아서 처리를 해준다. ex) getPrinterName()`<br/>
`그리고 실제 RealSubject가 필요한 시점에 해당 객체에게 요청을 위임한다.`

<br/><br/>
🔻 Main 클래스
```java
package StructuralPattern.Proxy;

public class ProxyMain {

	public static void main(String[] args) {
		PrintableSubject p = new PrinterProxy("Simple");
		
		// 프록시가 실행됨
		System.out.println(p.getPrinterName());
		
		// realSubject가 실행
		p.print("프린트 요청");
	}

}
```

<br/><br/>
🔻 콘솔 결과창
```console
Simple
PrinterRealSubject[Simple] 인스턴스 생성중..
생성 완료...
프린트 요청
```


> 로직에 많은 비용이 필요하면 처음부터 Printer클래스에서 분리해서 사용하면 되는 거 아니야?라는 의문에는<br/>
> 디자인의 원칙에 의해서 객체들의 역할을 분리해서 개별적으로 수정이 가능하게 하기 위함이다. <br/>
> 즉, 유지보수가 용이하고 클라이언트 입장에서는 지연이 필요할 경우 Proxy 객체를 사용할 필요 없이 PrinterRealSubject를 사용할 수 있다.

