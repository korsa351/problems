Рассмотрим два HTML-документа **A** и **B**.  
Из **A** можно перейти в **B** за один переход, если в **A** есть ссылка на **B**, т. е. 
внутри **A** есть тег `<a href="B">`, возможно с дополнительными параметрами внутри тега.  
Из **A** можно перейти в **B** за два перехода если существует такой документ **C**, 
что из **A** в **C** можно перейти за один переход и из **C** в **B** можно перейти за 
один переход.

Обратите внимание на то, что не все ссылки внутри HTML документа могут 
вести на существующие HTML документы.

---
**Sample Input 1:**
<p style="margin-left: 1em">https://stepic.org/media/attachments/lesson/24472/sample0.html<br>
https://stepic.org/media/attachments/lesson/24472/sample2.html</p>

---
**Sample Output 1:**
<p style="margin-left: 1em">Yes</p>

---
**Sample Input 2:**
<p style="margin-left: 1em">https://stepic.org/media/attachments/lesson/24472/sample0.html<br>
https://stepic.org/media/attachments/lesson/24472/sample1.html</p>

---
**Sample Output 2:**
<p style="margin-left: 1em">No</p>

---
**Sample Input 3:**
<p style="margin-left: 1em">https://stepic.org/media/attachments/lesson/24472/sample1.html<br>
https://stepic.org/media/attachments/lesson/24472/sample2.html</p>

---
**Sample Output 3:**
<p style="margin-left: 1em">Yes</p>