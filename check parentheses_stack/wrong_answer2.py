from collections import deque

def parentheses_checker(string):
    """주어진 문자열 인풋의 모든 괄호가 짝이 있는지 확인해주는 메소드"""

    print(f"테스트하는 문자열: {string}")
    stack = deque() # 사용할 스택 정의
    open_gwalho = 0
    close_gwalho = 0
   
    for i in range(len(string)):
        if '(' == string[i]:
            stack.appendleft(i+1)
            open_gwalho += 1
           
        elif ')' == string[i]:
            if len(stack) == 0:
                stack.appendleft(-(i+1))
                close_gwalho += 1
            elif len(stack) > 0:
                if open_gwalho != 0:
                    stack.popleft()   #pop()사용시 테스트하는 문자열: ((1+4)-(3*12)/3에서, 위치가 "0"이 아닌"7"로 나옴.
                    open_gwalho -= 1
                else:
                    stack.appendleft(-(i+1))
                    close_gwalho += 1
                   
                   
    if open_gwalho == 0 and close_gwalho == 0:
        pass
    elif open_gwalho > 0:
        while len(stack) > 0:
            n = (stack.popleft() - 1)
            print(f'문자열 {n} 번째 위치에 있는 닫는 괄호에 맞는 열리는 괄호가 없습니다')
    elif close_gwalho > 0:
        while len(stack) > 0:
            n = (stack.pop() + 1) * -1
            print(f"문자열 {n} 번째 위치에 있는 괄호가 닫히지 않았습니다")

case1 = "(1+2)*(3+5)"
case2 = "((3*12)/(41-31))"
case3 = "((1+4)-(3*12)/3"
case4 = "(12-3)*(56/3))"
case5 = ")1+14)/3"
case6 = "(3+15(*3"

parentheses_checker(case1)
parentheses_checker(case2)
parentheses_checker(case3)
parentheses_checker(case4)
parentheses_checker(case5)
parentheses_checker(case6)

