# K번째수

#### [문제보기](https://programmers.co.kr/learn/courses/30/lessons/42748)

##### `풀이`
```java
import java.util.*;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
		ArrayList<Integer> arr = new ArrayList();
		int[] answer = new int[commands.length];

		for (int i = 0; i < commands.length; i++) {

			for (int j = commands[i][0] - 1; j < commands[i][1]; j++) {
				arr.add(array[j]);
			}
			Collections.sort(arr);
			answer[i] = arr.get(commands[i][2]-1);
			arr.clear();
		}
        return answer;
    }
}
```
