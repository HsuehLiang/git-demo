import random

number = random.sample(range(1,50),6)
print('樂透號碼：'+' '.join(map(str,sorted(number))))
print(f'特別號：{random.sample(range(1,50),1)}')