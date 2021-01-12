# 🛠 Composite Pattern(컴포지트 패턴)
### ✔ 컴포지트 패턴이란?
* 단일 객체와 그 객체들을 가지는 집합 객체를 같은 타입으로 취급하며, **트리 구조로 객체들을 엮는 패턴**
* 쉽게 말해 일관적인 관리가 가능한 패턴으로 컴포지트의 의도는 트리 구조로 작성하여, **전체-부분(whole-part) 관계를 표현**하는 것
* 컴포지트 패턴은 3가지로 구성된다.
  - `Component` : Leaf와 Composite 가 구현해야하는 Interface 로, Leaf 와 Composite 는 모두 Component 라는 같은 타입으로 다뤄진다.
  - `Leaf` : 단일 객체로 Composite 의 부분(자식) 객체로 들어가게 된다. 이 때, Component 의 형태로 들어간다.
  - `Composite` : 집합 객체로 Leaf 객체나 Composite 를 부분(자식)으로 둔다. 이 때, Component 의 형태로 들어간다. 클라이언트는 이 Composite 를 통해 부분 객체들 (Leaf 나 Composite) 을 다룰 수 있다.


<br/><br/>
### ✔ 컴포지트 패턴을 쓰는 이유
* 객체들이 모두 같은 타입으로 취급되기 때문에 **새로운 클래스 추가가 용이**함
* 단일 및 집합 객체를 구분하지 않고 코드 작성 가능

<br/><br/>
### ✔ 컴포지트 패턴 단점
*설계를 일화 시켜 객체간의 **구분, 제약이 힘듦**

<br/><br/>
### ✔ 컴포지트 패턴 예제 구조
![캡처2](https://user-images.githubusercontent.com/54934681/104276089-80cc8e00-54e7-11eb-8bd6-0af6277733e9.PNG)

<br/><br/>
### ✔ 컴포지트 패턴 예제
🔻 Entry 클래스
```java
package StructuralPattern.Composite;

public abstract class Entry {
	String name;
	public Entry(String name) {
		this.name = name;
	}
	
	public abstract void add(Entry entry);
	public abstract void PrintList(String path);
	
}
```

<br/><br/>
🔻 File 클래스
```java
package StructuralPattern.Composite;

public class File extends Entry{
	public File(String name) {
		super(name);
	}

	@Override
	public void add(Entry entry) {
		// File은 내용물 객체로 안에 또 다른 객체를 포함할 수 없음.
	}

	@Override
	public void PrintList(String path) {
		System.out.println(path + "/" + this.name);
	}
	
}
```
`File은 내용물 객체로 또 다른 객체를 포함할 수 없다. add()를 비워두고 구현했다.`

<br/><br/>
🔻 Directory 클래스
```java
package StructuralPattern.Composite;

import java.util.ArrayList;

public class Directory extends Entry{

	ArrayList<Entry> directory = new ArrayList<Entry>(); //자식객체를 담기위한 ArrayList
	
	public Directory(String name) {
		super(name);
	}

	@Override
	public void add(Entry entry) {	//자식객체 추가
		directory.add(entry);
	}

	@Override
	public void PrintList(String path) { //디렉토리 목록 보여주기
		path += "/" + this.name;
		System.out.println(path);
		for(int i = 0; i < directory.size(); i++) {
			directory.get(i).PrintList(path);
		}
	}
}
```

<br/><br/>
🔻 Main 클래스
```java
package StructuralPattern.Composite;

public class CompositeMain {

	public static void main(String[] args) {
		Directory root = new Directory("root");
		Directory bin = new Directory("bin");
		Directory Lkt = new Directory("Lkt");
		File file1 = new File("file1");
		File file2 = new File("file2");
		File file3 = new File("file3");
		File file4 = new File("file4");
		
		root.add(file1); // root디렉토리에 file1 포함
		bin.add(file2); // bin디렉토리에 file2 포함
		bin.add(file3); // bin디렉토리에 file3 포함
		Lkt.add(file4); // Lkt디렉토리에 file4 포함
		root.add(Lkt); // root디렉토리에 Lkt디렉토리 포함
		root.add(bin); // root디렉토리에 bin디렉토리 포함
		
		root.PrintList("");
	}
}
```

<br/><br/>
🔻 콘솔 결과창
```console
/root
/root/file1
/root/Lkt
/root/Lkt/file4
/root/bin
/root/bin/file2
/root/bin/file3
```

