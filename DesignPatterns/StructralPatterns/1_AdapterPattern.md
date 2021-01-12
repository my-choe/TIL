# 🛠 Adapter Pattern(어댑터 패턴)
### ✔ 어댑터 패턴이란?
* 110V 콘센트에 220V 플러그를 꽂으려면 ‘110V ->220V 플러그 어댑터’가 필요하다.
* **기존 코드에 새로운 코드를 연동**하여 사용하고 싶거나, 두 코드의 인터페이스가 달라, 이를 **하나로 통일**하여 사용하고 싶을 때 사용하는 패턴
* 서로 다른 인터페이스를 가진 두 클래스가 있고, 이 둘을 그대로 둔 채 어댑터 클래스로 인터페이스를 통일 시켜 사용
* 클래스를 적응자(Adapter)로 만들거나, 객체를 적응자(Adapter)로 만들어 구현할 수 있음

<br/><br/>
### ✔ 어댑터 패턴을 쓰는 이유
* 기존 클라이언트단의 **코드 수정을 최소화**할 수 있음
* 클라이언트는 연동부분을 몰라도, 새로운 코드의 기능을 일관되게 사용할 수 있음

<br/><br/>
### ✔ 어댑터 패턴 단점
* 어댑터 클래스에서 통일 시켜주는 부분을 **하나씩 일일이 구현**해야 한다.

<br/><br/>
### ✔ 어댑터 패턴 예제 구조
![캡처](https://user-images.githubusercontent.com/54934681/104272767-31835f00-54e1-11eb-8645-1eb7698edc08.PNG)

<br/><br/>
### ✔ 어댑터 패턴 예제
🔻 음악을 재생하는 인터페이스
```java
package StructuralPattern.Adapter;

public interface MediaPlayer {

	public void play(String audioType, String fileName);
	
}
```

<br/><br/>
🔻 이 인터페이스를 구현하는 오디오 플레이어는 mp3포맷만 지원한다는 가정
```java
package StructuralPattern.Adapter;

public class AudioPlayer implements MediaPlayer{

	@Override
	public void play(String audioType, String fileName) {
		if(audioType.equalsIgnoreCase("mp3")) {
			System.out.println("♪ mp3 파일음악을 재생합니다. 파일명 : " + fileName);
		}
	}
	
}
```

<br/><br/>
🔻 오디오 플레이어는 다음과 같이 실행된다
```java
package StructuralPattern.Adapter;

public class AdapterPatternDemo {

	public static void main(String[] args) {
		AudioPlayer audioPlayer = new AudioPlayer();
		
		audioPlayer.play("mp3", "beyond the horizon.mp3");
	}
}
```


<br/><br/>
🔻 콘솔 결과창
```console
♪ mp3 파일음악을 재생합니다. 파일명 : beyond the horizon.mp3
```

<br/><br/>
🔻 그런데 앞으로는 mp3뿐만 아니라 mp4와 vlc도 지원해야한다는 요구사항이 들어왔다.<br/>
(이 포맷들을 실행할 수 있는 Mp4Player와 VlcPlayer는 이미 구현되어 있다는 가정)
```java
package StructuralPattern.Adapter;

public interface AdvanceMediaPlayer {
	public void playVlc(String fileName);
	public void playMp4(String fileName);
}
```

🔻 VlcPlayer
```java
package StructuralPattern.Adapter;

public class VlcPlayer implements AdvanceMediaPlayer{

	@Override
	public void playVlc(String fileName) {
		System.out.println("♪ vlc 파일음악을 재생합니다. 파일명 : " + fileName);
	}

	@Override
	public void playMp4(String fileName) {
		// do nothing
	}
}
```

🔻 Mp4Player
```java
package StructuralPattern.Adapter;

public class Mp4Player implements AdvanceMediaPlayer{

	@Override
	public void playVlc(String fileName) {
		// do nothing
	}

	@Override
	public void playMp4(String fileName) {
		System.out.println("♪ mp4 파일음악을 재생합니다. 파일명 : " + fileName);
	}
}
```
<br/><br/>
### `❓ 이미 구현되어 있는 두 객체를 어떻게 연동시켜서 사용할 수 있을까?`


<br/><br/>
🔻 MediaPlayer인터페이스를 구현하는 MediaAdapter 클래스 생성 `(🌟어댑터 패턴 등장!🌟)`
```java
package StructuralPattern.Adapter;

public class MediaAdapter implements MediaPlayer{

	AdvanceMediaPlayer advanceMusicPlayer;
	
	public MediaAdapter(String audioType) {
		// 생성 시, vlc인지 mp4인지 구분
		if(audioType.equalsIgnoreCase("vlc"))
			advanceMusicPlayer = new VlcPlayer();
		
		else if(audioType.equalsIgnoreCase("mp4"))
			advanceMusicPlayer = new Mp4Player();
	}
	
	@Override
	public void play(String audioType, String fileName) {
		// play호출 시, 구체적인 각 플레이어의 메소드를 호출
		if(audioType.equalsIgnoreCase("vlc"))
			advanceMusicPlayer.playVlc(fileName);
		
		else if(audioType.equalsIgnoreCase("mp4"))
			advanceMusicPlayer.playMp4(fileName);
	}
}
```

<br/><br/>
🔻 vlc와 mp4 확장자  추가 지원을 위해 AudioPlayer에 다음 내용 추가
```java
package StructuralPattern.Adapter;

public class AudioPlayer implements MediaPlayer{

	@Override
	public void play(String audioType, String fileName) {
		
		if(audioType.equalsIgnoreCase("mp3")) {
			System.out.println("♪ mp3 파일음악을 재생합니다. 파일명 : " + fileName);
		}
		
		// (내용 추가 부분)'vlc'나 'mp4' 포맷은 MediaAdapter로 처리한다.
		else if(audioType.equalsIgnoreCase("vlc") || audioType.equalsIgnoreCase("mp4")) {
			MediaAdapter mediaAdapter = new MediaAdapter(audioType);
			mediaAdapter.play(audioType, fileName);
		}
	}
}
```

<br/><br/>
🔻 AudioPlayer에 쓰이는 모습이 전혀 달라진 게 없이도 추가 포맷을 지원한다.
```java
package StructuralPattern.Adapter;

public class AdapterPatternDemo {

	public static void main(String[] args) {
		AudioPlayer audioPlayer = new AudioPlayer();
		
		audioPlayer.play("mp3", "beyond the horizon.mp3");
    audioPlayer.play("vlc", "Fixx me.vlc");
    audioPlayer.play("mp4", "Best Part.mp4");
	}
}
```

<br/><br/>
🔻 콘솔 결과창
```console
♪ mp3 파일음악을 재생합니다. 파일명 : beyond the horizon.mp3
♪ vlc 파일음악을 재생합니다. 파일명 : Fixx me.vlc
♪ mp4 파일음악을 재생합니다. 파일명 : Best Part.mp4
```
