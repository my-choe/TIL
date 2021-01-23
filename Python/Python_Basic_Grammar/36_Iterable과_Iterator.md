# 📝 36 Iterable 과 Iterator

## 1. Iterable 과 Iterator
### 1-1 Iterable
* iterable 객체 - 반복 가능한 객체
* 대표적으로 iterable한 타입 - list, dict, set, str, bytes, tuple, range
* 17. for in 반복문, Range, enumerate 에서 iterable한 타입과 iterable한 타입을 확인하는 방법이 있습니다.
<br/><br/>

1-2 Iterator
* iterator 객체 - 값을 차례대로 꺼낼 수 있는 객체입니다.
* iterator는 iterable한 객체를 내장함수 또는 iterable객체의 메소드로 객체를 생성할 수 있습니다.
* 파이썬 내장함수 ₩iter()₩를 사용해 iterator 객체를 만들어봅니다. REPL을 실행합니다.
```python
>>> a = [1, 2, 3]
>>> a_iter = iter(a)
>>> type(a_iter)
<class 'list_iterator'>
```
<br/>

* iterable객체는 매직메소드 __iter__ 메소드를 가지고 있습니다. 이 메소드로 iterator를 만들어보겠습니다.
```python
>>> b = {1, 2, 3}
>>> dir(b)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> b_iter = b.__iter__()
>>> type(b_iter)
<class 'set_iterator'>
```
<br/>

* iterator가 값을 차례대로 꺼낼 수 있는 객체라는 것의 의미를 한번 코드로 살펴봅니다.
* next내장함수를 사용할때 마다 첫번째, 두번째, 세번째 값이 출력됩니다.
* 네번째 실행에서는 ₩StopIteration₩ 이라는 예외가 발생합니다.
```python
>>> next(a_iter)
1
>>> next(a_iter)
2
>>> next(a_iter)
3
>>> next(a_iter)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> 
```
<br/>

* iterator 매직 메소드 '**next**'를 통해 하나씩 값을 꺼내봅니다.
```python
>>> b_iter.__next__()
1
>>> b_iter.__next__()
2
>>> b_iter.__next__()
3
>>> 
```

<br/><br/><br/>
> 참고 : [wikidocs(파이썬 - 기본을 갈고 닦자!)](https://wikidocs.net/16068)
