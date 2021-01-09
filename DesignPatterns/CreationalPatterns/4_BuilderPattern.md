# 🛠 Builder Pattern(빌더 패턴)
### ✔ 빌더 패턴이란?
* 생성자에 들어갈 매개변수가 만든 적든 차례차례 매개변수를 받아들이고, <br/>
모든 매개변수를 받은 뒤 이 변수들을 통합해서 한번에 사용하는 패턴.
* 복잡한 개게를 생성 및 표현하는 방법을 정의하는 클래스를 별도로 분리하여, <br/>
서로 다른 표현이더라도 이를 생성할 수 있는 동일한 절차를 제공하는 패턴

<br/><br/>
### ✔ 빌더 패턴을 쓰는 이유
* 제품에 대한 내부 표현을 다양하게 변화할 수 있음
* 생성과 표현에 필요한 코드를 분리할 수 있음
* 복합 객체 생성 절차를 좀 더 세밀하게 나눌 수 있음


<br/><br/>
### ✔ 빌더 패턴 단점
* 추가적인 빌더 클래스를 구현해야 함


<br/><br/>
### ✔ 빌더 패턴 예제
```java
public class PersonInfo {
  private String name;
  private Integer age;
  private String favoriteColor;
  private String favoriteAnimal;
  private Integer favoriteNumber;
  
  public PersonInfo(String name, Integer age, String favoriteColor, String favoriteNumber) {
    this.name = name;
    this.age = age;
    this.favoriteColor = favoriteColor;
    this.favoriteAnimal = favoriteAnimal;
    this.favoriteNumber = favoriteNumber;
  }
  
  public String getName() {
    return name;
  }
  
  public Integer getAge() {
    return age;
  }
  
  public String getFavoriteColor() {
    return favoriteColor;
  }
  
  public String getFavoriteAnimal() {
    return favoriteAnimal;
  }
  
  public String getFavoriteNumber() {
    return favoriteNumber;
  }
  
  public String getPersonInfo() {
    String personInfo = String.format("name:%s, age:%d, favoriteColor:%s, favoriteAnimal:%s, favoriteNumber:%d,
                                      name, age, favoriteColor, favoriteAnimal, favoriteNumber);
    return personInfo;
  }
}
```
🔺 한 사람의 정보를 담기 위한 클래스.<br/>
    하지만 setter 메소드는 존재할 수 없고 오로지 생성자를 통해서만 데이터를 입력받는다는 가정으로 만든 클래스이다.<br/>
    생성자를 보면 모든 매개변수를 받도록 하고 있다. 하지만 어떤 사람들은 모든 데이터가 없을 수도 있다.


<br/><br/>
🔻 예를 들어 "이름"과 나이만 알고있는 사람의 경우 다음 처럼 객체를 만들어내야 할 것이다.
```java
new PersonInfo("홍길동", 20, null, null, null);
```

<br/><br/>
🔻 하지만 위의 경우는 가독성이 좋지 않으므로 추가 생성자를 만들어 처리한다.
```java
public PersonInfo(String name, Integer age) {
  this(name, age, null, null, null);
}
```

<br/><br/>
🔻 하지만 위의 경우, 이름만 있다거나 좋아하는 동물만 있다거나 하는 새로운 유형의 정보가 들어온다면?<br/>
    그때마다 새로운 생성자를 만들어줘야할 뿐만 아니라 데이터를 입력하는 순서가 달라지면 코드상 문제가 발생한다.
```java
new PersonInfo("cat", 20, "홍길동", null, null);
```

<br/><br/>
#### 🔧 **빌더 패턴을 통해 해결해야 하는 것** 🔨
* 불필요한 생성자를 만들지 않고 객체를 만든다.
* 데이터 순서에 상관 없이 객체를 만들어 낸다.
* 사용자가 봤을 때 명시적이고 이해할 수 있어야 한다.
→ 빌더 패턴을 적용한 빌더 클래스가 필요함.<br/><br/>

🔻 하단의 빌더 클래스를 사용하면 PersonInfo 객체를 손쉽고 헷갈리지 않게 만들어낼 수 있다.<br/>
```java
// PersonInfoBuilder.java
public class PersonInfoBuilder {
  private String name;
  private Integer age;
  private String favoriteColor;
  private String favoriteAnimal;
  private Integer favoriteNumber;
  
  public PersonInfoBuilder setName(String name) {
    this.name = name;
    return this;
  }
  
  public PersonInfoBuilder setAge(Integer age) {
    this.age = age;
    return this;
  }
  
  public PersonInfoBuilder setFavoriteColor(String favoriteColor) {
    this.favoriteColor = favoriteColor;
    return this;
  }
  
  public PersonInfoBuilder setFavoriteAnimal(String favoriteAnimal) {
    this.favoriteAnimal = favoriteAnimal;
    return this;
  }
  
  public PersonInfoBuilder setFavoriteNumber(String favoriteNumber) {
    this.favoriteNumber = favoriteNumber;
    return this;
  }
  
  public PersonInfo build() {
    PersonInfo personInfo = new PersonInfo(name, age, favoriteColor, favoriteAnimal, favoriteNumber)
    return personInfo;
  }
}
```


<br/><br/>
🔻 빌더 사용
```java
public class BuilderPatternDemo {
  
  public static void main(String[] args) {
    // 빌더 객체 생성
    PersonInfoBuilder personInfoBuilder = new PersonInfoBuilder();
    
    PersonInfo result = PersonInfoBuilder
                        .setName("홍길동")
                        .setAge(29)
                        .setFavoriteColor("purple")
                        .setFavoriteAnimal("cat")
                        .setName("이순신") // 다시 같은 메소드를 호출한다면 나중에 호출한 값이 들어간다.
                        .setFavoriteNumber(14)
                        // 마지막에 .build()메소드를 호출해서 최종적인 결과물을 만들어 반환한다.
                        .build();
                        
     System.out.println(result.getPersonInfo());
  }
}
```


<br/><br/>
🔻 콘솔 결과창
```console
name:이순신, age:29, favoriteColor:purple, favoriteAnimal:cat, favoriteNumber:14
```

`사용자 입장에서 PersonInfo 객체를 만들어 낼 때 PersonInfoBuilder클래스를 이용한다면 더 명확하게 이해하고 만들어낼 수 있을 것이다.`

