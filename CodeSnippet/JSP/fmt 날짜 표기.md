## fmt 날짜 표기.md
#### String을 parseDate 후 format 설정

```jsp
<%@ taglib uri="http://java.sun.com/jsp/jstl/fmt" prefix="fmt" %>
```
```jsp
<fmt:parseDate value="${list.firstDate}" var="firstDate" pattern="yyyy-MM-dd"/>
<td><fmt:formatDate value="${firstDate}" pattern="yyyy-MM-dd"/></td>
```

`#fmt` `#parseDate` `#formatDate`
