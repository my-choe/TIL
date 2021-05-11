## Mybatis에서Foreach문 사용하기

```SQL
  <delete id="deleteSerialNo" parameterType="java.util.HashMap">
      delete from tableName where serial_no in 
      <foreach item="item" index="index" collection="SerialNoArr" open="(" separator="," close=")">
           #{item}
        </foreach>
   </delete>
 ```
 
 `#마이바티스` `#Mybatis` `#foreach` `#마이바티스foreach문`
