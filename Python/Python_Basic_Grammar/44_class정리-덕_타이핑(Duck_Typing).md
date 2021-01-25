# 📝 44 class 정리 - 덕 타이핑(Duck Typing)
## 1. 덕 타이핑(Duck Typing 이란?)
* Duck Typing - 'If it walks like a duck and it quacks like a duck, then it must be a duck' 해석해보면 '오리처럼 걷고, 오리처럼 꽥꽥거리면, 그것은 틀림없이 오리다.' 라는 뜻입니다.
* 파이썬과 같은 동적타입의 언어에서 본질적으로 다른클래스라도 객체의 적합성은 객체의 실제 유형이 아니라 특정 메소드와 속성의 존재에 의해 결정되는 것입니다.
* 예제 코드로 확인합니다. https://en.wikipedia.org/wiki/Duck_typing 예제 코드 발췌합니다.
* Parrot 클래스와 Airplane 클래스는 분명 서로 상속되거나 하는 그런 관계는 없습니다만, 내부에 동일한 메소드의 `fly()`메소드가 있는 것만으로 호출하는 `lift_off(entity)' 함수에서 fly가 정상적으로 실행됩니다.
* 마지막 Whale 클래스는 해당 `fly()` 메소드가 없기 때문에, `AttributeError`가 발생합니다.
* **속성과 메소드 존재에 의해 객체의 적합성이 결정된다.**
```python
class Parrot:
    def fly(self):
        print("Parrot flying")

class Airplane:
    def fly(self):
        print("Airplane flying")

class Whale:
    def swim(self):
        print("Whale swimming")

def lift_off(entity):
    entity.fly()

parrot = Parrot()
airplane = Airplane()
whale = Whale()

lift_off(parrot) # prints `Parrot flying`
lift_off(airplane) # prints `Airplane flying`
lift_off(whale) # Throws the error `'Whale' object has no attribute 'fly'`
```



<br/><br/><br/>
> 참고 : [wikidocs(파이썬 - 기본을 갈고 닦자!)](https://wikidocs.net/16076)
