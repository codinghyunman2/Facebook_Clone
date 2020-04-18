print('\n')
# 1번 별찍기 
n = 9 
for star in range(9):
  if n < 10: 
    print("*" * n)
    n -= 1 

print('\n')
# 2번 구구단 
m = 1
for two in range(9):
  print(f'2 * {m} = ', 2 * m)
  m += 1 

print('\n')
# 3번 1~1000 중 3의 배수 합 
t = 0 
multiple = 0 
while t <= 1000: 
  t += 1 
  if t % 3 == 0:
    multiple += t 
    continue
print(multiple)

print('\n')
# 4번 for문 평균 
mutsa_scores = [90, 77, 40, 55, 90, 100, 88]
total = 0 
for score in mutsa_scores: 
  total += score 
print(total / 7)