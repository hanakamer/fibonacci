import unittest
from fibonacci import Fibonacci

class TestMain(unittest.TestCase):

    def test_recursive(self):
        res = Fibonacci().recursive_fib(8)
        self.assertEqual(res,21)
    def test_recursive_negative(self):
        res = Fibonacci().recursive_fib(-5)
        self.assertEqual(res,'negatif sayi giremezsiniz')
    def test_recursive_zero(self):
        res = Fibonacci().recursive_fib(0)
        self.assertEqual(res,0)
    def test_recursive_one(self):
        res = Fibonacci().recursive_fib(1)
        self.assertEqual(res,1)

    def test_bottomup(self):
        res = Fibonacci().bottomup_fib(8)
        self.assertEqual(res[-1],21)
    def test_bottomup_negative(self):
        res = Fibonacci().bottomup_fib(-5)
        self.assertEqual(res,'negatif sayi giremezsiniz')
    def test_bottomup_zero(self):
        res = Fibonacci().bottomup_fib(0)
        self.assertEqual(res,0)
    def test_bottomup_one(self):
        res = Fibonacci().bottomup_fib(1)
        self.assertEqual(res[-1],1)

    def test_iterative(self):
        res = Fibonacci().iterative_fib(8)
        self.assertEqual(res,21)
    def test_iterative_negative(self):
        res = Fibonacci().iterative_fib(-5)
        self.assertEqual(res,'negatif sayi giremezsiniz')
    def test_iterative_zero(self):
        res = Fibonacci().iterative_fib(0)
        self.assertEqual(res,0)
    def test_iterative_one(self):
        res = Fibonacci().iterative_fib(1)
        self.assertEqual(res,1)

if __name__ =='__main__':
    unittest.main()
