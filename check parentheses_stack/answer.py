from collections import deque

def parentheses_checker(string):
    """주어진 문자열 인풋의 모든 괄호가 짝이 있는지 확인해주는 메소드"""

    stack = deque()  # 사용할 스택 정의

    print(f"테스트하는 문자열: {string}") 

    # 문자열의 각 문자를 돌면서
    for i in range(len(string)):
        # 열리는 괄호가 있는 위치를 스택에 저장한다
        if string[i] == "(":
            stack.append(i)
        # 닫히는 괄호가 있으면
        elif string[i] == ")":
            # 스택에 열린 괄호 위치 데이터가 있으면 삭제하고
            if stack:
                stack.pop()
            # 아니면 현재 위치에 있는 닫는 괄호에 맞는 열리는 괄호가 없다고 출력한
            else:
                print(f"문자열 {i} 번째 위치에 있는 닫는 괄호에 맞는 열리는 괄호가 없습니다")

    # 스택에 열린 괄호 위치 데이터가 남아 있으면 해당 열린 괄호는 짝이 맞는 닫힌 괄호가 없다는 뜻이다
    while stack:
        print(f"문자열 {stack.pop()} 번째 위치에 있는 괄호가 닫히지 않았습니다")