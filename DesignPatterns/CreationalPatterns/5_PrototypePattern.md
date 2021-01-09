# 🛠 Prototype Pattern(프로토타입 패턴)
### ✔ 프로토타입 패턴이란?
* '프로토타입'이란 주로 실제 제품을 만들기에 앞서 **대략적인 샘플** 정도의 의미로 사용되는 단어
* 객체를 생성하는데 비용(시간과 자원)이 많이 들고, 비슷한 객체가 이미 있는 경우에 사용되는패턴
* 생성할 객체들의 타입이 **프로토타입인 인스턴스로부터 결정**되도록 하며, 인스턴스는 새 객체를 만들기 위해 **자신을 복제**(clone)하게 됨
* 프로토타입 패턴은 **Original 객체를 새로운 객체에 복사**하여 필요에 따라 수정하는 매커니즘 제공
* 이 패턴은 **Java**에서 복사를 위해 제공하는 **clone**()을 이용함

<br/><br/>
### ✔ 프로토타입 패턴을 쓰는 이유
* 객체를 생성해주기 위한 **별도의 객체 생성 클래스가 불필요**함
* 객체의 각 부분을 조합해서 생성되는 형태에도 적용 가능
* Object 생성이 높은 비용으로 수많은 요청을 하는 경우 또는 비슷한 Object를 지속적으로 생성해야 할 때<br/>
이들을 미리 프로토타입으로 초기화해두고, 나중에 이를 복사해서 사용하는 것이 편함.


<br/><br/>
### ✔ 프로토타입 패턴 단점
* 생성될 객체들의 자료형인 클래스들이 **모두 clone() 메소드를 구현**해야 함

<br/><br/>
### ✔ 프로토타입 패턴 예제 구조
![그림3](https://user-images.githubusercontent.com/54934681/104094535-cc5b1e00-52d4-11eb-90d7-86511028b8dc.png)



<br/><br/>
### ✔ 프로토타입 패턴 예제
🔻 Clonable 인터페이스를 구현하는 추상클래스
```java
public abstract class Shape implements Cloneable {
  private String id;
  private String type;
  
  abstract void draw();

  public String getId() {
    return id;
  }
  
  public Integer getType() {
    return type;
  }
  
  public void setId(String id) {
    this.id = id;
  }
  
  public Object clone() {
    Object clone = null;
    try {
      clone = super.clone();
    } catch(Exception e) {
      e.printStackTrace();
    }
    return clone;
  }
}
```


<br/><br/>
🔻 Shape 클래스를 확장하는 구체적인 클래스
```java
public class Rectangle extends Shape {
  // 위 클래스를 확장하는 구체적인 클래스
  public Rectangle() {
    type = "Rectangle";
  }
  
  @Override
  public void draw() {
    System.out.println("Inside Rectangle::draw() method.");
  }
}
```

```java
public class Square extends Shape {
  // 위 클래스를 확장하는 구체적인 클래스
  public Square() {
    type = "Square";
  }
  
  @Override
  public void draw() {
    System.out.println("Inside Square::draw() method.");
  }
}
```

```java
public class Circle extends Shape {
  // 위 클래스를 확장하는 구체적인 클래스
  public Circle() {
    type = "Circle";
  }
  
  @Override
  public void draw() {
    System.out.println("Inside Circle::draw() method.");
  }
}
```

<br/><br/>
🔻 데이터베이스에서 구체적인 클래스를 가져와 Hashtable에 저장하는 클래스<br>

```java
public class ShapeCache {
  private static Hashtable<String, Shape> shapeMap = new Hashtable<String, Shape>();
  
  // 각 Shape마다 데이터베이스 쿼리 실행 및 shape 생성
  // shapeMap.put(shapeKey, shape);
  // 아래의 예시에서는 임의로 직접 추가하였음
  public static void loadCache() {
    Circle circle = new Circle();
    circle.setId("1");
    shapeMap.put(circle.getId(), circle);
    
    Square square = new Square();
    square.setId("2");
    shapeMap.put(square.getId(), square);
    
    Rectangle rectangle = new Rectangle();
    rectangle.setId("2");
    shapeMap.put(rectangle.getId(), rectangle);
  }
  
  public static Shape getShape(String shapeType) {
    Shape cachedShape = shapeMap.get(shapeType);
    return (Shape) cachedShape.clone();
  }
}
```

<br/><br/>
🔻 클라이언트는 다음과 같이 사용할 수 있다
```java
public class ProtoTypePatternDemo {
  
  public static void main(String[] args) {
    ShapeCache.loadCache();
    
    Shape cloneShape1 = ShapeCache.getShape("1");
    System.out.println("cloneShape1 Type : " + cloneShape1.getType());
    cloneShape1.draw();
    
    Shape cloneShape2 = ShapeCache.getShape("2");
    System.out.println("cloneShape2 Type : " + cloneShape2.getType());
    cloneShape2.draw();
    
    Shape cloneShape3 = ShapeCache.getShape("3");
    System.out.println("cloneShape3 Type : " + cloneShape3.getType());
    cloneShape3.draw();
  }
}
```


<br/><br/>
🔻 콘솔 결과창
```console
clonedSahpe1 Type : Circle
Inside Circle::draw() method.
clonedSahpe2 Type : Square
Inside Square::draw() method.
clonedSahpe3 Type : Rectangle
Inside Rectangle::draw() method.
```

