## fmt 정수 표시


#### 📌JSP 상단
```jsp
<%@ taglib uri="http://java.sun.com/jsp/jstl/fmt" prefix="fmt" %>
```

#### 📌JSP
```jsp
<fmt:parseNumber var="intValue" value="${floatValue / 100}" integerOnly="true" />
<td><c:out value="${intValue}" />m</td>
```

`#fmt` `#fmt정수표시` `#fmtIntvalue`
