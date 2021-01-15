# 📝 02_import 기본라이브러리

* python REPL을 실행 후 아래의 코드를 실행합니다.
* math는 수학 연산 기본 라이브러리이며, sqrt는 제곱근을 구합니다.
```python
import math
math.sqrt(81)
```
<br/>

* REPL상태에서 help메소드를 사용하면 import한 라이브러리의 document를 볼 수 있습니다.
```python
help(math)
```
<br/>

* factorial메소드를 실행해봅니다.
```python
math.factorial(5)
```
<br/>

* 아래와 같이 factorial 메소드만 import해서 사용할 수 있습니다.
```python
from math import factorial
factorial(5)
```
<br/>

* 메소드를 import할 때 별칭을 줄 수 있습니다.
```python
from math import factorial as fac
fac(5)
```


<br/><br/><br/>
> 참고 : [wikidocs(파이썬 - 기본을 갈고 닦자!)](https://wikidocs.net/16030)
