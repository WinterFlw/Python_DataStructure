def fib_tab(n):
    
    fiv_table = {}
    for i in range(n):
        if i+1 < 3:
            fiv_table[i+1] = 1
        else:
            fiv_table[i+1] = fiv_table[i] + fiv_table[i-1]
    
    return fiv_table[n]

# 테스트 코드
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))