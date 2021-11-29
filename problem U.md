Вашей программе на вход подаются три строки **s**, **a**, **b**, состоящие из строчных 
латинских букв.  
За одну операцию вы можете заменить все вхождения строки **a** в строку **s** на строку **b**.

Например, **s = "abab"**, **a = "ab"**, **b = "ba"**, тогда после выполнения одной операции 
строка **s** перейдет в строку **"baba"**, после выполнения двух и операций – 
в строку **"bbaa"**, и дальнейшие операции не будут изменять строку **s**.

Необходимо узнать, после какого минимального количества операций в строке s 
не останется вхождений строки a. Если операций потребуется более 1000, выведите **Impossible**.

Выведите одно число – минимальное число операций, после применения которых в 
строке **s** не останется вхождений строки **a**, или **Impossible**, 
если операций потребуется более 1000.
---
**Sample Input 1:**
<p style="margin-left: 1em">
ababa<br>
a<br>
b</p>

---
**Sample Output 1:**
<p style="margin-left: 1em">1</p>

---
**Sample Input 2:**
<p style="margin-left: 1em">
ababa<br>
b<br>
a</p>

---
**Sample Output 2:**
<p style="margin-left: 1em">1</p>

---
**Sample Input 3:**
<p style="margin-left: 1em">
ababa<br>
c<br>
c</p>

---
**Sample Output 3:**
<p style="margin-left: 1em">0</p>

---
**Sample Input 4:**
<p style="margin-left: 1em">
ababac<br>
c<br>
c</p>

---
**Sample Output 4:**
<p style="margin-left: 1em">Impossible</p>
