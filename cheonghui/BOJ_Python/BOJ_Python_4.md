## BOJ_Python 배우기4

31. BOJ_10156

`과자`

```python
k, n, m = map(int, input().split())
# 과자가격, 개수, 가진돈

if k*n-m <= 0:	# 부족한 액수가 0보다 작거나 같다면 0을 출력 
    print(0)
else:			# 그렇지 않다면 부족한 액수 출력 
    print(k*n-m) 	
```



32. BOJ_3009

`네 번째 점`

```python
x_nums = []
y_nums = []
for _ in range(3):
    x, y = list(map(int,input().split()))
    x_nums.append(x)  # x, y 좌표를 각 리스트에 추가해준다.
    y_nums.append(y)

for i in range(3):
    if x_nums.count(x_nums[i]) == 1:	# x축의 좌표의 리스트 안에 i가 1개만 존재한다면 
        result_x = x_nums[i]			# 해당 i가 네 번째 점의 x축의 좌표
    if y_nums.count(y_nums[i]) == 1:	# y축의 좌표의 리스트 안에 i가 1개만 존재한다면
        result_y = y_nums[i]			# 해당 i가 네 번째 점의 y축의 좌표
print(result_x, result_y)
```



33. BOJ_2476

`주사위 게임`

```python
n = int(input())

money = []
for i in range(n):
    a, b, c = map(int, input().split())

    if a == b and a==c and b == c:		# a, b, c가 모두 같을 경우
        money.append(10000 + a * 1000)

    elif a == b or a == c:				# 두개만 같은 경우
        money.append(1000 + a * 100)

    elif b == c:
        money.append(1000 + b * 100)

    else:								# 하나도 같지 않을 경우
        money.append(max(a,b,c)*100)	
print(max(money))
```



34. BOJ_2754

`학점계산`

```python
dict_grade = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7, 'B+': 3.3, 'B0': 3.0, 'B-': 2.7,'C+': 2.3, 'C0': 2.0, 'C-': 1.7,'D+': 1.3, 'D0': 1.0, 'D-': 0.7, 'F': 0.0}
#각 등급에 해당하는 평점을 딕셔너리 형태로 만들어준다.

level = input()
print(dict_grade[level])    #조회 - 딕셔너리[key]
```



35. BOJ_2884

`알람 시계`

```python
h, m = map(int, input().split())

if m >= 45:					# 분이 45분과 크거나 같을 때
    print(h, m - 45)
elif h != 0 and m <=44:		# 시간이 0시가 아니면서 분이 44분 보다 작거나 같을 때
    print(h - 1, m + 15 )	# 1시간을 빼고 15분을 더해주면, 결국 45분을 뒤로 돌린 것과 같게된다.
else:						# 시간이 0이면서 분이 45보다 작을때
    print(23, m + 15)
```



36. BOJ_7567

`그릇`

```python
dish = input()

result = 0
for i in range(len(dish)):
    if i == 0:
        result += 10
    elif dish[i] == dish[i-1]:	# i의 값이 i앞의 값과 같다면 (접시가 겹쳐져 있다면)
        result += 5
    else:
        result += 10

print(result)
```



37. BOJ_5063

`TGN`

```python
n = int(input())

# 광고 전 수익, 광고 후 수익, 광고 비용
for _ in range(n):
    r, e, c = map(int,input().split())

    if r < (e - c):
        print('advertise')
    elif r == (e - c):
        print('does not matter')
    else:
        print('do not advertise')
```



38. BOJ_10102

`개표`

```python
v = int(input())
vote = input()

lst = []
result = 0
# for문을 돌며 A인지 B인지 비교해서 값
for i in range(len(vote)):						# vote의 길이만큼 for문 반복
    if vote[i] == 'A' or vote[i] == 'B':		# vote의 i번 째 값이 A이거나 B라면
        lst.append(vote[i])						# 그 값을 리스트에 추가
        
        if lst.count('A') < lst.count('B'):		# 리스트 안에 있는 A와 B의 개수를 비교
            result = 'B'
        elif lst.count('A') > lst.count('B'):
            result = 'A'
        else:
            result = 'Tie'

print(result)
```



39. BOJ_10886

` 0 = not cute / 1 = cute`

```python
n = int(input())

result = 0
for _ in range(n):
    num = int(input())
    if num == 1:
        result += 1

if result >= (n // 2 + 1): #투표를 한 인원수의 반에 1을 더한 것 보다 크다면 과반수!!
    print("Junhee is cute!")
else: print( "Junhee is not cute!")

```



40. BOJ_10988

`팰린드롬인지 확인하기`

```python
word = input()

if word == word[::-1]: #[::-1] 값이 거꾸로
    print(1)
else:
    print(0)
```

