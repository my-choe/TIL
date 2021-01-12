# 🛠 Bridge Pattern(브리지 패턴)
### ✔ 브리지 패턴이란?
* 기능클래스 계층과 구현 클래스 **계층을 연결해주는 패턴**
   * **기능 클래스 계층**이란? A라는 상위클래스를 상속받는 B라는 하위 클래스에서 새로운 기능을 추가하는 계층
   * **구현 클래스 계층**이란? A라는 인터페이스를 구현한 B라는 객체가 존재할 때 구현 클래스 계층이라고 함
* 구현부에서 추상층을 분리하여 **각자 독립적으로 변형**할 수 있게 하는 패턴
* 즉, 기능과 구현을 별도의 클래스로 정의해서 서로를 분리하는 방법으로 호출은 추상부, 구현은 구현층에서 하는 패턴

<br/><br/>
### ✔ 브리지 패턴을 쓰는 이유
* 전형적인 상속을 이용한 패턴으로 **확장 설계 용이**
* 구현부가 어떤 식으로 구현했는지 **은닉**함으로써, **종속성을 없애고 결합도를 낮춤**
* 추상화된 부분을 구현한 구상 클래스를 바꿔도 클라이언트 쪽에는 영향을 끼치지 않음

<br/><br/>
### ✔ 브리지 패턴 단점
* 매우 응집력있는 클래스에 적용하면 코드가 더 복잡해질 수 있음

<br/><br/>
### ✔ 브리지 패턴 예제 구조
![캡처1](https://user-images.githubusercontent.com/54934681/104274422-254cd100-54e4-11eb-815c-bee562bbbb1c.PNG)
<table border="1" cellpadding="0" cellspacing="0" style="width:600px">
	<tbody>
		<tr>
			<td><strong>구분</strong></td>
			<td><strong>이름</strong></td>
			<td><strong>해설</strong></td>
		</tr>
		<tr>
			<td colspan="1" rowspan="2">기능 클래스 계층</td>
			<td>Display</td>
			<td>&#39;표시한다&#39;는 클래스</td>
		</tr>
		<tr>
			<td>CountDisplay</td>
			<td>&#39;지정 횟수만큼 표시한다&#39;는 기능 추가 클래스</td>
		</tr>
		<tr>
			<td colspan="1" rowspan="2">구현 클래스 계층</td>
			<td>DisplayImpl</td>
			<td>&#39;표시한다&#39;는 클래스</td>
		</tr>
		<tr>
			<td>StringDisplayImpl</td>
			<td>&#39;문자열을 사용하여 표시한다&#39;는 기능 추가 클래스</td>
		</tr>
		<tr>
			<td colspan="1">&nbsp;</td>
			<td>Main</td>
			<td>동작 테스트용 클래스</td>
		</tr>
	</tbody>
</table>


<br/><br/>
### ✔ 브리지 패턴 예제
🔻 기능 클래스 계층
```java
package StructuralPattern.Bridge;

public class Display {
	// impl필드는 Display의 구현을 나타내는 인스턴스로 두 클래스 계층의 '다리'역할
	private DisplayImpl impl;
	
	public Display(DisplayImpl impl) {
		this.impl = impl;
	}
	
	public void open() {
		impl.rawOpen();
	}
	
	public void print() {
		impl.rawPrint();
	}
	
	public void close() {
		impl.rawClose();
	}
	
	public final void display() {
		open();
		print();
		close();
	}
}
```

<br/><br/>
🔻 기능 추가
```java
package StructuralPattern.Bridge;

public class CountDisplay extends Display{

	public CountDisplay(DisplayImpl impl) {
		super(impl);
	}
	
	public void multiDisplay(int times) {
		open();
		for(int i = 0; i < times; i++) { // times회 반복해서 표시
			print();
		}
		close();
	}

}
```

<br/><br/>
🔻 구현 클래스 계층
```java
package StructuralPattern.Bridge;

public abstract class DisplayImpl {
	public abstract void rawOpen();
	public abstract void rawPrint();
	public abstract void rawClose();
}
```

> **구현클래스 계층의 최상위 클래스(추상 클래스)** <br/>
> rawOpen, rawPrint, rawClose는 Display의 open, print, close에 각각 대응하며 전처리, 표시, 후처리를 실행한다.


<br/><br/>
🔻 구체적인 구현 단계
```java
package StructuralPattern.Bridge;

public class StringDisplayImpl extends DisplayImpl{
	private String string; // 표시해야할 문자열
	private int width; // 바이트 단위로 계싼할 문자열의 '길이'
	
	public StringDisplayImpl(String string) {
		this.string = string;
		this.width = string.getBytes().length;	
		// ㄴ생성자에서 전달된 문자열 string의 바이트 단위의 길이를 필드에 기억해두고 나중에 사용한다
	}

	@Override
	public void rawOpen() {
		printLine();
	}

	@Override
	public void rawPrint() {
		System.out.println("|" + string + "|");    // 앞뒤에 "|" 를 붙여서 표시한다.
	}

	@Override
	public void rawClose() {
		printLine();
	}
	
	private void printLine() {
		System.out.print("+"); // 테두리의 모서리를 표현하는 "+" 마크를 표시한다.
		for(int i = 0; i < width; i++) {
			System.out.print("-"); // width개의 "-"를 표시해서 테두리 선으로 이용한다.
		}
		System.out.println("+"); // 테두리 모서리를 표시하는 "+" 마크를 표시한다.
	}

}
```
> **StringDisplayImpl클래스는 문자열을 표시하는 클래스** <br/>
> 단지 표시만 하는 것이 아니라 DisplayImpl 클래스의 하위 클래스로서<br/>
> rawOpen, rawPrint, rawClose의 구체적인 부분을 구현하고 있다.


<br/><br/>
🔻 Main클래스
```java
package StructuralPattern.Bridge;

public class BridgeMain {
  
	public static void main(String[] args) {
      // Main클래스는 앞에서 설명한 네 개의 클래스를 조합해서 문자열을 표시한다.
		Display d1 = new Display(new StringDisplayImpl("Hello, Korea!"));
		Display d2 = new CountDisplay(new StringDisplayImpl("Hello, World!"));
		
		CountDisplay d3 = new CountDisplay(new StringDisplayImpl("Hello, Universe!"));
		
		d1.display();
		d2.display();
		d3.display();
		
		d3.multiDisplay(5);
	}
}
```

<br/><br/>
🔻 콘솔 결과창
```console
+-------------+
|Hello, Korea!|
+-------------+
+-------------+
|Hello, World!|
+-------------+
+----------------+
|Hello, Universe!|
+----------------+
+----------------+
|Hello, Universe!|
|Hello, Universe!|
|Hello, Universe!|
|Hello, Universe!|
|Hello, Universe!|
+----------------+
```



### ➕ Bridge 패턴의 핵심
* Bridge 패턴의 핵심은 ' 기능 클래스 계층'과 '구현 클래스 계층'을 분리하는 것.
* 이 두 개의 클래스 계층을 분리해 두면 각각의 클래스 계층을 독립적으로 확장할 수 있다.
* 기능을 추가하고 싶으면 기능의 클래스 계층에 클래스를 추가한다.<br/>
이때 구현의 클래스 계층은 전혀 수정할 필요가 없다. 새로 추가한 기능은 모든 구현에서 이용할 수 있다. 
* 예제 프로그램에서는 Main 클래스 내에서 Display나 CountDisplay의 인스턴스를 만들고<br/>그때 StringDisplayImpl의 인스턴스를 인수에게 전달했다.<br/>
만약, StringDisplayImpl 클래스 말고 다른 ...DisplayImpl 클래스를 만들었다고 가정하고<br/>
인스턴스를 Dsiplay나 CountDisplay에게 전달하면 그것으로 구현이 확실히 교체된다.


### ➕ 브리지 패턴과 어댑터 패턴의 차이
* 두 패턴 모두 Interface의 detail을 감추고자 하며, 구조적인 차이가 없다.
* 하지만 두 패턴은 서로 사용하고자 하는 목적의 차이가 분명하다.
	- 어댑터는 어떤 클래스의 인터페이스가 다른 코드에서 기대하는 것과 다를 때(기능은 같은 데, 함수명이 다를 때)<br/>어댑터를 중간에 두어 맞춰주는 것이다.
	- 브릿지는 추상과 구현을 분리하는 것이다.<br/>(추상 클래스는 추상 클래스 대로, 구현은 구현 대로 변경해도 서로 영향을 주지 않도록 한다.)
	- 어댑터는 결국 어떤 코드에 맞게끔 기존의 코드를 쓰기 위해 사용되고,<br/>브릿지는 확장성을 고려하여 미리 예상하여 bridge class를 구현해 코드 작성시 사용되어진다.
