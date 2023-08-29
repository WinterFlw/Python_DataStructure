
from collections import deque

def parentheses_checker(string):
    """주어진 문자열 인풋의 모든 괄호가 짝이 있는지 확인해주는 메소드"""


    print(f"테스트하는 문자열: {string}")
    stack = deque() # 사용할 스택 정의
    string_stack = deque(string)
    open_stack = deque()
    close_stack = deque()
    # 여기에 코드를 작성하세요
    for i in range(len(string_stack)):
        compare_gwalho = string_stack.popleft()
        if compare_gwalho == "(":
            open_stack.append(i)
        elif compare_gwalho == ")":
            close_stack.append(i)
            
    while (len(open_stack)+len(close_stack)) > 0:
        if len(close_stack) > 0 and len(open_stack) > 0:
            open_stack.pop()
            close_stack.pop()
        else:
            if len(close_stack) == 0:
                open_comp = open_stack.pop()
                print(f"문자열 {open_comp} 번째 위치에 있는 괄호가 닫히지 않았습니다")
            else:
                close_comp = close_stack.popleft()
                print(f"문자열 {close_comp} 번째 위치에 있는 닫는 괄호에 맞는 열리는 괄호가 없습니다")

    
# stack 오른 쪽 끝, append pop
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