# 🛠 Abstract Factory Pattern(추상팩토리 패턴)
### ✔ 추상팩토리 패턴이란?
* 상세화된 서브클래스를 정의하지 않고도, 서로 관련성이 있거나 독립적인 여러 객체의 집합을 생성할 수 있는 인터페이스를 제공하는 패턴
* 추상팩토리 패턴은 클라이언트에서 추상 인터페이스를 통해 일련의 제품들을 공급받을 수 있음
* 이때, 실제로 어떤 제품이 생산되는지는 전혀 알 필요도 없기에 팩토리에서 생산되는 제품을 분리시킬 수 있음

<br/><br/>
### ✔ 추상팩토리 패턴을 쓰는 이유
* 팩토리 메소드 패턴을 쓰던 상황에서 팩토리의 종류를 늘려야 할 때
* 객체가 생성되거나 구성/표현되는 방식과 무관하게 시스템을 독립적으로 만들고자 할 때
* 여러 제품군 중 하나를 선택해서 시스템을 설정해야 하고 한번 구성한 제품을 다른 것으로 대체할 수 있을 때
* 관련된 제품 객체들이 함께 사용되도록 설계 되었고, 이 부분에 대한 제약이 외부에도 지켜지도록 하고싶을 때
* 제품에 대한 클래스 라이브러리를 제공하고, 그들의 구현이 아닌 인터페이스를 노출시키고 싶을 때


<br/><br/>
### ✔ 추상팩토리 패턴 단점
*  새로운 종류의 제품을 제공하기 어려움 → 하나의 팩토리 기본 세부 사항이 변경되면 모든 팩토리에 대해 인터페이스를 수정해야 함


<br/><br/>
### ✔ 추상팩토리 패턴 예제 구조
![그림2](https://user-images.githubusercontent.com/54934681/104093358-7d5dba80-52cd-11eb-8173-4afe84702a65.png)



<br/><br/>
### ✔ 추상팩토리 패턴 예제
🔻 팩토리의 팩토리인 상위 팩토리는 추상 클래스로 다음과 같이 정의할 수 있다.
```java
package CreationalPattern.AbstractFactory;

public abstract class AbstractFactory {
  abstract Shape getShape(String shapeType);
}
```

<br/><br/>
🔻 구체적인 팩토리들은 위의 추상클래스(AbstractFactory)를 상속받아 구현한다.
```java
package CreationalPattern.AbstractFactory;

public class ShapeFactory extends AbstractFactory {
  @Override
  Shape getShape(String shapeType) {
    if(shapeType.equalsIgnoreCase("RECTANGLE")) {
      return new Rectangle();
    }else if(shapeType.equalsIgnoreCase("SQUARE")) {
      return new Square();
    }
    return null;
  }
}
```
```java
package CreationalPattern.AbstractFactory;

public class RoundedShapeFactory extends AbstractFactory {
  @Override
  Shape getShape(String shapeType) {
    if(shapeType.equalsIgnoreCase("RECTANGLE")) {
      return new RoundedRectangle(); // 위 클래스와 이 부분이 다름
    }else if(shapeType.equalsIgnoreCase("SQUARE")) {
      return new RoundedSquare(); // 위 클래스와 이 부분이 다름
    }
    return null;
  }
}
```

<br/><br/>
🔻 위에서 만든 팩토리들은 다음 FactoryProducer를 통해 인스턴스로 만들어진다.
```java
package CreationalPattern.AbstractFactory;

public class FactoryProducer {
  public static AbstractFactory getFactory(boolean rounded) {
    if (rounded) {
      return new RounedSahpeFactory();
    } else {
      return new ShapeFactory();
    }
  }
}
```

<br/><br/>
🔻 클라이언트는 다음과 같이 사용할 수 있다.
```java
package CreationalPattern.AbstractFactory;

public class AbstractFactoryPatternDemo {
  
  public static void main(String[] args) {
    // 팩토리의 팩토리인 FactoryProducer를 통해 구체적인 팩토리 shapeFactory를 얻는다.
    AbstractFactory shapeFactory = FactoryProducer.getFactory(false);
    
    // shapeFactory로 구체적인 Product를 만든다(팩토리 메소드와 동일)
    Shape shape1 = shapeFactory.getShape("RECTANGLE");
    shape1.draw();
    
    Shape shape2 = shapeFactory.getShape("SQUARE");
    shape2.draw();
    
    // 이번엔 FactoryProducer를 통해 구체적인 팩토리 shapeFactory1을 얻는다.
    AbstractFactory shapeFactory1 = FactoryProducer.getFactory(true);
    
    // 위와 동일하지만, 이번엔 shapeFactory1로 Product를 만든다.
    Shape shape3 = shapeFactory1.getShape("RECTANGLE");
    shape3.draw();
    
    Shape shape4 = shapeFactory1.getShape("SQUARE");
    shape4.draw();
  }
}
```

<br/><br/>
🔻 콘솔 결과창
```console
Rectangle - draw() Method.
Square - draw() Method.
Rounded Rectangle - draw() Method.
Rounded Square - draw() Method.
```

