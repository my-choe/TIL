## tr onclick 특정 td 제외
### 제외하고자 하는 td 에 event.cancelBubble=true 사용

```html
<table>
  <tr onclick="javascript:fn_resultEnd('N');">
    <td>시작일</td>
    <td>구역</td>
    <td onclick="event.cancelBubble=true">
      <button onclick="javascript:fn_sitJournalLayer('VIEW');>일지조회</button>
    </td>
  </tr>
</table>
```


`#onclick제외` `#cancelBubble` `#event`
