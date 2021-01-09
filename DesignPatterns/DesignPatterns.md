# 🛠 Design Patterns(디자인 패턴)
### 디자인 패턴이란?

소프트웨어 공학론 안의 **좋은 코드**를 설계하기 위한 일종의 설계 디자인 방법론으로<br/>
자주 사용하는 설계 형태를 정형화해서 이를 유형별 설계 템플릿으로 만들어둔 것을 말한다.<br/>
> **좋은 코드란?**<br/>
> 가독성, 간결함 등 여러 방면이 있겠지만, 디자인 패턴에서는 설계적 관점에서의 좋은 코드를 말한다.<br/>
> 즉, 확장과 수정에 용이하여 설계 이후에도 추가적인 유지보수에 비용이 적게 들어가는 코드를 말한다.<br/>
> 객체지향적으로 생각하면, 추구해야 할 설계방향은 다음과 같다.<br/>
> **"객체 간 응집도는 높이고, 결합도는 낮게. 요구사항 변경 시 코드 변경을 최소화하는 방향으로."**

<br/><br/>
### 디자인패턴 장점
* **개발자(설계자)간의 원활한 의사소통**<br/>
  설계자들은 여러가지 디자인 패턴 특성을 잘 알고 있어 문제 해결을 위해 충분한 해결책 논의 가능<br/>
  
* **소프트웨어 구조 파악 용이**<br/>
  어떤 디자인패턴이 사용되었는지 알면 소프트웨어 전체 구조를 쉽게 파악할 수 있음<br/>
  
* **재사용을 통한 개발 시간 단축**<br/>
  만들어놓은 디자인패턴을 사용하면 처음부터 만드는 수고를 덜기 때문에 개발 시간을 줄일 수 있음<br/>
  
* **설계 변경 요청에 대한 유연한 대처**<br/>
  사용자의 지속적인 기능 추가 등 설계 변경 요청에 대해 쉽고 빠르게 대처할 수 있음<br/><br/>
  
  
### 디자인패턴 단점
* **우회 경로**<br/>
  유연성을 확보하기 위해 우회경로를 한 단계 더 거침→디자인은 복잡해지고 수행 성능에 부정적 영향 가능성 있음<br/>
  
* **초기 투자 비용 부담**<br/>
  디자인패턴을 사용하지 않는 경우보다 초기에 시간과 노력을 많이 투자해야 함<br/>
  
* **패턴 간 상충 문제**<br/>
  여러 명의 개발자를 거친 코드인 경우, 설계가 정확히 되어있지 않다면 패턴 간 상충되는 문제 발생 가능<br/><br/>
  
  
  ### 디자인 패턴 종류
  Gof(Gang of Four) 디자인 패턴이라고 불리며, 4명의 유명한 개발자들에 의해 고안되었다.<br/>

<table border="1" cellpadding="0" cellspacing="0">
	<thead>
		<tr>
			<th colspan="2" rowspan="1" scope="col">구분</th>
			<th scope="col">생성패턴(Creational Patterns)</th>
			<th scope="col">구조패턴(Structral Patterns)</th>
			<th scope="col">행동패턴(Behavior Patterns)</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td colspan="2" rowspan="1" align="center">의미</td>
			<td>
        - 객체의 생성방식을 결정하는 패턴<br/>
        - 객체생성과정의 유연성을 높이고<br/>코드 유지를 쉽게 함
      </td>
			<td>
        - 프로그램 구조에 관련된 패턴<br/>
        - 프로그램 내의 자료구조나 인터페이스<br/>
        구조 등 프로그램 구조설계 시 활용될 수<br/>
        있는 패턴
      </td>
			<td>
        - 반복적으로 사용되는 객체들의<br/>
        상호작용을 패턴화 해놓은 것
      </td>
		</tr>
		<tr>
			<td colspan="1" rowspan="2">범위</td>
			<td>클래스</td>
			<td>- 팩토리메서드(Factory Methods)</td>
			<td>- 어댑터(Adapter)</td>
			<td>
        - 인터프리터(Interpreter)<br/>
        - 템플릿메서드(Template Methods)
      </td>
		</tr>
		<tr>
			<td>객체</td>
			<td>
        - 싱글톤(Singleton)<br/>
        - 추상팩토리(Abstract Factory)<br/>
        - 빌더(Builder)<br/>
        - 프로토타입(ProtoType)
      </td>
			<td>
        - 브리지(Bridge)<br/>
        - 컴퍼지트(Composite)<br/>
        - 데코레이터(Decorator)<br/>
        - 퍼사드(Facade)<br/>
        - 플라이웨이트(Flyweight)<br/>
        - 프록시(Proxy)
      </td>
			<td>
        - 스트레티지(Strategy)<br/>
        - 옵저버(Observer)<br/>
        - 스테이트(State)<br/>
        - 비지터(Visitor)<br/>
        - 커맨드(Command)<br/>
        - 이터레이터(Iterator)<br/>
        - 미디에이터(Mediator)<br/>
        - 메멘토(Memento)<br/>
        - 책임연쇄(Chain of Responsibility)
      </td>
		</tr>
	</tbody>
</table>

  
  
