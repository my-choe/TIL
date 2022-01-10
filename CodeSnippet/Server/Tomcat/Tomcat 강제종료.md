## 톰캣 강제종료


#### 📌cmd 관리자권한으로 실행 후 명령어
```
netstat -a -o
```

<br/>

#### 📌톰캣이 사용하고 있는 포트의 pid 찾기
```
예) 
프로토콜    로컬주소            외부주소            상태         PID
  TCP    x.x.x.x:80       sampleMonitoring:0   clase_wait     11488
```


#### 📌톰캣 강제 종료
```console
taskkill /f /pid 11488
```


<br/><br/>

`#톰캣강제종료` `#tomcat강제종료`
