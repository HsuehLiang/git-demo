import random

#1. 增加勝負判斷(提示猜了幾次)

x =random.randint(1,50)
print(x)
win = False
count = 0

for i in range(5):
    y  = eval(input('請猜一個數字(1~50之間)：'))
    if x == y:
        win = True
        break

    if x > y:
        print('猜大一點')
    else:
        print('猜小一點')
    
    count += 1

if win:
    print(f'恭喜過關! 共猜了{count+1}次')
else:
    print(f'遊戲結束! 答案為：{x}')
