
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci(n-1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series
    

n = 25
print(fibonacci(n))































## the fibonacci series 0,1,1,2,3,5,8
#
#def fib(n):
#    if n == 0:
#        return 0
#    elif n == 1:
#        return 1
#    else:
#        x = fib(n-1) + fib(n-2)
#        print(x)
#
#def fibonacci(n, a=0, b=1):
#    if n > 0:
#        print(a, end=' ')
#        fibonacci(n-1, b, a+b)
#
## Example usage:
#n = 10  # Change this value to print more or fewer numbers in the series
#fibonacci(n)
##print(fib(5))