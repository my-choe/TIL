# 🛠 Flyweight Pattern(플라이웨이트 패턴)
### ✔ 플라이웨이트 패턴이란?
* FlyWeight 패턴은 이름 그대로 **더 가볍게 프로그래밍을 할 수 없을까**해서 만들어진 패턴
* 대규모의 작은 객체들을 효과적으로 사용하기 위해 본질적 상태(공유 가능)와 부가적 상태(공유 불가능)를 구분하여<br/>
  **불필요한 New를 생성하지 않도록** 하는 패턴
* 객체관리는 팩토리를 통해서 하며 객체들을 **중복없이 관리하기 위해 map 자료구조**를 활용
* 예시로, 서식이 있는 Text에서 문서 작성 시, 폰트/포인트를 pool에 넣고 복제하여 사용하다가 바뀔 때만 등록해서 사용하도록 구현

<br/><br/>
### ✔ 플라이웨이트 패턴을 쓰는 이유
* 작고 대량의 객체들을 공유하는 개념으로, 이미 pool에 있다면 있는 것을 사용하고,<br/>
  없는 경우에는 집어 넣어 사용하므로 공유 객체에 의해 **메모리에 로드 되는 객체의 개수를 줄일 수 있음**
* 여러 ‘가상’ 객체의 상태를 **한 곳에 집중**시켜놓을 수 있다.

<br/><br/>
### ✔ 플라이웨이트 패턴 단점
* 특정 인스턴스만 다른 인스턴스처럼 동작하도록 하는 것이 불가능
* 공통된 자원이기 떄문에 공통된 부분을 싱글톤처럼 사용하고, 서로 다른 일부 객체는 다르게 사용해야 함
* 객체 값을 변경하면 공유받은 ‘가상’객체를 사용하는 곳에 영향을 줄 수 있음

<br/><br/>
### ✔ 플라이웨이트 패턴 구조
![캡처5](https://user-images.githubusercontent.com/54934681/104279035-f9821900-54ec-11eb-9b91-6435012ecdfd.PNG)

<br/><br/>
### ✔ 플라이웨이트 패턴 예제
🔻 Shape 인터페이스
```java
package StructuralPattern.Flyweight;

public interface Shape {
	public void draw();
}
```
`해당 패턴을 적용할(공유로 사용될) 클래스들의 인터페이스를 작성한다.`

<br/><br/>
🔻 Circle 클래스
```java
package StructuralPattern.Flyweight;

public class Circle implements Shape {
	private String color;
	private int x;
	private int y;
	private int radius;
	
	public Circle(String color) {
		this.color = color;
	}
	
	public void setColor(String color) {
		this.color = color;
	}

	public void setX(int x) {
		this.x = x;
	}

	public void setY(int y) {
		this.y = y;
	}

	public void setRadius(int radius) {
		this.radius = radius;
	}
	
	@Override
	public void draw() {
		System.out.println("Circle [color=" + color + ", x=" 
					+ x + ", y=" + y + ", radius=" + radius + "]");
	}
}
```
`ConcreteFlyweight에 해당하며 인터페이스의 내용을 정의하고 필요한 속성을 가질 수 있다.`

<br/><br/>
🔻 ShapeFactory 클래스
```java
package StructuralPattern.Flyweight;

import java.util.HashMap;

public class ShapeFactory {
	private static final HashMap<String, Circle> circleMap = new HashMap<>();
	
	public static Shape getCircle(String color) {
		Circle circle = (Circle)circleMap.get(color);
		
		if(circle == null) {
			circle = new Circle(color);
			circleMap.put(color, circle);
			System.out.println("==== 새로운 객체 생성 : " + color + "색 Circle ====");
		}
		return circle;
	}
}
```
`getCircle() 메소드를 통해 객체의 생성 또는 공유 역할을 담당하며 클라이언트에게 응답해준다.`

<br/><br/>
🔻 Main 클래스
```java
package StructuralPattern.Flyweight;

public class FlyweightMain {

	public static void main(String[] args) {
		String[] colors = {"Red", "Green", "Blue", "Yellow"};
		
		for(int i = 0; i < 10; i++) {
			Circle circle = (Circle)ShapeFactory.getCircle(colors[(int)(Math.random()*4)]);
			circle.setX((int)(Math.random()*100));
			circle.setY((int)(Math.random()*4));
			circle.setRadius((int)(Math.random()*10));
			circle.draw();
		}
	}
}
```

<br/><br/>
🔻 콘솔 결과창
```console
==== 새로운 객체 생성 : Blue색 Circle ====
Circle [color=Blue, x=38, y=1, radius=5]
==== 새로운 객체 생성 : Green색 Circle ====
Circle [color=Green, x=14, y=2, radius=8]
Circle [color=Blue, x=8, y=1, radius=3]
Circle [color=Blue, x=45, y=0, radius=1]
==== 새로운 객체 생성 : Red색 Circle ====
Circle [color=Red, x=41, y=3, radius=7]
Circle [color=Red, x=1, y=1, radius=6]
Circle [color=Blue, x=25, y=0, radius=0]
Circle [color=Red, x=50, y=0, radius=1]
Circle [color=Green, x=97, y=2, radius=4]
Circle [color=Red, x=75, y=1, radius=1]
```
`로직에 의해 같은 색상의 원은 1개만 생성되며 생성된 객체를 공유하는 걸 확인할 수 있다.`
