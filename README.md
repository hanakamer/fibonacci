# fibonacci
comparison of different fibonacci methods with python

**fibonacci serisi**

Fibonacci serisi [0, 1] veya [1, 1] ile başlayan ve sonraki elemanın; önceki iki elemanın toplamından elde edildiği bir seridir. İtalyan matematikçi Leonardo of Pisa'dan (aynı zamanda Fibonacci olarak da bilinir) almıştır adını.

**Metodlar**

Burada fibonacci.pf dosyasına Fibonacci classı oluşturdum. Bu classın 3 farklı metodu var. Bu metodlar yardımı ile fibonacci serisinde istenen elemanının hesaplanıyor. Özyinelemeli (recursive), tek seferde liste oluşturarak ve tekrarlamalı (iterative).

Özyinelemeli yaklaşımda her sayı için öncesindeki sayıların tekrar tekrar hesaplanması gerekiyor. Serideki 5. elemanın hesaplanmasını ele alrırsak:
```
  fib(5) =
  = fib(4) + fib(3)
  = fib(3) + fib(2) + fib(2) + fib(1)
  = fib(2) + fib(1) + fib(1) + fib(0) + fib(1) + fib(0) + 1 
  = fib(1) + fib(0) + 1 + 1 + 0 + 1 + 0 + 1 
  = 1 + 0 + 4
  = 5
  ```
Her sayıda sıfırdan tekrar hesaplanıyor ve daha önceden hesaplanmış olması kullanılmıyor. Burada fib(1) 5 defa; fib(2) 3 defa; fib(0) 3 defa hesaplanmak zorunda kalmıştır.

Tek seferde liste oluşturarak hesapladığımızda daha önce yaptığımız hesapları kullanmış oluyoruz. Bu yüzden daha performanslı bir çözüme ulaşmış oluruz.

Tekrarlamalı yaklaşımda bir for döngüsünde işlemleri tekrarlamamıza rağmen elde ettiğimiz değeri bir sonraki işlem için kaydettiğimiz için özyinelemeli yaklaşım kadar performanssız bir sonuçla karşılaşmayız.

Aşağıdaki değerler fibonacci serisinin 40. elemanını hesaplarken harcanan zamanlardır.
