# event 켜기

#### ✔ MySQL Client CMD > root 접속

📌 이벤트 확인
```sql
show events;
```

<br/>

📌 이벤트 켜져있는 지 확인
```sql
show variables like 'event%';
```

<br/>

📌 이벤트 기능 켜기
```sql
SET GLOBAL event_scheduler = ON;
```


<br/>

📌 이벤트 보기
```sql
show create event F_TO_RBTMETA; 
(여기서 create문 복사해서 확인)
```

<br/>

📌 예시
```sql
CREATE DEFINER=`ochang`@`%` EVENT `F_TO_RBTMETA` 
ON SCHEDULE EVERY 5 SECOND STARTS '2021-03-10 18:00:00' 
ON COMPLETION NOT PRESERVE ENABLE DO call INSERT_F_TO_RBT_META()
```

<br/>

📌 이벤트가 돌지 않는다면 
```console
my.ini 파일에 event_scheduler=ON 추가 후 윈도우 서비스에서 mariaDB 재시작 후 확인
```

