def fib_memo(n, cache):
    if n < 3:
        cache[n] = 1
        return 1
    
    if n in cache:
        return cache[n]
    else:
        cache[n] = fib_memo(n-1, cache) + fib_memo(n-2, cache)
        return cache[n]

def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {} #key-value
    return fib_memo(n, fib_cache)

# 테스트 코드

print(fib(10))
print(fib(50))
print(fib(100))