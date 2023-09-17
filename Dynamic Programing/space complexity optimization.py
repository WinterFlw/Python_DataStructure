def fib_optimized(n):
    current = 1
    previous = 0
  
    for i in range(n-1):
        temp = current
        current += previous
        previous = temp 
    return current

# 테스트 코드
print(fib_optimized(10))
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))
