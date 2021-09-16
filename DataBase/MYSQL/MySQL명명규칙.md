# MySQL 명명규칙

### ✔ Common
  * **이름이 고유**하고 **예약어가 아니어야 한다.**
  * 길이는 **최대 30바이트 이내**어야 한다.
  * 문자로 시작해야하며 **_밑줄로 끝날 수 없다.**
  * 이름에는 **문자, 숫자, _밑줄**만 사용한다.
  * 밑줄을 여러 번 사용하지 않는다. (가독성 낮음)
  * 빈칸 대신 밑줄을 사용한다. 예) first_name
  * 가능하면 축약형 사용을 피한다. 예) register_date(O) / reg_date(X) 
  * 동사는 **능동태**를 사용한다. 예) register_date(O) / registered_date(X) 

<br/>

### ✔ Tables
  * **복수형**을 사용할 수 있다. 예) staff, employees
  * tbl 접두사와 같은 **설명 접두사 또는 헝가리어 표기법을 사용하지 않는다.**
  * 테이블에 **컬럼명과 동일한 이름을 지정하지 않는다.** (반대의 경우도 동일)
  * 두 개의 테이블 이름을 연결하여 릴레이션 테이블 이름을 만드는 것을 피한다.     예) cars_mechanics(X) / services(O)

<br/>

### ✔ Columns
  * 항상 **단수형**을 사용한다.
  * 가능한 경우 테이블 **기본키로 ID를 사용하지 않는다.**
  * 테이블 이름과 같은 컬럼을 추가하지 않는다.
  * 고유명사를 제외하고는 **항상 소문자를 사용**한다.

<br/>

### ✔ Aliasing or correlations
  * 별칭이라는 것을 알 수 있도록 **개체 또는 표현식으로든 연관**되어야 한다.
  * 상관 이름은 개체 이름에 있는 **각 단어의 첫글자**여야 한다. 예) first_name AS f_n
  * 동일한 이름이 있는 경우 번호를 추가한다.
  * 별칭 사용 시 **항상 AS를 사용**하여 명시적으로 표시한다.
  * 계산 데이터(sum 또는 avg)의 경우 스키마에 정의된 컬럼인 경우 **지정 이름을 사용**한다.

```sql
SELECT first_name AS fn
  FROM staff AS s1
  JOIN students AS s2
    ON s2.mentor_id = s1.staff_num;
```
```sql
SELECT SUM(s.monitor_tally) AS monitor_total
  FROM staff AS s;
```


<br/>

### ✔ Stored procedures
  * 이름에 동사를 포함해야 한다.
  * sp와 같은 **접두사 또는 헝가리어 표기법을 사용하지 않는다.**

<br/>

### ✔ Uniform suffixes
##### 다음 접미사는 SQL 코드에서 컬럼을 쉽게 읽고 이해할 수 있도록 하는 보편적인 의미를 갖는다. 올바른 접미사를 적절하게 사용할 수 있어야 한다.
  * **_id** : 기본 키와 같은 고유 식별자
  * **_status** : 플래그 값과 같은 상태 표시
  * **_total** : 합계
  * **_num** : 필드에 숫자를 포함하고 있음을 나타냄
  * **_name** : 이름 예) first_name
  * **_seq** :연속된 값 시퀀스 포함
  * **_date** : 날짜가 포함된 컬럼을 나타냄
  * **_tally** : 계산, 카운트
  * **_size** : 파일 크기나 옷 등의 크기
  * **_addr** : 주소 예) ip_addr


<br/><br/>

[참고 문서 - SQL Style Guide](https://www.sqlstyle.guide/)
