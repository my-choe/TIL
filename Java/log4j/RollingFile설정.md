## log4j2.xml 롤링(백업)파일 설정

```
<?xml version="1.0" encoding="UTF-8"?>
<Configuration>
  <Appenders>
    <Console name="console" target="SYSTEM_OUT">
      <PatternLayout charset="UTF-8" pattern="%d %5p %m%n" />
    </Console>
    
    <RollingFile name="socket"
      fileName="./logs/test/Thread.log"
      filePattern="./logs/test/backup/Thread_%d{yyyy-MM-dd}.log">
      <PatternLayout charset="UTF-8" pattern="%d %5p %m%n" />
      <Policies>
        <TimeBasedTriggeringPolicy interval="1" modulate="true" />
      </Policies>
    </RollingFile>
  </Appenders>
  
  <Loggers>
    <Logger
      name="system.com.common.service.impl.SocketSendThreadImpl"
      level="trace" additivity="false">
      <AppenderRef ref="socket" />
    </Logger>
    .
    .
    .
	</Loggers>
</Configuration>
```
<br />

#### RollingFile
* RollingFile : 롤링파일명
* fileName : 생성될 로그파일 path와 파일명
* filePattern : 로그파일 백업 시 path와 파일명 패턴 설정
* PatternLayout : 로그 레이아웃 설정
  * %d : 로깅 이벤트가 발생한 시간
  * %5p : 우측 정렬로 로그 레벨을 남김. 로그 레벨이 5글자가 안 되면 왼쪽에 공백을 추가하여 5글자 맞춤(-5인 경우 좌측 정렬) 
  * %m%n :  m은 에러메시지 출력, n은 개행문자

<br/>

#### Logger
* name : 롤링파일을 실행할 소스 path
* ref : 참고할 롤링파일 형식
