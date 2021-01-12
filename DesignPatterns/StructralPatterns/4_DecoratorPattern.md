# 🛠 Decorator Pattern(데코레이터 패턴)
### ✔ 데코레이터 패턴이란?
* 중심이 되는 객체에 **부가적인 기능을 동적으로 추가**하고자 할 때 사용하는 패턴
* 서브클래스에 유연성을 제공하여 **소스를 변경하지 않고도 부가 기능이 확장**되어 실행될 수 있도록 하는 패턴
* 데코레이터는 자신이 장식하고 있는 객체에게 어떤 행동을 위임하는 것 외에 원하는 추가적인 작업을 수행할 수 있고<br/>
객체는 언제든지 감쌀 수 있기 때문에 실행에 필요한 데코레이터를 마음대로 적용할 수 있음

<br/><br/>
### ✔ 데코레이터 패턴을 쓰는 이유
* 상황과 용도에 맞게 객체에 동적으로 새로운 책임을 추가할 수 있음
* 간단하게 **객체에 동적으로 기능추가** 가능

<br/><br/>
### ✔ 데코레이터 패턴 단점
* 자잘한 데코레이터 클래스들이 계속 추가되어 **클래스가 많아질 수 있음**
* 겹겹이 에워싸고 있기 때문에 객체의 **정체를 알기 힘들고** 복잡해질 수 있음

<br/><br/>
### ✔ 데코레이터 패턴 예제 구조
![캡처4](https://user-images.githubusercontent.com/54934681/104276758-dd7c7880-54e8-11eb-8281-b6d1d5655b87.PNG)
* Component: ConcreteComponent와 Decorator가 구현할 인터페이스. 두 객체를 동등하게 다루기 위해 존재
* ConcreteComponent: Decorator를 받을 객체. 즉, 기능 추가를 받을 기본 객체
* Decorator: Decorate를 할 객체의 추상 클래스. 즉, 기능추가를 할 객체는 이 객체를 상속받음
* ConcreteDecorator: Decorator를 상속받아 구현할 다양한 기능 객체. ConcreteComponent에 추가되기 위해 만들어짐

<br/><br/>
### ✔ 데코레이터 패턴 예제
* 크리스마스 트리에 다양한 장식을 하고싶다고 해보자.<br/>
* 기본 크리스마스 트리가 있고, 장식으로는 깜빡이는 불이나, 꽃들을 생각해볼 수 있다.
<br/>

🔻 Component
```java
package StructuralPattern.Decorator;

public interface ChristmasTree {
	String decorate();
}
```
`먼저 크리스마스 트리와 장식을 각각 추상화 해야할 것이다. 이들을 같은 인터페이스로 공통 추상화한다.`

<br/><br/>
🔻 ConcreteComponent
```java
package StructuralPattern.Decorator;

public class DefaultChristmasTree implements ChristmasTree {

	@Override
	public String decorate() {
		return "Christmas Tree";
	}
}
```
`먼저 기본 트리스마스 트리를 구체화 한다. (아무 장식 없는 그냥 나무)`


<br/><br/>
🔻 Decorator
```java
package StructuralPattern.Decorator;

public abstract class TreeDecorator implements ChristmasTree{
	private ChristmasTree christmasTree;
	
	public TreeDecorator(ChristmasTree christmasTree) {
		this.christmasTree = christmasTree;
	}
	
	@Override
	public String decorate() {
		return christmasTree.decorate();
	}
}
```
`트리에 올라갈 장식을 추상화 한다. 
구체적인 장식들, 즉 장식용 불이나 꽃은 이 추상클래스를 상속받아 구현하면 된다.`


<br/><br/>
🔻 ConcreteDecorator
```java
package StructuralPattern.Decorator;

public class Lights extends TreeDecorator{

	public Lights(ChristmasTree christmasTree) {
		super(christmasTree);
	}
	
	public String addLights() {
		return " with Lights";
	}
	
	@Override
	public String decorate() {
		return super.decorate() + addLights();
	}
}
```
`장식으로 두를 불을 구체화 한다.`


<br/><br/>
🔻 마찬가지로 장식용 꽃도 비슷하게 구체화 한다.
```java
package StructuralPattern.Decorator;

public class Flowers extends TreeDecorator {

	public Flowers(ChristmasTree christmasTree) {
		super(christmasTree);
	}
	
	public String addFlowers() {
		return " with Flowers";
	}
	
	@Override
	public String decorate() {
		return super.decorate() + addFlowers();
	}
}
```


<br/><br/>
🔻 Main 클래스
```java
package StructuralPattern.Decorator;

public class DecoratorMain {

	public static void main(String[] args) {
		//Christmas tree만 있음
		ChristmasTree tree = new DefaultChristmasTree();
		System.out.println(tree.decorate());
		
		// Christmas tree + Lights
		ChristmasTree treeWithLights = new Lights(new DefaultChristmasTree());
		System.out.println(treeWithLights.decorate());
		
		//Christmas tree + Lights + Flowers
		ChristmasTree treeWithLightsAndFlowers = new Flowers(new Lights(new DefaultChristmasTree()));
		System.out.println(treeWithLightsAndFlowers.decorate());
	}
}
```
> `기본 객체인 new DefaultChristmasTree() 에 기능 추가를 new Lights(new DefaultChristmasTree()); 와 같이 동적인 방식으로 하고 있다.`<br/>
> 이게 가능한 이유는 Decorator 객체의 생성자로 Component 를 받음으로써 Decorator 를 이어 붙일 수가 있고<br/>
> super를 통해 넘어오는 Component 의 operation(decorate()) 을 먼저 수행하기 때문이다. <br/>
> 이후 추가적인 장식(기능)을 만들고 싶으면 TreeDecorator 를 상속받아 위와 같은 꼴로 또 구현하면 된다.<br/>
> 즉, 새로운 기능을 유연하게 만들고 추가할 수 있다.


<br/><br/>
🔻 콘솔 결과창
```console
Christmas Tree
Christmas Tree with Lights
Christmas Tree with Lights with Flowers
```
