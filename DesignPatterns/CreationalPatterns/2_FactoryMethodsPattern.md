# 🛠 Factory Methods Patterns(팩토리 메소드 패턴)
### ✔ 팩토리메소드 패턴이란?
* 객체 생성을 **캡슐화**하는 패턴
* 객체를 생성하기 위해 인터페이스를 정의하지만, 어떤 클래스의 **인스턴스**를 **생성**할지에 대한 **결정은<br>**
**서브 클래스**가 내리도록 하는 패턴으로 가상 생성자(Virtual Constructor) 패턴으로도 불림

<br/><br/>
### ✔ 팩토리 메소드 패턴을 쓰는 이유
* 객체 생성 코드를 분리하여 클라이언트 코드와 **결합도(의존성)**을 낮춤 → 코드 변경 시, 객체 생성 클래스만 수정
* 인터페이스를 바탕으로 **유연성**과 **확장성**이 뛰어난 코드 제작 가능
* 객체 자료형이 하위 클래스에 의해 결정 → 확장 용이(상위 클래스에서는 그 객체에 대한 정확한 타입을 몰라도 됨)
* 객체 생성 책임을 몇 개의 서브클래스 중 하나에게 위임하고, 어떤 서브 클래스가 위임자인지에 대한 정보를 최소화
* **의존 관계 역전 원칙** 성립
> **의존 관계 역전 원칙(DIP, Dependency Inversion Principle)**<br/>
> 의존 관계를 맺을 때, 변화하기 쉬운 것보다 변화하기 어려운 것에 의존해야 한다는 원칙.<br/>
> 변화하기 쉬운 것(구체적인 것): 클래스, 서브 클래스, <br/>
> 변화하기 어려운 것(추상적인 것): 추상 클래스, 인터페이스


<br/><br/>
### ✔ 팩토리 메소드 패턴 단점
* 새로 생성할 객체의 종류가 늘어날 때마다 클래스가 많아짐

<br/><br/>
### ✔ 팩토리 메소드 패턴 예제 구조
![그림1](https://user-images.githubusercontent.com/54934681/104092722-2fdf4e80-52c9-11eb-9ff2-c8c0bdb72a73.png)


<br/><br/>
### ✔ 팩토리 메소드 패턴 예제
🔻 뒷단 구성
```java
package CreationalPattern.FactoryMethods;

// Shape.java
public interface Shape {
  void draw();
}
```

<br/><br/>
🔻 먼저, Factory에서 만들어낼 개체들을 정의한다.
```java
package CreationalPattern.FactoryMethods;

//Circle.java
public class Circle implements Shape {
  @Override
  public void draw() {
    System.out.println("Circle - draw() Method.");
  }
}
```
```java
package CreationalPattern.FactoryMethods;

//Rectangle.java
public class Rectangle implements Shape {
  @Override
  public void draw() {
    System.out.println("Rectangle - draw() Method.");
  }
}
```
```java
package CreationalPattern.FactoryMethods;

//Square.java
public class Square implements Shape {
  @Override
  public void draw() {
    System.out.println("Square - draw() Method.");
  }
}
```

<br/><br/>
🔻 객체들을 만들어 내보낼 팩토리를 정의한다.
```java
package CreationalPattern.FactoryMethods;

public class ShapeFactory {
  // 팩토리메소드 - 객체 생성 후 반환
  public Shape getShape(String shapeType) {
    if(shapeType == null) {
      return null;
    }
    if(shapeType.equalsIgnoreCase("CIRCLE")) {
      return new Circle();
    }
    if(shapeType.equalsIgnoreCase("RECTANGLE")) {
      return new Rectangle();
    }
    if(shapeType.equalsIgnoreCase("SQUARE")) {
      return new Square();
    }
    return null;
  }
}
```

<br/><br/>
🔻 메인에서 사용자는 다음과 같이 사용할 수 있다
```java
package CreationalPattern.FactoryMethods;

public class FactoryPatternTest {
  
  public static void main(String[] args) {
    // 팩토리 클래스에서 객쳋 생성 후 반환
    ShapeFactory shapeFactory = new ShapeFactory();
    
    Shape shape1 = shapeFactory.getShape("CIRCLE");
    shape1.draw(); // Circle 메소드 호출
    
    Shape shape2 = shapeFactory.getShape("RECTANGLE");
    shape2.draw(); // Rectangle 메소드 호출
    
    Shape shape3 = shapeFactory.getShape("SQUARE");
    shape3.draw(); // Square 메소드 호출
  }
}
```

<br/><br/>
🔻 콘솔 결과창
```console
Circle - draw() Method.
Rectangle - draw() Method.
Square - draw() Method.
```

