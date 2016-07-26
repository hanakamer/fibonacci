import time
import timeit
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
        if n < 2:
            return n
        return self.recursive_fib(n-1) + self.recursive_fib(n-2)


    # asagidan  yukari ilerleyerek liste olusturuyoruz
    # boylece onceden hesaplanan sayi daha sonra tekar kullanilabilir
    def bottomup_fib(self,n):
        if n < 0:
            return 'negatif sayi giremezsiniz'
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
        a = 0
        b = 1
        for i in range (1,n + 1):
            temp = a
            a = b
            b += temp
        return a

def timing(func, args):
    time_start = time.time()
    ret = func(args)
    time_stop = time.time()
    print '------ %s function took %0.3f ms ------' % (func.func_name, (time_stop-time_start)*1000.0)
    return ret

##############
# You can uncomment these lines to compare the methods and their performances
##############

# fibo = Fibonacci()

# timing(fibo.recursive_fib,5)
# timing(fibo.bottomup_fib,5)
# timing(fibo.iterative_fib,5)
