import time
class Fibonacci:
    # her sayi icin oncesindeki sayilari tekrar tekrar heaplamasi gerekiyor
    # fib(5) =
    # fib(4) + fib(3)=
    # fib(3) + fib(2) + fib(2) + fib(1)=
    # fib(2) + fib(1) + fib(1) + fib(0) + fib(1) + fib(0) + 1 =
    # fib(1) + fib(0) + 1 + 1 + 0 + 1 + 0 + 1 =
    # 1 + 0 + 4
    # her sayida sifirdan tekrar hesaplaniyor ve daha onceden hesaplanmis
    # olmasi kullanilmiyor

    def recursive_fib(self,n):
        if n < 0:
            return 'negatif sayi giremezsiniz'
        else:
            if n < 2:
                return n
            return self.recursive_fib(n-1) + self.recursive_fib(n-2)

    # asagidan  yukari ilerleyerek liste olusturuyoruz
    # boylece onceden hesaplanan sayi daha sonra tekar kullanilabilir
    def bottomup_fib(self,n):
        if n < 0:
            return 'negatif sayi giremezsiniz'
        else:
            if n == 0:
                return 0
            fibo = [0,1]
            for i in range(2, n+1):
                fibo.append(fibo[-1] + fibo[-2])
            stop_time_bottomup = time.time()
            return fibo

    def iterative_fib(self,n):
        if n < 0:
            return 'negatif sayi giremezsiniz'
        else:
            a = 0
            b = 1
            for i in range (1,n + 1):
                temp = a
                a = b
                b += temp
            return a


fibo = Fibonacci()

# start_time_reccursive = time.time()
# recursive_result = fibo.recursive_fib(40)
# stop_time_reccursive = time.time()
#
# recursive_time = stop_time_reccursive - start_time_reccursive
#
# start_time_bottomup = time.time()
# bottomup_result = fibo.bottomup_fib(40)
# stop_time_bottomup = time.time()
#
# bottomup_time = stop_time_bottomup - start_time_bottomup
#
start_time_iterative = time.time()
iterative_result = fibo.iterative_fib(40)
stop_time_iterative = time.time()

iterative_time = stop_time_iterative - start_time_iterative

# print("--- %s seconds --- recursive" % (recursive_time))
# print("--- %s seconds --- bottomup" % (bottomup_time))
print("--- %s seconds --- iterative" % (iterative_time))
