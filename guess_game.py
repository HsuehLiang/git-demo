import random

#1. 增加勝負判斷(提示猜了幾次)

x =random.randint(1,100)
print(x)
win = False
count = 0
start, end = 1, 50

for i in range(5):
    y  = eval(input('輸入(1 ~ 100)之間的一個數字：'))
    if x == y:
        win = True
        break

    if x > y:
        if start  < y:
            start = y
        print(f'提示： {start} ~ {end} 之間')
    else:
        if end > y:
            end = y
        print(f'提示 {start} ~ {end} 之間')
    
    count += 1

if win:
    print(f'恭喜過關! 共猜了{count+1}次')
else:
    print(f'沒猜中，遊戲結束! ans：{x}')
