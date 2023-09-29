def max_profit(price_list, count):
    max_profit_table = [0]
    if count < 2:
        max_profit_table[count] = price_list[count]
       
    for i in range(1, count // 2 + 1):
        profit = max(profit, max_profit_table[i] + max_profit_table[cound-i])
        # 계산된 최대 수익을 cache에 저장
        max_profit_table[count] = profit
    return max_profit[count]
# 테스트 코드
print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))
