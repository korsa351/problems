Вам дана последовательность строк.  
Выведите строки, содержащие **"cat"** в качестве подстроки хотя бы два раза.  

**Примечание:**  
Считать все строки по одной из стандартного потока ввода вы можете, например, так
```python
import sys

for line in sys.stdin:
    line = line.rstrip()
    # process line
```
<br>

---
**Sample Input:**
<p style="margin-left: 1em">catcat<br>
cat and cat<br>
catac<br>
cat<br>
ccaatt</p>

---
**Sample Output:**
<p style="margin-left: 1em">catcat<br>cat and cat</p>