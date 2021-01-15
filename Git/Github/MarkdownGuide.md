# ✒ Github Markdown
## 📜 Chapter 01. 마크다운에 관하여
### 🖋 1.1 마크다운이란?
* Github Repository에 관한 정보를 기록하는 README.md는 깃헙을 사용하는 사람이라면 누구나 가장 먼저 접하게 되는 마크다운 문서이다.
* Markdown은 텍스트 기반의 마크업언어로 2004년 존그루버에 의해 만들어졌으며 쉽게 쓰고 읽을 수 있으며 HTML로 변환이 가능하다.
* 마크다운을 통해서 설치방법, 소스코드 설명, 이슈 등을 간단하게 기록하고 가독성을 높일 수 있다.
* 특수기호와 문자를 이용한 매우 간단한 구조의 문법을 사용하여 웹에서도 보다 빠르게 컨텐츠를 작성하고 보다 직관적으로 인식할 수 있다.

<br/>

### 🖋 1.2 마크다운의 장·단점
* **장점**
    * 간결하다.
    * 별도의 도구없이 작성가능하다.
    * 다양한 형태로 변환이 가능하다.
    * 텍스트(Text)로 저장되기 때문에 용량이 적어 보관이 용이하다.
    * 텍스트파일이기에 버전관리시스템을 이용하여 변경이력을 관리할 수 있다.
    * 지원하는 프로그램과 플랫폼이 다양하다.
* **단점**
    * 표준이 없기 때문에 사용자나 도구에 따라서 문법이나 생성물이 다르다.
    * 모든 HTML 마크업을 대신하지 못한다.
    
<br/>   

### 🖋 1.3 Github 마크다운 작성페이지
* 빠른 마크다운 작성 사이트 : https://stackedit.io/app#


<br/><br/>
## 📜 Chapter 02. 마크다운 사용법
### 🖋 2.1 헤더 Headers
🔻 **큰 제목** : 문서 제목
```
This is an H1
=============
```
This is an H1
=============

<br/><br/>
🔻 **작은 제목** : 문서 부제목
```
This is an H2
-------------
```
This is an H2
-------------

<br/><br/>
🔻 **글머리** : 1~6까지만 지원하며 1,2의 경우 자동으로 하단에 밑줄이 생긴다.
```
# This is a H1
## This is a H2
### This is a H3
#### This is a H4
##### This is a H5
###### This is a H6
```
# This is a H1
## This is a H2
### This is a H3
#### This is a H4
##### This is a H5
###### This is a H6
####### This is a H7 (지원하지 않음)

<br/><br/>
### 🖋 2.2 인용 BlockQuote
🔻 이메일에서 사용하는 `> 블럭인용문자`를 이용한다.
```
> This is a first blockqute.
>> This is a second blockqute.
>>> This is a third blockqute.
```
> This is a first blockqute.
>> This is a second blockqute.
>>> This is a third blockqute.


<br/><br/>
🔻 이 안에서는 다른 마크 다운 요소를 포함할 수 있다.
```
> ### This is a H3
>> * list
>>> <pre><code>code</code></pre>
```
> ### This is a H3
>> * list
>>> <pre><code>code</code></pre>

<br/><br/>
### 🖋 2.3 목록
🔻 목록 사용 예시
```
1. 순서가 필요한 목록
2. 순서가 필요한 목록
      - 순서가 필요하지 않은 목록(서브) 
      - 순서가 필요하지 않은 목록(서브) 
3. 순서가 필요한 목록
      1. 순서가 필요한 목록(서브)
      2. 순서가 필요한 목록(서브)
4. 순서가 필요한 목록

- 순서가 필요하지 않은 목록에 사용 가능한 기호
  - 대쉬(hyphen)
  * 별표(asterisks)
  + 더하기(plus sign)
- 체크리스트
  - [ ] CSS 수정 (대괄호 사이 띄어쓰기 필수)
  - [x] 로직 변경
```
1. 순서가 필요한 목록
2. 순서가 필요한 목록
      - 순서가 필요하지 않은 목록(서브) 
      - 순서가 필요하지 않은 목록(서브) 
3. 순서가 필요한 목록
      1. 순서가 필요한 목록(서브)
      2. 순서가 필요한 목록(서브)
4. 순서가 필요한 목록

- 순서가 필요하지 않은 목록에 사용 가능한 기호
  - 대쉬(hyphen)
  * 별표(asterisks)
  + 더하기(plus sign)

- 체크리스트
  - [ ] CSS 수정 (대괄호 사이 띄어쓰기 필수)
  - [x] 로직 변경

  

<br/><br/>
### 🖋 2.4 들여쓰기
🔻 4개의 공백 또는 하나의 탭으로 된 들여쓰기를 만나면 들여쓰지 않은 행을 만날 때까지 변환이 계속된다.
```
This is a normal paragraph:

    This is a code block.

end code block.
```
This is a normal paragraph:

    This is a code block.

end code block.

<br/><br/>
🔻 한 줄 띄어쓰지 않으면(Enter 2번) 인식 되지 않는다.
```
This is a normal paragraph:
    This is a code block.
end code block.
```
This is a normal paragraph:
    This is a code block.
end code block.


<br/><br/>
### 🖋 2.5 코드블럭
🔻 `<pre><code>{code}</code></pre>` 태그를 이용하는 방법
```
<pre>
<code>
public class BootSpringBootApplication {
  public static void main(String[] args) {
    System.out.println("Hello, Honeymon");
  }
}
</code>
</pre>
```
👇
<pre>
<code>
public class BootSpringBootApplication {
  public static void main(String[] args) {
    System.out.println("Hello, Honeymon");
  }
}
</code>
</pre>


<br/><br/>
🔻 블럭코드("```") 를 이용하는 방법
* 사용 시 언어를 표기하면 해당 언어 형식으로 입력된다.

` ```java `<br/>
`public class BootSpringBootApplication {`<br/>
`  public static void main(String[] args) {`<br/>
`    System.out.println("Hello, Honeymon");`<br/>
`  }`<br/>
`}`<br/>
` ``` `<br/>
👇
```java
public class BootSpringBootApplication {
  public static void main(String[] args) {
    System.out.println("Hello, Honeymon");
  }
}
```


<br/><br/>
🔻 블럭코드("~~~") 를 이용하는 방법<br/>
` ~~~ `<br/>
`public class BootSpringBootApplication {`<br/>
`  public static void main(String[] args) {`<br/>
`    System.out.println("Hello, Honeymon");`<br/>
`  }`<br/>
`}`<br/>
` ~~~ `<br/>
👇
~~~
public class BootSpringBootApplication {
  public static void main(String[] args) {
    System.out.println("Hello, Honeymon");
  }
}
~~~


<br/><br/>
🔻 작은 코드블럭 (" ` ")
```
`printf(“작은 코드블럭”);` 
백그라운드가 생긴다.
```
`printf(“작은 코드블럭”);` 
백그라운드가 생긴다.

<br/><br/>
### 🖋 2.6 수평선
🔻 마크다운 문서를 미리보기로 출력할 때 페이지 나누기 용도로 많이 사용한다.
```
* * *
***
*****
- - -
--------------------------------------
```
* * *
***
*****
- - -
--------------------------------------

<br/><br/>
### 🖋 2.7 링크
🔻 URL 직접 입력
```
https://github.com/
<https://github.com/>
```
https://github.com/
<https://github.com/>

<br/><br/>
🔻 마크다운 문서를 미리보기로 출력할 때 페이지 나누기 용도로 많이 사용한다.
```
깃허브가 궁금하시다면, [깃허브 홈페이지]https://github.com/)를 클릭하세요.
```
깃허브가 궁금하시다면, [깃허브 홈페이지](https://github.com/)를 클릭하세요.


<br/><br/>
🔻 링크에 title(설명)추가
```
[깃허브 홈페이지 바로가기](https://github.com/ "깃허브 홈페이지입니다 ")
```
[깃허브 홈페이지 바로가기](https://github.com/ "깃허브 홈페이지입니다 ")


<br/><br/>
### 🖋 2.8 강조
🔻 강조
```
*이텔릭체 1*
_Italic type_
**문자열 강조**
__underbar bold__ (현재 적용되지 않음)
~~cancelline~~
<u>underline</u> 밑줄 (현재 적용되지 않음)
문장 중간에 사용할 경우에는 **띄어쓰기** 를 사용하는 것이 좋다.
```
*이텔릭체 1*<br/>
_Italic type_<br/>
**문자열 강조**<br/>
__underbar bold__ (현재 underbar 적용되지 않음)<br/>
~~cancelline~~<br/>
<u>underline</u> 밑줄 (현재 underbar 적용되지 않음)<br/>
문장 중간에 사용할 경우에는 **띄어쓰기** 를 사용하는 것이 좋다.

<br/><br/>
### 🖋 2.9 이미지
🔻 `![대체문자](이미지경로 "부가 제목")`
```
![고양이](https://user-images.githubusercontent.com/54934681/104692013-9261a000-574a-11eb-9ab0-02be721120a0.jpg "귀여워")
```
![고양이](https://user-images.githubusercontent.com/54934681/104692013-9261a000-574a-11eb-9ab0-02be721120a0.jpg "귀여워")


<br/><br/>
🔻 이미지에 링크 걸기 `[![대체문자](이미지경로)] (링크주소)`
```
[![코로나조심](https://user-images.githubusercontent.com/54934681/104692522-7ad6e700-574b-11eb-94d7-f0476bad16d4.jpg)](https://github.com/)
```
[![코로나조심](https://user-images.githubusercontent.com/54934681/104692522-7ad6e700-574b-11eb-94d7-f0476bad16d4.jpg)](https://github.com/)


<br/><br/>
🔻 사이즈 조절 기능은 없기 때문에 `<img width="" height=""></img>`를 이용한다.
```
<img src="https://user-images.githubusercontent.com/54934681/104692249-03a15300-574b-11eb-8624-3454e5f091dd.jpg" width="450px" height="300px" title="px(픽셀) 크기 설정" alt="socute"></img>
```
<img src="https://user-images.githubusercontent.com/54934681/104692249-03a15300-574b-11eb-8624-3454e5f091dd.jpg" width="450px" height="300px" title="px(픽셀) 크기 설정" alt="socute"></img>

<br/><br/>
### 🖋 2.10 줄바꿈
🔻 2칸 이상 띄어쓰기 또는 [엔터]키를 2번 입력하면 줄이 바뀐다.
```
* 줄 바꿈을 하기 위해서는 문장 마지막에서 3칸이상을 띄어쓰기해야 한다.
  이렇게

* 줄 바꿈을 하기 위해서는 문장 마지막에서 3칸이상을 띄어쓰기해야 한다.

  이렇게
```
* 줄 바꿈을 하기 위해서는 문장 마지막에서 3칸이상을 띄어쓰기해야 한다.
  이렇게

* 줄 바꿈을 하기 위해서는 문장 마지막에서 3칸이상을 띄어쓰기해야 한다.

  이렇게
  
  
  
  
<br/><br/>
### 🖋 2.11 테이블
🔻 사용 예
```
지역 | 1분기| 2분기| 3분기| 4분기| 
---- | ---- | ---- | ---- | ----
서울 | 1,800 | 2,300 | 1,700 | 2,600
인천 | 2,200 | 1,900 | 2,800 | 2,500
```

지역 | 1분기| 2분기| 3분기| 4분기| 
---- | ---- | ---- | ---- | ----
서울 | 1,800 | 2,300 | 1,700 | 2,600
인천 | 2,200 | 1,900 | 2,800 | 2,500


<br/><br/>

```
지역 | 1분기| 2분기| 3분기| 4분기| 
---- | ---- | ---- | ---- | ----
서울 |  | 2,300 | 1,700 | 2,600
인천 | 2,200 |  |  | 2,500
```

지역 | 1분기| 2분기| 3분기| 4분기| 
---- | ---- | ---- | ---- | ----
서울 |  | 2,300 | 1,700 | 2,600
인천 | 2,200 |  |  | 2,500


<br/><br/>

```
<table>
    <thead>
        <tr>
            <th>Layer 1</th>
            <th>Layer 2</th>
            <th>Layer 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=4>L1 Name</td>
            <td rowspan=2>L2 Name A</td>
            <td>L3 Name A</td>
        </tr>
        <tr>
            <td>L3 Name B</td>
        </tr>
        <tr>
            <td rowspan=2>L2 Name B</td>
            <td>L3 Name C</td>
        </tr>
        <tr>
            <td>L3 Name D</td>
        </tr>
    </tbody>
</table>
```

<table>
    <thead>
        <tr>
            <th>Layer 1</th>
            <th>Layer 2</th>
            <th>Layer 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=4>L1 Name</td>
            <td rowspan=2>L2 Name A</td>
            <td>L3 Name A</td>
        </tr>
        <tr>
            <td>L3 Name B</td>
        </tr>
        <tr>
            <td rowspan=2>L2 Name B</td>
            <td>L3 Name C</td>
        </tr>
        <tr>
            <td>L3 Name D</td>
        </tr>
    </tbody>
</table>
